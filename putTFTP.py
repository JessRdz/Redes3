import tftpy

tftp_server = input('Dirección: ')
archivo_origen = input('Nombre del archivo a subir: ')
tftp = tftpy.TftpClient(tftp_server, 69)
tftp.upload('startup-config', archivo_origen)
