# 2019-11-20 (수) | django & vue

**TodoList.vue** (complete 된 것 줄 긋기)

```vue
<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body" d-flex justify-content-between>
        <span @click="updateTodo(todo)" :class="{ complete: todo.completed }">{{ todo.title }}</span>
        <span @click="deleteTodo(todo)"><button>💀</button></span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  props: {
    todos: {
      type: Array,
      required: true,
    }
  },
  methods: {
    deleteTodo(todo) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestHeader)
      .then(res => {
        console.log(res)
        const targetTodo = this.todos.find(function(el) {
          return el === todo
        })
        const idx = this.todos.indexOf(targetTodo)
        if (idx > -1) {
          this.todos.splice(idx, 1)
        }
      })
      .catch(err => {
        console.log(err)
      })
    },
    updateTodo(todo) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
    }
  }
}
</script>

<style>
  .complete {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
```

**TodoList.vue**

```vue
<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body" d-flex justify-content-between>
        <span @click="updateTodo(todo)" :class="{ complete: todo.completed }">{{ todo.title }}</span>
        <span @click="deleteTodo(todo)"><button>💀</button></span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  props: {
    todos: {
      type: Array,
      required: true,
    }
  },
  methods: {
    deleteTodo(todo) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestHeader)
      .then(res => {
        console.log(res)
        const targetTodo = this.todos.find(function(el) {
          return el === todo
        })
        const idx = this.todos.indexOf(targetTodo)
        if (idx > -1) {
          this.todos.splice(idx, 1)
        }
      })
      .catch(err => {
        console.log(err)
      })
    },
    updateTodo(todo) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      const requestForm = new FormData()
      requestForm.append('completed', !todo.completed)
      requestForm.append('user', todo.user)
      requestForm.append('id', todo.id)
      requestForm.append('title', todo.title)
      console.log(!todo.completed, todo.user, todo.id, todo.title)

      axios.put(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestForm, requestHeader)
      .then(res => {
        console.log(res)
        todo.completed = !todo.completed
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
  .complete {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
```



## Logout 만들기

App.vue

```vue
<template>
  <div id="app" class="container">
    <div id="nav">
      <!-- 라우터 지원 앱에서 사용자 네비게이션을 가능하게 하는 컴포넌트 목표 위치는 to로 지정-->
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link> |
      <a @click.prevent="logout" href="#">Logout</a>
    </div>
    <!-- 특정 라우팅 경로에 맞는 컴포넌트가 렌더되는 자리 -->
    <div class="row justify-content-center"> <!-- container => row => col 순으로 -->
      <router-view class="col-6"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    logout() {
      this.$session.destroy()
      this.$router.push('/login')
    }
  }
}
</script>

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



## 링크 분기하기

App.vue ( DOM 의 변화를 )

```vue
<template>
  <div id="app" class="container">
    <div id="nav">
      <div v-if="isAuthenticated">
      <!-- 라우터 지원 앱에서 사용자 네비게이션을 가능하게 하는 컴포넌트 목표 위치는 to로 지정-->
      <router-link to="/">Home</router-link> |
      <a @click.prevent="logout" href="#">Logout</a>
      </div>
      <div v-else>
        <router-link to="/login">Login</router-link>
      </div>
    </div>
    <!-- 특정 라우팅 경로에 맞는 컴포넌트가 렌더되는 자리 -->
    <div class="row justify-content-center"> <!-- container => row => col 순으로 -->
      <router-view class="col-6"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isAuthenticated: this.$session.has('jwt')
    }
  },
  updated() {
    this.isAuthenticated = this.$session.has('jwt')
  },
  methods: {
    logout() {
      this.$session.destroy()
      this.$router.push('/login')
    }
  }
}
</script>

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



## vuex 라는 상태 관리 라이브러리가 있다.

- State = 상태들이 들어있는 것. 값으로 정의 -> computed 사용

- Getters = 상태정보를 가져와서 무언가를 해서 뱉어주는 것. 값으로 정의 -> computed 사용

- Mutations = 상태를 변화시키는 것. (상태를 변화시키기 때문에 무조건 동기적으로 처리해야함)

- Actions =  (동기, 비동기)모든 로직이 actions에 담김.



vue ui

> 왼쪽 하단에 위치가 todo-front 인지 확인
>
> 플러그인 - 플러그인 추가 - vuex 검색 최상단 선택 후 설치 - 설치완료 - 계속
>
> store라는 디렉토리 와  index.js가 생겼음.
>
> store 폴더 안에 modules라는 폴더 생성
>
> modules 폴더 안에 auth.js 파일 생성

