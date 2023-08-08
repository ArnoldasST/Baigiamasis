from sqlalchemy.orm import sessionmaker
from baze import engine, Elektronika
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

Session = sessionmaker(bind=engine)
session = Session()

langas = Tk()


def atidaryti_prideti_langa():
    prideti_langas = Toplevel(langas)
    prideti_langas.title("Pridėti įrašą")

    def prideti():
        try:
            pavadinimas = input_pavadinimas.get()
            kiekis = int(input_kiekis.get())
            kaina = float(input_kaina.get())
        except ValueError:
            status["text"] = "Neįvesti visi reikiami duomenys!"
            return

        SQLAlchemy = Elektronika(pavadinimas, kiekis, kaina)
        session.add(SQLAlchemy)
        session.commit()
        status["text"] = "Įrašas pridėtas!"

    prideti_pavadinima = Label(prideti_langas, text="Dalykas :")
    prideti_pavadinima.grid(row=1, column=0)
    input_pavadinimas = Entry(prideti_langas)
    input_pavadinimas.grid(row=1, column=1)

    prideti_langas.columnconfigure(2, minsize=20)

    prideti_kieki = Label(prideti_langas, text="Kiekis :")
    prideti_kieki.grid(row=1, column=3)
    input_kiekis = Entry(prideti_langas)
    input_kiekis.grid(row=1, column=4)

    prideti_langas.columnconfigure(5, minsize=20)

    prideti_kaina = Label(prideti_langas, text="Vieneto kaina :")
    prideti_kaina.grid(row=1, column=6)
    input_kaina = Entry(prideti_langas)
    input_kaina.grid(row=1, column=7)

    prideti_mygtukas = Button(prideti_langas, text="Pridėti", command=prideti)
    prideti_langas.bind("<Return>", lambda event: prideti())
    prideti_mygtukas.grid(row=2, column=1, columnspan=7)

    status = Label(prideti_langas, text="", bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=3, columnspan=8, sticky=W + E)


def perziureti():
    perziureti_langas = Toplevel(langas)
    perziureti_langas.title("Peržiūrėti įrašus")
    lentele = ttk.Treeview(perziureti_langas, columns=("ID", "Pavadinimas", "Kiekis", "Kaina"), show="headings")

    lentele.heading("ID", text="ID")
    lentele.heading("Pavadinimas", text="Dalykas")
    lentele.heading("Kiekis", text="Kiekis")
    lentele.heading("Kaina", text="Vieneto kaina")

    lentele.column("ID", width=20)
    lentele.column("Pavadinimas", width=200)
    lentele.column("Kiekis", width=50)
    lentele.column("Kaina", width=100)
    lentele.grid(row=0, column=0)

    sarasas = session.query(Elektronika).all()
    for irasas in sarasas:
        lentele.insert("", "end", values=(irasas.id, irasas.pavadinimas, irasas.kiekis, irasas.kaina))

    status = Label(perziureti_langas, text="", bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=1, column=0, sticky=W + E)


def atidaryti_istrinimo_langa():
    istrinimo_langas = Toplevel(langas)
    istrinimo_langas.title("Trinti įrašą")
    lentele = ttk.Treeview(istrinimo_langas, columns=("ID", "Pavadinimas", "Kiekis", "Kaina"), show="headings")

    lentele.heading("ID", text="ID")
    lentele.heading("Pavadinimas", text="Dalykas")
    lentele.heading("Kiekis", text="Kiekis")
    lentele.heading("Kaina", text="Vieneto kaina")

    lentele.column("ID", width=20)
    lentele.column("Pavadinimas", width=200)
    lentele.column("Kiekis", width=50)
    lentele.column("Kaina", width=100)
    lentele.grid(row=0, column=0)

    sarasas = session.query(Elektronika).all()
    for irasas in sarasas:
        lentele.insert("", "end", values=(irasas.id, irasas.pavadinimas, irasas.kiekis, irasas.kaina))

    def istrinti():
        try:
            trinti = int(input_trinti.get())
        except ValueError:
            status["text"] = "Įveskite įrašo ID!"
            return

        trinamas_irasas = session.query(Elektronika).get(trinti)
        if trinamas_irasas:
            session.delete(trinamas_irasas)
            session.commit()
            status["text"] = "Įrašas ištrintas!"
        else:
            status["text"] = "Irašas su nurodytu ID nerastas!"
        # istrinimo_langas.destroy()

    Label(istrinimo_langas, text="Įveskite trinamo įrašo ID:").grid(row=1, column=0)
    input_trinti = Entry(istrinimo_langas)
    input_trinti.grid(row=2, column=0)
    Button(istrinimo_langas, text="Ištrinti", command=istrinti).grid(row=3, column=0)
    istrinimo_langas.bind("<Return>", lambda event: istrinti())

    status = Label(istrinimo_langas, text="", bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=4, sticky=W + E)


