from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    url('^home/', include('friends.urls')),
    url('admin/', admin.site.urls),
]
