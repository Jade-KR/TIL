# 2019-10-31 (목) | Java Script

### 자바 스크립트 함수의 특징

- 다른 함수의 인자로 함수를 넘길수 있다.

- 리턴 값이 함수일 수 있다.

- 변수에 함수를 담을 수 있다.



document는 html 문서

arrow function은 eventlistener에서 사용하지 않음.



```javascript
setTimeout(function() {
    console.log('3초 후 출력된다')
}, 3000)
29
```



call back 함수의 예시

```javascript
function doSomething(subject) {
    alert(`자 이제 ${subject} 과목 평가 준비 좀 시작해볼까??`)
}
undefined
doSomething(`django`)
undefined

function doSomething(subject, callback) {
    alert(`자 이제 ${subject} 과목 평가 준비 좀 시작해볼까??`)
	callback()
}
undefined
doSomething(`django`, function() {
	alert('내일이 시험인데??')
})

function doSomething(subject, callback) {
    alert(`자 이제 ${subject} 과목 평가 준비 좀 시작해볼까??`)
	callback()
}
undefined
doSomething('django', alertFinished)
```



eventlistener = 무엇을 언제 어떻게 하겠다~

html에 자바 스크립트는 일반적으로 아래에 작성한다. (돔이 그려져야 함,

돔 조작에 해당하는 코드가 아직 그려지지 않았기 때문에)



```javascript

```



- 비동기 : 여러가지 일을 동시에 할 수 있음 (NonBlocking)
- 동기 : 일의 순서대로 진행되어야함(Blocking)



구글 axios 검색 github에 사용법 나와있음.

- install npm

- Using cdn 



```javascript
axios.get('https://dog.ceo/api/breeds/image/random')
Promise {<pending>}__proto__: Promise[[PromiseStatus]]: "resolved"[[PromiseValue]]: Object
axios.get('https://dog.ceo/api/breeds/image/random')
.then(res => console.log(res))
Promise {<pending>}
VM192:2 {data: {…}, status: 200, statusText: "", headers: {…}, config: {…}, …}config: {url: "https://dog.ceo/api/breeds/image/random", method: "get", headers: {…}, transformRequest: Array(1), transformResponse: Array(1), …}data: message: "https://images.dog.ceo/breeds/pinscher-miniature/n02107312_7.jpg"status: "success"__proto__: Objectheaders: {content-type: "application/json", cache-control: "no-cache, private"}request: XMLHttpRequest {readyState: 4, timeout: 0, withCredentials: false, upload: XMLHttpRequestUpload, onreadystatechange: ƒ, …}status: 200statusText: ""__proto__: Object
axios.get('https://dog.ceo/api/breeds/image/random')
.then(res => console.log(res.data.message))
Promise {<pending>}
VM620:2 https://images.dog.ceo/breeds/terrier-wheaten/n02098105_321.jpg
```





