function showTab(tabName) {
    // Hide all sections
    document.querySelectorAll('.tab-section').forEach(section => {
        section.classList.remove('active');
    });

    // Show selected section
    const target = document.getElementById(tabName);
    if (target) {
        target.classList.add('active');
    }

    // Update nav active state
    document.querySelectorAll('nav a').forEach(link => {
        link.classList.remove('active');
        if (link.dataset.tab === tabName) {
            link.classList.add('active');
        }
    });

    // Scroll to top of main
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// FIX: use defer on script tag instead of window.onload — but keeping
// this as a fallback for safety
document.addEventListener('DOMContentLoaded', function () {
    showTab('home');
});