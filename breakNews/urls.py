from django.urls import path
from . import views
from breakNews.models import News
from django.views.generic import ListView, DetailView
from breakNews.views import NewsListView, AuthorPostList
urlpatterns = [
    path('',  views.index, name="index"),
    path('news/', NewsListView.as_view(), name="news"),
    path('news/<int:pk>', DetailView.as_view(model = News, template_name = 'breakNews/news_page.html')),
    path('news/<author_name>', AuthorPostList.as_view()),
    path('news/add/',  views.addNews, name="add"),
    path('create/', views.create, name="create")
]
