#!/bin/bash

# Lista de paquetes fundamentales
essential_packages=(
    'base'
    'linux'
    'linux-firmware'
    'bash'
    'coreutils'
    'filesystem'
    'glibc'
    'systemd'
    'systemd-sysvcompat'
    'pacman'
)

# Crear un archivo temporal para almacenar la lista de paquetes fundamentales
essential_packages_file=$(mktemp)
for package in "${essential_packages[@]}"; do
    echo $package >> $essential_packages_file
done

# Lista de todos los paquetes instalados
installed_packages=$(pacman -Qq)

# Crear un archivo temporal para almacenar los paquetes a eliminar
packages_to_remove_file=$(mktemp)

# Filtrar los paquetes que no están en la lista de paquetes fundamentales
for package in $installed_packages; do
    if ! grep -qx $package $essential_packages_file; then
        echo $package >> $packages_to_remove_file
    fi
done

# Desinstalar los paquetes no fundamentales
xargs -a $packages_to_remove_file sudo pacman -Rns --noconfirm

# Limpiar la base de datos de paquetes
sudo pacman -Scc --noconfirm

# Eliminar archivos temporales
rm $essential_packages_file
rm $packages_to_remove_file

# Reiniciar el sistema
sudo reboot
