// docs/simulator.js

document.addEventListener('DOMContentLoaded', () => {
    // === 1. Element References ===
    const sliderBeta = document.getElementById('sliderBeta');
    const valBeta = document.getElementById('valBeta');
    
    const sliderGamma = document.getElementById('sliderGamma');
    const valGamma = document.getElementById('valGamma');
    
    const sliderN = document.getElementById('sliderN');
    const valN = document.getElementById('valN');
    
    const sliderI0 = document.getElementById('sliderI0');
    const valI0 = document.getElementById('valI0');
    
    const valR0 = document.getElementById('valR0');
    const ctx = document.getElementById('playgroundChart').getContext('2d');

    let sirChart;

    // === 2. Math Engine: Euler Method per SIR ODE ===
    function simulateSIR(N, I0, beta, gamma, days = 100, dt = 0.1) {
        const steps = Math.floor(days / dt);
        let S = N - I0;
        let I = I0;
        let R = 0;

        const historyS = [];
        const historyI = [];
        const historyR = [];
        const time = [];

        // Salviamo i dati ogni 1 giorno (non ad ogni dt)
        const saveInterval = Math.floor(1 / dt);

        for (let step = 0; step <= steps; step++) {
            if (step % saveInterval === 0) {
                historyS.push(S);
                historyI.push(I);
                historyR.push(R);
                time.push(step * dt);
            }

            // Derivate
            const dS = -beta * S * I / N;
            const dI = (beta * S * I / N) - gamma * I;
            const dR = gamma * I;

            // Aggiornamento Euler
            S += dS * dt;
            I += dI * dt;
            R += dR * dt;
        }

        return { time, S: historyS, I: historyI, R: historyR };
    }

    // === 3. Chart Integration ===
    function updateSimulator() {
        // Leggi i parametri correnti
        const beta = parseFloat(sliderBeta.value);
        const gamma = parseFloat(sliderGamma.value);
        const N = parseInt(sliderN.value, 10);
        let I0 = parseInt(sliderI0.value, 10);

        // Limita I0 a N
        if (I0 > N) {
            I0 = N;
            sliderI0.value = I0;
        }

        // Calcola e aggiorna UI badge
        valBeta.textContent = beta.toFixed(2);
        valGamma.textContent = gamma.toFixed(2);
        valN.textContent = N.toString();
        valI0.textContent = I0.toString();

        const R0 = beta / gamma;
        valR0.textContent = R0.toFixed(2);
        
        // Colore R0 (rosso se > 1)
        if (R0 > 1) {
            valR0.style.color = '#ef4444'; // red-500
        } else {
            valR0.style.color = '#3b82f6'; // blue-500
        }

        // Esegui Simulazione
        const data = simulateSIR(N, I0, beta, gamma, 120, 0.1);

        // Aggiorna o Crea Chart
        if (sirChart) {
            sirChart.data.labels = data.time;
            sirChart.data.datasets[0].data = data.S;
            sirChart.data.datasets[1].data = data.I;
            sirChart.data.datasets[2].data = data.R;
            sirChart.update('none'); // Update fluido senza animazione brutale
        } else {
            // Chart.js global defaults per dark mode
            Chart.defaults.color = '#94A3B8';
            Chart.defaults.font.family = 'Inter, sans-serif';

            sirChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.time,
                    datasets: [
                        {
                            label: 'Suscettibili (S)',
                            data: data.S,
                            borderColor: '#3b82f6', // blue
                            backgroundColor: 'rgba(59, 130, 246, 0.1)',
                            borderWidth: 3,
                            pointRadius: 0,
                            fill: true,
                            tension: 0.4
                        },
                        {
                            label: 'Infetti (I)',
                            data: data.I,
                            borderColor: '#ef4444', // red
                            backgroundColor: 'rgba(239, 68, 68, 0.1)',
                            borderWidth: 3,
                            pointRadius: 0,
                            fill: true,
                            tension: 0.4
                        },
                        {
                            label: 'Rimossi (R)',
                            data: data.R,
                            borderColor: '#10b981', // green
                            backgroundColor: 'rgba(16, 185, 129, 0.1)',
                            borderWidth: 3,
                            pointRadius: 0,
                            fill: true,
                            tension: 0.4
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    interaction: {
                        mode: 'index',
                        intersect: false,
                    },
                    plugins: {
                        legend: {
                            position: 'top',
                            labels: {
                                usePointStyle: true,
                                boxWidth: 8
                            }
                        },
                        tooltip: {
                            backgroundColor: 'rgba(0,0,0,0.8)',
                            titleFont: { size: 14 },
                            bodyFont: { size: 14 },
                            padding: 10,
                            cornerRadius: 8
                        }
                    },
                    scales: {
                        x: {
                            title: { display: true, text: 'Tempo (Giorni)' },
                            grid: { color: 'rgba(255,255,255,0.05)' }
                        },
                        y: {
                            title: { display: true, text: 'Popolazione' },
                            grid: { color: 'rgba(255,255,255,0.05)' },
                            beginAtZero: true
                        }
                    }
                }
            });
        }
    }

    // === 4. Event Listeners ===
    [sliderBeta, sliderGamma, sliderN, sliderI0].forEach(el => {
        el.addEventListener('input', updateSimulator);
    });

    // Inizializzazione
    updateSimulator();


    // === 5. Sidebar Navigation Logic ===
    const sections = document.querySelectorAll('.slide');
    const navLinks = document.querySelectorAll('.side-nav a');
    
    // Fallback: se stiamo usando JS, possiamo usare IntersectionObserver anche per la navbar
    const navObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                // Rimuovi active da tutti
                navLinks.forEach(link => link.classList.remove('active'));
                // Aggiungi active a quello corrente
                const currentLink = document.querySelector(`.side-nav a[href="#${id}"]`);
                if (currentLink) currentLink.classList.add('active');
            }
        });
    }, { threshold: 0.5 }); // 50% della slide visibile
    
    sections.forEach(sec => navObserver.observe(sec));
});
