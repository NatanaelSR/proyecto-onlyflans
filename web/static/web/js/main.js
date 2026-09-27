document.addEventListener('DOMContentLoaded', function () {
    const modalElement = document.getElementById('userWelcomeModal');

    // El modal solo existe en el HTML si el usuario está logeado
    if (modalElement) {
        new bootstrap.Modal(modalElement).show();
    }
});