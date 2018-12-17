##### 4회차 - 파이썬 문법강의 III, 그리고 웹

- 프로그램을 제어하는 기초 2-2 . 반복문 while 문
- 프로그램을 제어하는 기초 3. 에러  try and except
- 과제 - Job Korea Crawler 확인
- 웹 서비스를 구성하는 요소들 (HTML5, CSS, JS ) 분석하기
- Bs4 (BeautifulSoup4) 문법 알아보기

# 프로그램을 제어하는 기초 2-2 . 반복문 while 문

while문 : 일정한 조건 (True, False)를 만족하는 이상 지속적으로 동작하는 구문

```python
work = True
namelist = ["cho", "park", "lim", "kim"]

while work == True:
    for i in namelist:
        print(i)
        if i == "lim":
            print("임씨를 찾았습니다!")
            print(namelist.index(i))
            work = False
else:
    break
```

위의 처럼 특정 조건이 만족될때 까지 반복적으로 일정 동작을 수행시키고 싶을때 While문을 사용한다.

이러한 while문의 조건이 만들어지지 않을 경우 무한루프에 빠진다.

# 프로그램을 제어하는 기초 3. 에러  try and except

```python
try:
    a = driver.find_element_by_class_name('coreSpriteRightPaginationArrow').is_enabled()
    if a == True:
        driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
    else:
        time.sleep(3)
        driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
except exception as e:
    print(e)
    print("이 사진이 마지막 사진입니다")
    arrow = 1
    break
finally:
    print("%s 번째 루프가 끝났습니다." %i)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

```

try : 실행하고픈 문장. 이 문장이 진행중 에러가 발생된다면 except 문장으로 넘어간다.

에러처리를 한 후에 finally 문장으로 처리하고픈 문장을 지정할 수 있다.

이중 원하는 에러만 원해서 추가할 수 있다.  에러에 대한 추가적인 정보는 다음 링크를 참조하자

https://wikidocs.net/30

# 과제 - 잡코리아 기본 크롤러

https://github.com/vividcloudpark/FirstStepToPython/blob/master/Materials/Code/3rd%20assignment_company_info_crawler.py

과제는 잘 푸셨는지? 총총?

# 웹 서비스를 구성하는 요소들 (HTML5, CSS, JS ) 분석하기

```python
name_container = company_info_soup.find("div", class_="company-header-branding-body")
```

대체 이 코드는 어떤 코드인것인지? 궁금하진 않으셨는지?

soup에서 find를 한다는데. div, 그리고 class라는것이 보인다. 대체 이게 무엇일까?

### HTML, CSS, JS의 관계

- HTML, CSS, JS는 웹 화면을 구성하는 구성요소라고 볼 수 있음.
- HTML은 *HyperText Markup Language* 로서, 구성요소에 대해 “Mark Up”을 함.
- CSS는 Cascading style sheet로서 HTML이 마크해놓은 것에 대해 ‘스타일’을 지정함.
- Javascript는 어떠한 행동에 맞추어 팝업 등을 띄우는데 사용.
- 인터넷 브라우저는 이러한 HTML CSS JS를 해석하는 인터프리터라고도 볼 수 있음.

### 정적 웹 동적 웹, 그에 따른 크롤링 방식의 차이

##### 정적 웹인 경우

- 잡코리아의 경우 정적웹 (사이트 이동에 따라 주소창의 주소가 달라짐), 이 경우 브라우저를 대신해서 주소에 대한 요청과 응답을 읽어주는 모듈(urllib)를 통해 정보를 받고, Bs4를 통해 HTML을 분석함.
- 브라우저가 읽어서 표시하는 시간이 없고, 자바스크립트를 로딩하지 않아도 될 경우 (로딩 즉시 모든 데이터를 얻을 수 있는 경우 사용.

##### 동적 웹인 경우.

- 그에 비해 동적앱인 경우는 주소창이 달라지지 않는 경우를 볼 수 있음. ex인스타그램, 페이스북 등
- 그 이외에 클릭을 해야 데이터가 받아와 지는 경우도 동적웹이라고 볼 수 있음.
- 이 경우 실제로 사용자가 필요한 정보를 얻기 위해서는 클릭, 스크롤 등을 해야함. 이러한 행동을 파이썬 코드로 가능하게 해주는 것이 셀레니움.
- 셀레니움을 통해 브라우저의 페이지를 로드하고, 그 로드한 HTML을 Bs4로 받아와 분석함.
-

### 기본적인 html 문법

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

HTML은 <태그> </태그> 사이에 값을 지정하여 사용함. 한번 태그가 열리면 무조건 닫혀야함.

각각의 것들을 element라고 부름.

그 이외에 대해서는 W3CSchool https://www.w3schools.com/html/ 을  참고할 것.

### Class와 ID

```html
<div id="goog-gt-tt" class="skiptranslate" dir="ltr">
번역 제안하기<
/div>
```

id : 특정 단 ‘하나’의 객체에 대해 호출하기 쉽게 이름표를 붙여둔 것

class : 여러개의 객체에 대해 사용될 수 있도록 이름표를 붙여둔것.

id과 class가 있을때, 우리가 원하는 것을 가져올려면 id를 선택하는것이 바람직하다.

Bs4 문법 알아보기

```python
soup = BeautifulSoup(HTMLpage, "lxml")
info = soup.find_all("div", class_="table-basic-infomation-primary")
info[0].get_text()
```
- 우선 HTML 페이지를 BeautifulSoup가 읽을 수 있는 'Soup'객체로 변환시켜야 한다.
- 이후에는 find와 find_all을 통해서 검색을 한다.
- find의 경우 조건 (위의 경우 div중 class가 table-basic-infomation-primary인것) 중 가장 먼저보이는 ** 단 하나 ** 를 반환를 한다.
- , find_all의 경우에는 페이지 상의 모든 객체를 **리스트** 형식으로 반환한다 (단 하나라도! ) 그래서 인덱스를 통해 접근이 필요하다.
- 이후 get_text()는 `<div> 와</div>`사이의 값을 가져온다.
