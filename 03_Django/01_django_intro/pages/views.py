from django.shortcuts import render
from datetime import datetime
import random
import requests

# 1. 기본로직
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def introduce(request):
    return render(request, 'pages/introduce.html')

def image(request):
    return render(request, 'pages/image.html')

# 2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)  #'pick' 은 dinner.html에서 사용하겠다는 의미

# 3. Variable Routing(동적 라우팅)
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'name': name, 
        'age': age,
        'pick': pick,
        }
    return render(request, 'pages/hello.html', context)

# 4. 실습
# 4-1. variable routing(동적 라우팅)을 활용해서(name과 age를 인자로 받아) 자기소개 페이지
def prac1(request, name, age):
    context = {
        'name': name,
        'age': age
    }
    return render(request, 'pages/prac1.html', context)
# 4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력
def prac2(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'comp': num1 * num2
    }
    return render(request, 'pages/prac2.html', context)

#4-3. 반지름(r)을 인자로 받아 원의 넓이(area)를 구하시오.
def area(request, r):
    context = {
        'r': r,
        'area': 3.14 * r**2
    }
    return render(request, 'pages/area.html', context)

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

#6. 실습
#6-1. isbirth
def isbirth(request, month, day):
    today = datetime.now()
    if today.month == month and today.day == day:
        result = True
    else:
        result = False
    
    context = {
        'result': result
    }

    return render(request, 'pages/isbirth.html', context)

#6-2. 회문판별(palindrome)
def ispal(request, char):
    if char == char[::-1]:
        result = True
    else:
        result = False

    context = {
        'result': result
    }

    return render(request, 'pages/ispal.html', context)

#6-3. 로또 번호 추첨
# lottos -> 1 ~ 45까지의 번호 중 6개를 랜덤으로 pick한 리스트
# real_lottos -> [21, 24, 30, 32, 40, 42]
#1. lottos 번호를 하나씩 출력(DTL-for문)
#2. 컴시기가 뽑은 로또 번호와 실제 로또 당첨 번호를 비교해보기(DTL-if문)
def lotto(request):
    real_lottos = [21, 24, 30, 32, 40, 42]
    lottos = sorted(list(random.sample(range(1, 46), 6)))

    context = {
        'real_lottos': real_lottos,
        'lottos': lottos,
    }
    return render(request, 'pages/lotto.html', context)

#7. Form - GET (데이터를 요청할 때)
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2,
    }
    return render(request, 'pages/catch.html', context)

def ping(request):
    return render(request, 'pages/ping.html') #주소창에 Enter 치는 순간 부터 어떤 일이 벌어질지 순차적으로 확인

def pong(request):
    ball = request.GET.get('ball')
    ball2 = request.GET.get('ball2')
    context = {
        'ball': ball,
        'ball2': ball2,
    }
    return render(request, 'pages/pong.html', context)

#8. Form - GET 실습(아스키 아티)
def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form 으로 날린 데이터를 받는다.(GET)
    word = request.GET.get('word')
    #2. ARTII api로 요청을 보내 응답 결과를 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    
    #3. fonts(str)를 fonts(list)로 바꾼다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서 font라는 변수에 저장(str)
    font = random.choice(fonts)

    #5. 위에서 사용자에게 받은 word와 font를 가지고 다시 요청을 보낸다.
    # 그리고 응답 결과를 result에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    context = {
        'result': result,
    }
    return render(request, 'pages/result.html', context)

#9. Form - POST (주소창에 나타나지 않고 바디로 보내줌)(데이터베이스를 조작할 때)
def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'pwd': pwd,
    }
    return render(request, 'pages/user_create.html', context)

#10. 정적 파일
def static_example(request):
    return render(request, 'pages/static_example.html')