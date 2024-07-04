# ETL Process 구현하기

## 목표
웹사이트에서 데이터를 가져와 요구사항에 맞게 가공하는 ETL 파이프라인 제작
- web scraping
- Pandas dataframe
- ETL process
- database & SQL


## 시나리오
나는야 해외로 사업을 확장하고자 하는 기업의 Data Engineer\
경영진은 GDP가 높은 국가들을 대상으로 사업성을 평가하려 하지\
경영진이 지속적으로 요구하는 자료에 대한 자동화된 스크립트를 만들어야 해

## 요구사항
- IMF에서 제공하는 국가별 GDP를 구하세요. [link](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29)
- 국가별 GDP를 확인할 수 있는 테이블 제작
- 테이블은 GDP에 대해 내림차순
- GDP의 단위는 1B USD, 소수점 2자리까지.
- IMF에서 매년 2회 이 자료를 제공하기 때문에 정보가 갱신되더라도 해당 코드를 재사용해서 정보를 얻을 수 있어야 함.

## 팀 활동
- wikipeida 페이지가 아닌, IMF 홈페이지에서 직접 데이터를 가져오는 방법은 없을까요? 어떻게 하면 될까요?
    - IMF에서 제공하는 [DB](https://www.imf.org/en/Publications/WEO/weo-database/2024/April)를 이용
- 만약 데이터가 갱신되면 과거의 데이터는 어떻게 되어야 할까요? 과거의 데이터를 조회하는 게 필요하다면 ETL 프로세스를 어떻게 변경해야 할까요?
    - 과거의 데이터 보존이 필요한가? -> 경영진에게 문의 필요
    - 필요하다면
        1. 백업 디렉터리로 json 파일 이동
        2. 과거의 데이터를 조회할 수 있는 곳이 있다면 기간을 지정해서 동적으로 조회할 수 있도록 하기
        3. DB에 Year, Quarter 같은 새로운 column을 추가해서 사용