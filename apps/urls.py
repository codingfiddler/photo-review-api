from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from apps.photoreview.views import UpView

urlpatterns = [
    url(r'^$', UpView.as_view(), name='up'),
    path('admin/', admin.site.urls),
    path('users/', include('apps.photoreview.urls')),
]
