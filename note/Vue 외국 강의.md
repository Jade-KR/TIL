## v-show 

``` vue
<template>
<div class="app">
  <p v-show="inStock">In Stock</p>
</div>
</template>
<script>
	var app = new Vue({
    el: '#app',
    data: {
      product: 'Socks',
      image: '~~',
      inStock: false
    }
  })
</script>
```

​	

### list rendering 

할 때 tracking 할 수 있는 key값을 v-for 이후에 key값을 넣어줘야함

```vue
<div v-for="variant in variants" :key="variant.variantId">
  <p>
    {{ variant.variantColor }}
  </p>
</div>

<script>
	var app = new Vue({
    el: '#app',
    data: {
      product: 'Socks',
      image: '~~',
      inStock: false
      variant: [
      {
      variantId: 234,
      variantColor: "green"
    },
    {
    variantId: 235,
    variantColor: "blue"
  },
      ]
    }
  })
</script>
```



## Style Bindings 

스타일에 바인딩해서 스타일 먹일 수 있음. 속도가 빨라진다.

```vue
<div class="color-box"
     v-for="variant in variants"
     :key="variant.variantId"
     :style="{ backgrounColor: variant.variantColor }"
     @mouseoer="updateProduct(variant.variantImage)">
</div>
```



:disabled="false" 면 click 버튼이 작동하지 않음 그리고 class 조작으로 css와 연결시켜 색 변경

```vue
<button @click="addTocart"
        :disabled="!inStock"
        :class="{ disabledButton: !inStock}">
  
</button>
```

```css
.disabledButton {
  background-color: grey;
}
```



## Computed

데이터 변경에 반응한다.



### Component (2가지 방법)

[반복해야 할 작업을 할때 사용하면 좋음]

component가 새로운 데이터를 받아야 할 때는 props를 사용하여

현재 vue 파일에 정의한 데이터를 받아서 component로 넘겨주고

template에서 component에 v-bind를 해줘야함

(props로 넘겨줄때 type, required 정의해줘야함)

``` vue
<template>
	<div id="app">
        <product></product>
    </div>
</template>
<script>
	Vue.component('product', {
        props: {
            premium {
            type: Boolean,
            required: true,
        },
        template:`
        	<div clas=="product"> ...
		`,
        data() {
            return {
                ...
            }
        }
        }
    })
    // 이 페이지에서 데이터 조작할 수 있음
    var app = new Vue({
        el: '#app',
        data: {
            premium: true
        }
    })
</script>
```

```vue
<template>
	<componentName></componentName>
</template>
<script>
import componentName from '/componentLocation'
export default {
	name: 'Homepage',
	component: {
        componentName,
    }
}
</script>

```



## emit

props를 통해서 component로 데이터를 받았는데 component에서 어떤 일이 일어났을때 (버튼클릭같은) 부모에게 알려줄 방법이 필요하다.

```vue
<template>
	<product :premium="premium" @add-to-cart="updateCart"></product>
</template>

<script>
	Vue.component('product', {
        ...
        addToCart() {
        	this.$emit('add-to-cart')
    }
    })
    
    var app = new Vue({
        ...
        data: {
            ...
            cart: 1
        },
        methods: {
            updateCart() {
                this.cart += 1
            }
        }
    })
</script>
```



## v-model

template에서 data로 date에서 template으로 양방향 v-bind가 가능

v-model.number

