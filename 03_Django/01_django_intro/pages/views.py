from django.shortcuts import render
from datetime import datetime
import random

# 1. 기본로직
# Create your views here.
def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

def image(request):
    return render(request, 'image.html')

# 2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)  #'pick' 은 dinner.html에서 사용하겠다는 의미

# 3. Variable Routing(동적 라우팅)
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'name': name, 
        'age': age,
        'pick': pick,
        }
    return render(request, 'hello.html', context)

# 4. 실습
# 4-1. variable routing(동적 라우팅)을 활용해서(name과 age를 인자로 받아) 자기소개 페이지
def prac1(request, name, age):
    context = {
        'name': name,
        'age': age
    }
    return render(request, 'prac1.html', context)
# 4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력
def prac2(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'comp': num1 * num2
    }
    return render(request, 'prac2.html', context)

#4-3. 반지름(r)을 인자로 받아 원의 넓이(area)를 구하시오.
def area(request, r):
    context = {
        'r': r,
        'area': 3.14 * r**2
    }
    return render(request, 'area.html', context)

# DTL(Django Template Language)
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }

    return render(request, 'template_language.html', context)