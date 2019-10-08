# 21_workshop

## 01_문제

```html
<h1>{{ question.title }}</h1>
{% for choice in question.choice_set.all %}
{{ choice.content }} : {{ choice.votes }}
{% endfor %}
```



