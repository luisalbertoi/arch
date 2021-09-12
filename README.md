# Arch
### Configuración

1. instalar Arch Linux
2. copiar la configuracion en su directorio
3. añadir la direcion MAC de su equipo al archivo de red **/etc/udev**

### Instalar paquetes via AUR

1. instalar los siguientes paquetes

```
pacman -S sudo git base-devel
```

2. añadir la configuracion del archivo **/etc/sudoers**
3. instalar el asistente para AUR **yay**

```
# inicia sessión con su usuario
cd /temp/
git clone https://aur.archlinux.org/yay
cd yay/
makepkg -si
```
4. instalar paquetes AUR
```
yay -S name-package
```
### Paquetes necesarios

* [xorg](https://wiki.archlinux.org/title/xorg) Sistema de ventanas
* [qtile](/.config/qtile/README.md) Entorno de escritorio
* [ly](https://github.com/nullgemm/ly) Administrador de inicio de sesión

### Capturas de pantalla
![terminal](/captures/terminal.png)
![more](/captures/more.png)