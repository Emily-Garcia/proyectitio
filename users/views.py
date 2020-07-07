from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.models import User
from django import views
from .forms import UserUpdateform, Profileform, UserCreateform
def GetUsers(request):
    users = User.objects.filter(is_superuser=False)
    print(users)
    template_name ='users/list.html'
    context = {
        'usuarios': users
    }
    return render(request, template_name, context)

def GetUser(request, id):
    user = User.objects.get(id=id)
    template_name = 'users/detail.html'
    context = {
        'user': user
    }
    return render(request, template_name, context)

class CreateUser(views.View):
    def get(self, request):
        user_form = UserCreateform()
        profile_form = Profileform()
        template_name = 'users/form.html'
        context = {
            'user_form' : user_form,
            'profile_form' : profile_form
        }
        return render(request, template_name, context)

    def post(self, request):
        user_form = UserCreateform(request.POST)
        profile_form = Profileform(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('users:detail', user.id)
        else:
            template_name = 'users/form.html'
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            return render(request, template_name, context)

class UpdateUser(views.View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        user_form = UserUpdateform(instance=user)
        profile_form = Profileform(instance=user.profile)
        template_name = 'users/form.html'
        context = {
            'user_form' : user_form,
            'profile_form': profile_form,
            'id': id,
            'image': user.profile.image
        }
        return render(request, template_name, context)

    def post(self, request, id):
        user = User.objects.get(pk=id)
        user_form = UserUpdateform(request.POST, instance=user)
        profile_form = Profileform(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()
            return redirect('users:detail', user.id)
        else:
            template_name = 'users/form.html'
            context = {
                'user_form' : user_form,
                'profile_form': profile_form,
                'id': id,
                'image': user.profile.image
            }
            return redirect(request, template_name, context)

def DeleteUser(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('users:list')