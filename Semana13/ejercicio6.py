import datetime


def mostrarfecha():
    fecha = datetime.datetime.now()
    print("La hora actual (formato 24 horas) es: ")
    print(fecha.strftime("%H:%M:%S"))
    print("La hora actual (formato 12 horas) es: ")
    print(fecha.strftime("%I:%M:%S"))
    print("La fecha actual es: ")
    print(fecha.strftime("%Y-%m-%d")) 

mostrarfecha()

