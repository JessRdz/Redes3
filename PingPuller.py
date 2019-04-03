import subprocess
import ipaddress
import platform
import time
from Email import send_notification
import pynotify


def conocer_red():
    dispositivos = []
    f = open("Subnetworks", "r")
    subnets = f.readlines()

    for net_addr in subnets:

        # Subred
        ip_net = ipaddress.ip_network(net_addr.rstrip('\n'))

        # Obtener todos los dispositivos
        all_hosts = list(ip_net.hosts())

        # Hacer ping a cada direccion

        for i in range(len(all_hosts)):
            # Option for the number of packets as a function of
            param = '-n' if platform.system().lower() == 'windows' else '-c'

            # Building the command. Ex: "ping -c 1 google.com"
            command = ['ping', param, '1', "-w", "100", str(all_hosts[i])]

            if subprocess.call(command, stdout=False) == 0:
                if dispositivos.count(str(all_hosts[i])) == 0:
                    dispositivos.append([str(all_hosts[i]), 0])
    return dispositivos


def ping_dispositivos(dispositivos):
    dispositivos_temp = []
    for dispositivo, nivel in dispositivos:
        # Option for the number of packets as a function of
        param = '-n' if platform.system().lower() == 'windows' else '-c'

        # Building the command. Ex: "ping -c 1 google.com"
        command = ['ping', param, '1', "-w", "500", dispositivo]

        if subprocess.call(command, stdout=False) == 0:
            if nivel > 4:
                mensaje = "Se reanudo la comunicación con el dispositivo " + dispositivo
                send_notification("jesus-antonio-29@hotmail.com", "Dispositivo reconectado", mensaje)
                notificar(mensaje)
            nivel = 0
        else:
            nivel = nivel + 1
            if nivel == 5:
                mensaje = "Se interrumpió la comunicación con el dispositivo " + dispositivo
                send_notification("jesus-antonio-29@hotmail.com", "Dispositivo desconectado", mensaje)
                notificar(mensaje)

        dispositivos_temp.append([dispositivo, nivel])

    return dispositivos_temp

def notificar(mensaje):
    command = ['notify-send', mensaje]
    subprocess.call(command, stdout=False)


dispositivos = conocer_red()
print(dispositivos)
opc = 1
while opc:
    time.sleep(5)
    dispositivos = ping_dispositivos(dispositivos)
    print(dispositivos)

