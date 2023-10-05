const body = document.body;
const video = document.querySelector('#myVideo');

function toggleDarkVideoMode() {
    body.classList.toggle('dark'); // Alternar o modo escuro
    video.style.display = (video.style.display === 'none') ? 'block' : 'none'; // Alternar o vídeo
}
