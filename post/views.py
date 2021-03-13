from django.shortcuts import render,redirect
from .models import Post,Profile

# Create your views here.



def home(request):
    pf = Profile.objects.get(user=request.user)
    posts = Post.objects.exclude(author=pf)
    return render(request,'home.html',{'posts':posts})

    
def addpost(request):
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        author = Post.objects.all()
        author.create(author=user,img=request.FILES['mypost'],caption=request.POST['caption'])
        return redirect('profile/')
    else:
        return render(request,'addpost.html')


    
def editprofile(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST['username']
        user.save()
        profile = Profile.objects.get(user=request.user)
        profile.full_name = request.POST['fullname']
        profile.bio = request.POST['bio']
        profile.save()
        return redirect('profile/')

    else:
        return render(request,'editprofile.html')


    
def team(request):
    return render(request,'team.html')

    
def profile(request):
    prof = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(author=prof)
    return render(request,'profile.html',{'posts':posts,'pf':prof})