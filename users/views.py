from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User

def GetUsers(request):
    users = User.objects.filter(is_superuser=False)
    print(users)
    template_name ='users/list.html'
    context = {
        'usuarios': users
    }
    return render(request, template_name, context)