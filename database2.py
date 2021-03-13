# BASIC DATABASE OF THE FREQUENCY OWNERS QUITO-ECUADOR
# ALL RIGHTS RESERVED TO THE EDITOR: ANDRES FUERTES RUIZ @sirafr
# RECOMMENDATION: Python3 and Pillow package

from tkinter import *
from tkinter import messagebox
from PIL import Image

# BODY
root = Tk()
root.title("Frecuencias Almacenadas")

myFrame = Frame(root, width=1000, height=600)
myFrame.pack()

# DATA DECLARATION
data = StringVar()
frecuencias = [599, 617, 639, 549, 623, 189, 195, 207,
               213, 69, 57, 63, 563, 175, 557, 79, 85, 527, 587, 665, 521, 629, 677, 201, 575, 539, 533, 183]

# FUNCTIONS


def code_validation():

    if int(box_freq.get()) in frecuencias:
        data.set("Frecuencias disponible")
    else:
        data.set("Frecuencias no almacenada :(")


def new_windows():
    if box_freq.get() == "599":
        window1()
    if box_freq.get() == "617":
        window2()
    if box_freq.get() == "639":
        window3()
    if box_freq.get() == "549":
        window4()
    if box_freq.get() == "623":
        window5()
    if box_freq.get() == "189":
        window6()
    if box_freq.get() == "195":
        window7()
    if box_freq.get() == "207":
        window8()
    if box_freq.get() == "213":
        window9()
    if box_freq.get() == "69":
        window10()
    if box_freq.get() == "57":
        window11()
    if box_freq.get() == "63":
        window12()
    if box_freq.get() == "563":
        window13()
    if box_freq.get() == "175":
        window14()
    if box_freq.get() == "557":
        window15()
    if box_freq.get() == "79":
        window16()
    if box_freq.get() == "85":
        window17()
    if box_freq.get() == "527":
        window18()
    if box_freq.get() == "587":
        window19()
    if box_freq.get() == "665":
        window20()
    if box_freq.get() == "521":
        window21()
    if box_freq.get() == "629":
        window22()
    if box_freq.get() == "677":
        window23()
    if box_freq.get() == "201":
        window24()
    if box_freq.get() == "653":
        window25()
    if box_freq.get() == "575":
        window26()
    if box_freq.get() == "539":
        window27()
    if box_freq.get() == "533":
        window28()
    if box_freq.get() == "183":
        window29()

# PICTURES CODE


def print_image(number):
    try:
        imagen = Image.open('imagen{}_1.jpg'.format(number))
        imagen2 = Image.open('imagen{}_2.jpg'.format(number))
        imagen3 = Image.open('imagen{}_3.jpg'.format(number))
        imagen.show()
        imagen2.show()
        imagen3.show()
    except:
        print("No ha sido posible cargar la imagen")

# WINDOWS FUNCTIONS


