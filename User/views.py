from django.shortcuts import render
from django.views.generic import TemplateView
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
from django.views.generic.edit import FormView
from . import forms

# Create your views here.

class CreateUserView(FormView):
    form_class = forms.UserCreateForm
    template_name = 'user_form.html'
    success_url = 'save/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreatePostView(FormView):
    form_class = forms.PostCreateForm
    template_name = 'post_form.html'
    success_url = 'save/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Save_confirmation(TemplateView):
    template_name = 'save.html'
