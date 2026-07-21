document.addEventListener('DOMContentLoaded', function() {
    const gatilhos = document.querySelectorAll('.gatilho-select');
    
    gatilhos.forEach(select => {
        select.addEventListener('change', function() {
            const codigoGatilho = this.getAttribute('data-codigo');
            const cadContainer = document.getElementById('sub_cad_' + codigoGatilho);
            
            if (cadContainer) {
                if (this.value === 'SIM') {
                    cadContainer.style.display = 'block';
                } else {
                    cadContainer.style.display = 'none';
                }
            }
        });
    });
});