# 2019-10-29 (화) | Java Script

## 기본 세팅

- node js 설치
- beautify, Live Server, auto close tag, Rainbow Brackets, indent-rainbow 확장파일 설치
- javascript는 indenting이 2 space라서 설정 해줘야함

ctrl + shift + p => json -> preference.open.settings

```
{
    "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
    "workbench.iconTheme": "vscode-icons",
    "[python]": {
        "editor.tabSize": 4,
    },
    "editor.tabSize": 2,
    "editor.detectIndentation": false
}
```

file - preference - settings - commonly used - tabe size = 2 - Text Editor - [Editor: Detect Indentation](#)  check



```javascript
// 변수와 식별자
// var로 선언된 변수의 범위는 현재 실행 문맥 -> 함수 or 함수 외부 전역

var x = 1

if (x === 1) {
  var x = 2
  console.log(x)
}
console.log(x)


// let -> 값을 재할당 할 수 있는 변수 선언 키워드 (선언은 한번만, 할당은 여러번 가능)
// 블록 스코프

let x = 1
console.log(x)
x = 3
console.log(x)


let x = 1

if (x === 1) {
  let x = 2
  console.log(x) // 2
}
console.log(x) // 1


// const -> 상수, 값이 변하지 않는 상수를 선언하는 키워드
// 담긴 값이 변하지 않는 다는 의미가 아니라 단지 상수의 값은 재할당을 통해 바뀔 수 없고
// 재선언 될 수 없다.
// 블록 스코프

//const MY_FAV

const MY_FAV = 7
console.log(MY_FAV)
console.log("My favorite number is " + MY_FAV)
// MY_FAV = 20

const MY_FAV = 20

const MY_FAV = 7

if (MY_FAV === 7) {
  const MY_FAV = 20
  console.log("My favorite number is " + MY_FAV) // 20
}
console.log(MY_FAV) // 7


// let과 var의 scope 비교

// var
function varTest() {
  var x = 1
  if (true) {
    var x = 2
    console.log(x) // 2
  }
  console.log(x) // 2
}

varTest()


// let
function letTest() {
  let x = 1
  if (true) {
    let x = 2
    console.log(x) // 2
  }
  console.log(x) // 1
}
console.log(x) // 에러 (함수 밖이라서)
letTest()



var a = 1
var b = 2

if (a === 1) {
  var a = 11
  let b = 22

  console.log(a) // 11
  console.log(b) // 22
}
console.log(a) // 11
console.log(b) // 2

// var: 할당 및 선언 자유, 함수 스코프(현재 실행 문맥)
// let: 할당 자유, 선언은 한번만, 블록 스코프
// const: 할당 및 선언 한번만, 블록 스코프


// 변수와 식별자 - 식별자
// 객체, 변수, 함수 -> 카멜 케이스(lower-camel-case)

// 숫자, 문자, 불리언
let dog
let variableName

// 객체(Object)
const memberInfo = {
  id: 1,
  password: 12345,
  gender: 'male'
}

// 배열 - 배열은 보통 복수형을 사용
const dogs = []

// 정규표현식 - 'r'로 시작
const rDesc = /ab+c/

// 함수
function getPropertyName() {

}

// 이벤트 핸들러 - 이벤트 핸들러는 'on'으로 시작
const onClick = () => {}
const onKeyDown = () => {}

// boolean을 반환하는 함수 -> return 값이 불리언인 함수는 'is'로 시작
let isAvailable = false


// 파스칼 케이스(Upper-camel-case) - 클래스, 생성자
class User {
  constructor(options) {
    this.name = options.name
  }
}

const good = new User({
  name: 'yup',
})

console.log(good)
console.log(typeof good)

// 대문자 스네이크 케이스(_) - 상수
export const API_KEY = 'SOMEKEY'

export const MAPPING = {
  key: 'value'
}
```

```javascript
// Hoisting!
// 나중에 선언된 변수를 참조 할 수 있음
// 함수 or statement 최상단으로 올려지는 것 (hoisting)
// 변수와 함수를 위한 메모리를 확보하는 과정

// console.log(a)
// var a = 10
// console.log(a)

console.log(b)
let b = 10
console.log(b)
```

