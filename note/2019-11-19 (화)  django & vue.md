# 2019-11-19 (화) | django & vue

LoginForm.vue (div 태그 form 태그로 바꾸기, button 태그 속성 수정, click 수정, form 태그에 @submit... 넣기)

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



todoback.settings.py ( JWT_AUTH 작성) 

```python
JWT_AUTH = {
    # JWT encrypt함!! (SERCRET_KEY는 절대 외부 노출 금지!!)
    'JWT_SECRET_KEY': SECRET_KEY,
    # JWT 해싱 알고리즘
    'JWT_ALGORITHM': 'HS256',
    # 토큰 갱신 허용 여부
    'JWT_ALLOW_REFRESH': True,
    # 1주일간 유효한 토큰 - default 5분
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # 28일마다 토큰 갱신
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28),
}
```



django cors-headers 검색 (github 페이지)

```
'corsheaders.middleware.CorsMiddleware', 복사
```

### `CORS_ORIGIN_ALLOW_ALL` 복사 (모든 요청을 받아들이겠다..)

**settings.py** 에 MIDDLEWARE 상단에 붙여넣기

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL= True
```



djangorestframework-jwt 검색

from rest_framework_jwt.views import obtain_jwt_token 복사



**todo-back. urls.py**

```python
from django.contrib import admin
from django.urls import path
# username & password with POST request -> toekn 줌
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
]
```



**todos.models.py**

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass


class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```



**settings.py** (최하단에 작성)

```python
AUTH_USER_MODEL = 'todos.User'
```



경로 todo-back으로 가서 가상환경 실행

python manage.py makemigrations

python manage.py migrate



서버 실행 후에 api-token-auth 넣으면 token 얻을 수 있는 페이지 나옴 ( http://127.0.0.1:8000/api-token-auth/  )



jwt.io 에서 받은 코드 붙여넣어보기





**todo-front.LoginForm.vue** (methods - login 에 axios.post  요청으로 바꾸고 주소 뒤에 api-token-auth/ 붙임)

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
        axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
        .then(res => {
          this.loading = false
          console.log(res)
        })
        .catch(err => {
          this.loading = false
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



npm install vue-session



**main.js** 에 등록

```js
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSession from 'vue-session'

Vue.config.productionTip = false
Vue.use(VueSession)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```



**LoginForm.vue** (router import 하고 login 메서드 수정)

```js
import router from '../router'

methods: {
    login() {
      //1. 로그인 유효성 검사가 끝나면
      if (this.checkForm()) {
        // 2. 로딩의 상태를 true로 변경을 하고 (spinner-border가 돈다.)
        this.loading = true
        // 3. credentials(username, password) 정보를 담아 Django 서버로 로그인 요청을 보낸다.
        axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
        .then(res => {
          this.$session.start()
          this.$session.set('jwt', res.data.token)
          router.push('/')
          console.log(res)
        })
        .catch(err => {
          this.loading = false
          console.log(err)
        })
      } else {
        console.log('로그인 실패')
      }
    },
```



npm run serve 해서 Application 창에서 Session Storage 확인하면 key가 들어오는 것을 볼 수 있음.

로그인 하면 홈 화면으로 이동함.





**home.vue**

```vue
<template>
  <div class="home">
    <h1>Todo with Django</h1>
  </div>
</template>

<script>
import router from '../router'

export default {
  name: 'home',
  components: {

  },
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) {
      router.push('/login')
      }
    }
  },
  mounted() {
    this.checkLoggedIn()
  }
}
</script>

```

서버 키면 로그인 하지 않으면 home 으로 못감



touch todos/serializers.py

**serializers.py**

```python
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed',)
```



**todo-back. urls.py**

```python
from django.contrib import admin
from django.urls import path, include
# username & password with POST request -> toekn 줌
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
    path('api/v1/', include('todos.urls')),
]
```



todos 폴더에 urls.py 파일 만들기

**todos.urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_create),
]
```



**todos.views.py**

settings.py에 restframwork 에 내용들을 default로 잡아놨기 때문에 따로 import 하지 않아도됨.

```python
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        #serializer.data -> Json ({ 'id':1, 'user':1, 'title': 첫번째 할일, 'completed': false})
        return Response(serializer.data)
    return Response(status=400)
```



postman으로 요청 보내보기

post - body - data-form 작성

token 넘길때 - headers - KEY- Authorization - VALUE - JWT + 스페이스 + 토큰



## update 와 delete 설정 시작..

**todos.urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_create),
    path('todos/<int:id>/', views.todo_update_delete),
]
```



**views.py**

```python
from django.shortcuts import render, get_object_or_404
from .models import Todo
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        #serializer.data -> Json ({ 'id':1, 'user':1, 'title': 첫번째 할일, 'completed': false})
        return Response(serializer.data)
    return Response(status=400)

@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'PUT':
        # 기존 todo에서 request.POST(수정 내용)으로 변경
        serializer = TodoSerializer(todo, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            # save하고 Json으로 응답
            return Response(serializer.data)
        # 유효하지 않으면 에러 메세지와 함께 400 error
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        todo.delete()
        # 204 -> 해당하는 컨텐츠가 없는 경우(todo를 삭제 했기 때문에 해당하는 todo가 존재하지 않음을 알려줌)
        return Response(status=204)
```

**serializers.py**(get_user_model import 하고 )

```python
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Todo

User = get_user_model()

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed',)

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', )
```

**urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_create),
    path('todos/<int:id>/', views.todo_update_delete),
    path('users/', views.user_signup),
]
```

**views.py**

```python
from django.shortcuts import render, get_object_or_404
from .models import Todo
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import TodoSerializer, UserCreationSerializer
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        #serializer.data -> Json ({ 'id':1, 'user':1, 'title': 첫번째 할일, 'completed': false})
        return Response(serializer.data)
    return Response(status=400)