def atidaryti_pakeisti_langa():
    pakeitimo_langas = Toplevel(langas)
    pakeitimo_langas.title("Pakeisti įrašą")
    lentele = ttk.Treeview(pakeitimo_langas, columns=("ID", "Pavadinimas", "Kiekis", "Kaina"), show="headings")

    lentele.heading("ID", text="ID")
    lentele.heading("Pavadinimas", text="Dalykas")
    lentele.heading("Kiekis", text="Kiekis")
    lentele.heading("Kaina", text="Vieneto kaina")

    lentele.column("ID", width=20)
    lentele.column("Pavadinimas", width=200)
    lentele.column("Kiekis", width=50)
    lentele.column("Kaina", width=100)
    lentele.grid(row=0, column=0)

    sarasas = session.query(Elektronika).all()
    for irasas in sarasas:
        lentele.insert("", "end", values=(irasas.id, irasas.pavadinimas, irasas.kiekis, irasas.kaina))

    Label(pakeitimo_langas, text="Įveskite įrašo ID, kurį norite pakeisti:").grid(row=1, column=0)
    input_pakeisti = Entry(pakeitimo_langas)
    input_pakeisti.grid(row=2, column=0)

    Label(pakeitimo_langas, text="Naujas pavadinimas:").grid(row=3, column=0)
    input_naujas_pavadinimas = Entry(pakeitimo_langas)
    input_naujas_pavadinimas.grid(row=4, column=0)

    Label(pakeitimo_langas, text="Nauja kaina:").grid(row=7, column=0)
    input_nauja_kaina = Entry(pakeitimo_langas)
    input_nauja_kaina.grid(row=8, column=0)

    def pakeisti():
        keisti = input_pakeisti.get()
        keiciamas_irasas = session.query(Elektronika).get(keisti)

        if keiciamas_irasas:
            naujas_pavadinimas = input_naujas_pavadinimas.get()
            nauja_kaina = input_nauja_kaina.get()

            if not naujas_pavadinimas and not nauja_kaina:
                status["text"] = "Įveskite bent vieną naują reikšmę!"
                return

            if naujas_pavadinimas:
                keiciamas_irasas.pavadinimas = naujas_pavadinimas
            if nauja_kaina:
                keiciamas_irasas.kaina = nauja_kaina

            session.commit()
            status["text"] = "Įrašas pakeistas!"
        else:
            status["text"] = "Irašas su nurodytu ID nerastas!"

        # pakeitimo_langas.destroy()

    Button(pakeitimo_langas, text="Pakeisti", command=pakeisti).grid(row=9, column=0)
    pakeitimo_langas.bind("<Return>", lambda event: pakeisti())

    status = Label(pakeitimo_langas, text="", bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=10, sticky=W + E)


def atidaryti_papildyti_langa():
    papildymo_langas = Toplevel(langas)
    papildymo_langas.title("Papildyti inventorių")
    lentele = ttk.Treeview(papildymo_langas, columns=("ID", "Pavadinimas", "Kiekis", "Kaina"), show="headings")

    lentele.heading("ID", text="ID")
    lentele.heading("Pavadinimas", text="Dalykas")
    lentele.heading("Kiekis", text="Kiekis")
    lentele.heading("Kaina", text="Vieneto kaina")

    lentele.column("ID", width=20)
    lentele.column("Pavadinimas", width=200)
    lentele.column("Kiekis", width=50)
    lentele.column("Kaina", width=100)
    lentele.grid(row=0, column=0)

    sarasas = session.query(Elektronika).all()
    for irasas in sarasas:
        lentele.insert("", "end", values=(irasas.id, irasas.pavadinimas, irasas.kiekis, irasas.kaina))

    Label(papildymo_langas, text="Įveskite įrašo ID, kurį norite papildyti:").grid(row=1, column=0)
    input_papildyti = Entry(papildymo_langas)
    input_papildyti.grid(row=2, column=0)

    Label(papildymo_langas, text="Kiek vienetų norite pridėti:").grid(row=3, column=0)
    input_pildomas_kiekis = Entry(papildymo_langas)
    input_pildomas_kiekis.grid(row=4, column=0)

    def papildyti():
        try:
            pildyti = int(input_papildyti.get())
            pildomas_kiekis = int(input_pildomas_kiekis.get())
        except ValueError:
            status["text"] = "Neteisingai įvesti duomenys!"
            return

        pildomas_irasas = session.query(Elektronika).get(pildyti)

        if pildomas_irasas:
            pildomas_irasas.kiekis += int(pildomas_kiekis)
            session.commit()
            status["text"] = "Įrašas papildytas!"
        else:
            status["text"] = "Įrašas nerastas!"

    Button(papildymo_langas, text="Papildyti", command=papildyti).grid(row=5, column=0)
    papildymo_langas.bind("<Return>", lambda event: papildyti())

    status = Label(papildymo_langas, text="", bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=6, sticky=W + E)