def window1():
    toplevel599 = Toplevel()
    toplevel599.title("Frecuencia 599")
    toplevel599.focus_set()
    toplevel599.geometry('300x300')
    datafreq599 = Label(
        toplevel599, text="Datos de frecuencia 599", fg="blue", font=("Arial", 14))
    datafreq599a = Label(toplevel599, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq599b = Label(toplevel599, text="Tipo: Reptidor, canal 35 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq599c = Label(toplevel599, text="Representante legal: Rafael Peralta ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq599d = Label(toplevel599, text="Nombre del canal: Canal Intimas ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq599e = Label(toplevel599, text="Potencia efectiva radiada: 57100 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq599f = Label(toplevel599, text="Area de cobertura: Quito, Ruminahui ", font=("Verdana", 10), padx=12,
                         pady=7)
    button599 = Button(toplevel599, text="Ver mapa",
                       pady=12, command=lambda: print_image(599))

    datafreq599.pack()
    datafreq599a.pack()
    datafreq599b.pack()
    datafreq599c.pack()
    datafreq599d.pack()
    datafreq599e.pack()
    datafreq599f.pack()
    button599.pack()


def window2():
    toplevel617 = Toplevel()
    toplevel617.title("Frecuencia 617")
    toplevel617.focus_set()
    toplevel617.geometry('300x300')
    datafreq617 = Label(
        toplevel617, text="Datos de frecuencia 617", fg="blue", font=("Arial", 14))
    datafreq617a = Label(toplevel617, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq617b = Label(toplevel617, text="Tipo: Matriz , canal 38", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq617c = Label(toplevel617, text="Representante legal: Wilson Suarez ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq617d = Label(toplevel617, text="Nombre del canal: RED TV Ecuador", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq617e = Label(toplevel617, text="Potencia efectiva radiada: 39720 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq617f = Label(toplevel617, text="Area de cobertura: Quito y alrededores ", font=("Verdana", 10), padx=12,
                         pady=7)
    button617 = Button(toplevel617, text="Ver mapa",
                       pady=12, command=lambda: print_image(617))

    datafreq617.pack()
    datafreq617a.pack()
    datafreq617b.pack()
    datafreq617c.pack()
    datafreq617d.pack()
    datafreq617e.pack()
    datafreq617f.pack()
    button617.pack()


def window3():
    toplevel639 = Toplevel()
    toplevel639.title("Frecuencia 639")
    toplevel639.focus_set()
    toplevel639.geometry('300x300')
    datafreq639 = Label(
        toplevel639, text="Datos de frecuencia 639", fg="blue", font=("Arial", 14))
    datafreq639a = Label(toplevel639, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq639b = Label(toplevel639, text="Tipo: Matriz, canal 42 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq639c = Label(toplevel639, text="Representante legal: Jose Serrano ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq639d = Label(toplevel639, text="Nombre del canal: TV Legislativa ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq639e = Label(toplevel639, text="Potencia efectiva radiada: 21985 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq639f = Label(toplevel639, text="Area de cobertura: Quito, Pedro Moncayo, Caymbe ", font=("Verdana", 10),
                         padx=12, pady=7)
    button639 = Button(toplevel639, text="Ver mapa",
                       pady=12, command=lambda: print_image(639))

    datafreq639.pack()
    datafreq639a.pack()
    datafreq639b.pack()
    datafreq639c.pack()
    datafreq639d.pack()
    datafreq639e.pack()
    datafreq639f.pack()
    button639.pack()


def window4():
    toplevel549 = Toplevel()
    toplevel549.title("Frecuencia 549")
    toplevel549.focus_set()
    toplevel549.geometry('300x300')
    datafreq549 = Label(
        toplevel549, text="Datos de frecuencia 549", fg="blue", font=("Arial", 14))
    datafreq549a = Label(toplevel549, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq549b = Label(toplevel549, text="Tipo: Matriz, canal 27 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq549c = Label(toplevel549, text="Representante legal: Hernan Taco", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq549d = Label(toplevel549, text="Nombre del canal: ASOMA Vision ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq549e = Label(toplevel549, text="Potencia efectiva radiada: 43050 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq549f = Label(toplevel549, text="Area de cobertura: Quito", font=(
        "Verdana", 10), padx=12, pady=7)
    button549 = Button(toplevel549, text="Ver mapa",
                       pady=12, command=lambda: print_image(549))

    datafreq549.pack()
    datafreq549a.pack()
    datafreq549b.pack()
    datafreq549c.pack()
    datafreq549d.pack()
    datafreq549e.pack()
    datafreq549f.pack()
    button549.pack()


def window5():
    toplevel623 = Toplevel()
    toplevel623.title("Frecuencia 623")
    toplevel623.focus_set()
    toplevel623.geometry('300x300')
    datafreq623 = Label(
        toplevel623, text="Datos de frecuencia 623", fg="blue", font=("Arial", 14))
    datafreq623a = Label(toplevel623, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq623b = Label(toplevel623, text="Tipo: Matriz, canal 39 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq623c = Label(toplevel623, text="Representante legal: Sandra Aguirre", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq623d = Label(toplevel623, text="Nombre del canal: Majestad TV ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq623e = Label(toplevel623, text="Potencia efectiva radiada: 36659 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq623f = Label(toplevel623, text="Area de cobertura: Quininde la concordia", font=("Verdana", 10), padx=12,
                         pady=7)
    button623 = Button(toplevel623, text="Ver mapa",
                       pady=12, command=lambda: print_image(623))

    datafreq623.pack()
    datafreq623a.pack()
    datafreq623b.pack()
    datafreq623c.pack()
    datafreq623d.pack()
    datafreq623e.pack()
    datafreq623f.pack()
    button623.pack()


def window6():
    toplevel189 = Toplevel()
    toplevel189.title("Frecuencia 189")
    toplevel189.focus_set()
    toplevel189.geometry('300x300')
    datafreq189 = Label(
        toplevel189, text="Datos de frecuencia 189", fg="blue", font=("Arial", 14))
    datafreq189a = Label(toplevel189, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq189b = Label(toplevel189, text="Tipo: Repetidor, canal 9 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq189c = Label(toplevel189, text="Representante legal: Martha Moncayo", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq189d = Label(toplevel189, text="Nombre del canal: Cadena ecuatoriana de TV ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq189e = Label(toplevel189, text="Potencia efectiva radiada: 100 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq189f = Label(toplevel189, text="Area de cobertura: Sur de Quito", font=(
        "Verdana", 10), padx=12, pady=7)
    button189 = Button(toplevel189, text="Ver mapa",
                       pady=12, command=lambda: print_image(189))

    datafreq189.pack()
    datafreq189a.pack()
    datafreq189b.pack()
    datafreq189c.pack()
    datafreq189d.pack()
    datafreq189e.pack()
    datafreq189f.pack()
    button189.pack()


def window7():
    toplevel195 = Toplevel()
    toplevel195.title("Frecuencia 195")
    toplevel195.focus_set()
    toplevel195.geometry('300x300')
    datafreq195 = Label(
        toplevel195, text="Datos de frecuencia 195", fg="blue", font=("Arial", 14))
    datafreq195a = Label(toplevel195, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq195b = Label(toplevel195, text="Tipo: Repetidor, canal 10 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq195c = Label(toplevel195, text="Representante legal: Martha Moncayo", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq195d = Label(toplevel195, text="Nombre del canal: Cadena ecuatoriana de TV ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq195e = Label(toplevel195, text="Potencia efectiva radiada: 178250 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq195f = Label(toplevel195, text="Area de cobertura: El Carmen, San Miguel de los Bancos, Sto Domingo",
                         font=("Verdana", 10), padx=12, pady=7)
    button195 = Button(toplevel195, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(195))

    datafreq195.pack()
    datafreq195a.pack()
    datafreq195b.pack()
    datafreq195c.pack()
    datafreq195d.pack()
    datafreq195e.pack()
    datafreq195f.pack()
    button195.pack()


def window8():
    toplevel207 = Toplevel()
    toplevel207.title("Frecuencia 207")
    toplevel207.focus_set()
    toplevel207.geometry('300x300')
    datafreq207 = Label(
        toplevel207, text="Datos de frecuencia 207", fg="blue", font=("Arial", 14))
    datafreq207a = Label(toplevel207, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq207b = Label(toplevel207, text="Tipo: Repetidor, canal 12 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq207c = Label(toplevel207, text="Representante legal: Veronica Bolanos", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq207d = Label(toplevel207, text="Nombre del canal: CANAL UNO ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq207e = Label(toplevel207, text="Potencia efectiva radiada: 141253 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq207f = Label(toplevel207, text="Area de cobertura: Quito, Ruminahui", font=(
        "Verdana", 10), padx=12, pady=7)
    button207 = Button(toplevel207, text="Ver mapa ",
                       pady=12, command=lambda: print_image(207))

    datafreq207.pack()
    datafreq207a.pack()
    datafreq207b.pack()
    datafreq207c.pack()
    datafreq207d.pack()
    datafreq207e.pack()
    datafreq207f.pack()
    button207.pack()


def window9():
    toplevel213 = Toplevel()
    toplevel213.title("Frecuencia 213")
    toplevel213.focus_set()
    toplevel213.geometry('300x300')
    datafreq213 = Label(
        toplevel213, text="Datos de frecuencia 213", fg="blue", font=("Arial", 14))
    datafreq213a = Label(toplevel213, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq213b = Label(toplevel213, text="Tipo: Repetidor, canal 12 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq213c = Label(toplevel213, text="Representante legal: Veronica Bolanos", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq213d = Label(toplevel213, text="Nombre del canal: CANAL UNO ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq213e = Label(toplevel213, text="Potencia efectiva radiada: 100 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq213f = Label(toplevel213, text="Area de cobertura: Quito, Ruminahui", font=(
        "Verdana", 10), padx=12, pady=7)
    button213 = Button(toplevel213, text="Ver mapa",
                       pady=12, command=lambda: print_image(213))

    datafreq213.pack()
    datafreq213a.pack()
    datafreq213b.pack()
    datafreq213c.pack()
    datafreq213d.pack()
    datafreq213e.pack()
    datafreq213f.pack()
    button213.pack()


def window10():
    toplevel69 = Toplevel()
    toplevel69.title("Frecuencia 69")
    toplevel69.focus_set()
    toplevel69.geometry('300x300')
    datafreq69 = Label(toplevel69, text="Datos de frecuencia 69",
                       fg="blue", font=("Arial", 14))
    datafreq69a = Label(toplevel69, text="Pichincha - TV abierta ",
                        font=("Verdana", 10), padx=12, pady=7)
    datafreq69b = Label(toplevel69, text="Tipo: Matriz, canal 4 ",
                        font=("Verdana", 10), padx=12, pady=7)
    datafreq69c = Label(toplevel69, text="Representante legal: Sebastian Corral", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq69d = Label(toplevel69, text="Nombre del canal: Teleamazonas ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq69e = Label(toplevel69, text="Potencia efectiva radiada: 178250 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq69f = Label(toplevel69, text="Area de cobertura: Quito y alrededores", font=("Verdana", 10), padx=12,
                        pady=7)
    button69 = Button(toplevel69, text="Ver mapa",
                      pady=12, command=lambda: print_image(69))

    datafreq69.pack()
    datafreq69a.pack()
    datafreq69b.pack()
    datafreq69c.pack()
    datafreq69d.pack()
    datafreq69e.pack()
    datafreq69f.pack()
    button69.pack()


def window11():
    toplevel57 = Toplevel()
    toplevel57.title("Frecuencia 57")
    toplevel57.focus_set()
    toplevel57.geometry('300x300')
    datafreq57 = Label(toplevel57, text="Datos de frecuencia 57",
                       fg="blue", font=("Arial", 14))
    datafreq57a = Label(toplevel57, text="Pichincha - TV abierta ",
                        font=("Verdana", 10), padx=12, pady=7)
    datafreq57b = Label(toplevel57, text="Tipo: Matriz, canal 2 ",
                        font=("Verdana", 10), padx=12, pady=7)
    datafreq57c = Label(toplevel57, text="Representante legal: Jose Perez", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq57d = Label(toplevel57, text="Nombre del canal: TV del pacifico ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq57e = Label(toplevel57, text="Potencia efectiva radiada: 189290 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq57f = Label(toplevel57, text="Area de cobertura: Quito", font=(
        "Verdana", 10), padx=12, pady=7)
    button57 = Button(toplevel57, text="Ver mapa",
                      pady=12, command=lambda: print_image(57))

    datafreq57.pack()
    datafreq57a.pack()
    datafreq57b.pack()
    datafreq57c.pack()
    datafreq57d.pack()
    datafreq57e.pack()
    datafreq57f.pack()
    button57.pack()


def window12():
    toplevel63 = Toplevel()
    toplevel63.title("Frecuencia 63")
    toplevel63.focus_set()
    toplevel63.geometry('300x300')
    datafreq63 = Label(toplevel63, text="Datos de frecuencia 63",
                       fg="blue", font=("Arial", 14))
    datafreq63a = Label(toplevel63, text="Pichincha - TV abierta ",
                        font=("Verdana", 10), padx=12, pady=7)
    datafreq63b = Label(toplevel63, text="Tipo: Repetidor, canal 3 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq63c = Label(toplevel63, text="Representante legal: Jose Perez", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq63d = Label(toplevel63, text="Nombre del canal: TV del pacifico ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq63e = Label(toplevel63, text="Potencia efectiva radiada: 7227.2 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq63f = Label(toplevel63, text="Area de cobertura: Quito", font=(
        "Verdana", 10), padx=12, pady=7)
    button63 = Button(toplevel63, text="Mapa Geografico",
                      pady=12, command=lambda: print_image(63))

    datafreq63.pack()
    datafreq63a.pack()
    datafreq63b.pack()
    datafreq63c.pack()
    datafreq63d.pack()
    datafreq63e.pack()
    datafreq63f.pack()
    button63.pack()


def window13():
    toplevel563 = Toplevel()
    toplevel563.title("Frecuencia 563")
    toplevel563.focus_set()
    toplevel563.geometry('300x300')
    datafreq563 = Label(
        toplevel563, text="Datos de frecuencia 563", fg="blue", font=("Arial", 14))
    datafreq563a = Label(toplevel563, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq563b = Label(toplevel563, text="Tipo: Matriz, canal 29 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq563c = Label(toplevel563, text="Representante legal: Emilio Najas", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq563d = Label(toplevel563, text="Nombre del canal: Telesucesos ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq563e = Label(toplevel563, text="Potencia efectiva radiada: 39720 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq563f = Label(toplevel563, text="Area de cobertura: Ruminahui, Quito", font=(
        "Verdana", 10), padx=12, pady=7)
    button563 = Button(toplevel563, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(563))

    datafreq563.pack()
    datafreq563a.pack()
    datafreq563b.pack()
    datafreq563c.pack()
    datafreq563d.pack()
    datafreq563e.pack()
    datafreq563f.pack()
    button563.pack()


def window14():
    toplevel175 = Toplevel()
    toplevel175.title("Frecuencia 175")
    toplevel175.focus_set()
    toplevel175.geometry('300x300')
    datafreq175 = Label(
        toplevel175, text="Datos de frecuencia 175", fg="blue", font=("Arial", 14))
    datafreq175a = Label(toplevel175, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq175b = Label(toplevel175, text="Tipo: Matriz - Repetidor, canal 7 ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq175c = Label(toplevel175, text="Representante legal: Martha Moncayo", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq175d = Label(toplevel175, text="Nombre del canal: Ecuador TV ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq175e = Label(toplevel175, text="Potencia efectiva radiada: 80000,126,511,2594 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq175f = Label(toplevel175, text="Area de cobertura: Ruminahui, Quito, Minas", font=(
        "Verdana", 10), padx=12, pady=7)
    button175 = Button(toplevel175, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(175))

    datafreq175.pack()
    datafreq175a.pack()
    datafreq175b.pack()
    datafreq175c.pack()
    datafreq175d.pack()
    datafreq175e.pack()
    datafreq175f.pack()
    button175.pack()


def window15():
    toplevel557 = Toplevel()
    toplevel557.title("Frecuencia 557")
    toplevel557.focus_set()
    toplevel557.geometry('300x300')
    datafreq557 = Label(
        toplevel557, text="Datos de frecuencia 557", fg="blue", font=("Arial", 14))
    datafreq557a = Label(toplevel557, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq557b = Label(toplevel557, text="Tipo: Matriz - Matriz, canal 28 ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq557c = Label(toplevel557, text="Representante legal: Augusto Espinoza", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq557d = Label(toplevel557, text="Nombre del canal: Educa, Ministerio de educacion ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq557e = Label(toplevel557, text="Potencia efectiva radiada: 45496 ", font=("Verdana", 10),
                         padx=12, pady=7)
    datafreq557f = Label(toplevel557, text="Area de cobertura: Quito, Mejia, Pedro Moncayo, Cayambe",
                         font=("Verdana", 10), padx=12, pady=7)
    button557 = Button(toplevel557, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(557))

    datafreq557.pack()
    datafreq557a.pack()
    datafreq557b.pack()
    datafreq557c.pack()
    datafreq557d.pack()
    datafreq557e.pack()
    datafreq557f.pack()
    button557.pack()


def window16():
    toplevel79 = Toplevel()
    toplevel79.title("Frecuencia 79")
    toplevel79.focus_set()
    toplevel79.geometry('300x300')
    datafreq79 = Label(toplevel79, text="Datos de frecuencia 79",
                       fg="blue", font=("Arial", 14))
    datafreq79a = Label(toplevel79, text="Pichincha - TV abierta ",
                        font=("Verdana", 10), padx=12, pady=7)
    datafreq79b = Label(toplevel79, text="Tipo: Matriz - Repetidor, canal 5 ", font=("Verdana", 10), padx=12,
                        pady=7)
    datafreq79c = Label(toplevel79, text="Representante legal: Maria Hernandez", font=("Verdana", 10), padx=12,
                        pady=7)
    datafreq79d = Label(toplevel79, text="Nombre del canal: Televicentro - TVC ",
                        font=("Verdana", 10), padx=12, pady=7)
    datafreq79e = Label(toplevel79, text="Potencia efectiva radiada: 160430", font=("Verdana", 10),
                        padx=12, pady=7)
    datafreq79f = Label(toplevel79, text="Area de cobertura: Quito, Mejia, Pedro Moncayo, Cayambe",
                        font=("Verdana", 10), padx=12, pady=7)
    button79 = Button(toplevel79, text="Mapa Geografico",
                      pady=12, command=lambda: print_image(79))

    datafreq79.pack()
    datafreq79a.pack()
    datafreq79b.pack()
    datafreq79c.pack()
    datafreq79d.pack()
    datafreq79e.pack()
    datafreq79f.pack()
    button79.pack()


def window17():
    toplevel85 = Toplevel()
    toplevel85.title("Frecuencia 85")
    toplevel85.focus_set()
    toplevel85.geometry('300x300')
    datafreq85 = Label(toplevel85, text="Datos de frecuencia 85",
                       fg="blue", font=("Arial", 14))
    datafreq85a = Label(toplevel85, text="Pichincha - TV abierta ",
                        font=("Verdana", 10), padx=12, pady=7)
    datafreq85b = Label(toplevel85, text="Tipo: Repetidor, canal 7 ", font=("Verdana", 10), padx=12,
                        pady=7)
    datafreq85c = Label(toplevel85, text="Representante legal: Maria Hernandez", font=("Verdana", 10), padx=12,
                        pady=7)
    datafreq85d = Label(toplevel85, text="Nombre del canal: Televicentro - TVC ",
                        font=("Verdana", 10), padx=12, pady=7)
    datafreq85e = Label(toplevel85, text="Potencia efectiva radiada: 7062.7 ", font=("Verdana", 10),
                        padx=12, pady=7)
    datafreq85f = Label(toplevel85, text="Area de cobertura: Sur de Quito", font=("Verdana", 10),
                        padx=12, pady=7)
    button85 = Button(toplevel85, text="Mapa Geografico",
                      pady=12, command=lambda: print_image(85))

    datafreq85.pack()
    datafreq85a.pack()
    datafreq85b.pack()
    datafreq85c.pack()
    datafreq85d.pack()
    datafreq85e.pack()
    datafreq85f.pack()
    button85.pack()


def window18():
    toplevel527 = Toplevel()
    toplevel527.title("Frecuencia 527")
    toplevel527.focus_set()
    toplevel527.geometry('300x300')
    datafreq527 = Label(
        toplevel527, text="Datos de frecuencia 527", fg="blue", font=("Arial", 14))
    datafreq527a = Label(toplevel527, text="Pichincha - TV abierta ",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq527b = Label(toplevel527, text="Tipo: Matriz , canal 23  ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq527c = Label(toplevel527, text="Representante legal: Nelson Ortiz", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq527d = Label(toplevel527, text="Nombre del canal: Teleandina ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq527e = Label(toplevel527, text="Potencia efectiva radiada: 59570 ", font=("Verdana", 10),
                         padx=12, pady=7)
    datafreq527f = Label(toplevel527, text="Area de cobertura: Quito", font=("Verdana", 10),
                         padx=12, pady=7)
    button85 = Button(toplevel527, text="Mapa Geografico",
                      pady=12, command=lambda: print_image(527))

    datafreq527.pack()
    datafreq527a.pack()
    datafreq527b.pack()
    datafreq527c.pack()
    datafreq527d.pack()
    datafreq527e.pack()
    datafreq527f.pack()
    button85.pack()


def window19():
    toplevel587 = Toplevel()
    toplevel587.title("Frecuencia 587")
    toplevel587.focus_set()
    toplevel587.geometry('300x300')
    datafreq587 = Label(
        toplevel587, text="Datos de frecuencia 527", fg="blue", font=("Arial", 14))
    datafreq587a = Label(toplevel587, text="Pichincha - TV abierta",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq587b = Label(toplevel587, text="Tipo: Repetidor, canal 23 ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq587c = Label(toplevel587, text="Representante legal: Nelson Ortiz", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq587d = Label(toplevel587, text="Nombre del canal: Teleandina ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq587e = Label(toplevel587, text="Potencia efectiva radiada: 59570 ", font=("Verdana", 10),
                         padx=12, pady=7)
    datafreq587f = Label(toplevel587, text="Area de cobertura: Quito", font=("Verdana", 10),
                         padx=12, pady=7)
    button587 = Button(toplevel587, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(587))

    datafreq587.pack()
    datafreq587a.pack()
    datafreq587b.pack()
    datafreq587c.pack()
    datafreq587d.pack()
    datafreq587e.pack()
    datafreq587f.pack()
    button587.pack()


def window20():
    toplevel665 = Toplevel()
    toplevel665.title("Frecuencia 665")
    toplevel665.focus_set()
    toplevel665.geometry('300x300')
    datafreq665 = Label(
        toplevel665, text="Datos de frecuencia 665", fg="blue", font=("Arial", 14))
    datafreq665a = Label(toplevel665, text="Pichincha - TV abierta",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq665b = Label(toplevel665, text="Tipo: Matriz, canal 46 ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq665c = Label(toplevel665, text="Representante legal: Jose Penaherrera", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq665d = Label(toplevel665, text="Nombre del canal: RTU ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq665e = Label(toplevel665, text="Potencia efectiva radiada: 39720 ", font=("Verdana", 10),
                         padx=12, pady=7)
    datafreq665f = Label(toplevel665, text="Area de cobertura: Quito", font=("Verdana", 10),
                         padx=12, pady=7)
    button665 = Button(toplevel665, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(665))

    datafreq665.pack()
    datafreq665a.pack()
    datafreq665b.pack()
    datafreq665c.pack()
    datafreq665d.pack()
    datafreq665e.pack()
    datafreq665f.pack()
    button665.pack()


def window21():
    toplevel521 = Toplevel()
    toplevel521.title("Frecuencia 521")
    toplevel521.focus_set()
    toplevel521.geometry('300x300')
    datafreq521 = Label(
        toplevel521, text="Datos de frecuencia 521", fg="blue", font=("Arial", 14))
    datafreq521a = Label(toplevel521, text="Pichincha - TV abierta",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq521b = Label(toplevel521, text="Tipo: Repetidor, canal 22 ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq521c = Label(toplevel521, text="Representante legal: Jose Penaherrera", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq521d = Label(toplevel521, text="Nombre del canal: RTU ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq521e = Label(toplevel521, text="Potencia efectiva radiada: 121.21 ", font=("Verdana", 10),
                         padx=12, pady=7)
    datafreq521f = Label(toplevel521, text="Area de cobertura: Sur de Quito", font=("Verdana", 10),
                         padx=12, pady=7)
    button521 = Button(toplevel521, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(521))

    datafreq521.pack()
    datafreq521a.pack()
    datafreq521b.pack()
    datafreq521c.pack()
    datafreq521d.pack()
    datafreq521e.pack()
    datafreq521f.pack()
    button521.pack()


def window22():
    toplevel629 = Toplevel()
    toplevel629.title("Frecuencia 629")
    toplevel629.focus_set()
    toplevel629.geometry('300x300')
    datafreq629 = Label(
        toplevel629, text="Datos de frecuencia 629", fg="blue", font=("Arial", 14))
    datafreq629a = Label(toplevel629, text="Pichincha - TV abierta",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq629b = Label(toplevel629, text="Tipo: Repetidor, canal 40 ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq629c = Label(toplevel629, text="Representante legal: Mercedes Gomez", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq629d = Label(toplevel629, text="Nombre del canal: Canal UNO ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq629e = Label(toplevel629, text="Potencia efectiva radiada: 59570 ", font=("Verdana", 10),
                         padx=12, pady=7)
    datafreq629f = Label(toplevel629, text="Area de cobertura: Quito", font=("Verdana", 10),
                         padx=12, pady=7)
    button629 = Button(toplevel629, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(629))

    datafreq629.pack()
    datafreq629a.pack()
    datafreq629b.pack()
    datafreq629c.pack()
    datafreq629d.pack()
    datafreq629e.pack()
    datafreq629f.pack()
    button629.pack()


def window23():
    toplevel677 = Toplevel()
    toplevel677.title("Frecuencia 677")
    toplevel677.focus_set()
    toplevel677.geometry('300x300')
    datafreq677 = Label(
        toplevel677, text="Datos de frecuencia 677", fg="blue", font=("Arial", 14))
    datafreq677a = Label(toplevel677, text="Pichincha - TV abierta",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq677b = Label(toplevel677, text="Tipo: Matriz, canal 48 ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq677c = Label(toplevel677, text="Representante legal: Patricio Barriga", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq677d = Label(toplevel677, text="Nombre del canal: El ciudadano TV ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq677e = Label(toplevel677, text="Potencia efectiva radiada: 100004 ", font=("Verdana", 10),
                         padx=12, pady=7)
    datafreq677f = Label(toplevel677, text="Area de cobertura: Quito, Mejia, Pedro Moncayo, Ruminahui, Cayambe",
                         font=("Verdana", 10), padx=12, pady=7)
    button677 = Button(toplevel677, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(677))

    datafreq677.pack()
    datafreq677a.pack()
    datafreq677b.pack()
    datafreq677c.pack()
    datafreq677d.pack()
    datafreq677e.pack()
    datafreq677f.pack()
    button677.pack()


def window24():
    toplevel201 = Toplevel()
    toplevel201.title("Frecuencia 201")
    toplevel201.focus_set()
    toplevel201.geometry('300x300')
    datafreq201 = Label(
        toplevel201, text="Datos de frecuencia 629", fg="blue", font=("Arial", 14))
    datafreq201a = Label(toplevel201, text="Pichincha - TV abierta",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq201b = Label(toplevel201, text="Tipo: Matriz-Repetidor , canal 11 ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq201c = Label(toplevel201, text="Representante legal: Luis Gomez", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq201d = Label(toplevel201, text="Nombre del canal: RED Telesistema R.T.S ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq201e = Label(toplevel201, text="Potencia efectiva radiada: 141254, 734.8 ", font=("Verdana", 10),
                         padx=12, pady=7)
    datafreq201f = Label(toplevel201, text="Area de cobertura: Quito, Mejia, Pedro Moncayo, Ruminahui, Cayambe",
                         font=("Verdana", 10), padx=12, pady=7)
    button201 = Button(toplevel201, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(201))

    datafreq201.pack()
    datafreq201a.pack()
    datafreq201b.pack()
    datafreq201c.pack()
    datafreq201d.pack()
    datafreq201e.pack()
    datafreq201f.pack()
    button201.pack()


def window25():
    toplevel653 = Toplevel()
    toplevel653.title("Frecuencia 653")
    toplevel653.focus_set()
    toplevel653.geometry('300x300')
    datafreq653 = Label(
        toplevel653, text="Datos de frecuencia 653", fg="blue", font=("Arial", 14))
    datafreq653a = Label(toplevel653, text="Pichincha - TV abierta",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq653b = Label(toplevel653, text="Tipo: Repetidor , canal 44 ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq653c = Label(toplevel653, text="Representante legal: Alex Moreno", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq653d = Label(toplevel653, text="Nombre del canal: Canela TV ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq653e = Label(toplevel653, text="Potencia efectiva radiada: 79430 ", font=("Verdana", 10),
                         padx=12, pady=7)
    datafreq653f = Label(toplevel653, text="Area de cobertura: Quito", font=(
        "Verdana", 10), padx=12, pady=7)
    button653 = Button(toplevel653, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(653))

    datafreq653.pack()
    datafreq653a.pack()
    datafreq653b.pack()
    datafreq653c.pack()
    datafreq653d.pack()
    datafreq653e.pack()
    datafreq653f.pack()
    button653.pack()


def window26():
    toplevel575 = Toplevel()
    toplevel575.title("Frecuencia 575")
    toplevel575.focus_set()
    toplevel575.geometry('300x300')
    datafreq575 = Label(
        toplevel575, text="Datos de frecuencia 575", fg="blue", font=("Arial", 14))
    datafreq575a = Label(toplevel575, text="Pichincha - TV abierta",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq575b = Label(toplevel575, text="Tipo: Repetidor , canal 31 ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq575c = Label(toplevel575, text="Representante legal: Roberto Dager", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq575d = Label(toplevel575, text="Nombre del canal: Telerama ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq575e = Label(toplevel575, text="Potencia efectiva radiada: 79430 ", font=("Verdana", 10),
                         padx=12, pady=7)
    datafreq575f = Label(toplevel575, text="Area de cobertura: Quito", font=(
        "Verdana", 10), padx=12, pady=7)
    button575 = Button(toplevel575, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(575))

    datafreq575.pack()
    datafreq575a.pack()
    datafreq575b.pack()
    datafreq575c.pack()
    datafreq575d.pack()
    datafreq575e.pack()
    datafreq575f.pack()
    button575.pack()


def window27():
    toplevel539 = Toplevel()
    toplevel539.title("Frecuencia 539")
    toplevel539.focus_set()
    toplevel539.geometry('300x300')
    datafreq539 = Label(
        toplevel539, text="Datos de frecuencia 539", fg="blue", font=("Arial", 14))
    datafreq539a = Label(toplevel539, text="Pichincha - TV abierta",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq539b = Label(toplevel539, text="Tipo: Matriz , canal 25 ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq539c = Label(toplevel539, text="Representante legal: Luis Calle", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq539d = Label(toplevel539, text="Nombre del canal: Television Satelital ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq539e = Label(toplevel539, text="Potencia efectiva radiada: 39720 ", font=("Verdana", 10),
                         padx=12, pady=7)
    datafreq539f = Label(toplevel539, text="Area de cobertura: Quito", font=(
        "Verdana", 10), padx=12, pady=7)
    button539 = Button(toplevel539, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(539))

    datafreq539.pack()
    datafreq539a.pack()
    datafreq539b.pack()
    datafreq539c.pack()
    datafreq539d.pack()
    datafreq539e.pack()
    datafreq539f.pack()
    button539.pack()


def window28():
    toplevel533 = Toplevel()
    toplevel533.title("Frecuencia 533")
    toplevel533.focus_set()
    toplevel533.geometry('300x300')
    datafreq533 = Label(
        toplevel533, text="Datos de frecuencia 183", fg="blue", font=("Arial", 14))
    datafreq533a = Label(toplevel533, text="Pichincha - TV abierta",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq533b = Label(toplevel533, text="Tipo: Repetidor , canal 24 ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq533c = Label(toplevel533, text="Representante legal: Luis Calle", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq533d = Label(toplevel533, text="Nombre del canal: Television Satelital ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq533e = Label(toplevel533, text="Potencia efectiva radiada: 100 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq533f = Label(toplevel533, text="Area de cobertura: Sur de Quito", font=(
        "Verdana", 10), padx=12, pady=7)
    button533 = Button(toplevel533, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(533))

    datafreq533.pack()
    datafreq533a.pack()
    datafreq533b.pack()
    datafreq533c.pack()
    datafreq533d.pack()
    datafreq533e.pack()
    datafreq533f.pack()
    button533.pack()


def window29():
    toplevel183 = Toplevel()
    toplevel183.title("Frecuencia 183")
    toplevel183.focus_set()
    toplevel183.geometry('300x300')
    datafreq183 = Label(
        toplevel183, text="Datos de frecuencia 183", fg="blue", font=("Arial", 14))
    datafreq183a = Label(toplevel183, text="Pichincha - TV abierta",
                         font=("Verdana", 10), padx=12, pady=7)
    datafreq183b = Label(toplevel183, text="Tipo: Matriz , canal 8 ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq183c = Label(toplevel183, text="Representante legal: Juan Jaramillo", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq183d = Label(toplevel183, text="Nombre del canal: Televisora Nacional ", font=("Verdana", 10), padx=12,
                         pady=7)
    datafreq183e = Label(toplevel183, text="Potencia efectiva radiada: 89130 ", font=(
        "Verdana", 10), padx=12, pady=7)
    datafreq183f = Label(toplevel183, text="Area de cobertura: Quito, Mejia, Pedro Moncayo, Ruminahui, Cayambe",
                         font=("Verdana", 10), padx=12, pady=7)
    button183 = Button(toplevel183, text="Mapa Geografico",
                       pady=12, command=lambda: print_image(183))

    datafreq183.pack()
    datafreq183a.pack()
    datafreq183b.pack()
    datafreq183c.pack()
    datafreq183d.pack()
    datafreq183e.pack()
    datafreq183f.pack()
    button183.pack()


# LABELS
title_label = Label(myFrame, text="Datos de Frecuencias")
title_label.config(font=("Arial", 18))
title_label.grid(row=0, column=1, padx=12, pady=12)
frequency_label = Label(myFrame, text="Frecuencias Disponibles:")
frequency_label.grid(row=1, column=0, padx=12, pady=12)
labelextra = Label(myFrame, text="Powered by Andy", fg="red")
labelextra.grid(row=0, column=2, padx=10, pady=10)
label_freqname = Label(
    myFrame, text="599, 617, 639, 549 , 623, 189, 195, 207, 213, 69, 57, 63")
label_freqname.grid(row=1, column=1, padx=12, pady=12)
label_freqname1 = Label(
    myFrame, text="175, 557, 587, 665, 521, 629, 677, 201, 653, 575, 539, 533, 183")
label_freqname1.grid(row=2, column=1, padx=12, pady=12)
frequency_data1_label = Label(myFrame, text="Ingrese su frecuencia:")
frequency_data1_label.grid(row=3, column=0, padx=12, pady=12)
available_label = Label(myFrame, text="Disponibilidad (no llenar):")
available_label.grid(row=4, column=0, padx=12, pady=12)

# TEXT BOXES
box_freq = Entry(myFrame)
box_freq.grid(row=3, column=1, padx=12, pady=12)
box_available = Entry(myFrame, textvariable=data)
box_available.grid(row=4, column=1, padx=12, pady=12)

# Buttons
mybutton1 = Button(root, text="Disponibilidad", command=code_validation)
mybutton2 = Button(root, text="Ver informacion", command=new_windows)
mybutton1.pack()
mybutton2.pack()

# IMPORTANT LOOP
root.mainloop()
