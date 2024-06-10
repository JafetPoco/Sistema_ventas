import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#FUNCIONES
Memoria=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
def flimpiar():
    pr1_en.delete(0,'end')
    pr1_en.insert(0,0)
    pr2_en.delete(0,'end')
    pr2_en.insert(0,0)
    pr3_en.delete(0,'end')
    pr3_en.insert(0,0)
    pr4_en.delete(0,'end')
    pr4_en.insert(0,0)
    pr5_en.delete(0,'end')
    pr5_en.insert(0,0)
    pr6_en.delete(0,'end')
    pr6_en.insert(0,0)
    pr7_en.delete(0,'end')
    pr7_en.insert(0,0)
    pr8_en.delete(0,'end')
    pr8_en.insert(0,0)
    apellido_en.delete(0,'end')
    nombre_en.delete(0,"end")
    telefono_en.delete(0,"end")
    suma_pan.delete(1.0,'end')

def fmemoria(X,Y):
    for i in range(8):
        aux=X[i]+Y[i]
        X[i]=aux
    return Memoria

def fguardar(X):
    try:
        nombre = nombre_en.get()
        apellido = apellido_en.get()
        telefono = int(telefono_en.get())

        if str(telefono)[:1]!="9":
            return messagebox.showerror("Error", "El número telefónico es incorrecto, por favor volver a ingresar")
        if len(str(telefono))!=9:
            return messagebox.showerror("Error", "El número telefónico es incorrecto, por favor volver a ingresar")
        if nombre=="" or apellido=="" or telefono=="":
             return messagebox.showerror("Error", "Por favor, Ingrese los datos necesarios")

    
        messagebox.showinfo("Venta guardada", "La venta se ha guardado correctamente.")

        datos=suma_pan.get("1.0", "end-1c")

        archivo_guardado = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if archivo_guardado:
            with open(archivo_guardado, 'w') as f:
                f.write(datos)
        cantidades=[float(pr1_en.get()),float(pr2_en.get()),float(pr3_en.get()),float(pr4_en.get())
                    ,float(pr5_en.get()),float(pr6_en.get()),float(pr7_en.get()),float(pr8_en.get())]
        
        with open('Ventas.txt', 'a') as file:
            for i in range(8):
                aux=cantidades[i]+X[i]
                X[i]=aux
                file.write(f"{aux}\n")
    except ValueError:
        messagebox.showerror("Error", "Por favor, Verifique que el Nombre, Apellido y Telefono sean correctos")
    

def fgrafico():
    ventana2 = tk.Tk()
    ventana2.geometry("700x500")
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=ventana2)
    canvas.get_tk_widget().pack()
    plt.bar(elementos, Memoria)
    plt.xlabel('Productos')
    plt.ylabel('Cantidad Vendida')
    plt.title('Productos Vendidos')

def fsuma(x):
    nombres=nombre_en.get()
    apellido=apellido_en.get()
    telefono=telefono_en.get()
    elementos=('Martillo','Alicate','Taladro','Serrucho','C.Tornillos','C.Clavos','C.Tuercas','Cable Elec.')
    precios=(35,20,270,52,51,23,30,12)
    suma_pan.delete(1.0,'end')
    suma_pan.insert("end", ("          FERRETERIA\n"))
    suma_pan.insert("end", ("\n"))
    suma_pan.insert("end", ("Nombre: "+nombres+" "+apellido+"\n"))
    suma_pan.insert("end", ("Telefono: "+telefono+"\n"))
    suma_pan.insert("end", ("="*29+"\n"))
    suma_pan.insert("end", ("PRODUCTO   P.UNIT.  IMPORTE\n"))
    suma_pan.insert("end", ("="*29+"\n"))

    for i in range(8):
        if x[i] != 0:
            longitud_palabra=13-len(str(elementos[i]))
            suma_pan.insert("end",str(elementos[i])+" "*longitud_palabra+str(float(precios[i]))+" "*6+str(x[i])+"\n")
    suma_pan.insert("end",("-"*29+"\n"))
    suma_pan.insert("end","TOTAL:       "+str(sum(x))+"\n")
    suma_pan.insert("end", ("="*29+"\n"))

def fdatos():
    precios=[3,3,1,1,3,3,1,1]
    cantidades=[float(pr1_en.get()),float(pr2_en.get()),float(pr3_en.get()),float(pr4_en.get())
                ,float(pr5_en.get()),float(pr6_en.get()),float(pr7_en.get()),float(pr8_en.get())]
    boleta=[]
    for i in range(0,8):
        aux=precios[i]*cantidades[i]
        boleta.append(aux)
    return fsuma(boleta)


# Crear ventana principal
ventana = tk.Tk()
ventana.geometry("800x460")  #Tamaño de ventana
ventana.title("Sistema de Ventas") #Nombre de la ventana
ventana.config(bg="#c9c9c9") #Color Fondo

#TITULOS
titulo = tk.Label(ventana, text="Interfas de Ventas",
bd=5, font=("Arial black", 18), bg="#a1a09d", fg="#212120")
titulo.pack(fill=tk.X)

datos = tk.Label(ventana,bd=2,font=("Arial black",16),text="Datos del Cliente:",bg="#c9c9c9", fg="#212120")
datos.place(x=10,y=45)

nombre = tk.Label(ventana,bd=2,font=(10),text="Nombre",bg="#c9c9c9", fg="#212120")
nombre.place(x=50,y=80)
nombre_en = tk.Entry(ventana, bg="#babab3", fg="#212120")
nombre_en.place(x=135,y=86,width=115,height=20)

