import os 
os.system("cls")

titulo= """
Bienvenidos al taller de mecanica automotriz.
Porfavor selecciona una opcion.

1.Registrar Vehículo
2.Listar Todos los Vehículos Registrados
3.Imprimir orden de Reparación
4.Salir


"""
Listadodevehiculo = f"""                         {"Listado De todos los vehiculos"}
{"-"*75} 
{"Marca":<20}{"Año De fabricacion":<20}{"kilometraje":<20}{"costo de reparacion estimado":<20}{"impuesto":<20}{"Total":<20}
{"-"*75}
"""

Datos_vehiculo=["TOYOTA","KIA","CHEVROLET"]
datos=[]


def Registrar_vehículo():
    os.system("cls")
    try:
        marca=input("Marca: ").strip().upper()
        año_fabricacion=int(input("Año De Fabricacion: "))
        kilometraje=int(input("Kilometraje: "))
        Costo_de_reparacion=int(input("Costo de reparación estimado: "))
        if len(marca) < 1 or año_fabricacion <=0 or kilometraje < 0 or Costo_de_reparacion <=0:
            input("Error, otra vez...")
        else: 
            impuesto= round(Costo_de_reparacion*0.08)
            total=Costo_de_reparacion+impuesto
            datos.append([marca,año_fabricacion,kilometraje,Costo_de_reparacion,impuesto,total])
    except Exception as o:
        input(f"Exepcion en {str(o)}, reintente..")
    

def Listar_Todos_los_Vehículos_Registrados():
    ssalida= Listadodevehiculo
    for t in datos:
        ssalida += f"{t[0]:<20}"
        ssalida += f"{t[1]:<20}"
        ssalida += f"{t[2]:<20}"
        ssalida += f"{t[3]:<20}"
        ssalida += f"{t[4]:<20}"
        ssalida += f"{t[5]:<20}"
        ssalida += "\n"
    return ssalida

def xmarca():
    ssalida= Listadodevehiculo
    for t in datos:
        ssalida += f"{t[0]:<20}"
        ssalida += f"{t[1]:<20}"
        ssalida += f"{t[2]:<20}"
        ssalida += f"{t[3]:<20}"
        ssalida += f"{t[4]:<20}"
        ssalida += f"{t[5]:<20}"
        ssalida += "\n"
    return ssalida
  



def Imprimir_orden_de_Reparación():
    while True:
        try:
            imprimir= input(f"todos / {Datos_vehiculo}\n ¿como va imprimir?: ").upper()
            if imprimir in xmarca:
                with open(imprimir+".txt" , "w", encoding="utf-8") as archivo:
                archivo.write(xmarca)
                input("archivo imprimido con exito...")
                break
            elif imprimir== "TODOS":
                with open(imprimir+"txt","w", encoding="utf-8") as archivo:
                    archivo.write(Listar_Todos_los_Vehículos_Registrados())
                    input("se a creado con exito...")
                    break
            else:
                input("error...")
        except Exception as x:
            input(f"exepcion {str(x)}")


while True:
    try:
        o=int(input(titulo))
        if o < 0 or o > 4:
            input("Error.")
        elif o==1:
            Registrar_vehículo()
        elif o==2:
            print(Listar_Todos_los_Vehículos_Registrados())
            input()
        elif o==3:
            Imprimir_orden_de_Reparación()
        elif o==4:
            break
        else:
            input("error reintente.")
            os.system("cls")
    except Exception as e:
        input(f"Exception {str(e)}, reintente...")
        os.system("cls")








