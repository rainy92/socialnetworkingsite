from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db.models import Q
from .models import Friends


def home(request):
    return render(request, 'home.html', context={'title':'Home Page'})


def login(request):
    if request.method == 'POST':
        friend = Friends.objects.get(Q(email_id=request.POST['email_id']), Q(password=request.POST['pswd']))
        # friend = authenticate(username=request.POST['email_id'], password=request.POST['pswd'])
        if friend is not None:

            return render(request, 'user_data.html', context={'title':'Login', 'username':friend.first_name})
        else:
            return HttpResponse("Please Enter correct credentials")


def register(request):
    return render(request, 'register.html', context={'title': 'Sign Up'})

def create(request):
    if request.method == 'POST':
        # if form.is_valid:
        friend = Friends()
        friend.first_name = request.POST['firstname']
        friend.last_name = request.POST['lastname']
        friend.email_id = request.POST['email_id']
        friend.password = request.POST['pswd']
        friend.city = request.POST['city']
        friend.state = request.POST['state']
        friend.zip_code = request.POST['zip']
        friend.save()
        return render(request, 'home.html', context={'title':'Home Page'})  

def friend_list(request):
         friends = Friends.objects.all()
         return render(request, 'friends_details.html', context={'friends':friends} )