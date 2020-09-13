from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog, Comment, Profile
from django.core.paginator import Paginator
from .form import NewBlog, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import JsonResponse , HttpResponseRedirect

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 8)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다.
    posts = paginator.get_page(page)

    # assets =  get_object_or_404(Profile , user=request.user)
    return render(request, 'index.html', {'blogs':blogs, 'posts':posts})

# 홈페이지와는 다른 게시판 함수
def post_home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 8)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다.
    posts = paginator.get_page(page)
    return render(request, 'post.html', {'blogs':blogs, 'posts':posts})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/board/'+str(board.id))



def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})



def add_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():


            comment = form.save(commit=False)

            comment.post = blog
            comment.save()
            return redirect('detail', blog_id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

def del_comment(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.delete()
    return redirect('home')

def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.save()
            return redirect('home')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'add_comment.html', {'form': form})

@login_required(login_url='/login/')
def newcreate(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = NewBlog()
        return render(request, 'new.html', {'form':form})

@login_required(login_url='/login/')
def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    if request.method == "POST":
        form = NewBlog(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewBlog(instance = blog)
    return render(request, 'new.html', {'form':form})

@login_required(login_url='/login/')
def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

def search(request):
    if request.GET.get('q'):
        que = request.GET.get('q')
        variable_column = request.GET.get('search_filter')
        search_type = 'contains'
        filter = variable_column + '__' + search_type
        posts = Blog.objects.filter(**{ filter: request.GET.get('q') }).order_by('-pub_date')
        return render(request , 'result.html' , {'result' : posts , 'query' : que})
    else:
        return redirect('home') 

def like(request,blog_id):
    blog=get_object_or_404(Blog, pk = blog_id)
    if blog.like.filter(username=request.user.username).exists():
        blog.like.remove(request.user)    
    else:
        blog.like.add(request.user)
    blog.save()
    return redirect('/board/%d'%blog.pk)

def favorite(request,blog_id):
    blog=get_object_or_404(Blog, pk = blog_id)
    if blog.favorite.filter(username=request.user.username).exists():
        blog.favorite.remove(request.user)
    else:
        blog.favorite.add(request.user)
    blog.save()
    return redirect('detail', blog_id)

        # 카테고리
def category_notice(request):
    blogs = Blog.objects.all().filter(category='공지').order_by('-created_date')
    return render(request, 'index.html', {'posts':blogs})

    queryset = queryset.order_by('field1') # 지정 필드 오름차순 요청

def category_politics(request):
    blogs = Blog.objects.all().filter(category='정치').order_by('-created_date')
    return render(request, 'index.html', {'posts':blogs})

    queryset = queryset.order_by('field1') # 지정 필드 오름차순 요청

def category_social(request):
    blogs = Blog.objects.all().filter(category='사회').order_by('-created_date')
    return render(request, 'index.html', {'posts':blogs})

    queryset = queryset.order_by('field1') # 지정 필드 오름차순 요청

def category_economy(request):
    blogs = Blog.objects.all().filter(category='경제').order_by('-created_date')
    return render(request, 'index.html', {'posts':blogs})

    queryset = queryset.order_by('field1') # 지정 필드 오름차순 요청

def category_it(request):
    blogs = Blog.objects.all().filter(category='IT').order_by('-created_date')
    return render(request, 'index.html', {'posts':blogs})

    queryset = queryset.order_by('field1') # 지정 필드 오름차순 요청

def category_science(request):
    blogs = Blog.objects.all().filter(category='과학').order_by('-created_date')
    return render(request, 'index.html', {'posts':blogs})

    queryset = queryset.order_by('field1') # 지정 필드 오름차순 요청