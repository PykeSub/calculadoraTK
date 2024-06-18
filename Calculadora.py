from tkinter import *

root = Tk()
root.title("Calculadora")

display = Entry(root)
display.grid(row = 1, columnspan = 6, sticky= W+E)

i = 0

def obtener_numeros(n):
    global i
    display.insert(i, n)
    i += 1

def obtener_operacion(operator):
    global i
    operator_length = len(operator)
    display.insert(i, operator)
    i += operator_length

def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, 'Error')
        
def calcular():
    display_state = display.get()
    try:
        math_expression = compile(display_state, 'Calculadora.py', 'eval')
        resultado = eval(math_expression)
        clear_display()
        display.insert(0, resultado)
    except:
        clear_display()
        display.insert(0, 'Error')
        
# Botones Numericos

Button(root, text = '1', font = ('Arial', 24), command = lambda: obtener_numeros(1)).grid(row = 2, column = 0, sticky= W+E)
Button(root, text = '2', font = ('Arial', 24), command = lambda: obtener_numeros(2)).grid(row = 2, column = 1, sticky= W+E)
Button(root, text = '3', font = ('Arial', 24), command = lambda: obtener_numeros(3)).grid(row = 2, column = 2, sticky= W+E)

Button(root, text = '4', font = ('Arial', 24), command = lambda: obtener_numeros(4)).grid(row = 3, column = 0, sticky= W+E)
Button(root, text = '5', font = ('Arial', 24), command = lambda: obtener_numeros(5)).grid(row = 3, column = 1, sticky= W+E)
Button(root, text = '6', font = ('Arial', 24), command = lambda: obtener_numeros(6)).grid(row = 3, column = 2, sticky= W+E)

Button(root, text = '7', font = ('Arial', 24), command = lambda: obtener_numeros(7)).grid(row = 4, column = 0, sticky= W+E)
Button(root, text = '8', font = ('Arial', 24), command = lambda: obtener_numeros(8)).grid(row = 4, column = 1, sticky= W+E)
Button(root, text = '9', font = ('Arial', 24), command = lambda: obtener_numeros(9)).grid(row = 4, column = 2, sticky= W+E)

# Botones PART2

Button(root, text = 'AC', font = ('Arial', 24), command = lambda: clear_display()).grid(row = 5, column = 0, sticky= W+E)
Button(root, text = '0', font = ('Arial', 24), command = lambda: obtener_numeros(0)).grid(row = 5, column = 1, sticky= W+E)
Button(root, text = '%', font = ('Arial', 24), command = lambda: obtener_operacion('%')).grid(row = 5, column = 2, sticky= W+E)

# Botnoes de Operaciones

Button(root, text = '+', font = ('Arial', 24), command = lambda: obtener_operacion('+')).grid(row = 2, column = 3, sticky= W+E)
Button(root, text = '-', font = ('Arial', 24), command = lambda: obtener_operacion('-')).grid(row = 3, column = 3, sticky= W+E)
Button(root, text = '*', font = ('Arial', 24), command = lambda: obtener_operacion('*')).grid(row = 4, column = 3, sticky= W+E)
Button(root, text = '/', font = ('Arial', 24), command = lambda: obtener_operacion('/')).grid(row = 5, column = 3, sticky= W+E)

Button(root, text = '🠔', font = ('Arial', 24), command = lambda: undo()).grid(row = 2, column = 4, sticky= W+E, columnspan = 2)
Button(root, text = 'EXP', font = ('Arial', 24), command = lambda: obtener_operacion('**')).grid(row = 3, column = 4, sticky= W+E)
Button(root, text = '^2', font = ('Arial', 24), command = lambda: obtener_operacion('**2')).grid(row = 3, column = 5, sticky= W+E)
Button(root, text = '(', font = ('Arial', 24), command = lambda: obtener_operacion('()')).grid(row = 4, column = 4, sticky= W+E)
Button(root, text = ')', font = ('Arial', 24), command = lambda: obtener_operacion(')')).grid(row = 4, column = 5, sticky= W+E)
Button(root, text = '=', font = ('Arial', 24), command = lambda: calcular()).grid(row = 5, column = 4, sticky= W+E, columnspan = 2)

root.mainloop()