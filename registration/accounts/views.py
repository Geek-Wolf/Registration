from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserProfileForm, UserForm
# from django.contrib.auth.models import User
# from accounts.models import UserProfile

# Create your views here.
def SignupView(request):

    Registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)

        if(user_form.is_valid() and profile_form.is_valid()):
            user=user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            # username=user.username
            # password=user.password
            username=user_form.cleaned_data['username']
            password=user_form.cleaned_data['password']

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            Registered=True

            user=authenticate(username=username , password=password)
            login(request, user)
            return redirect('index')
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    return render(request,'accounts/signup.html' ,{'user_form':user_form,
                            'profile_form':profile_form,
                            'Registered':Registered})
