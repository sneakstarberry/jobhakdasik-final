from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from board.models import Blog

def mypage(request):
    post_list = Blog.objects.all()
    if request.user.is_authenticated:
        my_liked_post = Blog.objects.filter(like = request.user)
    else:
        my_liked_post = None
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'mypage.html', {'blogs':blogs,'liked_post':my_liked_post})

def change(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'change.html')

def opinion(request):
    blogs = Blog.objects.all().filter(category='공지').order_by('-created_date')
    return render(request, 'index.html', {'posts':blogs})
