# Web Scraping

웹사이트에서 데이터를 추출하여 수집하는 기술
특정 웹페이지의 내용을 자동으로 가져와 분석하거나 데이터베이스에 저장

## BeautifulSoup
HTML과 XML 문서를 파싱하기 위한 파이썬 라이브러리
tag, attribute, text 등을 기반으로 문서의 특정 부분을 검색하고 조작
다양한 파서(parser)를 지원하며, 기본적으로는 내장된 HTML 파서를 사용

```python
from bs4 import BeautifulSoup
import requests

url = 'http://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 특정 태그의 내용 추출
title = soup.find('title').get_text()
print(title)
```