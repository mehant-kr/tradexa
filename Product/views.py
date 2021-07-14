from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from . import forms

# Create your views here.

class CreateProductsView(FormView):
    form_class = forms.ProductCreateForm
    template_name = 'products_form.html'
    success_url = 'save/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Save_confirmation(TemplateView):
    template_name = 'save.html'