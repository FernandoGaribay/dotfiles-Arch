#!/bin/bash

APAGAR="<span foreground='#b70000'>⏻ </span> Apagar"
SUSPENDER="<span foreground='#004eb7'> </span> Suspender"
REINICIAR="<span foreground='#dcd200'> </span> Reiniciar"
CERRAR_SESION="<span foreground='#8200dc'> </span> CerrarSesion"

opciones="$APAGAR\n$SUSPENDER\n$REINICIAR\n$CERRAR_SESION"
seleccion=$(echo -e "$opciones" | rofi -dmenu -markup-rows -p "Selecciona una opción")

case "$seleccion" in
    "$APAGAR")
        systemctl poweroff
        ;;
    "$SUSPENDER")
	systemctl suspend
	sleep 5
	dm-tool switch-to-greeter
	;;
    "$REINICIAR")
        systemctl reboot
        ;;
    "$CERRAR_SESION")
        loginctl terminate-user "$(whoami)"
        ;;
esac
