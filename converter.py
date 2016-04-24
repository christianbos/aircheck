import requests


class Medidas:
    url = "http://habilita.com.mx/iArduino.txt"

    def getFile(self):
        rq = requests.get(self.url)
        contenido = rq.text
        contenido = contenido.strip()
        contenido = contenido.split(",")
        rangomed = float(contenido[0].strip())
        ppm = float(contenido[1].strip())
        celsius = float(contenido[2].strip())

        if rangomed > 225 and celsius > 16:
            return("hay gas metano en la zona {} y {}".format(rangomed))
        else:
            return("El ambiente esta bien {} y {}".format(rangomed, celsius))


medida = Medidas()
print(medida.getFile())
