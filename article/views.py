from django.shortcuts import render,redirect,get_object_or_404,reverse
from .models import Article,Comment
from .forms import AddArticle
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    
    context= {
        "articles":articles
    }
    return render(request,"dashboard.html",context)
@login_required(login_url = "user:login")
def addarticle(request):
    form= AddArticle(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author= request.user
        article.save()
        messages.success(request,"Makaleniz Kayıt Edildi")
        
        articles = Article.objects.filter(author = request.user)
    
        context= {
        "articles":articles
        }
        return redirect("article:dashboard")
    context= {
        "form":form
    }
    return render(request,"addarticle.html",context)

def articledetails(request,id):
    
    #article= Article.objects.filter(id=id).first()
    article= get_object_or_404(Article,id=id)
    comment = article.comments.all()
    context={
        "article":article,"comments":comment
    }
    
    
    return render(request,"articledetails.html",context)
def articles(request):

    keyword = request.GET.get("keyword")

    if keyword:
        
        articles = Article.objects.filter(title__contains=keyword)

        return render(request,"articles.html",{"articles":articles})

    articles= Article.objects.all()

    return render(request,"articles.html",{"articles":articles})

@login_required(login_url = "user:login")
def update(request,id):

    article = get_object_or_404(Article,id=id)
    
    form = AddArticle(request.POST or None,request.FILES or None, instance=article)

    if form.is_valid():
        article = form.save(commit=False)
        article.author= request.user
        article.save()
        messages.success(request,"Makaleniz Güncellendi")
        
        articles = Article.objects.filter(author = request.user)
    
        context= {
        "articles":articles
        }
        return redirect("article:dashboard")

    return render(request,"update.html",{"form":form})
@login_required(login_url = "user:login")
def delete(request,id):
    
    article= get_object_or_404(Article,id=id)
    article.delete()


    return redirect("article:dashboard")

def addcomment(request,id):
    
    article = get_object_or_404(Article,id=id)

    if request.method == "POST":

        comment_content = request.POST.get("comment_content")
        comment_author = request.POST.get("comment_author")

        newComment = Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()
        return redirect(reverse("article:articledetails",kwargs={"id":id}))