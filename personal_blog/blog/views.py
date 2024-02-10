from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article, Comment
from .forms import CommentForm
import bleach


class Index(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/index.html'
    paginate_by = 2

class Featured(ListView):
    model = Article
    queryset = Article.objects.filter(featured=True).order_by('-date')
    template_name = 'blog/featured.html'
    paginate_by = 2

class DetailArticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailArticleView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        context['comment_form'] = CommentForm()
        article = Article.objects.get(id=self.kwargs.get('pk'))
        context['comments'] = Comment.objects.filter(article=article)
        if article.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        return context
            
class LikeArticle(View):
    def post(self, request, pk):
        article = Article.objects.get(id=pk)
        if article.likes.filter(pk=self.request.user.id).exists():
            article.likes.remove(request.user.id)
        else:
            article.likes.add(request.user.id)
        
        article.save()
        return redirect('detail_article', pk)

class CommentArticle(CreateView):
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        article_pk = self.kwargs['pk']
        article = get_object_or_404(Article, pk=article_pk)
        cleaned_content = bleach.clean(form.cleaned_data['content'], tags=['p', 'br', 'strong', 'em', 'a'], attributes={'a': ['href', 'title']})
        comment = form.save(commit=False)
        comment.article = article
        comment.author = self.request.user
        comment.content = cleaned_content
        comment.save()
        return redirect(article.get_absolute_url())

class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        article = Article.objects.get(id=self.kwargs.get('pk'))
        return self.request.user.id == article.author.id
    
class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'

    def test_func(self):
        comment = Comment.objects.get(id=self.kwargs.get('pk'))
        return self.request.user.id == comment.author.id
    
    def get_success_url(self):
        article = self.object.article
        return reverse_lazy('detail_article', kwargs={'pk': article.pk})