# HMG_Softeer_Bootcamp_DE

현대자동차 소프티어 부트캠프 4기

240701~240829

## Learns

### Week 1
- Lecture
    - Data Engineering?
        - 데이터를 금전적 가치가 있는 정보로
    - Python programming standard: PEP 8
    - Simple Python version management: [pyenv](https://github.com/pyenv/pyenv)
    - What will we use?
        - JupyterLab / Jupyter Notebook
        - Pandas
        - Matplotlib
    - ETL (Extract, Transform, Load)

- mtcars 데이터셋 분석하기
    - Pandas
        - DataFrame 조작 및 정보 출력
    - Matplotlib
        - 다양한 수치를 시각화
        - plot, scatter, bar, etc.
    - Seaborn
        - 가독성 좋은 correation table

-  SQL Tutorial
    - Studied at [w3schools](https://www.w3schools.com/sql/default.asp)
    - 위 사이트에 없는 구문

- ETL 프로세스 구현하기
    - ETL 프로세스
        - Extract
            - 원시 데이터를 소스 위치에서 스테이징 영역으로 추출
            - 다양한 소스에서 데이터를 추출할 수 있고, 이는 정형 또는 비정형
            - 소스의 유형의 예시
                - SQL 또는 NoSQL 서버
                - 이메일
                - **웹페이지**
            - 사용한 라이브러리
                - requests
                - BeautifulSoup4
        - Transform
            - 스테이징 영역에서 원시 데이터를 처리함
            - 의도하는 분석 사용 사례에 맞게 변환 및 통합
            - 다음과 같은 작업을 포함할 수 있음
                - 데이터를 필터링, 정제, 중복 제거, 유효성 검사 및 인증
                - 원시 데이터를 기반으로 계산, 번역 또는 요약을 수행합니다. 여기에는 일관성을 위해 행 및 열 머리글 변경, 통화 또는 기타 측정 단위 변환, 텍스트 문자열 편집 등이 포함될 수 있음
                - 데이터 품질 및 규정 준수를 보장하기 위해 감사를 수행
                - 업계 또는 정부 규제 기관에서 관리하는 데이터를 제거, 암호화 또는 보호
                - 대상 데이터 웨어하우스의 스키마와 일치하도록 데이터를 테이블 또는 결합된 테이블로 포맷
        - Load
            - 변환된 데이터를 스테이징 영역에서 대상 데이터 웨어하우스로 이동
            - 일반적으로 모든 데이터를 처음 로드한 다음 증분 데이터 변경 사항을 주기적으로 로드
            - 드물게는 웨어하우스에서 데이터를 삭제하고 교체하는 전체 새로 고침을 수행하는 작업이 포함
            - 일반적으로 ETL은 소스 시스템과 데이터 웨어하우스의 트래픽이 가장 적은 근무 외 시간에 이루어짐

    - Logging
        - logging 라이브러리
        - datetime 라이브러리
            - strftime 메소드로 날짜/시간 포매팅



## Retrospective
|        | Mon | Tue | Wed | Thu | Fri |
| ------ | --- | --- | --- | --- | --- |
| Week 1 | [w1d1](retrospect/w1/d1_240701.md) | [w1d2](retrospect/w1/d2_240702.md) | [w1d3](retrospect/w1/d3_240703.md) | [w1d4](retrospect/w1/d4_240704.md) |     |
| Week 2 |     |     |     |     |     |
| Week 3 |     |     |     |     |     |
