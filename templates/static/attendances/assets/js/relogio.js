function updateClock() {
    const now = new Date();
    
    // Data
    const day = String(now.getDate()).padStart(2, '0');
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const year = now.getFullYear();
    const date = `${day}/${month}/${year}`;
    
    // Hora
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    const time = `${hours}:${minutes}:${seconds}`;
    
    document.getElementById('clock').textContent = time;
    document.getElementById('date').textContent = date;
}

// Atualiza o relógio a cada segundo
setInterval(updateClock, 1000);

// Atualiza imediatamente ao carregar a página
updateClock();