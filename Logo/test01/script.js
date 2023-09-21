function descomponerBarra() {
    const bar = document.querySelector('.bar');
    const numbers = document.querySelector('.numbers');
    
    const width = bar.clientWidth; // Obtenemos el ancho de la barra
    const count = 10; // Número de números a mostrar
    
    const step = width / count; // Calculamos el ancho de cada número
    
    // Creamos los números y los animamos
    for (let i = 0; i < count; i++) {
        const number = document.createElement('span');
        number.textContent = i + 1;
        number.style.width = step + 'px';
        setTimeout(() => {
            number.style.width = '0';
        }, i * 200); // Añadimos un retraso para animar uno por uno
        numbers.appendChild(number);
    }
    
    // Ocultamos la barra
    bar.style.width = '0';
}