**store 안에 index.js**

```js
import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
  }
})
```

**auth.js**

```js
import jwtDecode from 'jwt-decode'

//1. 상태정보
const state = {
  token: null,
  loading: false,
}

//2. getters는 state 를 변경하지 않음.
// state를 인자로 받아서 사용
const getters = {
  isLoggedIn: function(state) {
    return state.token ? true : false
  },
  requestHeader: function(state) {
    return {
      headers:{
        Authorization: 'JWT ' + state.token
      }
    }
  },
  userId: function(state) {
    return state.token ? jwtDecode(state.token).user_id : null
  }
}
//3. 상태(토큰)을 받아와서 변경함
// mutation을 통해 state(상태/데이터)를 변경함
const mutations = {
  setToken: function(state, token) {
    state.token = token
  },
  setLoading: function(state, status) {
    state.loading = status
  }
}

//4. 로그인/로그아웃
const actions = {
  login: function(context, token) {
    context.commit('setToken', token)
  },
  logout: function(context) {
    context.commit('setToken', null)
  },
  startLoading: function(context) {
    context.commit('setLoading', true)
  },
  endLoading: function(context) {
    context.commit('setLoading', false)
  }
}

export default {
  state,
  getters,
  mutations,
  actions,
}
```



**LoginForm.vue**

