document.addEventListener('DOMContentLoaded', function () {
    const welcomeKey = 'userWelcomeShown';

    const modalElement = document.getElementById('userWelcomeModal');
    if (modalElement && localStorage.getItem(welcomeKey) !== 'true') {
        new bootstrap.Modal(modalElement).show();
        localStorage.setItem(welcomeKey, 'true');
    }
    
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function () {
            localStorage.removeItem(welcomeKey);
        });
    }
});