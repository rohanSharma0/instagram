from django.urls import path , include

from . import views

urlpatterns = [
    path('' ,views.login ,name='login'),
    path('register/' , views.register ,name='register'),
    path('edit/<str:username>/', views.editprofile,name="editprofile"),
    path('logout/', views.logout,name="logout"),
]
