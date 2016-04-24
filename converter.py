class Medidas():
    archivo = open('static/iArduino.txt', 'r')
    contenido = archivo.read()
    contenido = contenido.strip()
    contenido = contenido.split(",")
    rangomed = float(contenido[0].strip())
    ppm = float(contenido[1].strip())
    celcius = float(contenido[2].strip())
