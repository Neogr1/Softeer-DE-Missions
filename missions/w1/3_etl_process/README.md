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