import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tabulate import tabulate
from datetime import datetime
import sqlite3

class SqlDatabase:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.create_connection()

    def create_connection(self):
        self.con = None
        try:
            self.con = sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            write_log(f"CREATE CONNECTION ERROR {e}")

    # run any sql query. But not return selected items
    def run_sql(self, sql: str, commit=False) -> None:
        try:
            cur = self.con.cursor()
            cur.execute(sql)
            if commit:
                self.con.commit()
        except sqlite3.Error as e:
            write_log(f"SQL ERROR: {e}")

    # insert or replace data into table
    def insert_data(self, table: str, data: list) -> None:
        try:
            sql = f"""
                INSERT OR REPLACE INTO {table}(Country, GDP_USD_billion, Region)
                VALUES(?, ?, ?);
            """
            cur = self.con.cursor()
            cur.executemany(sql, data)
            self.con.commit()
        except sqlite3.Error as e:
            write_log(f"SQL INSERT ERROR: {e}")
    
    # use when execute select query. returns selected items
    def select_data(self, select_sql: str) -> list:
        data = []
        try:
            cur = self.con.cursor()
            cur.execute(select_sql)
            data = cur.fetchall()
        except sqlite3.Error as e:
            write_log(f"SQL SELECT ERROR: {e}")
        finally:
            return data

'''
function to log
'''
def write_log(msg: str):
    with open("etl_project_log.txt", 'a+') as f:
        now = datetime.now()
        now_formatted = now.strftime("[%Y-%B-%d-%H-%M-%S] ")
        f.write(now_formatted + msg.strip() + '\n')

'''
decorator for logging
'''
def log_step(step_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            write_log(f"{step_name} started.")
            result = func(*args, **kwargs)
            write_log(f"{step_name} finished.")
            return result
        return wrapper
    return decorator

'''
Extract
function to scrap url
'''
@log_step("Scrapping HTML from URL")
def get_soup(url):
    try:
        page = requests.get(url)
        soup = bs(page.text, "html.parser") 
        return soup
    except:
        write_log("HTML request failed.")
        exit(1)

'''
Transform
function to parse html
'''
@log_step("Parsing HTML and transforming data")
def parse_soup(soup):
    cbc_df = pd.read_csv("countries_by_continent.csv")
    cbc_dict = dict((country, continent) for _,(country,_,_,continent) in cbc_df.iterrows())
    gdp_list = []
    try:
        trs = soup.select('table.wikitable > tbody > tr')

        for tr in trs:
            td = tr.select('td')
            if not td:
                continue

            country = td[0].text.strip()
            if country == 'World':
                continue
            gdp_string = td[1].text.strip().replace(',','')
            # WARNING: below is not dash symbol
            gdp = None if gdp_string == '—' else int(gdp_string) / 1000
            region = cbc_dict[country] if country in cbc_dict else None
            gdp_list.append((country, gdp, region))

        return gdp_list
    
    except:
        write_log("Parsing failed.")
        exit(2)

'''
Load
function to save result in json format
'''
@log_step("Saving data in json file")
def save_data_in_db(db_path: str, table_name: str, gdp_list: list):
    db = SqlDatabase(db_path)
    sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            Country text PRIMARY KEY,
            GDP_USD_billion real,
            Region text
        );
    """
    db.run_sql(sql)
    db.insert_data(table_name, gdp_list)
    return db

def get_gdp_upper_100_db(table_name: str) -> list:
    sql = f"""
        SELECT * FROM {table_name}
        WHERE GDP_USD_billion >= 100
        ORDER BY GDP_USD_billion DESC
    """
    gdp_upper_100_list = gdp_db.select_data(sql)
    return gdp_upper_100_list

def get_avg_gdp_of_top_n_by_region(table_name: str, n=5) -> list:
    sql = f"""
        WITH RankedCountries AS (
            SELECT *, ROW_NUMBER() OVER (PARTITION BY Region ORDER BY GDP_USD_billion DESC) as rank
            FROM {table_name}
        )
        SELECT Region, AVG(GDP_USD_billion) as Average_GDP
        FROM RankedCountries
        WHERE rank <= {n}
        GROUP BY Region
        ORDER BY Average_GDP DESC;
    """
    avg_gdp_list = gdp_db.select_data(sql)
    return avg_gdp_list

def print_db(data: list, header='keys') -> None:
    print(tabulate(data, headers=header, tablefmt='psql', floatfmt=".2f"))


if __name__ == "__main__":
    gdp_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
    dp_path = 'World_Economies.db'
    table_name = 'gdp_data'
    
    # Extract: scrap html
    gdp_soup = get_soup(gdp_url)

    # Transform: parse html and get gdp data in DataFrame
    gdp_list = parse_soup(gdp_soup)

    # Load: save in json format
    gdp_db = save_data_in_db(dp_path, table_name, gdp_list)

    # Print countries whose GDP is upper than 100B USD
    gdp_upper_100_list = get_gdp_upper_100_db(table_name)
    print("\n\n[ Countries whose GDP is upper than 100B USD ]")
    print_db(gdp_upper_100_list, header=('Country', 'GDP_USD_billion', 'Region'))

    # Print average GDP of top 5 countries by region
    avg_gdp_list = get_avg_gdp_of_top_n_by_region(table_name, n=5)
    print("\n\n[ Average GDP of top 5 countries by region ]")
    print_db(avg_gdp_list, header=('Region', 'Avg_GDP_USD_billion'))