from django.shortcuts import render
from django.views.generic import TemplateView


class MedidorView(TemplateView):
    def get(self, request):
        template_name = 'medidor.html'
        return render(request, template_name)
