function mostrar(dato){
    if (dato == "espectador") {
        document.getElementById("espectadores").style.display = "block";
        document.getElementById("pilotos").style.display = "none";
    }
    if (dato == "piloto") {
        document.getElementById("espectadores").style.display = "none";
        document.getElementById("pilotos").style.display = "block";
    }
}

function pago(dato){
    if (dato == "miembro") {
        document.getElementById("pago").style.display = "block";

    }
    if (dato == "no_miembro") {
        document.getElementById("pago").style.display = "none";

    }
}