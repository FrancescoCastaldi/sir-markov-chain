// docs/script.js - Single-Screen Page-by-Page Tabbed Architecture

document.addEventListener('DOMContentLoaded', () => {

    const pages = document.querySelectorAll('.page-view');
    const crumbBtns = document.querySelectorAll('.crumb-btn');
    const dots = document.querySelectorAll('.dot');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const totalPages = pages.length;

    const pageHashes = [
        '#intro',
        '#modello',
        '#dinamica',
        '#limite-fluido',
        '#analisi',
        '#playground'
    ];

    let currentPage = 0;

    // Inizializza la pagina in base all'hash dell'URL se presente
    const initialHash = window.location.hash.toLowerCase();
    const hashIndex = pageHashes.indexOf(initialHash);
    if (hashIndex !== -1) {
        currentPage = hashIndex;
    }

    function showPage(index) {
        if (index < 0 || index >= totalPages) return;

        currentPage = index;

        // Aggiorna visibilità pagine
        pages.forEach((page, idx) => {
            if (idx === currentPage) {
                page.classList.add('active');
                page.scrollTop = 0; // Reset scroll interno
            } else {
                page.classList.remove('active');
            }
        });

        // Aggiorna breadcrumb buttons
        crumbBtns.forEach((btn, idx) => {
            if (idx === currentPage) {
                btn.classList.add('active');
                btn.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
            } else {
                btn.classList.remove('active');
            }
        });

        // Aggiorna indicatori a punti (dots)
        dots.forEach((dot, idx) => {
            if (idx === currentPage) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });

        // Aggiorna stato pulsanti prev / next
        if (prevBtn) prevBtn.disabled = (currentPage === 0);
        if (nextBtn) nextBtn.disabled = (currentPage === totalPages - 1);

        // Sincronizza hash URL senza ricaricare la pagina
        if (pageHashes[currentPage]) {
            history.replaceState(null, null, pageHashes[currentPage]);
        }

        // Se passiamo al playground, ridisegna il chart
        if (currentPage === 5 && typeof window.updatePlayground === 'function') {
            setTimeout(window.updatePlayground, 50);
        }

        // Trigger rendering MathJax se presente
        if (window.MathJax && window.MathJax.typesetPromise) {
            window.MathJax.typesetPromise();
        }
    }

    // Event listeners per breadcrumb tabs
    crumbBtns.forEach((btn) => {
        btn.addEventListener('click', () => {
            const targetPage = parseInt(btn.getAttribute('data-page'), 10);
            showPage(targetPage);
        });
    });

    // Event listeners per indicatori dots
    dots.forEach((dot) => {
        dot.addEventListener('click', () => {
            const targetPage = parseInt(dot.getAttribute('data-page'), 10);
            showPage(targetPage);
        });
    });

    // Pulsanti Prev e Next
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            if (currentPage > 0) showPage(currentPage - 1);
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            if (currentPage < totalPages - 1) showPage(currentPage + 1);
        });
    }

    // Navigazione da tastiera: Frecce sinistra / destra
    document.addEventListener('keydown', (e) => {
        // Ignora se l'utente sta digitando in un input
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

        if (e.key === 'ArrowRight' || e.key === 'PageDown') {
            if (currentPage < totalPages - 1) {
                e.preventDefault();
                showPage(currentPage + 1);
            }
        } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
            if (currentPage > 0) {
                e.preventDefault();
                showPage(currentPage - 1);
            }
        }
    });

    // Modal Zoom Immagini per discussione e presentazione
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImageSrc');
    const closeModalBtn = document.getElementById('closeModal');
    const modalTriggers = document.querySelectorAll('.js-modal-trigger');

    modalTriggers.forEach((trigger) => {
        trigger.addEventListener('click', () => {
            const imgSrc = trigger.getAttribute('data-img');
            if (imgSrc && modal && modalImg) {
                modalImg.src = imgSrc;
                modal.classList.add('visible');
            }
        });
    });

    function closeModal() {
        if (modal) {
            modal.classList.remove('visible');
            if (modalImg) setTimeout(() => { modalImg.src = ''; }, 200);
        }
    }

    if (closeModalBtn) closeModalBtn.addEventListener('click', closeModal);
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal();
        });
    }

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal && modal.classList.contains('visible')) {
            closeModal();
        }
    });

    // Mostra la schermata iniziale
    showPage(currentPage);
});

