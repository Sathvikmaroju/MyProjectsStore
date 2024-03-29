import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk 
import urllib3
from io import BytesIO

window = tk.Tk()
window.geometry('600x500')
window.title("Pokedex")
window.config(padx=10,pady=10)

title_label = tk.Label(window,text="Pokedex")
title_label.config(font=('Arial',32))
title_label.pack(padx=10,pady=10)

pokemon_img = tk.Label(window)
pokemon_img.config(font=('Arial',20))
pokemon_img.pack(padx=10,pady=10)

pokemon_info = tk.Label(window)
pokemon_info.config(font=('Arial',20))
pokemon_info.pack(padx=10,pady=10)

pokemon_type = tk.Label(window)
pokemon_type.config(font=('Arial',20))
pokemon_type.pack(padx=10,pady=10)

def load_pokemon():
    pokemon=pypokedex.get(name=text_id_name.get(1.0,"end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get("default"))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_img.config(image=img)
    pokemon_img.image = img

    pokemon_info.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_type.config(text=" - ".join([t for t in pokemon.types]).title())

label_id_name = tk.Label(window,text='ID OR Name')
label_id_name.config(font=('Arial',20))
label_id_name.pack(padx=10,pady=10)

text_id_name = tk.Text(window,height=1)
text_id_name.config(font=('Arial',20))
text_id_name.pack(padx=10,pady=10)

btn_load = tk.Button(window,text='Load Pokememon',command=load_pokemon)
btn_load.config(font=('Arial',20))
btn_load.pack(padx=10,pady=10)

window.mainloop()