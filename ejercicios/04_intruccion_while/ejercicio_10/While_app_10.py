import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acu_negativo = 0
        acu_positivo = 0
        contador_positivo = 0
        contador_negativo = 0

        ceros = 0

        while True:
            numero = prompt(" ","Ingrese un numero")
            if numero == None:
                break
            numero=int(numero)
            if numero > 0:
                contador_positivo += 1
                acu_positivo += numero
            elif numero < 0:
                contador_negativo += 1
                acu_negativo += numero
            else: ceros += 1
        diferencia_positivo_negativo = (acu_positivo - (acu_negativo))
        alert("Resumen","Se ingresaron {0} numero/s positivos, {1} numero/s negativos y {2} vez/ces 0. La suma de los positivos es {3} y la suma de los negativos es {4}. La diferencia de ambos es {5} ".format(contador_positivo,contador_negativo,ceros,acu_positivo,acu_negativo,diferencia_positivo_negativo))



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
