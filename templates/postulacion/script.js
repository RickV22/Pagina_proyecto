function actualizarOpciones() {
    var tipoMonitoria = document.querySelector('input[name="tipo_monitoria"]:checked').value;
    var moduloAreaContainer = document.getElementById('moduloAreaContainer');
    moduloAreaContainer.innerHTML = ''; // Limpiar el contenido anterior
    
    if (tipoMonitoria === 'academica') {
        var academicaOptions = [
            { value: 'modulo_calculo', text: 'Cálculo' },
            { value: 'modulo_algebra', text: 'Álgebra y Trigonometría' },
            // Agregar más opciones según sea necesario
        ];
        
        var selectModulo = document.createElement('select');
        selectModulo.setAttribute('id', 'modulo');
        selectModulo.setAttribute('name', 'modulo');
        
        academicaOptions.forEach(function(option) {
            var optionElement = document.createElement('option');
            optionElement.value = option.value;
            optionElement.textContent = option.text;
            selectModulo.appendChild(optionElement);
        });
        
        moduloAreaContainer.appendChild(selectModulo);
    } else if (tipoMonitoria === 'administrativa') {
        var administrativaOptions = [
            { value: 'area_sistemas', text: 'Área de Sistemas' },
            { value: 'area_administracion', text: 'Área de Administración' },
            // Agregar más opciones según sea necesario
        ];
        
        var selectArea = document.createElement('select');
        selectArea.setAttribute('id', 'area');
        selectArea.setAttribute('name', 'area');
        
        administrativaOptions.forEach(function(option) {
            var optionElement = document.createElement('option');
            optionElement.value = option.value;
            optionElement.textContent = option.text;
            selectArea.appendChild(optionElement);
        });
        
        moduloAreaContainer.appendChild(selectArea);
    }
}

// Manejar cambios en el tipo de monitoria
document.querySelectorAll('input[name="tipo_monitoria"]').forEach(function(radio) {
    radio.addEventListener('change', actualizarOpciones);
});

// Manejar el envío del formulario
document.getElementById('formularioPostulacion').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar que se recargue la página
    
    var formData = new FormData(this);
    
    // Simular el envío de datos usando AJAX (Debes adaptar esto a tu backend)
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'guardar_postulacion.php'); // Cambiar a tu script de guardado de datos
    xhr.onload = function() {
        if (xhr.status === 200) {
            alert('Postulación enviada exitosamente');
            // Aquí puedes agregar código para actualizar la página del administrador dinámicamente
            // Por ejemplo, haciendo otra solicitud AJAX para obtener y mostrar la lista actualizada de postulaciones
        } else {
            alert('Error al enviar la postulación');
        }
    };
    xhr.send(formData);
});

// Ejecutar la función inicial de actualización de opciones
actualizarOpciones();