@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'PUT':
        # 기존 todo에서 request.POST(수정 내용)으로 변경
        serializer = TodoSerializer(todo, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            # save하고 Json으로 응답
            return Response(serializer.data)
        # 유효하지 않으면 에러 메세지와 함께 400 error
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        todo.delete()
        # 204 -> 해당하는 컨텐츠가 없는 경우(todo를 삭제 했기 때문에 해당하는 todo가 존재하지 않음을 알려줌)
        return Response(status=204)

@api_view(['POST'])
# 로그인을 하지 않아도 요청 허용
@permission_classes((AllowAny, ))
def user_signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save()의 return 값은 User 모델의 인스턴스
        serializer.save()
        return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})
```

postman에서 확인



패스워드가 그대로 보이기 때문에 수정해줘야함.

user.set_password 검색

```python
@api_view(['POST'])
# 로그인을 하지 않아도 요청 허용
@permission_classes((AllowAny, ))
def user_signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save()의 return 값은 User 모델의 인스턴스
        user = serializer.save()
        # User model의 인스턴스가 갖고 있는 set_password -> 인자는 raw password가 들어감
        user.set_password(request.data.get('password'))
        user.save()
        print(serializer.data)
        return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})
```



**serializers.py**

```python
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Todo

User = get_user_model()

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed',)

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', )

class UserSerializer(serializers.ModelSerializer):
    # 특정 유저가 가지고 있는 todo 목록들(여러개 -> many=True)
    todo_set = TodoSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'todo_set', )
```

**urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_create),
    path('todos/<int:id>/', views.todo_update_delete),
    path('users/', views.user_signup),
    path('users/<int:id>/', views.user_detail),
]
```

**views.py** (from django.http import HttpResponseForbidden

from django.contrib.auth import get_user_model, detail 로직 작성)

```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from .models import Todo
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import TodoSerializer, UserCreationSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes

User = get_user_model()

@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        #serializer.data -> Json ({ 'id':1, 'user':1, 'title': 첫번째 할일, 'completed': false})
        return Response(serializer.data)
    return Response(status=400)

@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'PUT':
        # 기존 todo에서 request.POST(수정 내용)으로 변경
        serializer = TodoSerializer(todo, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            # save하고 Json으로 응답
            return Response(serializer.data)
        # 유효하지 않으면 에러 메세지와 함께 400 error
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        todo.delete()
        # 204 -> 해당하는 컨텐츠가 없는 경우(todo를 삭제 했기 때문에 해당하는 todo가 존재하지 않음을 알려줌)
        return Response(status=204)

@api_view(['POST'])
# 로그인을 하지 않아도 요청 허용
@permission_classes((AllowAny, ))
def user_signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save()의 return 값은 User 모델의 인스턴스
        user = serializer.save()
        # User model의 인스턴스가 갖고 있는 set_password -> 인자는 raw password가 들어감
        user.set_password(request.data.get('password'))
        user.save()
        print(serializer.data)
        return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})

@api_view(['GET'])
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    if request.user != user:
        # Response(status=403) 과 동일
        return HttpResponseForbidden()
    serializer = UserSerializer(user)
    return Response(serializer.data)
```



## 다시 Front ㄱ

touch src/components/TodoList.vue



**TodoList.vue** (등록한다)

```vue
<template>
  <div class="todo-list">

  </div>
</template>

<script>
export default {
  name: 'TodoList',
  
}
</script>

<style>

</style>
```

**Home.vue** (불러온다, 보여준다)

