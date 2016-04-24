class Medidas:
    archivo = open('static/iArduino.txt', 'r')
    contenido = archivo.read()
    contenido = contenido.strip()
    contenido = contenido.split(",")
    rangomed = float(contenido[0].strip())
    ppm = float(contenido[1].strip())
    celsius = float(contenido[2].strip())

    def GasMetano(self):
        if self.rangomed > 225 and self.celsius > 16:
            print("hay gas metano en la zona {} y {}".format(self.rangomed))

        else:
            print("El ambiente esta bien {} y {}".format(self.rangomed, self.celsius))

medida = Medidas()
print(medida.GasMetano())
