from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    def get(self, request):
        template_name = 'index.html'
        return render(request, template_name)
