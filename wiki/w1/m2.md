# W1M2 - SQL Tutorial

[w3schools](https://www.w3schools.com/sql/default.asp)을 참고해 학습

## SQL Keywords

#### SELECT
```sql
SELECT column1, column2 FROM table_name;
```
데이터베이스에서 데이터를 선택합

#### SELECT DISTINCT
```sql
SELECT DISTINCT column1 FROM table_name;
```
컬럼에서 유일한 값을 선택

#### WHERE
```sql
SELECT column1, column2 FROM table_name WHERE condition;
```
조건에 따라 레코드를 필터링

#### ORDER BY
```sql
SELECT column1, column2 FROM table_name ORDER BY column1 ASC;
```
결과 세트를 오름차순 또는 내림차순으로 정렬

#### AND, OR, NOT
```sql
SELECT column1 FROM table_name WHERE condition1 AND condition2;
SELECT column1 FROM table_name WHERE condition1 OR condition2;
SELECT column1 FROM table_name WHERE NOT condition;
```
#### 여러 조건을 결합

#### INSERT INTO
```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```
테이블에 새 데이터를 삽입

#### NULL
```sql
SELECT column1 FROM table_name WHERE column1 IS NULL;
```
NULL 값을 확인

#### UPDATE
```sql
UPDATE table_name SET column1 = value1 WHERE condition;
```
테이블의 기존 데이터를 업데이트

#### DELETE
```sql
DELETE FROM table_name WHERE condition;
```
테이블에서 데이터를 삭제

#### LIMIT
```sql
SELECT column1 FROM table_name LIMIT number;
```
반환되는 행의 수를 제한

#### MIN(), MAX()
```sql
SELECT MIN(column1) FROM table_name;
SELECT MAX(column1) FROM table_name;
```
컬럼에서 가장 작은/큰 값을 반환

#### COUNT(), AVG(), SUM()
```sql
SELECT COUNT(column1) FROM table_name;
SELECT AVG(column1) FROM table_name;
SELECT SUM(column1) FROM table_name;
```
컬럼에서 집계 함수를 수행

#### LIKE
```sql
SELECT column1 FROM table_name WHERE column1 LIKE pattern;
```
컬럼에서 지정된 패턴을 검색

#### Wildcards
```sql
SELECT column1 FROM table_name WHERE column1 LIKE 'a%';
```
LIKE 연산자와 함께 와일드카드 (%, _)를 사용

#### IN
```sql
SELECT column1 FROM table_name WHERE column1 IN (value1, value2);
```
값이 지정된 값 세트 내에 있는지 확인

#### BETWEEN
```sql
SELECT column1 FROM table_name WHERE column1 BETWEEN value1 AND value2;
```
지정된 범위 내의 값을 선택

#### AS
```sql
SELECT column1 AS alias_name FROM table_name;
```
컬럼이나 테이블에 별칭을 부여

#### JOIN
```sql
SELECT columns FROM table1 INNER JOIN table2 ON table1.column = table2.column;
```
관련된 컬럼을 기반으로 두 개 이상의 테이블에서 행을 결합

#### UNION
```sql
SELECT column1 FROM table1 UNION SELECT column1 FROM table2;
```
두 개 이상의 SELECT 문의 결과 세트를 결합

#### GROUP BY
```sql
SELECT COUNT(column1) FROM table_name GROUP BY column2;
```
같은 값을 가진 행을 요약 행으로 그룹화

#### HAVING
```sql
SELECT COUNT(column1) FROM table_name GROUP BY column2 HAVING COUNT(column1) > value;
```
그룹에 조건을 적용

#### EXISTS
```sql
SELECT column1 FROM table_name WHERE EXISTS (SELECT column1 FROM table_name WHERE condition);
```
서브쿼리에 레코드가 존재하는지 확인

#### ANY, ALL
```sql
SELECT * FROM table_name WHERE column1 = any(1, 2, 3);
```
값을 목록의 모든 값과 비교 (SQLite에서 지원되지 않음)

#### SELECT INTO
```sql
SELECT column1 INTO new_table FROM table_name;
```
한 테이블에서 새로운 테이블로 데이터를 복사

#### CASE WHEN THEN
```sql
SELECT column1,
CASE
    WHEN condition THEN result
    ELSE result
END
FROM table_name;
```
쿼리에서 조건부 로직을 수행

#### IFNULL()
```sql
SELECT IFNULL(column1, 'default_value') FROM table_name;
```
식이 NULL인 경우 지정된 값을 반환

#### Stored Procedure
```sql
-- SQLite does not support stored procedures
```
저장된 SQL 문장 집합 (SQLite에서 지원되지 않음)

#### Comments
```sql
-- This is a single-line comment
/* This is a 
multi-line comment */
```
SQL 코드에 주석을 추가

#### Operators
```sql
SELECT column1 + column2 FROM table_name;
```
산술 연산을 수행

## SQL in Python
### [SQLite3](https://docs.python.org/3/library/sqlite3.html)

- `conn = sqlite.connect(path)`
    - `path`에 있는 Database에 연결
- `conn.commit()`
    - 변경사항을 데이터베이스에 저장
- `cursor = conn.cursor()`
    - 데이터베이스와의 상호작용을 위한 커서 객체 생성
- `cursor.execute(statement)`
    - SQL 문(statement)을 실행
- `cursor.fetchall()`
    - 모든 결과 행을 가져옴
- `cursor.description`
    - 결과 행의 열 설명 (메타데이터)

---

- 아래와 같이 함수 구성하여 database에 대해 SQL문 실행, 결과 데이터프레임 리턴
```python
def run_sql(statement, path='database.db', commit=False):
    try:
        with sqlite3.connect(path) as conn:
            cursor = conn.cursor()
            cursor.execute(statement)
            
            rows = cursor.fetchall()
            desc = cursor.description if cursor.description else []
            columns = [description[0] for description in desc]
            df = pd.DataFrame(rows, columns=columns)
            if commit:
                conn.commit()
            return df
    except sqlite3.Error as e:
        return e

statement = """
    SELECT * FROM Customers
"""

run_sql(statement)
```
