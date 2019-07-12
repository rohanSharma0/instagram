from django.shortcuts import render
from django.contrib.auth.models import  User
from django.urls import reverse
from django.views.generic import ListView , CreateView , DeleteView
from django.contrib.auth.decorators import login_required
from .models import InstaPost
# Create your views here.



class PostListView(ListView):
    model = InstaPost
    template_name = 'main/index.html'
    context_object_name = 'posts'
    ordering = ['-post_date']
    paginate_by = 4

class PostCreateView(CreateView,ListView):
    model = InstaPost
    template_name = 'main/profile.html'
    context_object_name = 'posts'
    
    fields = [ 'post_image', 'post_caption' , 'post_location']

    def form_valid(self , form):
        form.instance.post_user = self.request.user
        return super().form_valid(form)


