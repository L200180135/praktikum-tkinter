### kg 1

from Tkinter import Tk, Label, Entry, Button
from tkMessageBox import showinfo

my_app = Tk()
L1 = Label(my_app, text="Data diri", font=("Arial" , 24))
L1.grid(row=0, column=0, sticky="w")
L2 = Label(my_app, text="Nama")
L2.grid(row=1, column=0, sticky="w")
L3 = Label(my_app, text="Anisa Ghoyatul F")
L3.grid(row=1, column=1, sticky="w")
L4 = Label(my_app, text="NIM")
L4.grid(row=2, column=0, sticky="w")
L5 = Label(my_app, text="L200180135")
L5.grid (row=2, column=1, sticky="w")
L6 = Label(my_app, text="Buku Faforit")
L6.grid(row=3, column=0, sticky="w")
L7 = Label(my_app, text="Negeri 5 Menara")
L7.grid(row=3, column=1, sticky="w")
L8 = Label(my_app, text="Idola kalangan Sahabat")
L8.grid(row=4, column=0, sticky="w")
L9 = Label(my_app, text="Abu Bakar as-Sidiq")
L9.grid(row=4, column=1, sticky="w")
L10 = Label(my_app, text="Motto")
L10.grid(row=5, column=0, sticky="w")
L11 = Label(my_app, text="Semangat")
L11.grid(row=5, column=1, sticky="w")

def tampilpesan() :
    showinfo ("quit" , my_app.destroy())

B=Button (my_app, text="quit", command=tampilpesan)
B.grid (row=6, column=1)
my_app.mainloop()

## kg 2
from Tkinter import Tk, Label, Entry, Button, DoubleVar
from tkMessageBox import showinfo

kalkulator = Tk (className="Kalkulator")
L1 = Label (kalkulator, text="Angka 1")
L1.grid (row=0, column=0)
int1 = DoubleVar(value=0)
E1 = Entry (kalkulator, textvariable=int1)
E1.grid (row=0, column=3)
L2 = Label (kalkulator, text="Angka 2")
L2.grid (row=1, column=0)
int2 = DoubleVar(value=0)
E2 = Entry (kalkulator, textvariable=int2)
E2.grid (row=1, column=3)
L3 = Label (kalkulator, text="Hasil" )
L3.grid (row=3, column=0)
L4 = Label (kalkulator)
L4.grid (row=3, column=1)

def tambah() :
    penjumlahan = int1.get() + int2.get()
    L4.config(text=penjumlahan)
def kurang() :
    pengurangan = int1.get() - int2.get()
    L4.config(text=pengurangan)
def kali():
    perkalian = int1.get() * int2.get()
    L4.config(text=perkalian)
def bagi():
    pembagian = int1.get() / int2.get()
    L4.config(text=pembagian)


B1 = Button(kalkulator, text="+", command=tambah)
B1.grid (row=2, column=0)
B2 = Button(kalkulator, text="-", command=kurang)
B2.grid (row=2, column=1,)
B3 = Button(kalkulator, text="x", command=kali)
B3.grid (row=2, column=3)
B3 = Button(kalkulator, text=":", command=bagi)
B3.grid (row=2, column=4)
kalkulator.mainloop()

####kg 3
from Tkinter import Tk, Label, Entry, Button, Canvas, StringVar

rumus = Tk(className="Hitung luas")
L1 = Label (rumus, text="Bangun Geometri", font=("Arial", 26))
L1.grid (row=0, column=0)
L2 = Label (rumus, text="Bangun Ruang Limas Segi Empat")
L2.grid (row=1, column=0)
L3 = Label (rumus, text="Sisi")
L3.grid (row=2, column=2)
str1 = StringVar (value=0) 
E1 = Entry (rumus, textvariable=str1)
E1.grid (row=2, column=1)
L4 = Label (rumus, text="Alas")
L4.grid (row=3, column=2)
str2 = StringVar (value=0) 
E2 = Entry (rumus, textvariable=str2)
E2.grid (row=3, column=1)
L4 = Label (rumus, text="Tinggi")
L4.grid (row=4, column=2)
str3 = StringVar (value=0) 
E3 = Entry (rumus, textvariable=str3)
E3.grid (row=4, column=1)
L5 = Label (rumus, text="Hasil")
L5.grid (row=5, column=1)

def limas() :
    s = float(str1.get())
    a = float(str2.get())
    t = float(str3.get())
    lslimas = s*s+4*0.5*a*t
    L5.config (text=lslimas)

B = Button (rumus, text="Hitung Luas", command=limas)
B.grid (row=5, column=0)
rumus.mainloop()

