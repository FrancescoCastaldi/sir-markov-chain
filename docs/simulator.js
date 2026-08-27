// docs/simulator.js - Dark Mode Minimalist Palette #10 Playground

document.addEventListener('DOMContentLoaded', () => {
    const sliderBeta = document.getElementById('sliderBeta');
    const valBeta = document.getElementById('valBeta');
    
    const sliderGamma = document.getElementById('sliderGamma');
    const valGamma = document.getElementById('valGamma');
    
    const sliderN = document.getElementById('sliderN');
    const valN = document.getElementById('valN');
    
    const sliderI0 = document.getElementById('sliderI0');
    const valI0 = document.getElementById('valI0');
    
    const valR0 = document.getElementById('valR0');
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

    function updateSimulator() {
        if (!sliderBeta || !sliderGamma || !sliderN || !sliderI0) return;

        const beta = parseFloat(sliderBeta.value);
        const gamma = parseFloat(sliderGamma.value);
        const N = parseInt(sliderN.value, 10);
        let I0 = parseInt(sliderI0.value, 10);

        if (I0 > N) {
            I0 = N;
            sliderI0.value = I0;
        }

        valBeta.textContent = beta.toFixed(2);
        valGamma.textContent = gamma.toFixed(2);
        valN.textContent = N.toString();
        valI0.textContent = I0.toString();

        const R0 = beta / gamma;
        valR0.textContent = R0.toFixed(2);
        
        if (R0 > 1) {
            valR0.style.color = '#f87171'; // Red highlight
        } else {
            valR0.style.color = '#38bdf8'; // Blue highlight
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
        updateSimulator();
    };

    [sliderBeta, sliderGamma, sliderN, sliderI0].forEach(el => {
        if (el) el.addEventListener('input', updateSimulator);
    });

    updateSimulator();
});

