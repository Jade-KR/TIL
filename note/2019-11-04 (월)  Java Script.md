# 2019-11-04 (월) | Java Script

https://docs.thecatapi.com/

get all public images 클릭

주소만 복사 https://api.thecatapi.com/v1/images/search

```javascript
Live reload enabled.
axios.get('https://api.thecatapi.com/v1/images/search')
Promise {<pending>}
axios.get('https://api.thecatapi.com/v1/images/search')
.then(res => console.log(res))
Promise {<pending>}
VM275:2 
{data: Array(1), status: 200, statusText: "", headers: {…}, config: {…}, …}
config: {url: "https://api.thecatapi.com/v1/images/search", method: "get", headers: {…}, transformRequest: Array(1), transformResponse: Array(1), …}
data: Array(1)
0: {breeds: Array(0), id: "9pr", url: "https://cdn2.thecatapi.com/images/9pr.jpg", width: 1024, height: 678}
length: 1
__proto__: Array(0)
headers: {content-length: "102", last-modified: "Mon Nov 04 2019 01:46:01 GMT+0000 (Coordinated Universal Time)", content-type: "application/json; charset=utf-8", cache-control: "post-check=0, pre-check=0", expires: "Tue, 03 Jul 2001 06:00:00 GMT"}
request: XMLHttpRequest {readyState: 4, timeout: 0, withCredentials: false, upload: XMLHttpRequestUpload, onreadystatechange: ƒ, …}
status: 200
statusText: ""
__proto__: Object

axios.get('https://api.thecatapi.com/v1/images/search')
.then(res => console.log(res.data[0].url))
```

### 고양이 만들기

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style>
    img {
      width: 300px;
      height: 300px;
    }
  </style>
</head>
<body>
  <h1>댕댕이</h1>
  <div class="animals"></div>
  <button id="dog">댕댕이 내놔</button>
  <button id="cat">고양이 내놔</button>

  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script>
    const getDogImage = () => {
      // axios로 get 요청을 보낸다
      axios.get('https://dog.ceo/api/breeds/image/random')
      // 약속이 잘 지켜져서 응답이 오면
      .then(res => {
        // 이미지를 추출해 imgUrl에 담는다.
        const imgUrl = res.data.message
        // 이미지 태그를 만든다.
        const imgTag = document.createElement('img')
        // 이미지 태그의 src 속성에 imgUrl을 넣는다.
        imgTag.src = imgUrl
        // 원하는 위치에 이미지를 넣자!
        document.querySelector('.animals').append(imgTag)
      })
      .catch(err => console.log(err))
    }

    const getCatImage = () => {
      axios.get('https://api.thecatapi.com/v1/images/search')
      .then(res => {
        const imgUrl = res.data[0].url
        const imgTag = document.createElement('img')
        imgTag.src = imgUrl
        document.querySelector('.animals').append(imgTag)
      })
      .catch(err => console.log(err))
    }

    const dogButton = document.querySelector('#dog')
    dogButton.addEventListener('click', getDogImage)

    const catButton = document.querySelector('#cat')
    catButton.addEventListener('click', getCatImage)

  </script>
