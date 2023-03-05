from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    order = Article.objects.all()
    context = {'object_list' : order}
    return render(request, template, context)
