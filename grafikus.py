import tkinter as tk

def on_dobas():
    pass

root = tk.Tk()
root.title("Kocskadobás statisztika")
root.geometry("600x400")

cim_cim = tk.Label(root, text="Kockadobások", font=("Ariel", 16))
cim_cim.grid(row=0, column=1, pady=20)

dobasok_szama_bemenet = tk.StringVar(value="10")
dobasszam = tk.Entry(root, textvariable = dobasok_szama_bemenet, width=10)
dobasszam.grid(row=1, column=0, pady=20, padx=50)

eredmeny_cimke_szoveg = tk.StringVar(value="...\n...\n...")
eredmeny_cimke = tk.Label(root, textvariable=eredmeny_cimke_szoveg, font=("Ariel", 16))
eredmeny_cimke.grid(row=2, column=1, pady=26)

gomb = tk.Button(root, text="Dobás", command = on_dobas)
gomb.grid(row=1, column=2)

kilepes = tk.Button(root, text="Kilépés", command = root.destroy, bg="red")
kilepes.grid(row=1, column=3, padx=50)

tk.mainloop()