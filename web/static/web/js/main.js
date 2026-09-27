document.addEventListener('DOMContentLoaded', function () {
    const welcomeKey = 'userWelcomeShown';

    // Mostrar el modal una sola vez tras iniciar sesión
    const modalElement = document.getElementById('userWelcomeModal');
    if (modalElement && localStorage.getItem(welcomeKey) !== 'true') {
        new bootstrap.Modal(modalElement).show();
        localStorage.setItem(welcomeKey, 'true');
    }

    // Al cerrar sesión, reiniciar para el próximo login
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function () {
            localStorage.removeItem(welcomeKey);
        });
    }
});