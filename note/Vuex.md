# Vuex

```js
const store = new Vuex.Store({
    state: {
        ...
    },
    mutations: {   // state의 변화를 commit하고 track 한다.
        ...
    },
    actions: {    // methods 같이 Vuex state를 업데이트해 준다.
        ...
    },
    getters: {     // state에 접근할 수 있음
        ...
    },
})
```



store.js

```js
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: { id: 'abc123', name: 'Adam Jahr' },
    categories: [
      'sustainability',
      'nature',
      'animal welfare',
      'housing',
      'education',
      'food',
      'community'],
    events: [
      { id: 1, text: '...', done: true },
      { id: 2, text: '...', done: false },
      { id: 3, text: '...', done: true },
      { id: 4, text: '...', done: false },
    ]
  },
  mutations: {},
  actions: {},
  getters: {
    getEventById: state => id => {
      return state.events.find(event => event.id === id)
    }
  }
});

```

EventCreate.vue

```vue
<template>
  <div>
    <h1>Create an Event, {{ user.name }}</h1>
    <p>This event was created by {{ user.id }}</p>
    <p>{{ getEventById(1)}}</p>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
export default {
  computed:{
  ...mapGetters(['getEventById']),
  ...mapState(['user','categories'])
  }
}
</script>

<style>

</style>
```



Mutation은 동기적이고 Actions은 비동기적이다

그래서 axios같은 비동기요청을 할때 actions을 사용



### mutation

```js
state: {
    user: null
    count: 0
},
    mutations: {
        INCREMENT_COUNT(state, value) {
            state.count += value
        }
    },
    actions: {
         updateCount({ state, commit }, value) {
             if (state.user) {
                 commit('INCREMENT_COUNT', value)
             }
         }
```

Component.vue

```vue
<template>
	<div>
        <input type="number" v-model.number="incrementBy">
        <button @click="incrementCount">Increment</button>
    </div>
</template>
<script>
 export default {
     data() {
         return {
             incrementBy: 1
         }
     },
	method: {
        incrementCount() {
            this.$store.commit('INCREMENT_COUNT', this.incrementBy) // mutations
            this.$store.dispatch('updateCount', this.incrementBy) // actions
        }
    },
  }
</script>
```

