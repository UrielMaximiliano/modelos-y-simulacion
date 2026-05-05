document.addEventListener('DOMContentLoaded', () => {
    // Referencias a los gráficos
    const charts = {};

    // Función auxiliar para agrupar datos en intervalos (Histograma)
    function calculateFrequencies(data, numBins = 10) {
        const bins = new Array(numBins).fill(0);
        const binSize = 1.0 / numBins;

        data.forEach(item => {
            const val = item.r_n_raw;
            let binIndex = Math.floor(val / binSize);
            if (binIndex >= numBins) binIndex = numBins - 1; // Para valores que sean exactamente 1.0
            if (binIndex < 0) binIndex = 0;
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
    function renderChart(canvasId, title, frequencies, color) {
        const ctx = document.getElementById(canvasId).getContext('2d');
        
        if (charts[canvasId]) {
            charts[canvasId].destroy();
        }

        charts[canvasId] = new Chart(ctx, {
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
                        grid: { color: 'rgba(255, 255, 255, 0.05)' },
                        ticks: { color: 'rgba(255, 255, 255, 0.5)' }
                    },
                    x: {
                        grid: { display: false },
                        ticks: { color: 'rgba(255, 255, 255, 0.5)' }
                    }
                }
            }
        });
    }

    // Actualizar Tabla (Solo 20 primeros)
    function updateTable(tableId, data) {
        const tbody = document.querySelector(`#${tableId} tbody`);
        if (!tbody) return;
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

    // Manejar Formularios Generico
    async function handleFormSubmit(e) {
        e.preventDefault();
        const form = e.target;
        const data = {};
        
        // Recoger todos los inputs del formulario
        Array.from(form.elements).forEach(el => {
            if (el.tagName === 'INPUT' && el.id) {
                // extrae el nombre ignorando prefijos. Ej: gen-x0 -> x0
                const parts = el.id.split('-');
                const key = parts[parts.length - 1]; 
                data[key] = el.value;
            }
        });

        const apiEndpoint = form.getAttribute('data-endpoint') || form.dataset.endpoint;
        
        // Determinar qué IDs usar para la tabla y gráfico
        let tableId = 'table-generico';
        let canvasId = 'chart-generico';
        let color = 'rgba(16, 185, 129, 0.6)';

        if (form.id === 'form-fibo-1') {
            tableId = 'table-fibo-1'; canvasId = 'chart-fibo-1'; color = 'rgba(59, 130, 246, 0.6)';
        } else if (form.id === 'form-fibo-2') {
            tableId = 'table-fibo-2'; canvasId = 'chart-fibo-2'; color = 'rgba(139, 92, 246, 0.6)';
        } else if (form.id === 'form-congruencial') {
            tableId = 'table-congruencial'; canvasId = 'chart-congruencial'; color = 'rgba(16, 185, 129, 0.6)';
        } else if (form.id === 'form-generico') {
             tableId = 'table-generico'; canvasId = 'chart-generico'; color = 'rgba(16, 185, 129, 0.6)';
        }

        try {
            const response = await fetch(apiEndpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            const results = await response.json();

            updateTable(tableId, results);
            const freqs = calculateFrequencies(results);
            renderChart(canvasId, 'Frecuencia', freqs, color);

        } catch (error) {
            console.error('Error generando datos:', error);
        }
    }

    // Vincular todos los formularios de la página (dinámico)
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', handleFormSubmit);
        // Autodisparar si hay un boton de submit
        const submitBtn = form.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.click();
        }
    });

});
