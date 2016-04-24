from django.shortcuts import render
from django.views.generic import TemplateView
import requests


class HomeView(TemplateView):
    def get(self, request):
        template_name = 'index.html'
        return render(request, template_name)


class MedidasView(TemplateView):
    url = "http://habilita.com.mx/iArduino.txt"
    template_name = 'index.html'

    def getFile(self):
        rq = requests.get(self.url)
        contenido = rq.text
        contenido = contenido.strip()
        contenido = contenido.split(",")
        rangomed = float(contenido[0].strip())
        celsius = float(contenido[2].strip())

        if rangomed > 225 and celsius > 16:
            gasMetano = True
            return(gasMetano)
        else:
            gasMetano = False
            return(gasMetano)

    def get(request, getFile):
        template_name = 'index.html'
        gasmetano = {'gasmetano': getFile}
        return render(request, template_name, gasmetano)
