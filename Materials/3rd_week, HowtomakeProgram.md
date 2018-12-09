##### 3회차- 파이썬 문법강의 II  (:)

- 함수란?

  함수를 만드는 방법

  함수를 실행하는 방법

  전역변수와 지역변수

- 모듈과 패키지란?

- 프로그램을 제어하는 기초 1 . 분기문 - if문	

- 프로그램을 제어하는 기초 2 . 반복문 while, for 문



# 함수란?

반복적인 작업을 담는 ‘그릇’  어떠한 프로그램의 프로세스를 담아둔것.

함수로 어떠한 작업을 모듈화 해 놓으면 어떤 부분에서 에러가 발생했는지 편하고, 재사용 하기가 편하다.

### 함수를 만드는 방법

```python
def nameprinter(name):
	print(name)
    lastname = name[0]
	return lastname
```

def (definition)으로 함수를 작성한다. 함수를 작성 후에는 : (콜론)을 꼭 붙여야한다. 

* nameprinter는 함수의 이름이고, name은 함수의 변수이다. 이 변수는 함수의 안에서 사용된다. 

* 아래의 명령문이 함수에 소속되어있다는 것을 알기 위해서는 스페이스 4칸 (혹은 Tab)을 사용한다. 이를 Indentation이라 하는데, 매우 중요한 개념이며, 파이썬만이 가지고 있는 특징이다. (다른 언어는 {} 등으로 표시함)
* 함수내에서 사용되는 변수는 ‘지역변수, Local Variable’ 로서 함수 안에서만 사용할 수 있다. 
* 이러한 것을 메인 함수에 있는 변수 (전역변수)로 이용하기 위해서는 return을 통해 함수 값을 전달한다. 아래의 예시를 보자
* 리턴을 하는 순간 함수는 끝난다.

### 함수를 실행하는 방법

```python
if __name__ == "__main__":
    professor_name = input("교수님의 이름은 무엇입니까?")
    professor_last = nameprinter(professor_name)
    student_name = input("학생의 이름은요?")
    student_last = nameprinter(student_name)
```

1)아무 indentation이 없는 곳에 함수를 쓰던가

2)if __name__ == "__main__": 밑에 인덴테이션을 넣어 적어준다. 이 name == “main”은 추후 모듈과 패키지에서 좀 더 자세히 설명한다.

```python
def test_a():
    print("안녕하세요, test_a입니다")
    try:
        print(tutor)
    except:
        print("no tutor!")
        pass
    return

def test_b(tutor):
    print(professor)
    print(tutor)
    return

def test_c(tutor):
    print("test_c입니다")
    professor = "cloud"
    print(f"교수님은 {professor}")
    print(f"튜터는 {tutor}")
    return

if __name__ == "__main__":
    tutor = 'cloud'
    professor = '조성준교수님'
    print(f"교수님은 {professor}")
    test_a()
    test_b(tutor)
    print("1번째 test_b 완료")
    test_b(professor)
    print("2번째 test_b 완료")
    print(f"교수님은 {professor}")
    
```

파이썬은 ‘스크립트’ 언어다. 위에서부터 아래까지 읽으면서 기본적인 문법오류( : 이 빠져있나등의 여부)를 검사한다. 

이후 if__name__==“__main_”: 부분을 실행하게 된다.

여기서 주목해야하는점은.

1)매개변수가 없어도 된다.

​	*test_a를 보면 알겠지만, 매개변수가 없어도 함수는 만들고, 실행될 수 있다.

2)함수 안의 변수는 함수 안에서만 쓸 수 있다.

​	*위의 함수를 실행시키면 에러가 뜬다. 왜냐하면 test_b에서 함수 안에 들어간 변수는 tutor인데, professor를 이용하려고 하고있기때문이다. 아래의 함수를 보자.

3.함수의 매개변수는 꼭 같은 이름일 필요가 없다 (순서대로 파이썬은 인식한다.)

​	*test_b(tutor)를 보면 test_b에 무조건 tutor가 들어가야하는것 같지만, 우리가 인지하기 편하게 tutor라는 것을 함수 안에서 사용할 뿐이지, 컴퓨터는 순서대로 변수를 인식한다. 

```python
def hello_sungjun():
	name = "sungjun"

name="cloud"
print(name)
hello_sungjun()
print(name)
```

함수를 실행시키면 name이 sungjun으로 할당되었기때문에 바뀔것 같지만, 메인 함수에서 return을 해주어야한다.

```python
def hello_sungjun():
	name = "sungjun"

name="cloud"
print(name)
name = hello_sungjun()
print(name)
```

자 이 스크립트의 결과가 어떨것 같은가? 예상한대로일것이다. 이렇듯 함수 안과 밖의 변수는 다르게 이용된다는 점을 기억하자.

# 모듈과 패키지란?

파이썬 하나하나의 .py파일은 모듈로서 이용할 수 있다. 아래의 예를 보자.

