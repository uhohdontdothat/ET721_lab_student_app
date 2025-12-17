from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import NotesForm
from .models import Notes

# Create your views here.
class HomePageView(ListView):
    model = Notes
    template_name = 'image_list.html'

class CreatePostView(CreateView):
    model = Notes
    form_class = NotesForm
    template_name = 'post.html'
    success_url = reverse_lazy('image_list')