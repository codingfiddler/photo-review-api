from django.urls import path
from .views import LoginViewSet, EditCustomUserViewSet, SearchPersonViewSet, CommentViewSet, CheckAuthenticated, SearchImagesViewSet, LogoutViewset, SignUpViewSet, UploadedPhotoViewSet
from django.urls import include
from django.conf.urls import url, include

urlpatterns = [
    url(r'^login/$',LoginViewSet.as_view({"post":"checkToken"}), name='login'),
    url(r'^checker/$',CheckAuthenticated.as_view({"get":"isAuthenticated"}), name='checker'),
    url(r'^logout/$',LogoutViewset.as_view(), name='logout'),
    url(r'^signup/$',SignUpViewSet.as_view({"post":"userInfo"}), name='signup'),
    url(r'^upload/$',UploadedPhotoViewSet.as_view({"post":"create", "get":"list"}), name='upload'),
    url(r'^upload/(?P<pk>[a-fA-F0-9-]+)/$', UploadedPhotoViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='edit'),
    url(r'^comment/$',CommentViewSet.as_view({"post":"create", "get":"list"}), name='comment'),
    url(r'^search/$',SearchImagesViewSet.as_view(), name='search'),
    url(r'^searchuser/$',SearchPersonViewSet.as_view(), name='searchuser'),
    url(r'^edit/(?P<pk>[a-fA-F0-9-]+)/$',EditCustomUserViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update',}), name='edit'),
]
