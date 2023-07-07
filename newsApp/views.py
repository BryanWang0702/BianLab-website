from django.shortcuts import render

from newsApp.models import News


# Create your views here.


def news(request):
    news = News.objects.all().order_by('-time')
    context = {
        'news': news
    }
    return render(request, "news/news.html", context)
