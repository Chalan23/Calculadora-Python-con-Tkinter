import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Chalan-Calculadora")
ventana.config(bg="#2e2e2e")

ventana.rowconfigure(0, weight=1)
for i in range(6): ventana.rowconfigure(i, weight=1)
for i in range(4): ventana.columnconfigure(i, weight=1)

i = 0

entrada = tk.Entry(ventana, font=("Segoe UI", 22), bg="#1e1e1e", fg="#00FFAA",
                   insertbackground="white", bd=0, justify="right")
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

def clickBoton(valor):
    global i
    entrada.insert(i, valor)
    i += len(str(valor))

def borrarTodo():
    global i
    entrada.delete(0, tk.END)
    i = 0

def borrarUno():
    global i
    texto = entrada.get()
    if texto:
        entrada.delete(len(texto) - 1)
        i -= 1

def hacerOperacion():
    global i
    try:
        resultado = eval(entrada.get())
        borrarTodo()
        entrada.insert(0, resultado)
    except:
        borrarTodo()
        messagebox.showerror("Error", "Operación inválida")

def crear_boton(texto, fila, columna, comando, color="#444", col_span=1, row_span=1):
    btn = tk.Button(ventana, text=texto, font=("Segoe UI", 18), fg="white",
                    bg=color, activebackground="#666", bd=0,
                    command=comando)
    btn.grid(row=fila, column=columna, columnspan=col_span, rowspan=row_span,
             sticky="nsew", padx=5, pady=5)

crear_boton("AC", 1, 0, borrarTodo, color="#e74c3c")
crear_boton("←", 1, 1, borrarUno, color="#e67e22")
crear_boton("(", 1, 2, lambda: clickBoton("("))
crear_boton(")", 1, 3, lambda: clickBoton(")"))

crear_boton("7", 2, 0, lambda: clickBoton("7"))
crear_boton("8", 2, 1, lambda: clickBoton("8"))
crear_boton("9", 2, 2, lambda: clickBoton("9"))
crear_boton("/", 2, 3, lambda: clickBoton("/"), color="#2980b9")

crear_boton("4", 3, 0, lambda: clickBoton("4"))
crear_boton("5", 3, 1, lambda: clickBoton("5"))
crear_boton("6", 3, 2, lambda: clickBoton("6"))
crear_boton("*", 3, 3, lambda: clickBoton("*"), color="#2980b9")

crear_boton("1", 4, 0, lambda: clickBoton("1"))
crear_boton("2", 4, 1, lambda: clickBoton("2"))
crear_boton("3", 4, 2, lambda: clickBoton("3"))
crear_boton("-", 4, 3, lambda: clickBoton("-"), color="#27ae60")

crear_boton("0", 5, 0, lambda: clickBoton("0"), col_span=2)
crear_boton(".", 5, 2, lambda: clickBoton("."))
crear_boton("+", 5, 3, lambda: clickBoton("+"), color="#27ae60")

crear_boton("=", 6, 0, hacerOperacion, color="#f39c12", col_span=4)

ventana.mainloop()
