from django.shortcuts import render

# Create your views here.

def article_view(request):
    return render(request, 'articles.html')
