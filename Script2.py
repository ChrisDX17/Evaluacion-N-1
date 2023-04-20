
check = 0

while check == 0:
    vlan = int(input("¿Cual es el numero de su Vlan? "))
    if vlan >=1 and vlan <=1005:
        print("La Vlan ingresada corresponde a una Vlan Normal")
        break
    elif vlan >= 1006 and vlan <= 4095:
        print("La Vlan ingresada corresponde a una Vlan de Rango Extendido")
        break
    else:
        print("El numero de Vlan ingresado no es valido")
        check = 0
