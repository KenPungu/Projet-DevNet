from netmiko import ConnectHandler

# Paramètres de connexion du routeur Cisco1
Cisco1 = {
    "device_type": "cisco_nxos",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345"
}


# L'établissement de la Connexion au routeur Cisco1
try:
    connexion = ConnectHandler(**Cisco1)
    print("La Connexion est établie avec succès au routeur.")
except Exception as e:
    print(f"Impossible de se connecter au routeur : {str(e)}")
    exit()


# 1. Affichage du nom du routeur, sa version du OS et le modèle du routeur du Cisco1
print("\n1. Les Informations sur le routeur:")
output = connexion.send_command("show version")
print(output)


# 2. Affichage de la liste des interfaces UP du routeur Cisco1
print("\n2. Voici la liste des interfaces UP:")
output = connexion.send_command("show ip interface brief | include up")
print(output)


# 3. Affichage de la liste des interfaces Down du routeur Cisco1
print("\n3. Voici la liste des interfaces Down:")
output = connexion.send_command("show ip interface brief | include down")
print(output)


# 4. Affichage du nombre d'interfaces Fast Ethernet et Gigabit Ethernet du routeur Cisco1
print("\n4. Nombre d'interfaces Fast Ethernet et Gigabit Ethernet:")
output = connexion.send_command("show ip interface brief | include Fast|GigabitEthernet")
interfaces = output.splitlines()
fast_ethernet_count = 0
gigabit_ethernet_count = 0
for interface in interfaces:
    if "FastEthernet" in interface:
        fast_ethernet_count += 1
    elif "GigabitEthernet" in interface:
        gigabit_ethernet_count += 1
print("Nombre d'interfaces Fast Ethernet:", fast_ethernet_count)
print("Nombre d'interfaces Gigabit Ethernet:", gigabit_ethernet_count)


# 5. Affichage de la liste des réseaux accessibles via le routeur
print("\n5. Voici la liste des réseaux accessibles via le routeur:")
output = connexion.send_command("show ip route")
print(output)


# Fin de la connexion SSH
connexion.disconnect()