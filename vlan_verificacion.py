
def verificar_vlan(vlan):
    if 1 <= vlan <= 1005:
        return "VLAN pertenece al rango normal."
    elif 1006 <= vlan <= 4094:
        return "VLAN pertenece al rango extendido."
    else:
        return "Número de VLAN no válido. Debe estar entre 1 y 4094."

try:
    vlan_input = int(input("Ingrese el número de VLAN: "))
    resultado = verificar_vlan(vlan_input)
    print(resultado)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
