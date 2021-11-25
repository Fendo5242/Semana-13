import datetime


def mostrarfecha():
    fecha = datetime.datetime.now()
    print("La fecha actual es: ")
    print(fecha.strftime("%Y-%m-%d")) 
    print("La hora actual es: ")
    print(fecha.strftime("%I:%M:%S"))


mostrarfecha()
