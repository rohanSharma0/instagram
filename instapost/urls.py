from django.urls import path
from .views import PostListView , PostCreateView

from . import views

urlpatterns = [
    path('home/' , PostListView.as_view() ,name='home'),
    path('accounts/<str:username>/' ,PostCreateView.as_view() ,name='profile'),
]