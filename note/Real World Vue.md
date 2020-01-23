## Client-Side Routing

브라우저 스스로가 자바스크립트를 사용해 routing 해준다

SPA(Single Page Application) 는 client-side routing이 필요하다.



## Dinamic router

Router.js 에서 path에 어떤 것이든 '/' 뒤에 ':' 이 붙으면 vue에게 다이나믹 라우터라고 알려주는것이다.

달러($) 사인 이후 route는 현재 route의 상태를 나타냄



router.js

```js
import User from "./views/User.vue";

Vue.use(Router);
export default new Router({
  routes: [
    {
      path: "/user/:username",
      name: "user",
      component: User
    }
  ]
})
```

**User.vue (달러($) 사인 이후 route는 현재 route의 상태를 나타냄)**

```vue
<template>
	<div>
    <h1>This is {{ $route.params.username }}</h1>
  </div>
</template>
```

### 다이나믹 route 를 링크로 만드는 방법

App.vue

```vue
<template>
	<div id="app">
    <router-link :to="{ name: 'User', params: {username: 'Gregg'}}">Gregg</router-link>
  </div>
</template>
```



### 다이나믹 라우터 유연하게 만들기

컴포넌트 안에 달러사인으로 라우터를 만드는 것은 유연하지 못하다.



Router.js

```js
import User from "./views/User.vue";

Vue.use(Router);
export default new Router({
  routes: [
    {
      path: "/user/:username",
      name: "user",
      component: User,
      props: true
    }
  ]
})
```

**User.vue**

username을 prop으로 보내서 컴포넌트를 더 쉽게 재사용 가능해진다

```vue
<template>
	<div>
    <h1>This is {{ username }}</h1>
  </div>
</template>
<script>
	export default {
    props: ["username"]
  }
</script>
```

이렇게 하면 주소창에 # 가 붙는데 이를 없앨 수 있는 방법이있다.

Router.js ( mode: history )

```js
import User from "./views/User.vue";

Vue.use(Router);
export default new Router({
  mode: "history"
  routes: [
    {
      path: "/user/:username",
      name: "user",
      component: User,
      props: true
    }
  ]
})
```



#### 왜 history mode가 default 가 아닌가?

- history.pushstate API 가 Internet Explorer 10 이상만 지원하기 때문에
- vue.js 는 Internet Explorer 9 이상을 지원함







