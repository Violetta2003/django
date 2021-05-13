from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from breakNews.models import News
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404, get_object_or_404
from breakNews.forms import NewsForm
def index(request):
    return render(request, 'breakNews/index.html', {'title': 'Главная'})


def addNews(request):
    return render(request, 'breakNews/add.html', {'title': 'Добавить новость'})

class NewsListView(ListView):
    model = News
    paginate_by = 2
    template_name = 'breakNews/news.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-date')

class AuthorPostList(ListView):
    model = News
    template_name = 'breakNews/news_author.html'
    context_object_name = 'news'
    def get_queryset(self):
        self.author_name = get_object_or_404(User, username = self.kwargs['author_name'])
        return News.objects.filter(user__username = self.author_name)

def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid() : 
            form.save()
            return redirect('/news')
        else: 
            error = 'Неверные данные пользователя'
    form = NewsForm()
    data = {
        'form': form,
        'error': error 
    }
    return render(request, 'breakNews/create.html', {'title': 'Создать новость', 'data': data})