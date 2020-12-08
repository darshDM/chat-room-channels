from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:room_name>/',views.room,name='room'),
    path('create/',views.Create.as_view(),name='create-room')
]