from django.urls import path
from .views import LoginViewSet, EditCustomUserViewSet, CheckAuthenticated, SearchImagesViewSet, LogoutViewset, SignUpViewSet, UploadedPhotoViewSet
from django.urls import include
from django.conf.urls import url, include

urlpatterns = [
    url(r'^login/$',LoginViewSet.as_view({"post":"checkToken"}), name='login'),
    url(r'^checker/$',CheckAuthenticated.as_view({"get":"isAuthenticated"}), name='checker'),
    url(r'^logout/$',LogoutViewset.as_view(), name='logout'),
    url(r'^signup/$',SignUpViewSet.as_view({"post":"userInfo"}), name='signup'),
    url(r'^upload/$',UploadedPhotoViewSet.as_view({"post":"create", "get":"list"}), name='upload'),
    url(r'^search/$',SearchImagesViewSet.as_view(), name='search'),
    url(r'^edit/(?P<pk>[a-fA-F0-9-]+)/$',EditCustomUserViewSet.as_view({'patch': 'partial_update',}), name='edit'),

]
