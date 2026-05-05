document.addEventListener('DOMContentLoaded', () => {
    // Referencias a los gráficos
    let chartFibo1 = null;
    let chartFibo2 = null;
    let chartCongruencial = null;

    // Función auxiliar para agrupar datos en intervalos (Histograma)
    function calculateFrequencies(data, numBins = 10) {
        const bins = new Array(numBins).fill(0);
        const binSize = 1.0 / numBins;

        data.forEach(item => {
            const val = item.r_n_raw;
            let binIndex = Math.floor(val / binSize);
            if (binIndex >= numBins) binIndex = numBins - 1; // Para valores que sean exactamente 1.0
            bins[binIndex]++;
        });

        const labels = Array.from({length: numBins}, (_, i) => {
            const start = (i * binSize).toFixed(1);
            const end = ((i + 1) * binSize).toFixed(1);
            return `${start} - ${end}`;
        });

        return { labels, data: bins };
    }

    // Renderizar Gráfico
    function renderChart(canvasId, title, chartRef, frequencies, color) {
        const ctx = document.getElementById(canvasId).getContext('2d');
        
        if (chartRef) {
            chartRef.destroy();
        }

        return new Chart(ctx, {
            type: 'bar',
            data: {
                labels: frequencies.labels,
                datasets: [{
                    label: 'Frecuencia',
                    data: frequencies.data,
                    backgroundColor: color,
                    borderColor: color.replace('0.6', '1'),
                    borderWidth: 1,
                    borderRadius: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: { color: 'rgba(255, 255, 255, 0.1)' },
                        ticks: { color: '#cbd5e1' }
                    },
                    x: {
                        grid: { display: false },
                        ticks: { color: '#cbd5e1' }
                    }
                }
            }
        });
    }

    // Actualizar Tabla (Solo 20 primeros)
    function updateTable(tableId, data) {
        const tbody = document.querySelector(`#${tableId} tbody`);
        tbody.innerHTML = '';
        
        const displayData = data.slice(0, 20);
        displayData.forEach(row => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${row.iteracion}</td>
                <td>${row.x_n}</td>
                <td>${row.r_n}</td>
            `;
            tbody.appendChild(tr);
        });
    }

    // Manejar Formularios
    async function handleFormSubmit(e, apiEndpoint, tableId, canvasId, chartRefVar, color) {
        e.preventDefault();
        const form = e.target;
        const data = {};
        
        // Recoger todos los inputs del formulario
        Array.from(form.elements).forEach(el => {
            if (el.tagName === 'INPUT') {
                const key = el.id.split('-')[1]; // ej: f1-x0 -> x0
                data[key] = el.value;
            }
        });
        // Siempre generamos 1000
        data.n = 1000;

        try {
            const response = await fetch(apiEndpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            const results = await response.json();

            updateTable(tableId, results);
            
            const freqs = calculateFrequencies(results);
            if (chartRefVar === 'chartFibo1') {
                chartFibo1 = renderChart(canvasId, 'Frecuencia', chartFibo1, freqs, color);
            } else if (chartRefVar === 'chartFibo2') {
                chartFibo2 = renderChart(canvasId, 'Frecuencia', chartFibo2, freqs, color);
            } else {
                chartCongruencial = renderChart(canvasId, 'Frecuencia', chartCongruencial, freqs, color);
            }

        } catch (error) {
            console.error('Error generando datos:', error);
        }
    }

    // Listeners
    document.getElementById('form-fibo-1').addEventListener('submit', (e) => {
        handleFormSubmit(e, '/api/generar/fibonacci', 'table-fibo-1', 'chart-fibo-1', 'chartFibo1', 'rgba(59, 130, 246, 0.6)');
    });

    document.getElementById('form-fibo-2').addEventListener('submit', (e) => {
        handleFormSubmit(e, '/api/generar/fibonacci', 'table-fibo-2', 'chart-fibo-2', 'chartFibo2', 'rgba(139, 92, 246, 0.6)');
    });

    document.getElementById('form-congruencial').addEventListener('submit', (e) => {
        handleFormSubmit(e, '/api/generar/congruencial', 'table-congruencial', 'chart-congruencial', 'chartCongruencial', 'rgba(16, 185, 129, 0.6)');
    });

    // Disparar las generaciones iniciales por defecto
    document.querySelector('#form-fibo-1 button').click();
    document.querySelector('#form-fibo-2 button').click();
    document.querySelector('#form-congruencial button').click();
});
