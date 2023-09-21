const character = document.querySelector('.character');

// Obtener la animación
const animation = character.animate(
    [
        {
            transform: 'translateX(0) translateY(0)',
        },
        {
            transform: 'translateX(100%) translateY(100%)',
        },
    ],
    {
        duration: 5000,
        iterations: Infinity,
        easing: 'linear',
        fill: 'both',
    }
);
