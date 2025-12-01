import tkinter as tk
from tkinter import messagebox
import random


class KockaDobas:
    def __init__ (self, master):
        self.master = master
        self.master.title("Kocskadobás statisztika")
        self.master.geometry("600x408")
        self.cim_cimke = tk.Label(self.master, text="Kockadobások", font=("Ariel", 16))
        self.cim_cimke.grid(row=0, column=1, pady=20)
        self.dobasok_szama_bemenet = tk.StringVar(value="10")
        self.dobasszam= tk. Entry(self.master, textvariable=self.dobasok_szama_bemenet, width=10)
        self.dobasszam.grid(row=1, column=0, pady=20, padx=50)
        self.eredmeny_cimke_szoveg = tk.StringVar(value="...\n...\n...")
        self.eredmeny_cimke = tk.Label(self.master, textvariable=self.eredmeny_cimke_szoveg, font=("Ariel", 16))
        self.eredmeny_cimke.grid(row=2, column=1, pady=20)
        self.gomb = tk.Button(self.master, text="Dobás", command=self.on_dobas)
        self.gomb.grid(row=1, column=2)
        self.kilepes = tk.Button(self.master, text="Kilépés", command=self.master.destroy, bg="red")
        self.kilepes.grid(row=1, column=3, padx=50)
        
    def dobas (self, dobasok):
        eredmenyek=[0 for _ in range(7)]
        for _ in range(dobasok):
            szam=random.randint(1,6)
            eredmenyek[szam] +=1
            self.eredmeny_cimke_szoveg.set(
            f"1-- {eredmenyek [1]}\n" 
            f"2-- {eredmenyek[2]}\n"
            f"3-- {eredmenyek [3]}\n"
            f"4-- {eredmenyek [4]}\n"
            f"5 -- {eredmenyek [5]}\n"
            f"6 -- {eredmenyek [6]}"
            )
    def on_dobas(self):
        try:
            self.dobasok_szama=int (self.dobasok_szama_bemenet.get())
            self.dobas (self.dobasok_szama)

        except:
            messagebox.showerror(title="Hiba", message= "Rossz értéket adott meg a dobásszámra!")


if __name__ == "__main__":
    root = tk.Tk()
    app = KockaDobas(root)
    tk.mainloop()