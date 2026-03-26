// creates sakura petals and drops them from the top
function createPetals() {
    const layer = document.getElementById('petals');
    const colors = ['#f9c0d0', '#f5a8be', '#fbd0dc', '#eed0e8', '#dcc8f0'];
    
    for (let i = 0; i < 25; i++) {
        const petal = document.createElement('div');
        petal.className = 'petal';

        // random size between 5px and 13px
        const size = (Math.random() * 8 + 5).toFixed(1);

        // random horizontal drift while falling
        const drift = ((Math.random() - 0.5) * 150).toFixed(0);

        // random speed and start time so they don't all fall together
        const duration = (Math.random() * 10 + 8).toFixed(1);
        const delay = (Math.random() * 14).toFixed(1);

        // random color from our list
        const color = colors[Math.floor(Math.random() * colors.length)];

        petal.style.cssText = `
            left: ${(Math.random() * 100).toFixed(1)}%;
            width: ${size}px;
            height: ${size}px;
            --dr: ${drift}px;
            animation-duration: ${duration}s;
            animation-delay: -${delay}s;
            background: ${color};
            opacity: 0.75;
        `;

        layer.appendChild(petal);
    }
}

createPetals();