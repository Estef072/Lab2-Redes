import matplotlib.pyplot as plt

titulos = [
    "Acierto en 10000 mensajes con ruido de 0.001",
    "Acierto en 10000 mensajes de con cadena de 10 caracteres",
    "Acierto en mensajes con ruido de 0.001 y cadena de 10 caracteres"
]

labels = [
    "Longitud de cadena",
    "Porcentaje de ruido",
    "Numero de mensajes"
]

def graphit(headers, python, javascript, labelindex):

    # Plot
    plt.figure(figsize=[10,6])
    plt.plot(headers, python, marker='o', label='Python')
    plt.plot(headers, javascript, marker='o', label='Javascript')
    plt.xlabel(labels[labelindex])
    plt.ylabel("Mensajes correctos")
    plt.title(titulos[labelindex])
    plt.legend()
    plt.grid(True)
    plt.show()

graphit(
    [10000, 25000, 50000, 100000],
    [9984/10000, 24946/25000, 49923/50000, 99835/100000],
    [9973/10000, 24948/25000, 49911/50000, 99809/100000],
    2
)

