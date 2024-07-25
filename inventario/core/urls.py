from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
urlpatterns += [
    path('item/create/', views.create_item, name='create_item'),
    path('item/<int:pk>/edit/', views.edit_item, name='edit_item'),
    path('item/<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('item/<int:pk>/', views.view_item, name='view_item'),
]
urlpatterns += [
    path('dashboard/', views.dashboard, name='dashboard'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]