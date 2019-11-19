# 2019-11-18 (월) | django & vue

### django

클라이언트가 처음에 로그인 했을대 json web token을 발급 받고 다음번 요청에

요청 받았던 토큰을 사용하여 들어간다.



### json web token

- Json 형태로 만들어준 토큰
- 정보를 교환, 권한이 있는지 확인할때 쓰임.
- xxxx.yyyy.zzzz 형태

- 보안이 뛰어나고 구조가 덜 복잡하기 때문에 사용.

https://jwt.io/ 





# 수업 vue router

- 특정 router와 component를 매칭시켜준다.



cors = 도메인/포트가 다른 서버의 자원을 요청하는 행위 (cors를 browser에서 보안을 위해 막음)

CORS 정책을 통해 서버에서 허용해주면 가능함.



서버에서 cross-origin HTTP 요청 허가 (whitelisting)





> vue create todo-front
>
> todo back 폴더 만들기
>
> todo back 에서
>
> python -m venv venv
>
> source venv/Scripts/Activate
>
> pip install django
>
> django-admin startproject todoback .
>
> python manage.py startapp todos



가상환경 종료



todoback의 settings에 todos 앱 등록



todo-front 폴더로 이동.

> vue ui (왼쪽 하단에 현재 프로젝트 폴더가 맞는지 항상 확인)
>
> 가져오기 에서 todo-front 폴더 열기
>
> 플러그인 - 플러그인 추가 - router (최상단) - 설치 - 활성화 - 설치완료 - 계속

router 와 views가 생성됨.



views 안에 Login.vue 만들기.



**Login.vue** (기본 뼈대 만들기)

```vue
<template>
  
</template>

<script>
export default {

}
</script>

<style>

</style>
```



**index.js** (Login import 하고 기존에 있던 about  지우고 login으로 만듦)

```js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'

// VueRouter를 사용하기 위한 코드
Vue.use(VueRouter)

// rouer와 components를 연결 (Django 의 urls.py와 유사)
const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  }
]

const router = new VueRouter({
  // vue-router를 설치할 때 설정했던 History 모드
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

```



**App.vue** (about을 login으로 바꿈)

```vue
<template>
  <div id="app">
    <div id="nav">
      <!-- 라우터 지원 앱에서 사용자 네비게이션을 가능하게 하는 컴포넌트 목표 위치는 to로 지정-->
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link>
    </div>
    <!-- 특정 라우팅 경로에 맞는 컴포넌트가 렌더되는 자리 -->
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

```



bootstrap 추가 ( index.html에 css cdn 복사 붙여넣기)

**app.vue** ( router-view 에 div태그 씌우기)

```vue
<div class="container col-6">
      <router-view/>
    </div>
```

**Home.vue** (정리하기)

```vue
<template>
  <div class="home">

  </div>
</template>

<script>

export default {
  name: 'home',
  components: {
  }
}
</script>
```



componenets 폴더 안에 LoginForm.vue 파일 만들기

**LoginForm.vue**

```vue
<template>
  <div class="login-div">
    <div class="form-group">
      <label for="id">ID</label>
      <input type="text" class="form-control" id="id" placeholder="아이디를 입력해주세요.">
    </div>
    <div class="form-group">
      <label for="password">Password</label>
      <input type="password" class="form-control" id="password" placeholder="비밀번호를 입력해주세요.">
    </div>
    <button class="btn btn-primary">로그인</button>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
```



**Login.vue** ( LoginForm.vue 등록)

```vue
<template>
  <div class="login">
    <LoginForm/>
  </div>
</template>

<script>
// @ -> alias to src
import LoginForm from '@/components/LoginForm'

export default {
  name: 'Login',
  components: {
    LoginForm,
  }
}
</script>

<style>

</style>
```



**LoginForm.vue**

```vue
<template>
  <div class="login-div">
    <div class="form-group">
      <label for="id">ID</label>
      <input type="text" class="form-control" id="id" placeholder="아이디를 입력해주세요.">
    </div>
    <div class="form-group">
      <label for="password">Password</label>
      <input type="password" class="form-control" id="password" placeholder="비밀번호를 입력해주세요.">
    </div>
    <button class="btn btn-primary">로그인</button>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return{
      credentials: {},
      loading: false,
    }
  }
}
</script>

<style>

</style>
```



package.json에 rules에 내용 추가 ()

```vue
"rules": {
      "no-console": "off"
    },
```



LoginForm.vue (spinner-border 클래스의 div 태그 만들고 ...)

