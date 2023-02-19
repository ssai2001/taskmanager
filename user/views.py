from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            return redirect('list/')
        else:
            messages.error(request, "Invalid credentials")

    return render(request,'user/signin.html')

def signup(request):
    if request.method == "POST":
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        error = False

        print(f_name, l_name, username, email, password)

        if User.objects.filter(username=username).exists():
            # print('SIC already taken')
            messages.error(request,"SIC already exists")
            error = True
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"E-mail already exists")
            error = True
        
        if(error):
            return render(request,'user/signup.html')

        try:
            user = User.objects.create_user(
                first_name = f_name,
                last_name = l_name,
                username = username,
                email = email,
                password = password
            )
            user.save()
            # print('user created')
            messages.success(request,'Account created successfully. Login to continue')
            return redirect('signin')
        except Exception as e:
            print(e)
    return render(request,'user/signup.html')

def log_out(request):
    logout(request)
    return redirect('signin')
