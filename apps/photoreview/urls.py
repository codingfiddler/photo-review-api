from django.urls import path
from .views import LoginViewSet, CheckAuthenticated, LogoutViewset
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^login1/$',LoginViewSet.as_view({"post":"checkToken"}), name='login1'),
    url(r'^checker/$',CheckAuthenticated.as_view({"get":"isAuthenticated"}), name='checker'),
    url(r'^logout1/$',LogoutViewset.as_view(), name='logout1'),
]