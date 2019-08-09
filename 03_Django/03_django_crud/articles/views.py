from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.order_by('-id')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # article = Article(title=title, content=content) 이것도 가능
    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect(f'/articles/{article.pk}/')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(reqeust, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    
    return redirect('/articles/')

def edit(request, pk):
    article = Article.objects.get(pk=pk) #기존에 작성한 것을 수정해야하기때문에 불러와야함 (get으로)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk): #기존 글을 가져와야하기 때문에 create보다 조금 로직이 더 추가됨
    #기존 글 가져오기
    article = Article.objects.get(pk=pk)
    # create에서 한 것과 같은데 좀 더 줄인 것.
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    #내용이 수정됐는지 확인하기 위해 detail.html로 보냄
    return redirect(f'/articles/{article.pk}/')
