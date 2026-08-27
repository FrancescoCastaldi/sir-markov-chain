// docs/simulator.js - Dark Mode Minimalist Palette #10 Playground with Direct R0 Slider

document.addEventListener('DOMContentLoaded', () => {
    const sliderBeta = document.getElementById('sliderBeta');
    const valBeta = document.getElementById('valBeta');
    
    const sliderGamma = document.getElementById('sliderGamma');
    const valGamma = document.getElementById('valGamma');

    const sliderR0 = document.getElementById('sliderR0');
    const valR0 = document.getElementById('valR0');
    const valR0Card = document.getElementById('valR0Card');
    const r0Regime = document.getElementById('r0Regime');
    const sThresholdInfo = document.getElementById('sThresholdInfo');
    
    const sliderN = document.getElementById('sliderN');
    const valN = document.getElementById('valN');
    
    const sliderI0 = document.getElementById('sliderI0');
    const valI0 = document.getElementById('valI0');
    
    const chartCanvas = document.getElementById('playgroundChart');
    if (!chartCanvas) return;
    
    const ctx = chartCanvas.getContext('2d');
    let sirChart;

    // === Math Engine: Euler Method per SIR ODE ===
    function simulateSIR(N, I0, beta, gamma, days = 120, dt = 0.1) {
        const steps = Math.floor(days / dt);
        let S = N - I0;
        let I = I0;
        let R = 0;

        const historyS = [];
        const historyI = [];
        const historyR = [];
        const time = [];

        const saveInterval = Math.floor(1 / dt);

        for (let step = 0; step <= steps; step++) {
            if (step % saveInterval === 0) {
                historyS.push(S);
                historyI.push(I);
                historyR.push(R);
                time.push(step * dt);
            }

            const dS = -beta * S * I / N;
            const dI = (beta * S * I / N) - gamma * I;
            const dR = gamma * I;

            S += dS * dt;
            I += dI * dt;
            R += dR * dt;
        }

        return { time, S: historyS, I: historyI, R: historyR };
    }

    function updateFromParams() {
        if (!sliderBeta || !sliderGamma || !sliderN || !sliderI0) return;

        const beta = parseFloat(sliderBeta.value);
        const gamma = parseFloat(sliderGamma.value);
        const N = parseInt(sliderN.value, 10);
        let I0 = parseInt(sliderI0.value, 10);

        if (I0 > N) {
            I0 = N;
            sliderI0.value = I0;
        }

        const R0 = beta / gamma;

        // Sincronizza lo slider R0 se non è lui l'evento attivo
        if (sliderR0) {
            sliderR0.value = Math.min(6.0, Math.max(0.2, R0)).toFixed(2);
        }

        renderSimulation(N, I0, beta, gamma, R0);
    }

    function updateFromR0() {
        if (!sliderR0 || !sliderGamma) return;

        const R0 = parseFloat(sliderR0.value);
        let gamma = parseFloat(sliderGamma.value);
        let beta = R0 * gamma;

        // Se beta eccede 1.0, riadatta gamma
        if (beta > 1.0) {
            beta = 1.0;
            gamma = beta / R0;
            sliderGamma.value = gamma.toFixed(2);
            if (valGamma) valGamma.textContent = gamma.toFixed(2);
        }

        sliderBeta.value = beta.toFixed(2);
        if (valBeta) valBeta.textContent = beta.toFixed(2);

        const N = parseInt(sliderN.value, 10);
        const I0 = parseInt(sliderI0.value, 10);

        renderSimulation(N, I0, beta, gamma, R0);
    }

    function renderSimulation(N, I0, beta, gamma, R0) {
        if (valBeta) valBeta.textContent = beta.toFixed(2);
        if (valGamma) valGamma.textContent = gamma.toFixed(2);
        if (valN) valN.textContent = N.toString();
        if (valI0) valI0.textContent = I0.toString();

        const r0Str = R0.toFixed(2);
        if (valR0) valR0.textContent = r0Str;
        if (valR0Card) valR0Card.textContent = r0Str;

        // Aggiorna stato del regime e colore
        if (R0 > 1.0) {
            const sStar = Math.floor(N / R0);
            if (valR0) valR0.style.color = '#f87171';
            if (valR0Card) valR0Card.style.color = '#f87171';
            if (r0Regime) {
                r0Regime.textContent = 'Sovracritico (Epidemia)';
                r0Regime.style.color = '#f87171';
            }
            if (sThresholdInfo) {
                sThresholdInfo.textContent = `Soglia di picco: S* = ${sStar} individui (${((sStar/N)*100).toFixed(0)}%)`;
            }
        } else if (Math.abs(R0 - 1.0) < 0.05) {
            if (valR0) valR0.style.color = '#9D9BA2';
            if (valR0Card) valR0Card.style.color = '#9D9BA2';
            if (r0Regime) {
                r0Regime.textContent = 'Soglia Critica (R₀ ≈ 1.0)';
                r0Regime.style.color = '#9D9BA2';
            }
            if (sThresholdInfo) {
                sThresholdInfo.textContent = 'Transizione di fase: nessun picco epidemico';
            }
        } else {
            if (valR0) valR0.style.color = '#38bdf8';
            if (valR0Card) valR0Card.style.color = '#38bdf8';
            if (r0Regime) {
                r0Regime.textContent = 'Subcritico (Estinzione spontanea)';
                r0Regime.style.color = '#38bdf8';
            }
            if (sThresholdInfo) {
                sThresholdInfo.textContent = 'Decrescita monotona: I(t) ≤ I₀';
            }
        }

        const data = simulateSIR(N, I0, beta, gamma, 120, 0.1);

        if (sirChart) {
            sirChart.data.labels = data.time;
            sirChart.data.datasets[0].data = data.S;
            sirChart.data.datasets[1].data = data.I;
            sirChart.data.datasets[2].data = data.R;
            sirChart.update('none');
        } else {
            Chart.defaults.color = '#9D9BA2';
            Chart.defaults.font.family = "'Plus Jakarta Sans', sans-serif";

            sirChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.time,
                    datasets: [
                        {
                            label: 'Suscettibili (S)',
                            data: data.S,
                            borderColor: '#38bdf8',
                            backgroundColor: 'rgba(56, 189, 248, 0.12)',
                            borderWidth: 2.5,
                            pointRadius: 0,
                            fill: true,
                            tension: 0.3
                        },
                        {
                            label: 'Infetti (I)',
                            data: data.I,
                            borderColor: '#f87171',
                            backgroundColor: 'rgba(248, 113, 113, 0.15)',
                            borderWidth: 2.5,
                            pointRadius: 0,
                            fill: true,
                            tension: 0.3
                        },
                        {
                            label: 'Rimossi (R)',
                            data: data.R,
                            borderColor: '#34d399',
                            backgroundColor: 'rgba(52, 211, 153, 0.12)',
                            borderWidth: 2.5,
                            pointRadius: 0,
                            fill: true,
                            tension: 0.3
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
                                color: '#EBEAEC',
                                usePointStyle: true,
                                boxWidth: 8,
                                font: { size: 12, weight: '600' }
                            }
                        },
                        tooltip: {
                            backgroundColor: 'rgba(60, 49, 61, 0.95)',
                            titleColor: '#EBEAEC',
                            bodyColor: '#EBEAEC',
                            borderColor: '#55535B',
                            borderWidth: 1,
                            padding: 10,
                            cornerRadius: 8
                        }
                    },
                    scales: {
                        x: {
                            title: { display: true, text: 'Tempo (Passi / Giorni)', color: '#9D9BA2' },
                            grid: { color: 'rgba(157, 155, 162, 0.12)' },
                            ticks: { color: '#9D9BA2' }
                        },
                        y: {
                            title: { display: true, text: 'Individui', color: '#9D9BA2' },
                            grid: { color: 'rgba(157, 155, 162, 0.12)' },
                            ticks: { color: '#9D9BA2' },
                            beginAtZero: true
                        }
                    }
                }
            });
        }
    }

    // Esporta per invocazione globale al cambio tab
    window.updatePlayground = () => {
        if (sirChart) {
            sirChart.resize();
        }
        updateFromParams();
    };

    [sliderBeta, sliderGamma, sliderN, sliderI0].forEach(el => {
        if (el) el.addEventListener('input', updateFromParams);
    });

    if (sliderR0) {
        sliderR0.addEventListener('input', updateFromR0);
    }

    updateFromParams();
});


