const character = document.querySelector('.character');

// Definir variables para la posición inicial y las velocidades iniciales
let x = 0;
let y = window.innerHeight - 100; // Altura de la ventana del navegador

let vx = 5; // Velocidad horizontal
let vy = -15; // Velocidad vertical

// Función de animación
function animate() {
    // Actualizar la posición del carácter
    x += vx;
    y += vy;

    // Aplicar la posición al carácter
    character.style.left = x + 'px';
    character.style.top = y + 'px';

    // Actualizar la velocidad vertical para simular la gravedad
    vy += 1; // Ajusta este valor según lo rápido que quieras que caiga

    // Detener la animación cuando el carácter esté en el suelo
    if (y + character.clientHeight >= window.innerHeight) {
        clearInterval(animation);
    }
}

// Iniciar la animación
const animation = setInterval(animate, 1000 / 60); // Actualiza la animación a 60 FPS
