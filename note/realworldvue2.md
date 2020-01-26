Global Component 는 언제 사용해야 할까?

- 자주 사용하거나, 베이스가 될 때



사용법

Component 파일을 만들고 자주 사용할만한 내용들을 담는다.

main.js 에 import 해주고 등록해준다.

main.js

```js
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import BaseIcon from '@/components/BaseIcon.vue';
import BaseButton from '@/components/BaseButton.vue';
import BaseInput from '@/components/BaseInput.vue';

Vue.component('BaseIcon', BaseIcon)
Vue.component('BaseButton', BaseButton)
Vue.component('BaseInput', BaseInput)

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");

```

Base component가 몇개 없으면 이런식으로 작성할 수 있지만 나중에 스케일이 더 커지고

복잡해지면 이런식으로 하기에 너무 귀찮기 때문에 더 효율적인 방법을 사용해야한다.



## Slot

컴포넌트를 가져다 쓸 때 내용을 바꾸고 싶을때 사용한다.

```vue
<template>
  <div>
    <span><slot name="TD">@{{ event.time }} on {{ event.date }}</slot></span>
    <h4>{{ event.title }}</h4>
    <span>{{ event.attendees.length }} attending</span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      event: {
      id: 1,
      title: 'Beach Cleanup',
      date: 'Tues Aug 19. 2018',
      time: '6:00',
      attendees: [
        { id: 'abc12', name: 'Adam Jahr'},
        { id: 'def12', name: 'Jade Jahr'},
      ]
    }
    }
  }
}
</script>

<style scoped>
h4 {
  color: green;
}
</style>
```



```vue
<template>
  <div>
  <h1>Events Listing</h1>
  <EventCard><h1 slot="TD"></h1></EventCard>
  <BaseIcon></BaseIcon>
  </div>
</template>

<script>
import EventCard from '@/components/EventCard.vue';
export default {
  components: {
    EventCard
  }
}
</script>

<style>

</style>
```



# Axios

첫번째로 우리 어플리케이션이 브라우저에 로드 되고,  그리고 그것이 API call 을 만들어서

api/events를 요청한다. 그리고 서버는 JSON 응답을 돌려준다. 



Vue는 API call 을 만들 필요가 없다.  왜냐하면 javascript에 그 일을 할 많은 라이브러리가 있기 때문이다.

그 중에서도 Vue에서 사용되는 가장 유명한 것이 Axios다.



Axios 라이브러리

- GET, POST, PUT 그리고 DELETE 요청을 할 수 있다.
- 각 요청에 권한을 추가 할 수 있다.
- 요청이 너무 오래걸리면 timeouts을 설정 할 수 있다.
- 각 요청에 default값을 구성할 수 있다.
- middleware를 생성하기 위해 요청을 가로챌 수 있다.
- 요청들을 적절하게 취소하고 에러를 조작 할 수 있다.
- 요청과 응답에 적절한 serialize와 deserialize를 할 수 있다.



가장 기본적인 axios GET 요청

```js
axios.get('https://example.com/events') // 이 URL을 불러낸다.
	.then(response =>
         console.log(response.data) // response가 return되면 console에 log한다.
      })
	.catch(error =>					// log에서 에러들을 찾아낸다.
          console.log(error)
      })
```

Axios Call은 비동기적 요청이다.

- 코드가 완료될 때 까지 기다리지 않는다.

**example,**

```js
apiCall() {
    console.log('Enter')
    axios.get('https://example.com/events')
    .then(response =>
         console.log(response.data)
          })
    .catch(error =>
          console.log(error)
           })
    console.log('Exit')
}
```

**answer**

```
Enter
Exit
{
	"events: [...]"
}
```



Axios call 이 각 컴포넌트마다 있으면 매번 import 해줘야하고 디버깅할 때 불편하다.

그래서!

EventService.js 파일을 하나 만든다

