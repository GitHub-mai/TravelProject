from django.urls import path
from .views import (
    RegistUserView, HomeView, UserLoginView,
    UserLogoutView, UserView, TodoView
)
from . import views

app_name = 'TravelApp'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('regist/', RegistUserView.as_view(), name='regist'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    path('user_logout/', UserLogoutView.as_view(), name='user_logout'),

    path('user/', UserView.as_view(), name='user'),
    path('insert_TravelRecord/', views.insert_TravelRecord, name='insert_TravelRecord'),
    path('destinations_list/', views.destinations_list, name='destinations_list'),
    path('update_destination/<int:destination_id>', views.update_destination, name='update_destination'),
    path('delete_destination/<int:destination_id>', views.delete_destination, name='delete_destination'),
    path('map/', views.map, name='map'),

    path('Todo/', TodoView.as_view(), name='Todo'),
    path('insert_TodoList/', views.insert_TodoList, name='insert_TodoList'),
    path('Todo_List/', views.Todo_List, name='Todo_List'),
    path('update_TodoList/<int:TodoList_id>', views.update_TodoList, name='update_TodoList'),
    path('delete_TodoList/<int:TodoList_id>', views.delete_TodoList, name='delete_TodoList'),

    path('user_edit', views.user_edit, name='user_edit'),
    path('change_password', views.change_password, name='change_password'),
]
