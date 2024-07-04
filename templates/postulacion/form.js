function actualizarOpciones() {
    var tipoMonitoria = document.querySelector('input[name="tipo_monitoria"]:checked').value;
    var moduloAreaSelect = document.getElementById('modulo_area');
    
    moduloAreaSelect.innerHTML = '<option value="">Seleccione...</option>';
    
    if (tipoMonitoria === 'academica') {
        var academicaOptions = [
            { value: 'calculo', text: 'Cálculo' },
            { value: 'algebra_trigonometria', text: 'Álgebra y Trigonometría' },
            { value: 'programacion_modular', text: 'Programación Modular' },
            { value: 'estructura_datos', text: 'Estructura de Datos' }
            // Agrega más opciones según sea necesario
        ];
        
        academicaOptions.forEach(function(option) {
            var optionElement = document.createElement('option');
            optionElement.value = option.value;
            optionElement.textContent = option.text;
            moduloAreaSelect.appendChild(optionElement);
        });
    } else if (tipoMonitoria === 'administrativa') {
        var administrativaOptions = [
            { value: 'area_sistemas', text: 'Área de Sistemas' },
            { value: 'area_administracion', text: 'Área de Administración' },
            { value: 'area_admisiones', text: 'Área de Admisiones' },
            { value: 'area_rrhh', text: 'Área de Recursos Humanos' }
            // Agrega más opciones según sea necesario
        ];
        
        administrativaOptions.forEach(function(option) {
            var optionElement = document.createElement('option');
            optionElement.value = option.value;
            optionElement.textContent = option.text;
            moduloAreaSelect.appendChild(optionElement);
        });
    }
}

document.querySelectorAll('input[name="tipo_monitoria"]').forEach(function(radio) {
    radio.addEventListener('change', actualizarOpciones);
});

actualizarOpciones();



/*postulacion*//////////////////////////////////////////////////////

