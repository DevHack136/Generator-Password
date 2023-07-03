from random import choice, randint
import string
from tkinter import *

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def exit():
    quit()
    
# Création de la fenêtre
window = Tk()
window.title("Générateur de Mot de Passe")
window.geometry("920x480")
window.config(background='black')

# Création de la frame principale
frame = Frame(window, bg='#000000', bd=1, relief=SUNKEN, pady=50, padx=50)

# Création d'image
width = 300
height = 300
image = PhotoImage(file="Projets/Generator Password/eagle.png").zoom(35).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='black')
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# Création d'une sous boite
right_frame = Frame(frame, bg='black', bd=1, relief=SUNKEN, pady=50, padx=50)

# Création d'un titre
label_title = Label(right_frame, text="Mot de Passe", font=("", 20), bg='black', fg='white')
label_title.pack()

# Création d'un champs/input
password_entry = Entry(right_frame, font=("", 20), bg='black', fg='white')
password_entry.pack(pady=10)

# Création d'un bouton
generate_password_button = Button(right_frame, text="Générer un Mot de Passe", font=("", 20), bg='black', fg='blue', command=generate_password)
generate_password_button.pack(pady=10, fill=X)

# On place la sous boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W,)

# Affichage de la frame
frame.pack(expand=YES)

# Création d'une barre de navigation
menu_bar = Menu(window)

# Création d'un premier menu
file_menu = Menu(menu_bar)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=exit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# Configuration de la fenêtre
window.config(menu=menu_bar)

# Affichage de la fenêtre
window.mainloop()