```js
import axios from 'axios'

const apiClient = axios.create({ // 전체 앱을 위한 하나의 Axios 인스턴스를 만든다
  baseURL: 'http://localhost:3000', // Base url을 설정하고
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json' // 권한과 구성을 위해 설정해놓음
  }
})

export default {
  getEvents() {
    return apiClient.get('/events')
  }
}
```



```vue
<script>
  import EventCard from '@/components/EventCard.vue';
  import EventService from '@/services/EventService.js';
  export default {
    components: {
      EventCard
    },
    data() {
      return {
        events: []
      }
    },
    created() {
      EventService.getEvents()
        .then(response => {
          this.events = response.data
        })
        .catch(error => {
          console.log('There was an error:' + error.response)
        })
    }
  }
  </script>
```



## Vue Lifecycle

**BeforeCreate**

```
이름처럼 가장 먼저 실행되는 beforeCreate훅입니다. Vue 인스턴스가 초기화 된 직후에 발생됩니다. 컴포넌트가 DOM에 추가되기도 전이어서 this.$el에 접근할 수 없습니다. 또한 data, event, watcher에도 접근하기 전이라 data, methods에도 접근할 수 없습니다.
```

**Created**

```
created훅에서는 data를 반응형으로 추적할 수 있게 되며 computed, methods, watch 등이 활성화되어 접근이 가능하게 됩니다. 하지만 아직까지 DOM에는 추가되지 않은 상태입니다.

data에 직접 접근이 가능하기 때문에, 컴포넌트 초기에 외부에서 받아온 값들로 data를 세팅해야 하거나 이벤트 리스너를 선언해야 한다면 이 단계에서 하는 것이 가장 적절합니다.
```

**BeforeMount**

``` 
DOM에 부착하기 직전에 호출되는 beforeMount훅입니다. 이 단계 전에서 템플릿이 있는지 없는지 확인한 후 템플릿을 렌더링 한 상태이므로, 가상 DOM이 생성되어 있으나 실제 DOM에 부착되지는 않은 상태입니다.
```

**Mounted**

``` 
일반적으로 가장 많이 사용하는 mounted훅입니다. 가상 DOM의 내용이 실제 DOM에 부착되고 난 이후에 실행되므로, this.$el을 비롯한 data, computed, methods, watch 등 모든 요소에 접근이 가능합니다.
```

BeforeUpdate

```
컴포넌트에서 사용되는 data의 값이 변해서, DOM에도 그 변화를 적용시켜야 할 때가 있습니다. 이 때, 변화 직전에 호출되는 것이 바로 beforeUpdate훅입니다. 변할 값을 이용해 가상 DOM을 렌더링하기 전이지만, 이 값을 이용해 작업할 수는 있습니다. 이 훅에서 값들을 추가적으로 변화시키더라도 랜더링을 추가로 호출하지는 않습니다.
```

Updated

```
가상 DOM을 렌더링 하고 실제 DOM이 변경된 이후에 호출되는 updated훅입니다. 변경된 data가 DOM에도 적용된 상태입니다. 만약 변경된 값들을 DOM을 이용해 접근하고 싶다면, updated훅이 가장 적절합니다.

다만 이 훅에서 data를 변경하는 것은 무한 루프를 일으킬 수 있으므로 이 훅에서는 데이터를 직접 바꾸어서는 안됩니다.

mounted훅과 마찬가지로, this.$nextTick을 이용해, 모든 화면이 업데이트 된 이후의 상태를 보장할 수 있습니다.
```

BeforeDestroy

```
해당 인스턴스가 해체되기 직전에 beforeDestroy훅이 호출됩니다. 아직 해체되기 이전이므로, 인스턴스는 완전하게 작동하기 때문에 모든 속성에 접근이 가능합니다. 이 단계에서는 이벤트 리스너를 해제하는 등 인스턴스가 사라지기 전에 해야할 일들을 처리하면 됩니다.
```

Destroyed

```
인스턴스가 해체되고 난 직후에 destroyed훅이 호출됩니다. 해체가 끝난 이후기 때문에, 인스턴스의 속성에 접근할 수 없습니다. 또한 하위 Vue 인스턴스 역시 삭제됩니다.
```























