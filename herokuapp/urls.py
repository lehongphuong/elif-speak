from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('chatBotGet', views.chatBotGet, name='chatBotGet'),
    path('chatBotPost', views.chatBotPost, name='chatBotPost'),
    # *******************************************************
    # begin User 
    path('createDataUser', views.createDataUser, name='createDataUser'),
    path('readDataUser', views.readDataUser, name='readDataUser'),
    path('updateDataUser', views.updateDataUser, name='updateDataUser'),
    path('deleteDataUser', views.deleteDataUser, name='deleteDataUser'),
    path('findDataUser', views.findDataUser, name='findDataUser'),
    # end User
    # *******************************************************
]
