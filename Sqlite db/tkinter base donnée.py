from tkinter import *
import sqlite3
from PIL import ImageTk, Image

root = Tk()
root.title("tkinter et sqlite3")
root.geometry("400x400")
connect = sqlite3.connect("tkinter.db")
cursor = connect.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS adresses(
    first_name TEXT,
    last_name TEXT,
    adresse TEXT,
    city TEXT,
    state TEXT,
    zipcoder INTEGER)""")
def submit():
    #avec base de données
    # mettre petit points ou securisé avec (?,?)",(variables))
    connect = sqlite3.connect("tkinter.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO adresses VALUES (:f_name, :l_name, :adresse, :city, :state, :zipcode)", #important pas fermer paranthèse
                   {#permet de préciser la valeur en input en fonction de la table dans database adresses
                       'f_name': f_name.get(),
                       'l_name': l_name.get(),
                       'adresse': adresse.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zipcode': zipcode.get(),
                   })


    connect.commit()
    connect.close()
    #supprimer les données sur la fenetre
    f_name.delete(0, END)
    l_name.delete(0, END)
    adresse.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#afficher données dans la fentre tkinter
def query():
    connect = sqlite3.connect("tkinter.db")
    cursor = connect.cursor()
    cursor.execute("SELECT *, oid FROM adresses")# oid permet de supprimer plus fzcilement les donnees de la table
    enregistrement = cursor.fetchall()
    #print(enregistrement)
    print_enregiestrement = ''
    for enregistrements in enregistrement:
        print_enregiestrement += str(enregistrements[0]) + " " +str(enregistrements[1]) + " " + str(enregistrements[2]) + " " + str(enregistrements[3]) + " " + str(enregistrements[4]) + " " +str(enregistrements[5]) + "\n" #sauter ligne
        query_label = Label(root, text=print_enregiestrement)
        query_label.grid(row=8, column=0, columnspan=2)


def nouvelle_fenetre():
    pass
    connect.commit()
    connect.close()

#creation variables sur tk
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)#soit grid(), pack(padx, pady) place(x, y) padx pady, row, column, .place(x,y), sticky, .pack(fill=x, side=WN...)  place extention grid.columnspan, ipadx, ipady
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
adresse = Entry(root, width=30)
adresse.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

#creation label pour chaque valeur data
f_name_label = Label(root, text="first name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="last name")
l_name_label.grid(row=1, column=0)
adresse_label = Label(root, text="your adressse")
adresse_label.grid(row=2, column=0)
city_label = Label(root, text="your city")
city_label.grid(row=3, column=0)
state_label = Label(root, text="your state")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=5, column=0)

#creation bouton et command
boutton = Button(root, text="ajoute une valeur a la data base", command=submit)
boutton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)#permet au bouton de s'étandre du deux colonnes
btn = Button(root, text="montrer les enregistrement", font=("Helvetica", 10), fg="black", relief=RAISED, command=query)#pas image
btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

#creation nmenu
menu = Menu(root)
menu_fill = Menu(menu, tearoff= 0)
menu_fill.add_command(label="nouveau", command=nouvelle_fenetre)
menu.add_cascade(label="Le Menu", menu=menu_fill)
root.config(menu=menu)
connect.commit()
connect.close()
root.update()
root.mainloop()
