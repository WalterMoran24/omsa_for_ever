'''Inicio de la aplicacion'''
#ACTUALIZAR PARITARIAS
from tkinter import Button, Label, Entry, Tk

def quincena_1():
    '''Funcion de la primer quincena'''
    try:
        valor_1 = txt.get()
        valor_2 = txt1.get()
        f= (float(valor_1)) * (float(valor_2))
        g = f* 0.195
        r= round(f-g,2)
        txt2.delete(0,'end')
        txt2.insert(0,r)
    except ValueError:
        print("Error,ingrese un dato valido")

def quincena_2():
    '''Funcion de la segunda quincena'''
    try:
        valor_1 =txt.get()
        valor_4 =txt3.get()
        f= (float(valor_1)) * (float(valor_4))
        g = f* 0.195
        r= round(f-g,2)
        txt4.delete(0,'end')
        txt4.insert(0,r)
    except ValueError:
        print("Error")

def mes_completo():
    '''Sumatoria de quincenas'''
    try:
        valor_1= txt.get()
        valor_2 = txt1.get()
        valor_4 =txt3.get()
        rta = (float(valor_2)) + (float(valor_4))
        rta_bruto = rta*float(valor_1)
        rta_descuento = rta_bruto*0.195
        rta_total= round(rta_bruto-rta_descuento,2)
        txt5.delete(0,'end')
        txt5.insert(0,rta_total)
    except ValueError:
        print("Error")

def minimo():
    '''Calculo del minimo global'''
    try:
        valor_1= txt.get()
        valor_2 = txt1.get()
        valor_4 =txt3.get()
        rta = (float(valor_2)) + (float(valor_4))
        rta_bruto = rta*float(valor_1)
        rta_descuento = rta_bruto*0.195
        rta_total= round(rta_bruto-rta_descuento,2)
        imgr = 727823.48
        imgr_neto = imgr * 0.195
        imgr_total= imgr-imgr_neto
        rta_posta=round(imgr_total-rta_total,2)
        txt6.delete(0,'end')
        txt6.insert(0,rta_posta)
        txt7.delete(0,'end')
        txt7.insert(0,imgr_total)
    except ValueError:
        print("Error")

ventana = Tk()
ventana.geometry("480x360") #ESTO DEBE IR T0DO JUNTO
ventana.title("Aplicacion suma")

#<<<<<<<< PRIMER CAJA >>>>>>>>>>>

lbl= Label(ventana,text = "Valor hora") # IMPRIME LO DE ENCIMA DE LA CAJA "Lo activa"
lbl.place(x=0, y=10, width=100, height=20) # UBICACION DEL TEXTO ENCIMA DE LA CAJA
txt = Entry(ventana,bg="grey") # "Activa" LA CAJA DONDE INGRESAR EL DATO
txt.place(x=10, y=30, width=70, height=20) #UBICACION DE LA CAJA DONDE


#<<<<<<<<<<<<< SEGUNDA CAJA >>>>>>>>>>>

lbl1= Label(ventana,text = "Horas trabajadas")
lbl1.place(x=0, y=60, width=100, height=20)
txt1 = Entry(ventana,bg="yellow")
txt1.place(x=10, y=80, width=70, height=20)

#<<<<<<<<<<<<< Quincena neto >>>>>>>>>>>>>

lbl2= Label(ventana,text = "Primer quincena")
lbl2.place(x=10, y=110, width= 100, height=20)
txt2=Entry(ventana,bg="yellow")
txt2.place(x=10, y=130, width= 70, height=20)

btn_producto = Button(ventana,text= "Quincena 1",command=quincena_1)
btn_producto.place(x=200, y=30, width= 70,height= 20)

#################################################################################

btn_producto = Button(ventana,text= "Quincena 2",command=quincena_2)
btn_producto.place(x=200, y=60, width= 70,height= 20)

########################################################################################

btn_producto = Button(ventana,text= "Sueldo total",command=mes_completo)
btn_producto.place(x=200, y=90, width= 70,height= 20)

########################################################################################
btn_producto = Button(ventana,text= "Minimo global",command=minimo)
btn_producto.place(x=200, y=120, width= 100,height= 20)

lbl3= Label(ventana,text = "Horas trabajadas")
lbl3.place(x=10, y=170, width= 100, height=20)
txt3=Entry(ventana,bg="pink")
txt3.place(x=10, y=190, width= 70, height=20)

lbl4= Label(ventana,text = "Segunda quincena")
lbl4.place(x=10, y=230, width= 100, height=20)
txt4=Entry(ventana,bg="pink")
txt4.place(x=10, y=250, width= 70, height=20)

lbl5= Label(ventana,text = "Horas mes")
lbl5.place(x=10, y=290, width= 100, height=20)
txt5=Entry(ventana,bg="pink")
txt5.place(x=10, y=310, width= 70, height=20)

lbl6= Label(ventana,text = "minimo global")
lbl6.place(x=120, y=170, width= 100, height=20)
txt6=Entry(ventana,bg="white")
txt6.place(x=120, y=190, width= 70, height=20)

lbl7= Label(ventana,text = "Total mensual")
lbl7.place(x=120, y=220, width= 100, height=20)
txt7=Entry(ventana,bg="white")
txt7.place(x=120, y=250, width= 70, height=20)
ventana.mainloop()
