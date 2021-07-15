from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'


class TestPage(TemplateView):
    template_name = 'test.html'
