from django.conf.urls import url
from . import views


app_name = 'home'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/(?P<utype>\w+)/$', views.RegisterView.as_view(), name='register'),
    url(r'^verify$', views.VerifyView.as_view(), name='verify'),
    url(r'^updateinfo/(?P<utype>\w+)/$', views.ChangeUserInfo.as_view(), name='updateinfo'),
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),

]