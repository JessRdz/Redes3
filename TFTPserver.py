import tftpy

server = tftpy.TftpServer('/home/jesus/Documentos/Redes/Administrador')
server.listen('50.0.0.2', 69)
