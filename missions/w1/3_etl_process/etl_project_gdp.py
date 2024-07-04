import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tabulate import tabulate
from datetime import datetime

def write_log(msg: str):
    with open("etl_project_log.txt", 'a+') as f:
        now = datetime.now()
        now_formatted = now.strftime("[%Y-%B-%d-%H-%M-%S] ")
        f.write(now_formatted + msg.strip() + '\n')

def log_step(step_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            write_log(f"{step_name} started.")
            result = func(*args, **kwargs)
            write_log(f"{step_name} finished.")
            return result
        return wrapper
    return decorator


@log_step("Scrapping HTML from URL")
def get_soup(url):
    try:
        page = requests.get(url)
        soup = bs(page.text, "html.parser") 
        return soup
    except:
        write_log("HTML request failed.")
        exit(0)


@log_step("Parsing HTML and transforming data")
def parse_soup(soup):
    cbc_df = pd.read_csv("countries_by_continent.csv")
    cbc_dict = dict((country, continent) for _,(country,_,_,continent) in cbc_df.iterrows())

    try:
        gdp_list = []
        trs = soup.select('table.wikitable > tbody > tr')

        for tr in trs:
            td = tr.select('td')
            if not td:
                continue

            country = td[0].text.strip()
            gdp_string = td[1].text.strip().replace(',','')
            # WARNING: below is not dash symbol
            gdp = None if gdp_string == '—' else int(gdp_string) / 1000
            continent = cbc_dict[country] if country in cbc_dict else None
            gdp_list.append((country, gdp, continent))
        
        gdp_df_ = pd.DataFrame(gdp_list, columns=('Country', 'GDP', 'Region'))
        gdp_df = gdp_df_[gdp_df_['Country']!='World'].sort_values(by='GDP', ascending=False, ignore_index=True)

        return gdp_df
    
    except:
        write_log("Parsing failed.")
        exit(0)

@log_step("Saving data in json file")
def save_data_in_json_format(df, json_path):
    df.to_json(json_path, orient='records', indent=4)


def get_top5_average_by_region(df):
    avg_df = pd.DataFrame(columns=('Region', 'Average GDP'))
    for region in df['Region'].unique():
        region_countries = df[df['Region'] == region]
        top_5_countries = region_countries.sort_values(by='GDP', ascending=False).iloc[:5]
        avg_gdp = top_5_countries['GDP'].mean()

        new_row = {'Region':region, 'Average GDP':avg_gdp}
        avg_df.loc[len(avg_df)] = new_row
    return avg_df

def print_data_frame(df):
    print(tabulate(df, headers='keys', tablefmt='psql', floatfmt=".2f"))



def run(gdp_url, json_path):
    # Extract: scrap html
    gdp_soup = get_soup(gdp_url)

    # Transform: parse html and get gdp data in DataFrame
    gdp_df = parse_soup(gdp_soup)

    # Load: save in json format
    save_data_in_json_format(gdp_df, json_path)

    # Print countries whose GDP is upper than 100B USD
    print("\n\n[ Countries whose GDP is upper than 100B USD ]")
    print_data_frame(gdp_df[gdp_df['GDP'] >= 100])

    # Print average GDP of top 5 countries for each region
    avg_gdp_df = get_top5_average_by_region(gdp_df)
    print("\n\n[ Average GDP of top 5 countries for each region ]")
    print_data_frame(avg_gdp_df)


if __name__ == "__main__":
    gdp_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
    json_path = 'Countries_by_GDP.json'
    run(gdp_url, json_path)