```vue
<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <Todolist/>
  </div>
</template>

<script>
import router from '../router'
import TodoList from '@/components/TodoList'

export default {
  name: 'home',
  components: {
    TodoList,
  },
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) {
      router.push('/login')
      }
    }
  },
  mounted() {
    this.checkLoggedIn()
  }
}
</script>

```



todo-front 에서 npm install jwt-decode (함호화 된 유저 id를 해석하기위해 라이브러리 사용)

**Home.vue**

```vue
<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <Todolist/>
  </div>
</template>

<script>
import router from '../router'
import TodoList from '@/components/TodoList'

import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  name: 'home',
  components: {
    TodoList,
  },
  data() {
    return {
      todos: []
    }
  },
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) {
      router.push('/login')
      }
    },
    getTodos() {
      this.$session.start()
      const token = this.$session.get('jwt')
      console.log(token)
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      const user_id = jwtDecode(token).user_id
      console.log(jwtDecode(token))
      axios.get(`http://127.0.0.1:8000/api/v1/users/${user_id}/`, requestHeader)
      .then(res => {
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

서버 다 키고 콘솔창 확인하면 내용들 확인가능

**Home.vue** ( 쓴 글 내려주기 )

```vue
<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
import router from '../router'
import TodoList from '@/components/TodoList'

import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  name: 'home',
  components: {
    TodoList,
  },
  data() {
    return {
      todos: []
    }
  },
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) {
      router.push('/login')
      }
    },
    getTodos() {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      const user_id = jwtDecode(token).user_id
      axios.get(`http://127.0.0.1:8000/api/v1/users/${user_id}/`, requestHeader)
      .then(res => {
        console.log(res)
        this.todos = res.data.todo_set
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



**TodoList.vue** ()

```vue
<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body" d-flex justify-content-between>
        <span>{{ todo.title }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TodoList',
  props: {
    todos: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style>

</style>
```



touch src/components/TodoInput.vue

**TodoInput.vue** (등록한다)

```vue
<template>
  <div class="todo-input">
    <form class="input-group mb-3">
      <input type="text" class="form-control">
      <button type="submit" class="btn btn-primary">+</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'TodoInput'
}
</script>

<style>

</style>
```

**Home.vue** (불러온다, 보여준다)

```vue
<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <TodoInput/>
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
import router from '../router'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'

import axios from 'axios'
import jwtDecode from 'jwt-decode'

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
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) {
      router.push('/login')
      }
    },
    getTodos() {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      const user_id = jwtDecode(token).user_id
      axios.get(`http://127.0.0.1:8000/api/v1/users/${user_id}/`, requestHeader)
      .then(res => {
        console.log(res)
        this.todos = res.data.todo_set
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



TodoInput.vue

```vue
<template>
  <div class="todo-input">
    <form class="input-group mb-3" @submit.prevent="createTodo">
      <input type="text" class="form-control" v-model="title">
      <button type="submit" class="btn btn-primary">+</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data() {
    return {
      title: '',
    }
  },
  methods: {
    createTodo() {
      this.$emit('createTodo', this.title)
      this.title = ''
    }
  }
}
</script>

<style>

</style>
```

Home.vue ( 자식컴포넌트 TodoInput에서 올라오는 정보를 받을 준비 하기 ( 귀열어 )) , createTodo 메서드 작성

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
import jwtDecode from 'jwt-decode'

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
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) {
      router.push('/login')
      }
    },
    getTodos() {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      const user_id = jwtDecode(token).user_id
      axios.get(`http://127.0.0.1:8000/api/v1/users/${user_id}/`, requestHeader)
      .then(res => {
        console.log(res)
        this.todos = res.data.todo_set
      })
      .catch(err => {
        console.log(err)
      })
    },
    createTodo(title) {
      this.$session.start()
      const token = this.$session.get('jwt')
      const requestHeader = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      const user_id = jwtDecode(token).user_id
      // requestForm -> 빈 object
      const requestForm = new FormData()
      requestForm.append('user', user_id)
      requestForm.append('title', title)

      axios.post(`http://127.0.0.1:8000/api/v1/todos/`, requestForm, requestHeader)
      .then(res => {
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

console 창에서 확인하고 뭐 넣어야 할지 확인 후, 

서버에서는 삭제됐지만 화면에 보여주기 위해 this.todos.push(res.data) 작성

```js
axios.post(`http://127.0.0.1:8000/api/v1/todos/`, requestForm, requestHeader)
      .then(res => {
        this.todos.push(res.data)
        console.log(res)
```

**TodoList.vue**

```vue
<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body" d-flex justify-content-between>
        <span>{{ todo.title }}</span>
        <span @click="deleteTodo(todo)">💀</span>
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
    }
  }
}
</script>

<style>

</style>
```

