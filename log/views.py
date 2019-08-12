from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from board.models import Profile
from django.contrib import auth
from django.utils import timezone

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            
            new_images = Profile()
            new_images.upload_date = timezone.datetime.now()
            new_images.user = user 
            new_images.image = request.FILES['img1']
            new_images.save()

            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')