</body>
</html>
```



## 좋아요 비동기 요청 만들기

base.html에 <script src="https://unpkg.com/axios/dist/axios.min.js"></script>

```html
{% load bootstrap4 %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://kit.fontawesome.com/8d054fca2e.js" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    {% bootstrap_css %}
    <style>
        div > h3 {
            color: powderblue;
        }
    </style>
    <title>Document</title>
</head>
<body>
    {% include 'articles/_nav.html' %}
    <div class="container">
        {% block body %}
        {% endblock %}
    </div>
    {% bootstrap_javascript jquery='full' %}
</body>
</html>
```

_article.html 에 a태그로 된 것 다 날리고 i 태그 새로 넣기

```html
<div class="card">
    <h5 class="card-header">글 작성자: <a href="{% url 'accounts:profile' article.user %}" class="card-link">{{ article.user }}</a>
    </h5>
    <div class="card-body">
        <h5 class="card-title">글 제목: {{ article.title }}</h5>
        <p>글 번호: {{ article.pk }}</p>
        <p class="card-text">
           <i class="{% if user in article.like_users.all %}
           fas
           {% else %}>
           far
           {% endif %}  fa-heart like-button"
           data-id="{{ article.pk }}"
           style="color:crimson"
           >
           </i>
        </p>
        <a href="{% url 'articles:detail' article.pk %}" class="btn btn-primary">글 상세보기</a>
    </div>
</div>
```

index.html - endblock 바로 위에 script 태그 넣음

```html
{% extends 'articles/base.html' %}

{% block body %}
    <h1>Articles</h1>
    <p><b>{{ request.user.username }}님의 방문 횟수: {{ visits_num }}{% if visits_num == 1 %} time{% else %} times {% endif %}</b></p>
    {% for article in articles %}
        {% include "articles/_article.html" %}
    {% endfor %}
        {% if user.is_authenticated %}
        <a href="{% url 'articles:create' %}">[글 작성]</a>
    {% else %}
        <a href="{% url 'accounts:login' %}"><b>[글을 작성하려면 로그인 해주세요]</b></a>
    {% endif %}
    <script>
        const likeButtons = document.querySelectorAll('.like-button')
        likeButtons.forEach(button => {
            button.addEventListener('click', function(event) {
                console.log(event)
                // 1. event.target.dataset.id는 아이콘 태그의 data-id로 지정한 값
                const articleId = event.target.dataset.id
                // 2. 해당 상세 게시글에 좋아요를 누르는 요청을 보내자
                axios.get(`/articles/${articleId}/like/`)
                // 3. 응답을 확인하자!!
                .then(res => {
                    console.log(res)
                })
                .catch(err => console.log(err))
            })
        })
    </script>
{% endblock %}
```

views.py - redirect로 되어있는 것을 json으로 응답하도록 바꿈

```python
from django.http import JsonResponse

@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user

    # 해당 게시글에 좋아요를 누른 사람들 중에서 user.pk(현재 요청 유저)를 가진 user가 존재하면
    if article.like_users.filter(pk=user.pk).exists():
        # 좋아요 취소
        article.like_users.remove(user)
        liked = False
    # 존재하지 않는다면 좋아요를 누른 유저 목록에 유저 추가
    else:
        # 좋아요 누름
        article.like_users.add(user)
        liked = True
    context = {'liked': liked,}
    return JsonResponse(context)
```

index.html (.then 안에 로직 추가)

```html
{% extends 'articles/base.html' %}

{% block body %}
    <h1>Articles</h1>
    <p><b>{{ request.user.username }}님의 방문 횟수: {{ visits_num }}{% if visits_num == 1 %} time{% else %} times {% endif %}</b></p>
    {% for article in articles %}
        {% include "articles/_article.html" %}
    {% endfor %}
        {% if user.is_authenticated %}
        <a href="{% url 'articles:create' %}">[글 작성]</a>
    {% else %}
        <a href="{% url 'accounts:login' %}"><b>[글을 작성하려면 로그인 해주세요]</b></a>
    {% endif %}
    <script>
        const likeButtons = document.querySelectorAll('.like-button')
        likeButtons.forEach(button => {
            button.addEventListener('click', function(event) {
                console.log(event)
                // 1. event.target.dataset.id는 아이콘 태그의 data-id로 지정한 값
                const articleId = event.target.dataset.id
                // 2. 해당 상세 게시글에 좋아요를 누르는 요청을 보내자
                axios.get(`/articles/${articleId}/like/`)
                // 3. 응답을 확인하자!!
                .then(res => {
                    console.log(res)
                    if (res.data.liked) {
                        event.target.classList.remove('far')
                        event.target.classList.add('fas')
                    } else {
                        event.target.classList.remove('fas')
                        event.target.classList.add('far')
                    }
                })
                .catch(err => console.log(err))
            })
        })
    </script>
{% endblock %}
```

views.py 

```python
@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user

    # 해당 게시글에 좋아요를 누른 사람들 중에서 user.pk(현재 요청 유저)를 가진 user가 존재하면
    if article.like_users.filter(pk=user.pk).exists():
        # 좋아요 취소
        article.like_users.remove(user)
        liked = False
    # 존재하지 않는다면 좋아요를 누른 유저 목록에 유저 추가
    else:
        # 좋아요 누름
        article.like_users.add(user)
        liked = True
    context = {
        'liked': liked,
        'count': article.like_users.count(),
        }
    return JsonResponse(context)
```

_article.html

```html
<div class="card">
    <h5 class="card-header">글 작성자: <a href="{% url 'accounts:profile' article.user %}" class="card-link">{{ article.user }}</a>
    </h5>
    <div class="card-body">
        <h5 class="card-title">글 제목: {{ article.title }}</h5>
        <p>글 번호: {{ article.pk }}</p>
        <p class="card-text">
            <span id="like-count-{{ article.pk }}" class="card-text">{{ article.like_users.count }}명이 이 글을 좋아합니다.</span>
            <i class="{% if user in article.like_users.all %}
            fas
            {% else %}>
            far
            {% endif %}  fa-heart like-button"
            data-id="{{ article.pk }}"
            style="color:crimson"
            >
            </i>
        </p>
        <a href="{% url 'articles:detail' article.pk %}" class="btn btn-primary">글 상세보기</a>
    </div>
</div>
```

index.html (like-count id를 잡아서 innerText 넣어줌)

```html
{% extends 'articles/base.html' %}

{% block body %}
    <h1>Articles</h1>
    <p><b>{{ request.user.username }}님의 방문 횟수: {{ visits_num }}{% if visits_num == 1 %} time{% else %} times {% endif %}</b></p>
    {% for article in articles %}
        {% include "articles/_article.html" %}
    {% endfor %}
        {% if user.is_authenticated %}
        <a href="{% url 'articles:create' %}">[글 작성]</a>
    {% else %}
        <a href="{% url 'accounts:login' %}"><b>[글을 작성하려면 로그인 해주세요]</b></a>
    {% endif %}
    <script>
        const likeButtons = document.querySelectorAll('.like-button')
        likeButtons.forEach(button => {
            button.addEventListener('click', function(event) {
                console.log(event)
                // 1. event.target.dataset.id는 아이콘 태그의 data-id로 지정한 값
                const articleId = event.target.dataset.id
                // 2. 해당 상세 게시글에 좋아요를 누르는 요청을 보내자
                axios.get(`/articles/${articleId}/like/`)
                // 3. 응답을 확인하자!!
                .then(res => {
                    console.log(res)
                    document.querySelector(`#like-count-${articleId}`).innerText = `${res.data.count}명이 이 글을 좋아합니다.`
                    if (res.data.liked) {
                        event.target.classList.remove('far')
                        event.target.classList.add('fas')
                    } else {
                        event.target.classList.remove('fas')
                        event.target.classList.add('far')
                    }
                })
                .catch(err => console.log(err))
            })
        })
    </script>
{% endblock %}
```

index.html (요청을 post요청으로 바꾸고 csrf_token 넣어주기)

```javascript
likeButtons.forEach(button => {
            button.addEventListener('click', function(event) {
                console.log(event)
                // 1. event.target.dataset.id는 아이콘 태그의 data-id로 지정한 값
                const articleId = event.target.dataset.id
                axios.defaults.xsrfCookieName = 'csrftoken'
                axios.defaults.xsrfHeaderName = 'X-CSRFToken'
                // 2. 해당 상세 게시글에 좋아요를 누르는 요청을 보내자
                axios.post(`/articles/${articleId}/like/`)
```

views.py (HttpResponseBadRequest import 받기, 비동기요청일때만 안의 로직을 수행하고 아니면 Badrequest)

```python
from django.http import JsonResponse, HttpResponseBadRequest

@login_required
def like(request, article_pk):
    if request.is_ajax():
        article = get_object_or_404(Article, pk=article_pk)
        user = request.user

        # 해당 게시글에 좋아요를 누른 사람들 중에서 user.pk(현재 요청 유저)를 가진 user가 존재하면
        if article.like_users.filter(pk=user.pk).exists():
            # 좋아요 취소
            article.like_users.remove(user)
            liked = False
        # 존재하지 않는다면 좋아요를 누른 유저 목록에 유저 추가
        else:
            # 좋아요 누름
            article.like_users.add(user)
            liked = True
        context = {
            'liked': liked,
            'count': article.like_users.count(),
            }
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()
```

index.html ( )

```javascript
button.addEventListener('click', function(event) {
                console.log(event)
                // 1. event.target.dataset.id는 아이콘 태그의 data-id로 지정한 값
                const articleId = event.target.dataset.id
                // XHR 요청을 확인하는 것은 요청 정보 내에 HTTP_X_REQUESTED_WITH header에 XMLHttpRequest 값이 있어야 한다.
                axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
                axios.defaults.xsrfCookieName = 'csrftoken'
                axios.defaults.xsrfHeaderName = 'X-CSRFToken'
                // 2. 해당 상세 게시글에 좋아요를 누르는 요청을 보내자
                axios.post(`/articles/${articleId}/like/`)
                // 3. 응답을 확인하자!!
```



### 비동기요청은 내가 원하는 부분만 요청하고 바뀌는 것

