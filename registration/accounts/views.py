from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.views.generic import CreateView
from .forms import UserProfileForm, UserForm
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

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            Registered=True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    return render(request,'accounts/signup.html' ,{'user_form':user_form,
                            'profile_form':profile_form,
                            'Registered':Registered})
