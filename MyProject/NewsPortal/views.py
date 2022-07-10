from django.shortcuts import render
from .models import Post
from datetime import datetime
from django.views import View
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm
class PostsList(ListView):

    model = Post

    ordering = 'time_in'

    template_name = 'posts.html'

    context_object_name = 'posts'

    paginate_by = 3

    form_class = PostForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['form'] = PostForm()
        return context

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request,*args,**kwargs)



class OnePost(DetailView):

    model = Post

    template_name = 'post.html'

    context_object_name = 'post'



class NewsSearch(ListView):
    model = Post

    template_name = 'posts_search.html'

    context_object_name  = 'posts'

    ordering = '-time_in'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['filter'] = PostFilter(self.request.GET,queryset = self.get_queryset())

        return context

class Add(ListView):
    model = Post

    template_name = 'posts.html'

    context_object_name = 'post_add'

    form_class = PostForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = PostForm()
        return context