```python
#아래의 함수는 namehello.py에 있음.
def hello_sungjun():
	print("sungjun")
```



```python
#아래의 코드는 main.py에 있음
import namehello as nh

nh.hello_sungjun()
```

두개의 파일이지만, 이러한 식으로 부를 수 있다는 것.

아나콘다는 이러한 여러개의 파일 (패키지)들을 설치환경에 다운로드받아놓았다. 

파이썬은 이런 패키지들을 pip라는 것으로 관리하는데, 아래의 명령을 사용해보자

```python
pip install numpy
```

아마, 이미 다운로드 되어서 안될것이다. 넘파이를 업그레이드해보자.

```python
 pip install --upgrade numpy 
```

이렇듯, 패키지들은 우리의 컴퓨터에 설치되어있기때문에 부를 수 있는것이다. 이러한 패키지에 대한 이용은 나중에 다시 설명할 기회가 있으니 이런 개념만 일단 들고가자. 

# 프로그램을 제어하는 기초 1 . 분기문 - if문

만약에..내가만약에..★

AI도, 컴퓨터도 모두 정해놓은 분기문에 따라 반복작업을 수행하는것이다. AI는 이러한 if문에 대한 변수들을 학습하고, 사용하는것이다. 그러한 ‘분기’를 하는것이다. 

## if, elif, else:

```python
def namechecker(name):
    if "성준" in name:
        print("혹시 조교수님?")
    elif "글경" in name:
        print("글경관계자세요?")
    elif "cloud" in name:
        print("운한이니?")
    else:
        print("누구...?")

namechecker((input("이름을 밝히시오    ")))
```

아래의 입력어에 대한 결과가 무엇일까?

1)조성준

2)Cloud

3)글경 조성준

elif문이 위에있을수록 우선순위가 커진다. 그리고 이러한 실수가 있기 쉽다.

```python
def namechecker(name):
    if "성준" in name:
        print("혹시 조교수님?")
    elif "글경" in name:
        print("글경관계자세요?")
    elif "cloud" in name:
        print("운한이니?")
    elif "가천" or "교수" in name:
        print("아이쿠야!")
    else:
        print("누구...?")

namechecker((input("이름을 밝히시오    ")))
```

자 여기서 ‘유진영’을 입력하면 어떻게 될까?

```python
def namechecker(name):
    if "성준" in name:
        print("혹시 조교수님?")
    elif "글경" in name:
        print("글경관계자세요?")
    elif "cloud" in name:
        print("운한이니?")
    elif ("가천" in name) or ("교수" in name):
        print("아이쿠야!")
    else:
        print("누구...?")

namechecker((input("이름을 밝히시오    ")))
```

컴퓨터는 어떠한 값이 있다는 자체로 True이므로 elif문에서 빠져나갈 수 없던것이다. 고로 분기문을 쓸때는 잘 보고, 테스트도 여러번 해보아야한다. 인간의 언어에 닮아있지만, 인간의 언어가 아니다.



# 프로그램을 제어하는 기초 2 . 반복문 for 문

자, 이제 우리는 분기문을 배웠으니, 반복문을 배워야한다. 반복문은 꽃이다. 이러한 반복문을 통해 우리는 반복하고, 프로그램의 진가를 발휘한다.

## for

일정한 배열들에 대해 하나씩 반복 (iterate) 한다. 

```python
for i in range(5):
	print(i)
	print("으아아악")
```

range(n) : 0부터 시작해 n-1개까지 반복한다.

```python
namelist = ["박운한", "조성준", "이선무"]
for name in namelist:
	print(name)
```



# 실습과제

```python
jsonlized_namelist = {"name" : ["박운한", "홍주평", "이선무", "전상훈"], "company" : ["SAP", "IBM", "미국", "군대"]}
```

이 리스트를 통해 갈 수 있는 모든 조합을 

그는 {이름}, {회사}에 갈 수 있습니다. 식으로 출력해라.

*****아래는 보지 마시오.







정답은 이중 for문.

```python
for name in jsonlized_namelist['name']:
	for jobs in jsonlized_namelist['company']:
		print(f"{name}은 {jobs}에 갈 수 있습니다")
        
박운한은 SAP에 갈 수 있습니다
박운한은 IBM에 갈 수 있습니다
박운한은 미국에 갈 수 있습니다
박운한은 군대에 갈 수 있습니다
홍주평은 SAP에 갈 수 있습니다
홍주평은 IBM에 갈 수 있습니다
홍주평은 미국에 갈 수 있습니다
홍주평은 군대에 갈 수 있습니다
이선무은 SAP에 갈 수 있습니다
이선무은 IBM에 갈 수 있습니다
이선무은 미국에 갈 수 있습니다
이선무은 군대에 갈 수 있습니다
전상훈은 SAP에 갈 수 있습니다
전상훈은 IBM에 갈 수 있습니다
전상훈은 미국에 갈 수 있습니다
전상훈은 군대에 갈 수 있습니다
```





