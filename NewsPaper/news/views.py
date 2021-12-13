from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post, Author, PostCategory, Category, Comment
from .filters import PostFilter
from .forms import PostForm

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name ='posts'
    ordering = ['-id']
    paginate_by = 10
    form_class = PostForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context



class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    queryset = Post.objects.all()

class PostSearchList(PostList):
    model = Post
    template_name = 'search.html'
    context_objects_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

class PostCreateList(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm


class PostUpdateList(UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteList(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'