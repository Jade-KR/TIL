from django.urls import path
from . import views

urlpatterns = [
    path('static_example/', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('lotto/', views.lotto),
    path('ispal/<char>/', views.ispal),
    path('isbirth/<int:month>/<int:day>/', views.isbirth),
    path('template_language/', views.template_language),
    path('area/<int:r>/', views.area),
    path('prac2/<int:num1>/<int:num2>/', views.prac2),
    path('prac1/<name>/<int:age>/', views.prac1),
    path('hello/<str:name>/<int:age>/', views.hello), # str 빼도 됨. default가 string. 여러 개 넘겨 받을 수 있음
    path('image/', views.image),
    path('dinner/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
]