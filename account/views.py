from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from post.models import Profile

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('instag/')
    else:
        err = ''
        message = ''
        message_class = ''
        if request.method == 'POST':
            username=request.POST['username']
            password=request.POST['password']
            
            user=auth.authenticate(username=username,password=password)
                
            if user is not None:
                auth.login(request,user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('post/')

            else:
                err = 'Invalid Username or Password'
        
            if err:
                message = err
                message_class = 'alert-danger'

        return render(request,'login.html',{'message':message,'message_class':message_class})
    

def register(request):
    err = ''
    message = ''
    message_class = ''
    if request.method == 'POST':
        full_name = request.POST['Full_Name']
        username = request.POST['Username']
        email = request.POST['Email']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']
 
        if password1 == password2 :
            if User.objects.filter(username=username).exists() : 
                err = 'Username already taken'
                    
            elif User.objects.filter(email=email).exists() :
                err = 'Email already taken'
                    
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                profile = Profile()
                profile.user = user
                profile.full_name = full_name
                profile.save()
                    
                message = 'User successfully created'
                message_class = 'alert-success'

                return render(request,'login.html',{'message':message,'message_class':message_class})
        else:
            err = 'Passwords does not match'
        
        if err:
            message = err
            message_class = 'alert-danger'

    return render(request,'signup.html',{'message':message,'message_class':message_class})

def logout(request):
    auth.logout(request)
    return redirect('/')


def about(request):
    return render(request,'about.html')