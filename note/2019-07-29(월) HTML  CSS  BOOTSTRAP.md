# HTML / CSS / BOOTSTRAP

**요청의 종류**

1. 줘라(Get)
2. 받아라(Post)



서버컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다.

사용자는 브라우저를 통해서 서버에 요청을 함.

**172.217.27.78 구글의 ip주소.** 

> 8비트0~255)까지의 숫자로 구성된 숫자의 집합

**google.com  = 도메인 네임**

> 네트워크상의 컴퓨터를 식별하는 호스트명

**URL**

htttps://www.google.com.

> 도메인 + 경로, 실제로 해당 서버에 저장된 자료의 위치

### Static Web (정적인 웹)

정해진 응답만 하는 것

접속 시 마다 내용이 변할 필요가 없는 사이트

ex) 학교 홈페이지, 댓글 기능이 없는 블로그



### Dynamic Web(동적인 웹)

상황에 맞게 변화하면서 제공해 주는 것.

접속할 때마다 변해야 할 필요가 있는 사이트

ex) 일반적인 웹사이트 (댓글 기능)



## HTML

Hyper Text Mark up Language

텍스트를 넘나드는 텍스트에 역할을 부여한 언어

웹페이지를 작성하기 위한 역할을 표시한 언어



## CSS

Cascating Style Sheets

HTML이 존재해야 CSS 도 존재함. HTML에 스타일을 입혀주는 것.



 ## Java Script







## HTML 문서의 기본 구조

```html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Hello World!</title>
    </head>
    <body>
        <!--이것은 주석입니다. 화면에 나오지 않아요.-->
        <h1>Hi, There! Introduce Jade!</h1>
        <h2>My favorite food is chicken!</h2>
    </body>
</html>
```



element 와 content로 구성되어 있다. element 소문자로 작성하는 것이 규칙

<img src="url"/> 같이 닫는 태그가 없는 것도 있다.



**속성**

<a href="google.com"> 	a태그는 링크를 만들기 위한 태그

속성은 HTML 전역 속성 중 일부로 모든 태그에서 사용 가능하다.

id : 유일한 식별자 (중복 지정 불가능)

class : 중복 지정 가능

style : 



Dom 트리

```html
<body>
    <h1>웹문서</h1>	body 태그와 h1태그는 부모-자식 관계
    <ul>
        <li>HTML</li>
        <li>CSS</li>
    </ul>
</body>
```

태그는 중첩되어 사용가능하며, 이때 위와 같은 관계를 갖는다.



시맨틱태그

```
<div>이것은 공간</div> -> division -> 공간 분할
공간 자체에 대한 어떠한 의미도 가지고 있지 않다.
```

개발자가 의도한 요소의 의미가 명확히 보인다.

코드의 가독성을 높이고 유지보수가 쉽다.



```html
<b> content </b>
<strong> content </strong>  시맨틱 태그

<ol>
<li>항목</li>
</ol>
<ul>
<li>항목</li>
</ul>

<div>의미 없는 블록</div>
<span>의미 없는 인라인</span>

<a href="google.com"/>  링크태그 a

<img src="/profile.jpg"/>

<video src="video.mp4"/>

<iframe src="https://www.w3schools.com"></iframe>  html에서 다른 html을 넣는 것


```



