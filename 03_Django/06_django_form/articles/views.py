from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from IPython import embed

def index(request):
    articles = Article.objects.all() #articles에 전체 목록을 다 가져옴
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터로 채운다
        form = ArticleForm(request.POST)
        # 해당 form이 유효한지 확인
        if form.is_valid():
            # form.cleaned_data를 통해 form 데이터를 정제한다. (form.cleaned_data == Dictionary)
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title, content=content)
            # embed()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        # embed()
    context = {'form': form,}
    return render(request, 'articles/create.html', context)

def detail(request, article_pk): # urls 파일에 따라서 인자 이름 정하면 됨.
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index') # redirect -> GET 요청
    else:
        return redirect('articles:detail', article.pk)