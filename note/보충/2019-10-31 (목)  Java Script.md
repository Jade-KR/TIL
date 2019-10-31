# 2019-10-31 (목) | 보충

- console(browser)
- node(파일로 작용할 수 있는 것)



#### 변수, 상수를 선언할 수 있는 세가지

- var (ES5) - hoisting 선언을 끌어올리면서 초기화가 동시에 이루어짐
- let (ES6+) - 선언 1, 재할당 가능
- const (ES6+) - 선언, 할당 둘 다 1번 가능 (함수는 const)

**var 와 let, const를 구분하고 let 과 const를 구분**



lower camel case

upper camel case

snake case  - 보통 상수를 선언할때 (전부 대문자)



#### null 과 undefined 차이

- 잘못만들었음.. 
- type -> object, undefined



#### NaN = Not a Number

- undefined + 1



#### 문자열 표현

- single quote
- double quote
- back tic - 줄바꿈 가능, f string처럼 사용 가능



동등연산자

비교연산자

자동 형변환 ( 1 == '1'  -> true)

일치 연산자 (===)



switch ( case에 맞는 조건일때, break 필요, break 안하면 default까지 돌아감 )



eventlistener는 function을 사용함



callback은 익명 뿐만 아니라 기명 함수도 넘길 수 있다.





#### 인자가 없을 때 -> (), _ 표현 가능

let noArgs = () => 'No args'

console.log(noArgs())



noArgs = _ => 'No args'

console.log(noArgs())



익명함수 쓰는 방법

- 변수에 담아 사용
- 즉시실행함수



## object와 json의 차이

object - 자바스크립트에서 key와 value의 자료구조로 표현된 객체

json - 데이터를 자바스크립트의 object 형태로 표현하기 위한 string





#### callback 함수

- 비동기 요청
- setTimeout - 첫번째 인자로 callback 함수를 받음. 2번째 인자는 초
- 나중에 다시 불러주는 함수



자바스크립트 3가지 조건

- 함수를 변수에 담을 수 있다.
- 리턴값이 함수가 될 수 있다.
- 함수를 인자로 전달 할 수 있다.



DOM 조작

- (BOM) browser object model 
- DOM조작
- 일반적인 프로그래밍



돔조작 - script 태그 안에 자바 스크립트 작성



eventlistener 무엇을 언제 어떻게 한다.

어떻게는 2번째 함수에 정의된 것.