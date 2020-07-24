from django.urls import path
from .views import SignUpViewSet
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),

    url(r'^signup/$',SignUpViewSet.as_view({"post":"checkToken"}), name='signup'),
]