```vue
<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span> <!-- 검색엔진이 알 수 있게 표시 -->
    </div>

    <form v-else class="login-form" @submit.prevent='login'>
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
        >
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" 
        class="form-control" 
        id="password" 
        placeholder="비밀번호를 입력해주세요."
        v-model="credentials.password"
        >
      </div>
      <button type="submit" class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'

export default {
  name: 'LoginForm',
  data() {
    return{
      credentials: {
        username: '',
        password: '',
      },
      errors: [],
    }
  },
  computed: {
    loading: function() {
      return this.$store.state.loading
    }
  },
  methods: {
    login() {
      //1. 로그인 유효성 검사가 끝나면
      if (this.checkForm()) {
        // 2. 로딩의 상태를 true로 변경을 하고 (spinner-border가 돈다.)
        this.$store.dispatch('startLoading')
        // 3. credentials(username, password) 정보를 담아 Django 서버로 로그인 요청을 보낸다.
        axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
        .then(res => {
          this.$store.dispatch('endLoading')
          this.$store.dispatch('login', res.data.token)
          router.push('/')
        })
        .catch(err => {
          this.$store.dispatch('endLoading')
          console.log(err)
        })
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

TodoList.vue

```vue
<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body" d-flex justify-content-between>
        <span @click="updateTodo(todo)" :class="{ complete: todo.completed }">{{ todo.title }}</span>
        <span @click="deleteTodo(todo)"><button>💀</button></span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  props: {
    todos: {
      type: Array,
      required: true,
    }
  },
  computed: {
    requestHeader: function() {
      return this.$store.getters.requestHeader
    }
  },
  methods: {
    deleteTodo(todo) {
      axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, this.requestHeader)
      .then(res => {
        console.log(res)
        const targetTodo = this.todos.find(function(el) {
          return el === todo
        })
        const idx = this.todos.indexOf(targetTodo)
        if (idx > -1) {
          this.todos.splice(idx, 1)
        }
      })
      .catch(err => {
        console.log(err)
      })
    },
    updateTodo(todo) {
      const requestForm = new FormData()
      requestForm.append('completed', !todo.completed)
      requestForm.append('user', todo.user)
      requestForm.append('id', todo.id)
      requestForm.append('title', todo.title)

      axios.put(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestForm, this.requestHeader)
      .then(res => {
        console.log(res)
        todo.completed = !todo.completed
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
  .complete {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
```

**Home.vue**

```vue
<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <TodoInput @createTodo="createTodo"/>
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
import router from '../router'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'

import axios from 'axios'
// Object destructuring
import { mapGetters } from 'vuex'
// import jwtDecode from 'jwt-decode'

export default {
  name: 'home',
  components: {
    TodoList,
    TodoInput,
  },
  data() {
    return {
      todos: []
    }
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'requestHeader',
      'userId',
    ])
  },
  methods: {
    checkLoggedIn() {
      if (!this.isLoggedIn) {
      router.push('/login')
      }
    },
    getTodos() {
      axios.get(`http://127.0.0.1:8000/api/v1/users/${this.userId}/`, this.requestHeader)
      .then(res => {
        console.log(res)
        this.todos = res.data.todo_set
      })
      .catch(err => {
        console.log(err)
      })
    },
    createTodo(title) {
      // requestForm -> 빈 object
      const requestForm = new FormData()
      requestForm.append('user', this.userId)
      requestForm.append('title', title)

      axios.post(`http://127.0.0.1:8000/api/v1/todos/`, requestForm, this.requestHeader)
      .then(res => {
        this.todos.push(res.data)
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  mounted() {
    this.checkLoggedIn()
    this.getTodos()
  }
}
</script>
```

**App.vue**

```vue
<template>
  <div id="app" class="container">
    <div id="nav">
      <div v-if="isLoggedIn">
      <!-- 라우터 지원 앱에서 사용자 네비게이션을 가능하게 하는 컴포넌트 목표 위치는 to로 지정-->
      <router-link to="/">Home</router-link> |
      <a @click.prevent="logout" href="#">Logout</a>
      </div>
      <div v-else>
        <router-link to="/login">Login</router-link>
      </div>
    </div>
    <!-- 특정 라우팅 경로에 맞는 컴포넌트가 렌더되는 자리 -->
    <div class="row justify-content-center"> <!-- container => row => col 순으로 -->
      <router-view class="col-6"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isLoggedIn
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
      this.$router.push('/login')
    }
  }
}
</script>

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

**src/main.js**

```js
import Vue from 'vue'
import App from './App.vue'
import router from './router'
// import VueSession from 'vue-session'
import store from './store'

Vue.config.productionTip = false
// Vue.use(VueSession)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
```



touch src/components/RegisterForm.vue

**RegisterForm.vue**

```vue
<template>
  <div class="register-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>
    <form v-else class="register-form" @submit.prevent="register">
      <div v-if="errors.length" class="error-list alert alert-danger">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">{{ error }}</div>
      </div>
      <div class="form-group">
        <label for="id">ID</label>
        <input 
          type="text" 
          class="form-control" 
          id="id" 
          placeholder="아이디를 입력해주세요"
          v-model="credentials.username"
        >
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input 
          type="password" 
          class="form-control" 
          id="password" 
          placeholder="비밀번호를 입력해주세요"
          v-model="credentials.password"
        >
      </div>
      <div class="form-group">
        <label for="password-confirm">Password Confirm</label>
        <input 
          type="password" 
          class="form-control" 
          id="password-confirm" 
          placeholder="비밀번호를 다시 입력해주세요"
          v-model="credentials.passwordConfirm"
        >
      </div>
      <button type="submit" class="btn btn-primary">회원가입</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'
​
export default {
  name: 'RegisterForm',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirm: '',
      },
      errors: []
    }
  },
  computed: {
    loading() {
      return this.$store.state.loading
    }
  },
  methods: {
    register() {
      if (this.checkForm()) {
        this.$store.dispatch('startLoading')
        console.log(this.credentials)
        axios.post('http://localhost:8000/api/v1/users/', this.credentials)
        .then(res => {
          console.log(res)
          this.$store.dispatch('endLoading')
          alert("회원가입이 성공적으로 완료되었습니다.")
          router.push("/login")
        })
        .catch(err => {
          this.$store.dispatch('endloading')
          console.log(err)
        })
      } else {
        console.log("검증 실패")
      }
    },
    checkForm() {
      this.errors = []
      if (!this.credentials.username) {
        this.errors.push("아이디를 입력해주세요.")
      } 
      if (this.credentials.password.length < 8) {
        this.errors.push("비밀번호는 8글자 이상 넣어주세요.")
      }
      if (this.credentials.password !== this.credentials.passwordConfirm) {
        this.errors.push("비밀번호가 일치하지 않습니다.")
      }
      if (this.errors.length === 0) {
        return true
      }
    }
  }
}
</script>
```



touch src/views/Resgister.vue

**Register.vue**

```vue
<template>
  <div class="register">
    <RegisterForm/>
  </div>
</template>
​
<script>
import RegisterForm from '@/components/RegisterForm'
​
export default {
  name: 'Register',
  components: {
    RegisterForm,
  },
}
</script>
```



**router - index.js (import 추가, 로직 수정)**

```js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

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
  },
  {
    path: '/register',
    name: 'register',
    component: Register
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

**App.vue** (추가)

```vue
<div v-else>
    <router-link to="/login">Login</router-link> |
    <router-link to="/register">Register</router-link>
</div>
```

