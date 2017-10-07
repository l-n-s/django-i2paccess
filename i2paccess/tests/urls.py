from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^secretview/$', views.secretfunction, name='secret function'),
    url(r'^secretclassview/$', views.SecretClass.as_view(), name='secret class'),
]
