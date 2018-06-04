from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'login/', views.login, name = 'login'),
    url(r'register/', views.register, name = 'register'),
    url(r'create/', views.create, name = 'create'),
    url(r'friendlist/', views.friend_list, name='friendlist')

]