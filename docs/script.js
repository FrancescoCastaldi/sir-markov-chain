document.addEventListener('DOMContentLoaded', () => {
    // Navigation Tabs Logic
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section-content');

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Remove active from all links and sections
            navLinks.forEach(l => l.classList.remove('active'));
            sections.forEach(s => s.classList.remove('active-section'));

            // Add active to clicked
            link.classList.add('active');
            
            const targetId = link.getAttribute('data-target');
            document.getElementById(targetId).classList.add('active-section');

            // Optional smooth scroll to top if needed
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });

    // Close modal on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeModal();
        }
    });

    // Close modal on click outside image
    const modal = document.getElementById('imageModal');
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });
});

// Modal Logic
function openModal(imgSrc) {
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('expandedImg');
    
    modal.style.display = "block";
    modalImg.src = imgSrc;
    
    // Trigger reflow to apply animation
    void modal.offsetWidth;
    modal.classList.add('show');
}

function closeModal() {
    const modal = document.getElementById('imageModal');
    modal.classList.remove('show');
    
    // Wait for transition before hiding
    setTimeout(() => {
        modal.style.display = "none";
    }, 300);
}