```vue
<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span> <!-- 검색엔진이 알 수 있게 표시 -->
    </div>

    <div v-else class="login-form">
      <div class="form-group">
        <label for="id">ID</label>
        <input 
        type="text" 
        class="form-control" 
        id="id" 
        placeholder="아이디를 입력해주세요."
        v-model="credentials.username"
        @keyup.enter="login"
        >
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" 
        class="form-control" 
        id="password" 
        placeholder="비밀번호를 입력해주세요."
        v-model="credentials.password"
        @keyup.enter="login"
        >
      </div>
    </div>
    <button class="btn btn-primary" @click="login">로그인</button>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return{
      credentials: {},
      loading: false,
    }
  },
  methods: {
    login() {
      console.log('Login button clicked!!')
    }
  }
}
</script>

<style>

</style>
```



**LoginForm.vue** (로그인 검증하기, credentials 안에 내용 넣고 errors만들거 checkform만들기)

```vue
<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span> <!-- 검색엔진이 알 수 있게 표시 -->
    </div>

    <div v-else class="login-form">
      <div v-if="errors.length" class="error-list alert alert-danger">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">{{error}}</div>
      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input 
        type="text" 
        class="form-control" 
        id="id" 
        placeholder="아이디를 입력해주세요."
        v-model="credentials.username"
        @keyup.enter="login"
        >
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" 
        class="form-control" 
        id="password" 
        placeholder="비밀번호를 입력해주세요."
        v-model="credentials.password"
        @keyup.enter="login"
        >
      </div>
    </div>
    <button class="btn btn-primary" @click="login">로그인</button>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return{
      credentials: {
        username: '',
        password: '',
      },
      loading: false,
      errors: [],
    }
  },
  methods: {
    login() {
      if (this.checkForm()) {
        console.log('로그인 성공')
      } else {
        console.log('로그인 실패')
      }
    },
    checkForm() {
      this.errors = []
      // 1. 사용자가 아이디를 입력하지 않은 경우
      if (!this.credentials.username) {
        this.errors.push("아이디를 입력해주세요.")
      }
      // 2. 패스워드가 8글자 미만인 경우
      if (this.credentials.password.length < 8) {
        this.errors.push("비밀번호는 8글자 이상 입력해주세요.")
      }
      // 3. 아이디와 패스워드 모두 잘 입력한 경우
      if (this.errors.length === 0) {
        return true
      }
    }
  }
}
</script>

<style>

</style>
```



### Django 서버로 요청 보내기

npm install axios

axios로 요청을 보냄

LoginForm.vue (axios import 받고 method 수정, )

```vue
<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span> <!-- 검색엔진이 알 수 있게 표시 -->
    </div>

    <div v-else class="login-form">
      <div v-if="errors.length" class="error-list alert alert-danger">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">{{error}}</div>
      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input 
        type="text" 
        class="form-control" 
        id="id" 
        placeholder="아이디를 입력해주세요."
        v-model="credentials.username"
        @keyup.enter="login"
        >
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" 
        class="form-control" 
        id="password" 
        placeholder="비밀번호를 입력해주세요."
        v-model="credentials.password"
        @keyup.enter="login"
        >
      </div>
      <button class="btn btn-primary" @click="login">로그인</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginForm',
  data() {
    return{
      credentials: {
        username: '',
        password: '',
      },
      loading: false,
      errors: [],
    }
  },
  methods: {
    login() {
      //1. 로그인 유효성 검사가 끝나면
      if (this.checkForm()) {
        // 2. 로딩의 상태를 true로 변경을 하고 (spinner-border가 돈다.)
        this.loading = true
        // 3. credentials(username, password) 정보를 담아 Django 서버로 로그인 요청을 보낸다.
        axios.get('http://127.0.0.1:8000/', this.credentials)
      } else {
        console.log('로그인 실패')
      }
    },
    checkForm() {
      this.errors = []
      // 1. 사용자가 아이디를 입력하지 않은 경우
      if (!this.credentials.username) {
        this.errors.push("아이디를 입력해주세요.")
      }
      // 2. 패스워드가 8글자 미만인 경우
      if (this.credentials.password.length < 8) {
        this.errors.push("비밀번호는 8글자 이상 입력해주세요.")
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
      }
      // 3. 아이디와 패스워드 모두 잘 입력한 경우
      if (this.errors.length === 0) {
        return true
      }
    }
  }
}
</script>

<style>

</style>
```



### Django 로 요청에 대한 응답하기.

가상환경 킨다.

3개의 라이브러리 설치.

> pip install djangorestframework
>
> pip install djangorestframework-jwt
>
> pip install django-cors-headers



**todoback** - settings.py ( 앱 등록, import datetime )

```python
import datetime

INSTALLED_APPS = [
    'todos',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
]
```

django-rest-framework-jwt 구글에 검색해서 2번째 글 - Usage 박스 안의 내용 복사

**settings.py** ( middleware 위에 붙여넣기 )

``` python
INSTALLED_APPS = [
    'todos',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```



django-jwt-auth 검색

 https://github.com/jpadilla/django-jwt-auth 

















