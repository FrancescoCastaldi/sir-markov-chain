/**
 * script.js
 * Vanilla JS logic for the Glassmorphic Dashboard
 */

document.addEventListener("DOMContentLoaded", () => {
    // --- Tab Navigation Logic ---
    const navItems = document.querySelectorAll('.nav-item');
    const tabPanes = document.querySelectorAll('.tab-pane');

    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Remove active class from all nav items
            navItems.forEach(nav => nav.classList.remove('active'));
            // Add active class to clicked item
            item.classList.add('active');

            // Hide all tab panes
            tabPanes.forEach(pane => pane.classList.remove('active'));
            
            // Show target tab pane
            const targetId = item.getAttribute('data-target');
            const targetPane = document.getElementById(targetId);
            if (targetPane) {
                targetPane.classList.add('active');
            }
        });
    });

    // --- Modal Logic for Plot Expansion ---
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImageSrc');
    const closeModalBtn = document.getElementById('closeModal');
    const triggerImages = document.querySelectorAll('.js-modal-trigger');

    // Open modal
    triggerImages.forEach(container => {
        container.addEventListener('click', () => {
            const imgSrc = container.getAttribute('data-img');
            modalImg.src = imgSrc;
            modal.classList.add('visible');
            document.body.style.overflow = 'hidden'; // Prevent background scrolling
        });
    });

    // Close modal via button
    closeModalBtn.addEventListener('click', () => {
        closeModal();
    });

    // Close modal via background click
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Close modal via Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('visible')) {
            closeModal();
        }
    });

    function closeModal() {
        modal.classList.remove('visible');
        document.body.style.overflow = '';
        // Wait for transition before clearing src
        setTimeout(() => {
            modalImg.src = '';
        }, 300);
    }
});
