from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db.models import Q
from .models import Friends, FriendRequest, Connections
from .forms import LoginForm
# import pdb


def home(request):
    # if request.session:
    #     del request.session['username']
    return render(request, 'home.html', context={'title':'Home Page'})


def login(request):
    if request.method == 'POST':
        # friend = get_object_or_404(Friends, Q(email_id=request.POST['email_id']), Q(password=request.POST['pswd']))
        friend = get_object_or_404(Friends, Q(username=request.POST['username']), Q(password=request.POST['pswd']))
    
        if friend is not None:
            request.session['username']= request.POST['username']
            return render(request, 'user_data.html', context={'title':'Login', 'username':request.POST['username']})
        else:
            return HttpResponse("Please Enter correct credentials")


def register(request):
    return render(request, 'register.html', context={'title': 'Sign Up'})

def create(request):
    if request.method == 'POST':
        friend = Friends()
        friend.first_name = request.POST['firstname']
        friend.last_name = request.POST['lastname']
        friend.email_id = request.POST['email_id']
        friend.username = request.POST['username']
        friend.password = request.POST['pswd']
        friend.city = request.POST['city']
        friend.state = request.POST['state']
        friend.zip_code = request.POST['zip']
        friend.save()
        return render(request, 'home.html', context={'title':'Home Page'})

def get_current_user(request):
    if request.session:
        return Friends.objects.get(username = request.session['username'])

def friend_list(request):
    # current_user = Friends.objects.exclude(Q(username = request.session['username']))
    current_user = get_current_user(request)
    friends = Connections.objects.filter(Q(person=current_user.pk))
    return render(request, 'friends_details.html', context={'title':'Login', 'username':request.session['username'], 'friends':friends})


def search(request):
    if request.method == 'POST':
        # friends = get_object_or_404(Friends, Q(first_name = request.POST['searchbar']))
        friends = Friends.objects.filter(Q(first_name = request.POST['searchbar']))
        return render(request, 'friends_details.html', context={'title':'Login', 'username':request.session['username'], 'friends': friends})

def sent_request(request,slug,*args, **kwargs):
    if request.method == 'POST':
        # request_from = Friends.objects.get(username = request.session['username'])
        request_from = get_current_user(request)
        request_to = Friends.objects.get(username = slug)
        friend_request = FriendRequest()
        friend_request.from_person = request_from
        friend_request.to_person = request_to
        friend_request.accepted = False
        friend_request.save()
        return render(request, 'user_data.html', context={'title':'Login', 'username':request.session['username']})

def accept_request(request, slug):
    if request.method == 'POST':
        # current_user = Friends.objects.get(username = request.session['username'])
        current_user = get_current_user(request)
        from_users = FriendRequest.objects.filter(Q(to_person=current_user.pk), Q(accepted=False))
        from_user_pk = None
        for from_user in from_users:
            from_user_pk = Friends.objects.get(Q(username = slug)).pk

        FriendRequest.objects.filter(Q(to_person=current_user.pk), 
                                    Q(from_person=from_user_pk), Q(accepted = False)).update(accepted = True)
        connection = Connections()
        connection.person = current_user.pk
        connection.connected_to = from_user_pk
        connection.save()
        return render(request, 'user_data.html', context={'title':'Login', 'username':request.session['username']})

def show_requests(request):
    # current_user = Friends.objects.get(username = request.session['username'])
    current_user = get_current_user(request)
    print(current_user.pk, current_user.username)
    friend_requests = FriendRequest.objects.filter(Q(to_person=current_user.pk), Q(accepted=False))
    return render(request, 'requests_list.html', context={'title':'Login',
                     'username':request.session['username'], 'friends':friend_requests})        

def messages(request):
    pass

def posts(request):
    pass
