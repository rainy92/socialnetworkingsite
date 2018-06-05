from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'login/', views.login, name = 'login'),
    url(r'register/', views.register, name = 'register'),
    url(r'create/', views.create, name = 'create'),
    url(r'friendlist/', views.friend_list, name='friendlist'),
    url(r'searchlist/', views.search, name='searchlist'),
    url(r'sentrequest', views.sent_request, name='sentrequest'),
    url(r'acceptrequest', views.accept_request, name='acceptrequest'),

]