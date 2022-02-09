from django.urls import include, path, re_path
from . import views

app_name='catalog'
urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r'^$', views.index, name='index')
]
