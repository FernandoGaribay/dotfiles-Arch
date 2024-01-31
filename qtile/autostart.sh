#!/bin/sh

# Configuracion de monitores
xrandr --output DP-1 --off --output HDMI-1 --primary --mode 1920x1080 --pos 1280x0 --rotate normal --output DP-2 --mode 1280x768 --pos 0x156 --rotate normal --output DP-3 --off --output HDMI-1-2 --off --output DVI-D-1-1 --off --output HDMI-1-3 --off &

# Configuracion del teclado en latinoamerica
setxkbmap latam &

# Inicializar Picom para efectos visuales
picom -f --xrender-sync-fence &

# Inicializar nitrogen (fondo de pantalla)
nitrogen --restore &

# Iconos del sistema
udiskie -t &
nm-applet &
volumeicon &
cbtticon -u 5 &
