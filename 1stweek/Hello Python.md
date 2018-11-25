# 오늘의 목표

- 파이썬의 소개와 개발환경 설치 
- 네트워크 기초와 패키지에 대한 이해 (셀레니움과 BS4 사용)
- 파이썬과 친해지기 1 (대화형 인터프리터)
  - 사칙연산, 변수, 데이터타입
  - "Hello World" 

https://wikidocs.net/4307

https://wikidocs.net/4307

------

# 파이썬 소개와 개발환경 설치

![img](https://wikidocs.net/images/page/5/pahkey_KRRKrp.png)

## 파이썬? 프로그래밍 언어. 

1990년 암스테르담의 귀도 반 로섬(Guido Van Rossum)이 개발한 인터프리터 언어이다.  크리스마스에 할일없어서 만든것임. 

##### ‘인터프리터 언어’ 파이썬

우리가 쓰는 언어는 **‘Text**’, 컴퓨터가 읽을 수 있는 언어는 ‘0 or 1으로 불리는 **‘바이너리’**언어.  우리가 쓴 Text를 컴퓨터가 읽는 바이너리 파일로 바꾸는 것이 **‘컴파일’** 

C나 C++, 자바등은 실행 전에 미리 컴파일하는 **‘컴파일 언어’**, 파이썬은 실행 즉시 ‘인터프리터(번역기)‘ 가 컴파일하는 **인터프리터 언어**. 코드가 비교적 쉽고 단순하나, 속도가 비교적 느리다는 단점이 있음.

## 개발환경 설치

##### Anaconda

과학/연구용 파이썬 패키지들을 모두 모아 배포하는 패키지. 필요한 여러 패키지가 미리 설치되어 있어서 한번에 설치하기 유용함. 

##### Pycharm

파이썬 코드를 작성할  ‘IDE’ (프로그램 안에서 모든것을 해결할 수 있게 해둔 프로그램) 코드작성을 위해 사용할것임.

**터미널이란?**

개발자들이 많이 쓰는 검정 화면은 ‘CLI’ (Command Line Interface)라고도 불림. DOS때처럼 명령어를 실행하는것임. 많은 부분이 GUI되어있지만 여전히 코드 실행은 터미널에서 하는것이 일반적. 터미널에서 사용할 수 있게 윈도우에 등록해두어야하는데, 설치시 누르면 자동으로 등록이 됨.

------

# 네트워크 기초와 패키지에 대한 이해

## 웹은 어떻게 구성되어있나?

인터넷 브라우저에 떠있는 화면은 모두 ‘텍스트’로 구성되어있음.

F12를 눌러 확인해볼것.

- 화면의 골격과 내용을 구성하는 ‘HTML’
- 화면을 아름답게 꾸며주는 ‘CSS’
- 화면에 보이는 다양한 애니메이션과 통신을 위한 ‘JavaScript’

로 구성되어있음. 

## 우리는 어떻게 웹을 가져오는가?

우리가 크롤링을 위해서 다양한 패키지를 사용할 것이지만, 아주 크게는 3가지 부분이라고 볼수 있음. 파이썬의 많은 부분은 이미 개발되어 공유되고 있는 ‘라이브러리’ 형태를 띄고있음.

- 파이썬 > 모든 프로그래밍 동작을 관리함. 패키지들이 작동할 수 있게 모든 코드가 파이썬으로 짜여짐
- BeautifulSoup4 (Bs4) > HTML을 ‘텍스트’가 아닌, ‘HTML’로 읽어주는 파이썬 라이브러리 (모듈, 패키지).
- 셀레니움 > ‘자동화 테스트 프로그램’. 보통은 웹 개발시 구성요소들이 잘 동작하는지 테스트하기 위해 사람이 하는것과 동일한 행동을 하게 프로그래밍 할 수 있음. 우리는 이것을 통해 자동화를 할 것임.
- 크롬드라이버 > 셀레니움이 조작할 대상은 ‘브라우저’. ‘브라우저’를 어떻게 다루는지 알려주는 드라이버.
- 그리고...여러 패키지

------

# 파이썬 실습, Hello, world!

Teminal 실행 (cmd나 Powershell)

##### 기본적인 터미널 동작 실습 

```
cd [디렉토리명] : 원하는 폴더로 가기
cd .. : 앞으로 돌아가기
dir : 폴더 안에 있는 파일들 보기
python : 파이썬 인터프리터 실행 - 변수설정이 되어있어야 실행이 됨.
```



##### 파이썬 실습 1 - 사칙연산

```python
>>> 1 + 2
3
>>> 1 - 2
-1
>>> 2 * (2+1)
6
>>> 3 / 2.4
1.25
>>> 3 * 9.5252
28.5756
>>> 10 %3
1
```

##### 파이썬 실습 2 - 변수 넣기 (숫자)

이제 당신도 개발자와 대화할 수 있다! a =1 과, a == 1은 다르다!

```python
>>> a = 1
>>> a #a 에 1을 대입.
1
>>> a == 1 
True
>>> a == 2
False
>>> a =2
>>> a == 1
False
>>> a == 2
True
>>> a == '2'
False
```

9과 10이 다른 이유는 파이썬만의 독특한 특징때문임. 파이썬은 데이터타입을 알아서 지정한다! (그래서 에러도 많이난다)   1과 ‘1’은 다르다!  데이터타입때문이다.

##### 파이썬 실습 3 - 데이터타입 확인

```python
a = 1
b = '1'
c = 1.0

>>> type(a)
<class 'int'>
>>> type(b)
<class 'str'>
>>> type(c)
<class 'float'>
```

##### 파이썬 실습 3 -1 - 데이터타입 비교하기, (정수와 실수)

정수와 실수 (int, float)는 비교가 가능하다. 

```python
>>> a = 1
>>> b = '1'
>>> a == b
False

>>> a = 1
>>> b = 1.0
>>> a == b
True
>>> a > b
False
>>> a >= b
True
```



##### 파이썬 실습 3 -2 - 데이터타입 비교하기 0과 1, True False (Boolean)

컴퓨터이기때문에 숫자 0과 1은 각각 False와 True를 의미한다.

```python
>>> a = 1
>>> a == True
True
>>> a == False
False
>>> a = '1'
>>> a == True
False
>>> a == False
False
>>> a = 0
>>> a == True
False
>>> a == False
True
```



##### 파이썬 실습 4-1 - 데이터타입 바꾸기 (1)

데이터타입을 알아서 지정하는것을 ‘동적 타이핑 언어’라고 한다. 자신이 원하는 데이터타입으로도 변환할 수 있다.

```python
>>> a = 1
>>> a
1
>>> type(a)
<class 'int'>
>>> a = str(a)
>>> a
'1'
>>> type(a)
<class 'str'>
```

##### 파이썬 실습 4-2 - 데이터타입 바꾸기 (2)

물론, 안되는건 안된다. 형 변환이 가능한 경우가 있고 ,없는경우가 있다. 

```python
>>> a = '안녕하세요'
>>> a = int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '안녕하세요'

>>> a = 1.0
>>> a = str(a)
>>> a
'1.0'
>>> a  = int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '1.0'
>>> a  = float(a)
>>> a
1.0
```

##### 파이썬 실습 5, Finally, “Hello, World”

```python
>>> print('Hello, World')
KeyboardInterrupt
>>> print("Hello, World")
Hello, World
>>> print('Hello, World')
Hello, World
>>> print('Hello, World")
  File "<stdin>", line 1
    print('Hello, World")
                        ^
SyntaxError: EOL while scanning string literal
```

