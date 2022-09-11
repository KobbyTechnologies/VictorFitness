from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView,  DetailView
from .models import Post

# Create your views here.
class ArticleView(ListView):
    template_name = 'articles.html'
    queryset = Post.objects.all()
    context_object_name = 'articles'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class ArticleDetailView(DetailView):
    template_name = 'article-detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def article_view(request):
    return render(request, 'articles.html')

