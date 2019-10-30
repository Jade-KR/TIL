# 2019-10-30 (수) | Java Script

구글 크롬에서  콘솔창에서 if문 연습



```javascript
const userName = prompt('Hello! Who are you?')
undefined

userName
"Jade"

let message = ''
undefined

if (userName === '1q2w3e4r') {
	message = '<h1>This is secret Admin Page</h1>'
} else if (userName === 'ssafy') {
	message = '<h1>You are from matrix</h1>'
} else {
	message = `<h1>Hello ${userName}</h1>`
}
"<h1>Hello Jade</h1>"

document.write(message)
undefined

```

```javascript
const userName = prompt('Hello! Who are you?')
undefined

switch(userName) {
    case '1q2w3e4r': {
		message = '<h1>This is secret admin page.</h1>'
    }
    case 'ssafy': {
		message = '<h1>You are from matrix.</h1>'
    }
    default: {
		message = `<h1>Hello ${userName}</h1>`
    }
}
"<h1>Hello Jade</h1>"

document.write(message)
undefined
```

```javascript
const userName = prompt('Hello! Who are you?')
undefined
let message = ''
undefined
switch(userName) {
    case '1q2w3e4r': {
		message = '<h1>This is secret admin page.</h1>'
    }
    case 'ssafy': {
		message = '<h1>You are from matrix.</h1>'
    }
    default: {
		message = `<h1>Hello ${userName}</h1>`
    }
}
"<h1>Hello ssafy</h1>"
switch(userName) {
    case '1q2w3e4r': {
		message = '<h1>This is secret admin page.</h1>'
		console.log(message)
    }
    case 'ssafy': {
		message = '<h1>You are from matrix.</h1>'
		console.log(message)
    }
    default: {
		message = `<h1>Hello ${userName}</h1>`
		console.log(message)
    }
}
VM2231:8 <h1>You are from matrix.</h1>
VM2231:12 <h1>Hello ssafy</h1>
```

```javascript
switch(userName) {
    case '1q2w3e4r': {
		message = '<h1>This is secret admin page.</h1>'
		console.log(message)
		break
    }
    case 'ssafy': {
		message = '<h1>You are from matrix.</h1>'
		console.log(message)
		break
    }
    default: {
		message = `<h1>Hello ${userName}</h1>`
		console.log(message)
    }
}
VM2256:9 <h1>You are from matrix.</h1>
undefined
```

