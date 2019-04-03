import telnetlib

HOST = input("Dirección:")
password = input("Contraseña:")
archivo = input("Nombre del archivo:")

tn = telnetlib.Telnet(HOST)

print(tn.read_until(str.encode("Password: ")).decode())
tn.write(str.encode(password + "\n"))

tn.write(str.encode("enable\npass\nconfig t\nip ftp username jesus\nip ftp password ja29040421um\nexit\n"))

tn.write(str.encode("copy ftp: startup-config\n50.0.0.2\n" + archivo + "\n\nexit\n"))

print((tn.read_all()).decode())
