// docs/script.js

document.addEventListener('DOMContentLoaded', () => {

    /* =========================================================================
     * 1. PROGRESSIVE ENHANCEMENT: Scroll Animations
     * ========================================================================= 
     * Il CSS moderno (animation-timeline: view()) gestisce l'animazione al 100% 
     * su GPU per i browser moderni (Chrome 115+, Safari 26+).
     * 
     * Se il browser NON lo supporta, eseguiamo il fallback basato su JS (IntersectionObserver).
     */
    
    const supportsNativeScrollAnimations = CSS.supports('(animation-timeline: scroll()) and (animation-range: 0% 100%)');
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!supportsNativeScrollAnimations && !prefersReducedMotion) {
        // Fallback: IntersectionObserver
        const observerOptions = {
            root: null, // usa la viewport come root
            rootMargin: '0px',
            threshold: 0.2 // attiva l'effetto quando il 20% dell'elemento è visibile
        };

        const scrollObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    // Opzionale: de-osservare l'elemento se si vuole animare una volta sola
                    // observer.unobserve(entry.target); 
                } else {
                    // Rimuovi questa riga se vuoi che l'elemento resti visibile per sempre
                    entry.target.classList.remove('is-visible');
                }
            });
        }, observerOptions);

        const scrollElements = document.querySelectorAll('.animate-on-scroll');
        scrollElements.forEach((el) => {
            scrollObserver.observe(el);
        });
        
        console.log("JavaScript Scroll Observer initialized (CSS Scroll-Driven Animations non supportate).");
    } else {
        console.log("Native CSS Scroll-Driven Animations in uso, o Prefers Reduced Motion abilitato. (JS Observer bypassed).");
    }

    /* =========================================================================
     * 2. IMAGE MODAL LOGIC
     * ========================================================================= 
     * Apre e chiude una modale full-screen per i grafici
     */

    const frames = document.querySelectorAll('.plot-frame');
    const modal = document.createElement('div');
    modal.classList.add('modal');
    modal.innerHTML = `
        <button class="modal-close" aria-label="Close modal">&times;</button>
        <div class="modal-content">
            <img class="modal-img" src="" alt="Zoomed Plot">
        </div>
    `;
    document.body.appendChild(modal);

    const modalImg = modal.querySelector('.modal-img');
    const closeBtn = modal.querySelector('.modal-close');

    // Open Modal
    frames.forEach(frame => {
        frame.addEventListener('click', () => {
            const img = frame.querySelector('img');
            if(img) {
                modalImg.src = img.src;
                modalImg.alt = img.alt;
                modal.classList.add('visible');
            }
        });
    });

    // Close Modal Logic
    const closeModal = () => {
        modal.classList.remove('visible');
        setTimeout(() => { modalImg.src = ''; }, 300); // Wait for transition
    };

    closeBtn.addEventListener('click', closeModal);
    
    // Chiudi cliccando fuori dall'immagine
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Chiudi con ESC
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('visible')) {
            closeModal();
        }
    });
});
