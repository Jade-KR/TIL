const axios = require('axios').default

axios.get('https://jsonplaceholder.typicode.com/posts')
.then(res => {
  console.log(res)
})
.catch(err => {
  console.log(err)
})