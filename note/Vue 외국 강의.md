v-show 

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

list rendering 할 때 tracking 할 수 있는 key값을 v-for 이후에 key값을 넣어줘야함

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



Style Bindings (스타일에 바인딩해서 스타일 먹일 수 있음. 속도가 빨라진다.)

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



Computed

데이터 변경에 반응한다.



