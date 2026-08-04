/**
 * script.js
 * Logic for Academic Scrollytelling Presentation
 */

document.addEventListener("DOMContentLoaded", () => {
    
    // --- Intersection Observer for Scroll Animations ---
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    const slides = document.querySelectorAll('.slide');

    // Observer per gli elementi che appaiono (fade in up)
    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Aggiungiamo una classe al parent slide per triggerare i child
                entry.target.classList.add('is-visible');
            } else {
                // Rimuoviamo per far ripartire l'animazione tornando indietro
                entry.target.classList.remove('is-visible');
            }
        });
    }, {
        threshold: 0.2 // Triggera quando il 20% della slide è visibile
    });

    // Osserviamo tutte le slide
    slides.forEach(slide => {
        fadeObserver.observe(slide);
    });

    // --- Modal Logic for Image Presentation ---
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImageSrc');
    const closeModalBtn = document.getElementById('closeModal');
    const triggerImages = document.querySelectorAll('.js-modal-trigger');

    // Apri modale
    triggerImages.forEach(container => {
        container.addEventListener('click', () => {
            const imgSrc = container.getAttribute('data-img');
            modalImg.src = imgSrc;
            modal.classList.add('visible');
            document.body.style.overflow = 'hidden'; // Blocco scroll accidentale in modale
        });
    });

    // Chiudi modale
    function closeModal() {
        modal.classList.remove('visible');
        document.body.style.overflow = '';
        setTimeout(() => {
            modalImg.src = '';
        }, 300);
    }

    closeModalBtn.addEventListener('click', closeModal);

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('visible')) {
            closeModal();
        }
        
        // --- Accessibilità Navigazione da Tastiera per le slide ---
        if (e.key === 'ArrowDown' || e.key === 'PageDown') {
            if (!modal.classList.contains('visible')) {
                // Lasciamo gestire lo scroll nativo, oppure potremmo forzare il salto
            }
        }
    });
});
