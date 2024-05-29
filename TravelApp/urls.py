from django.urls import path
from .views import (
     HomeView, UserLoginView,
    UserLogoutView, UserView, TodoView
)
from . import views

app_name = 'TravelApp'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    #path('regist/', RegistUserView.as_view(), name='regist'),
    path('regist/', views.regist, name='regist'),
    path('regist_completion', views.regist_completion, name='regist_completion'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    path('user_logout/', UserLogoutView.as_view(), name='user_logout'),

    path('user/', UserView.as_view(), name='user'),
    path('insert_TravelRecord/', views.insert_TravelRecord, name='insert_TravelRecord'),
    path('insert_TravelRecord_completion/', views.insert_TravelRecord_completion, name='insert_TravelRecord_completion'),
    path('destinations_list/', views.destinations_list, name='destinations_list'),
    path('update_destination/<int:destination_id>', views.update_destination, name='update_destination'),
    path('update_destination_completion/', views.update_destination_completion, name='update_destination_completion'),
    path('delete_destination/<int:destination_id>', views.delete_destination, name='delete_destination'),
    path('delete_destination_completion/', views.delete_destination_completion, name='delete_destination_completion'),
    path('map/', views.map, name='map'),

    path('Todo/', TodoView.as_view(), name='Todo'),
    path('insert_TodoList/', views.insert_TodoList, name='insert_TodoList'),
    path('insert_TodoList_completion/', views.insert_TodoList_completion, name='insert_TodoList_completion'),
    path('Todo_List/', views.Todo_List, name='Todo_List'),
    path('update_TodoList/<int:TodoList_id>', views.update_TodoList, name='update_TodoList'),
    path('update_TodoList_completion', views.update_TodoList_completion, name='update_TodoList_completion'),
    path('delete_TodoList/<int:TodoList_id>', views.delete_TodoList, name='delete_TodoList'),

    path('user_edit', views.user_edit, name='user_edit'),
    path('user_edit_completion', views.user_edit_completion, name='user_edit_completion'),
    path('change_password', views.change_password, name='change_password'),
    path('change_password_completion', views.change_password_completion, name='change_password_completion'),
]
