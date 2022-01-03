from tkinter import *


root = Tk()
root.title("Calculadora")

#Pantalla

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

#Función para obtener números

i = 0 #Índice en pantalla

def obtener_numeros(n):
    global i
    display.insert(i, n)
    i+=1

def obtener_operador(operador):
    global i
    long_operador = len(operador)
    display.insert(i, operador)
    i += long_operador

def limpiar_pantalla():
    display.delete(0, END)

def retroceso():
    display_state = display.get()
    if len(display_state):
        display_newstate = display_state[:-1]
        limpiar_pantalla()
        display.insert(0, display_newstate)
    else:
        limpiar_pantalla()
        display.insert(0,"ERROR")

def calculo():
    display_state = display.get()
    try:
        expr_math = compile(display_state, "calculadora.py", "eval")
        resultado = eval(expr_math)
        limpiar_pantalla()
        display.insert(0,resultado)
    except: 
        limpiar_pantalla()
        display.insert(0, "ERROR")

#Botones numéricos

Button(root, text="1", command=lambda:obtener_numeros(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda:obtener_numeros(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda:obtener_numeros(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", command=lambda:obtener_numeros(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda:obtener_numeros(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda:obtener_numeros(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", command=lambda:obtener_numeros(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda:obtener_numeros(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", command=lambda:obtener_numeros(9)).grid(row=4, column=2, sticky=W+E)

#Botones Adicionales

Button(root, text="AC", command=lambda:limpiar_pantalla()).grid(row=5, column=0, sticky=W+E)
Button(root, text="0", command=lambda:obtener_numeros(0)).grid(row=5, column=1, sticky=W+E)
Button(root, text="%", command=lambda:obtener_operador("%")).grid(row=5, column=2, sticky=W+E)

Button(root, text="+", command=lambda:obtener_operador("+")).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", command=lambda:obtener_operador("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda:obtener_operador("*")).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda:obtener_operador("/")).grid(row=5, column=3, sticky=W+E)

Button(root, text="🠔", command=lambda:retroceso()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text="exp", command=lambda:obtener_operador("**")).grid(row=3, column=4, sticky=W+E)
Button(root, text="^2", command=lambda:obtener_operador("**2")).grid(row=3, column=5, sticky=W+E)
Button(root, text="(", command=lambda:obtener_operador("(")).grid(row=4, column=4, sticky=W+E)
Button(root, text=")", command=lambda:obtener_operador(")")).grid(row=4, column=5, sticky=W+E)
Button(root, text="=", command=lambda:calculo()).grid(row=5, column=4, sticky=W+E, columnspan=2)

root.mainloop()