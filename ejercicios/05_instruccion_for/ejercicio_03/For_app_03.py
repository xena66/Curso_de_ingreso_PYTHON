import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''yanina osorio
Enunciado:
Al presionar el botón Mostrar tomar del campo de texto cantidad de veces que se desea
repetir el mensaje "Hola UTN FRA" (utilizando el Dialog Alert)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_repetir = customtkinter.CTkEntry(master=self)
        self.txt_repetir.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
       
        repetir=self.txt_repetir.get()
        repetir_int=int(repetir)
        for i in range(0,repetir_int,1):
            alert(" ","Hola UTN FRA")


        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()