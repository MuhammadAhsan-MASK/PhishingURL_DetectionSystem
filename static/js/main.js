document.addEventListener('DOMContentLoaded', () => {
    const scanBtn = document.getElementById('scanBtn');
    const urlInput = document.getElementById('urlInput');
    const results = document.getElementById('results');
    const loader = document.getElementById('loader');
    const statusCard = document.getElementById('statusCard');
    const statusIcon = document.getElementById('statusIcon');
    const statusTitle = document.getElementById('statusTitle');
    const statusDesc = document.getElementById('statusDesc');
    const confidenceFill = document.getElementById('confidenceFill');
    const confidenceText = document.getElementById('confidenceText');
    const featuresGrid = document.getElementById('featuresGrid');

    const featureLabels = {
        'url_length': 'URL Length',
        'have_at': 'Contains @ Symbol',
        'double_slash_redirect': 'Redirect Check',
        'prefix_suffix': 'Domain Hyphens',
        'sub_domain': 'Subdomains Count',
        'https': 'SSL / HTTPS',
        'domain_age': 'Domain Age',
        'have_ip': 'IP Address Host',
        'short_url': 'URL Shortener'
    };

    scanBtn.addEventListener('click', performScan);
    urlInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') performScan();
    });

    async function performScan() {
        const url = urlInput.value.trim();
        if (!url) return;

        // Reset & Show loading
        results.style.display = 'none';
        loader.style.display = 'block';
        scanBtn.disabled = true;

        try {
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url })
            });

            const data = await response.json();
            
            if (data.error) {
                alert(data.error);
                return;
            }

            displayResults(data);
        } catch (error) {
            console.error('Scan failed:', error);
            alert('An error occurred during scanning. Please check your connection.');
        } finally {
            loader.style.display = 'none';
            scanBtn.disabled = false;
        }
    }

    function displayResults(data) {
        const isPhishing = data.prediction === 'phishing';
        
        statusCard.className = 'status-card ' + (isPhishing ? 'phishing' : 'safe');
        statusIcon.innerHTML = isPhishing ? '<i class="fas fa-exclamation-triangle"></i>' : '<i class="fas fa-check-circle"></i>';
        statusTitle.innerText = isPhishing ? 'Phishing Detected!' : 'Safe Website';
        statusDesc.innerText = isPhishing 
            ? 'Warning: Our AI has identified high-risk indicators on this URL.' 
            : 'No malicious indicators found. This website appears to be legitimate.';
        
        confidenceText.innerText = data.confidence + '%';
        confidenceFill.style.width = '0%';
        setTimeout(() => {
            confidenceFill.style.width = data.confidence + '%';
        }, 100);

        // Populate features
        featuresGrid.innerHTML = '';
        for (const [key, value] of Object.entries(data.features)) {
            if (featureLabels[key]) {
                const item = document.createElement('div');
                item.className = 'feature-item';
                
                let displayValue = value;
                if (typeof value === 'number' && (key === 'have_at' || key === 'https' || key === 'have_ip' || key === 'short_url')) {
                    displayValue = value === 1 ? 'Yes' : 'No';
                }
                
                item.innerHTML = `
                    <div class="feature-label">${featureLabels[key]}</div>
                    <div class="feature-value">${displayValue}</div>
                `;
                featuresGrid.appendChild(item);
            }
        }

        results.style.display = 'block';
        results.scrollIntoView({ behavior: 'smooth' });
    }
});