def atidaryti_mazinti_langa():
    pamazinimo_langas = Toplevel(langas)
    pamazinimo_langas.title("Mažinti inventorių")
    lentele = ttk.Treeview(pamazinimo_langas, columns=("ID", "Pavadinimas", "Kiekis", "Kaina"), show="headings")

    lentele.heading("ID", text="ID")
    lentele.heading("Pavadinimas", text="Dalykas")
    lentele.heading("Kiekis", text="Kiekis")
    lentele.heading("Kaina", text="Vieneto kaina")

    lentele.column("ID", width=20)
    lentele.column("Pavadinimas", width=200)
    lentele.column("Kiekis", width=50)
    lentele.column("Kaina", width=100)
    lentele.grid(row=0, column=0)

    sarasas = session.query(Elektronika).all()
    for irasas in sarasas:
        lentele.insert("", "end", values=(irasas.id, irasas.pavadinimas, irasas.kiekis, irasas.kaina))

    Label(pamazinimo_langas, text="Įveskite įrašo ID, kurį norite pamažinti:").grid(row=1, column=0)
    input_pamazinti = Entry(pamazinimo_langas)
    input_pamazinti.grid(row=2, column=0)

    Label(pamazinimo_langas, text="Kiek vienetų norite išimti:").grid(row=3, column=0)
    input_mazinamas_kiekis = Entry(pamazinimo_langas)
    input_mazinamas_kiekis.grid(row=4, column=0)

    def pamazinti():
        try:
            mazinti = int(input_pamazinti.get())
            mazinamas_kiekis = int(input_mazinamas_kiekis.get())
        except ValueError:
            status["text"] = "Neteisingai įvesti duomenys!"
            return

        mazinamas_irasas = session.query(Elektronika).get(mazinti)

        if mazinamas_irasas:
            if mazinamas_irasas.kiekis >= int(mazinamas_kiekis):
                mazinamas_irasas.kiekis -= int(mazinamas_kiekis)
                if mazinamas_irasas.kiekis == 0:
                    session.delete(mazinamas_irasas)
                session.commit()
                status["text"] = "Įrašas pamažintas!"
            else:
                status["text"] = "Nėra tiek vienetų!"
        else:
            status["text"] = "Įrašas nerastas!"

    Button(pamazinimo_langas, text="Pamažinti", command=pamazinti).grid(row=5, column=0)
    pamazinimo_langas.bind("<Return>", lambda event: pamazinti())

    status = Label(pamazinimo_langas, text="", bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=6, sticky=W + E)


def iseiti():
    langas.destroy()


langas.title("Projektas")
langas.iconbitmap(r'inventory_icon.ico')

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)
meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Pridėti naują įrašą", command=atidaryti_prideti_langa)
submeniu.add_command(label="Peržiūrėti inventorių", command=perziureti)
submeniu.add_separator()
submeniu.add_command(label="Pakeisti įrašo informaciją", command=atidaryti_pakeisti_langa)
submeniu.add_command(label="Papildyti esamą inventorių", command=atidaryti_papildyti_langa)
submeniu.add_command(label="Pamažinti esamą inventorių", command=atidaryti_mazinti_langa)
submeniu.add_separator()
submeniu.add_command(label="Ištrinti įrašą", command=atidaryti_istrinimo_langa)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)

elektronika = Label(langas, text="INVENTORIUS")
elektronika.pack()

paveikslelis = Image.open("inv.jpg")
naujas_dydis = (600, 400)
sumazintas_paveikslelis = paveikslelis.resize(naujas_dydis)
img = ImageTk.PhotoImage(sumazintas_paveikslelis)
panel = Label(langas, image=img)
panel.pack(side="bottom", fill="both")

rezultatu_laukas = Label(langas, text="Norėdami pradėti, spauskite 'Meniu'")
rezultatu_laukas.pack()

langas.mainloop()
