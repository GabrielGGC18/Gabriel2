



window.onload = function() {
    const title = document.getElementById('Cachorro 1337');
    let text = title.innerHTML;
    title.innerHTML = '';

    let i = 0;

    function typeText() {
        if (i < text.length) {
            title.innerHTML += text.charAt(i);
            i++;
            setTimeout(typeText, 100); // Controla a velocidade da digitação
        }
    }

    typeText(); // Inicia o efeito de digitação
};