apellido = tk.Label(ventana,bd=2,font=(10),text="Apellido",bg="#c9c9c9", fg="#212120")
apellido.place(x=300,y=80)
apellido_en = tk.Entry(ventana, bg="#babab3", fg="#212120")
apellido_en.place(x=385,y=86,width=115,height=20)

telefono = tk.Label(ventana,bd=2,font=(10),text="Telefono",bg="#c9c9c9", fg="#212120")
telefono.place(x=550,y=80)
telefono_en = tk.Entry(ventana, bg="#babab3", fg="#212120")
telefono_en.place(x=635,y=86,width=115,height=20)


productos = tk.Label(ventana, bd=0,text="Tabla de Productos", font=("Arial black",14),bg="#a1a09d", fg="#212120")
productos.pack(pady=86,fill=tk.X)

#PRODUCTOS
elementos=('Martillo','Alicate','Taladro','Serrucho','C.Tornillos','C.Clavos','C.Tuercas','Cable Elec.')

herramientas = tk.Label(ventana,bd=2,font=(10),text="Herramientas",bg="#c9c9c9", fg="#212120")
herramientas.place(x=70,y=170)
materiales = tk.Label(ventana,bd=2,font=(10),text="Materiales",bg="#c9c9c9", fg="#212120")
materiales.place(x=350,y=170)
boleta = tk.Label(ventana,bd=2,font=(10),text="BOLETA",bg="#c9c9c9", fg="#212120")
boleta.place(x=600,y=170)

pr1 = tk.Label(ventana,bd=2,font=(10),text=elementos[0],bg="#c9c9c9", fg="#212120")
pr1.place(x=50,y=210)
pr1_en = tk.Entry(ventana, bg="#babab3", fg="#212120")
pr1_en.place(x=150,y=216,width=60,height=20)
pr1_en.insert(0,0)

pr2 = tk.Label(ventana,bd=2,font=(10),text=elementos[1],bg="#c9c9c9", fg="#212120")
pr2.place(x=50,y=260)
pr2_en = tk.Entry(ventana, bg="#babab3", fg="#212120")
pr2_en.place(x=150,y=266,width=60,height=20)
pr2_en.insert(0,0)

pr3 = tk.Label(ventana,bd=2,font=(10),text=elementos[2],bg="#c9c9c9", fg="#212120")
pr3.place(x=50,y=310)
pr3_en = tk.Entry(ventana, bg="#babab3", fg="#212120")
pr3_en.place(x=150,y=316,width=60,height=20)
pr3_en.insert(0,0)

pr4 = tk.Label(ventana,bd=2,font=(10),text=elementos[3],bg="#c9c9c9", fg="#212120")
pr4.place(x=50,y=360)
pr4_en = tk.Entry(ventana, bg="#babab3", fg="#212120")
pr4_en.place(x=150,y=366,width=60,height=20)
pr4_en.insert(0,0)

pr5 = tk.Label(ventana,bd=2,font=(10),text=elementos[4],bg="#c9c9c9", fg="#212120")
pr5.place(x=320,y=210)
pr5_en = tk.Entry(ventana, bg="#babab3", fg="#212120")
pr5_en.place(x=420,y=216,width=60,height=20)
pr5_en.insert(0,0)

pr6 = tk.Label(ventana,bd=2,font=(10),text=elementos[5],bg="#c9c9c9", fg="#212120")
pr6.place(x=320,y=260)
pr6_en = tk.Entry(ventana, bg="#babab3", fg="#212120")
pr6_en.place(x=420,y=266,width=60,height=20)
pr6_en.insert(0,0)

pr7 = tk.Label(ventana,bd=2,font=(10),text=elementos[6],bg="#c9c9c9", fg="#212120")
pr7.place(x=320,y=310)
pr7_en = tk.Entry(ventana, bg="#babab3", fg="#212120")
pr7_en.place(x=420,y=316,width=60,height=20)
pr7_en.insert(0,0)

pr8 = tk.Label(ventana,bd=2,font=(10),text=elementos[7],bg="#c9c9c9", fg="#212120")
pr8.place(x=320,y=360)
pr8_en = tk.Entry(ventana, bg="#babab3", fg="#212120")
pr8_en.place(x=420,y=366,width=60,height=20)
pr8_en.insert(0,0)

scroll = tk.Scrollbar(ventana, orient="vertical")
suma_pan = tk.Text(ventana,bg="#babab3",bd=2, fg="#212120",relief=tk.FLAT,yscrollcommand=scroll.set)
suma_pan.place(x=520,y=216,width=240,height=180)
scroll.place(x=760,y=216,width=18,height=180)
scroll.config(command=suma_pan.yview)

#BOTONES
sumar = tk.Button(ventana,bd=2,font=(10),text="Sumar",bg="#ffffff", fg="#212120",command=fdatos)
sumar.place(x=350,y=410)

guardar = tk.Button(ventana,bd=2,font=(10),text="Guardar",bg="#ffffff", fg="#212120",command=lambda:fguardar(Memoria))
guardar.place(x=500,y=410)

grafico = tk.Button(ventana,bd=2,font=(10),text="Graficar",bg="#ffffff", fg="#212120",command=fgrafico)
grafico.place(x=650,y=410)

limpiar = tk.Button(ventana,bd=2,font=(10),text="Limpiar",bg="#ffffff", fg="#212120",command=flimpiar)
limpiar.place(x=100,y=410)

# Ejecutar la interfaz
ventana.mainloop()