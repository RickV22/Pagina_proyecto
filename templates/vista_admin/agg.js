function agregarHoras() {
    var horasInput = document.getElementById('horasCumplidas');
    var horasRealizadas = document.getElementById('horas-realizadas');
    var horas = parseFloat(horasInput.value);
    if (!isNaN(horas) && horas > 0) {
        var nuevasHoras = parseFloat(horasRealizadas.textContent) + horas;
        horasRealizadas.textContent = nuevasHoras;
        alert('Horas agregadas: ' + horas);
        horasInput.value = '';
    } else {
        alert('Por favor, ingrese una cantidad válida de horas.');
    }
}


