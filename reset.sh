#!/bin/bash

# Lista de paquetes a no borrar (fundamentales)
essential_packages=(
    'base'
    'base-devel'
    'linux'
    'linux-firmware'
    'sudo'
    'git'
    'neofetch'
    'vim'
)

# Marcar todos los paquetes instalados como dependencias
sudo pacman -D --asdeps $(pacman -Qqe)

# Marcar la lista de paquetes esenciales como explícitos
sudo pacman -D --asexplicit "${essential_packages[@]}"

# Borrar todos los paquetes que se hayan quedado como dependencias
sudo pacman -Rsn $(pacman -Qttdq)

# Limpiar la base de datos de paquetes
sudo pacman -Scc --noconfirm

# Preguntar al usuario si desea reiniciar el sistema
read -p "¿Desea reiniciar el sistema ahora? (s/n): " answer
case $answer in
    [Ss]* ) sudo reboot;;
    [Nn]* ) echo "El sistema no se reiniciará."; exit;;
    * ) echo "Respuesta no válida. El sistema no se reiniciará."; exit;;
esac
