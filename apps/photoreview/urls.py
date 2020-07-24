from django.urls import path
from .views import SignUpView
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),

    url(r'^signup/$',SignUpView.as_view(), name='signup'),
]