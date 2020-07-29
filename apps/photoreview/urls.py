from django.urls import path
from .views import LoginViewSet, CheckAuthenticated, LogoutViewset, SignUpViewSet, UploadedPhotoViewSet, UpView
from django.urls import include
from django.conf.urls import url, include

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^logout1/$', LogoutViewset.as_view(), name='logout1'),
    url(r'^login1/$', LoginViewSet.as_view({"post":"checkToken"}), name='login1'),
    url(r'^checker/$', CheckAuthenticated.as_view({"get":"isAuthenticated"}), name='checker'),
    url(r'^logout1/$', LogoutViewset.as_view(), name='logout1'),
    url(r'^signup1/$', SignUpViewSet.as_view({"post": "userInfo"}), name='signup1'),
    url(r'^upload/$', UploadedPhotoViewSet.as_view({"post":"create", "get":"list"}), name='upload'),

    # url(r'^show/$',UploadedImagesViewSet.as_view()),

]
