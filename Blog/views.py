from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DetailView,View,TemplateView,DeleteView
from Blog.models import Blog,Comment,Like
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

class Create_blog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'Blog/create.html'
    fields = ('bTitle', 'bContent', 'image',)

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.writter = self.request.user
        title = blog.bTitle
        blog.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog.save()
        return HttpResponseRedirect(reverse('index'))


class Blog_List(ListView):
    object = 'blogs'
    model = Blog
    template_name = 'Blog/blog_list.html'
