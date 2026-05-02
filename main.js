document.addEventListener('DOMContentLoaded', () => {
    const primaryColor = '#F7941D';
    const darkBg = '#0d0d1a';

    // 1. IntersectionObserver for Impact Stats
    const stats = document.querySelectorAll('.metric-number');
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.getAttribute('data-target'));
                animateValue(entry.target, 0, target, 2000);
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    stats.forEach(stat => statsObserver.observe(stat));

    function animateValue(obj, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const easedProgress = 1 - Math.pow(1 - progress, 3); // easeOutCubic
            obj.innerText = Math.floor(easedProgress * (end - start) + start);
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }

    // 2. How it Works Step Animation
    const steps = document.querySelectorAll('.step-card');
    const stepsObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('animate');
                }, index * 150);
                stepsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });
    steps.forEach(step => stepsObserver.observe(step));

    // 3. Industry Tab Switching
    const industryTabs = document.querySelectorAll('.industry-tab');
    const industryCards = document.querySelectorAll('.industry-card');
    industryTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.getAttribute('data-industry');
            industryTabs.forEach(t => t.classList.remove('active'));
            industryCards.forEach(c => c.classList.remove('active'));
            tab.classList.add('active');
            const targetCard = document.getElementById(`${target}-card`);
            if (targetCard) targetCard.classList.add('active');
        });
    });

    // 4. Hero Charts Initialization
    const heroSovCtx = document.getElementById('heroSovChart');
    if (heroSovCtx) {
        new Chart(heroSovCtx, {
            type: 'doughnut',
            data: {
                labels: ['Brand A', 'Brand B', 'Brand C', 'Brand D', 'Others'],
                datasets: [{
                    data: [34, 22, 18, 15, 11],
                    backgroundColor: [primaryColor, '#ffb347', '#ffcc80', '#e0e0e0', '#9ca3af'],
                    borderWidth: 0
                }]
            },
            options: { 
                responsive: true, 
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                cutout: '70%'
            }
        });
    }

    const heroSentCtx = document.getElementById('heroSentimentChart');
    if (heroSentCtx) {
        new Chart(heroSentCtx, {
            type: 'line',
            data: {
                labels: Array.from({length: 14}, (_, i) => i + 1),
                datasets: [
                    { label: 'Positive', data: [65, 72, 68, 80, 85, 78, 90, 88, 92, 95, 90, 88, 94, 92], borderColor: '#3b82f6', tension: 0.4, pointRadius: 0 },
                    { label: 'Neutral', data: [20, 18, 22, 15, 10, 15, 8, 10, 5, 4, 8, 10, 5, 6], borderColor: '#9ca3af', tension: 0.4, pointRadius: 0 },
                    { label: 'Negative', data: [15, 10, 10, 5, 5, 7, 2, 2, 3, 1, 2, 2, 1, 2], borderColor: '#ef4444', tension: 0.4, pointRadius: 0 }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: { x: { display: false }, y: { display: false } }
            }
        });
    }

    // Creative Score Animation
    const scoreVal = document.querySelector('.score-value');
    if (scoreVal) {
        let count = 0;
        const interval = setInterval(() => {
            count++;
            scoreVal.innerText = count;
            const circle = document.getElementById('scoreCircle');
            if (circle) circle.style.background = `conic-gradient(${primaryColor} ${count}%, rgba(0,0,0,0.05) 0%)`;
            if (count >= 92) clearInterval(interval);
        }, 15);
    }

    // 5. Live Action SOV Chart
    let liveChart;
    const liveSovCtx = document.getElementById('liveSovChart');
    if (liveSovCtx) {
        const ctx = liveSovCtx.getContext('2d');
        liveChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['HDFC', 'Maruti', 'Flipkart', 'Zomato', 'Airtel'],
                datasets: [{
                    label: 'SOV %',
                    data: [32, 28, 25, 20, 15],
                    backgroundColor: [primaryColor, '#555', '#555', '#555', '#555'],
                    borderRadius: 8
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: {
                    x: { grid: { display: false }, ticks: { color: '#fff' }, max: 50 },
                    y: { grid: { display: false }, ticks: { color: '#fff' } }
                }
            }
        });

        setInterval(() => {
            liveChart.data.datasets[0].data = liveChart.data.datasets[0].data.map(val => {
                const change = (Math.random() * 6 - 3); // -3% to +3%
                return Math.max(5, Math.min(45, val + change));
            });
            liveChart.update();
            const timeAgo = document.getElementById('time-ago');
            if (timeAgo) timeAgo.innerText = '0';
        }, 3000);

        setInterval(() => {
            const span = document.getElementById('time-ago');
            if (span) span.innerText = parseInt(span.innerText) + 1;
        }, 1000);
    }

    // 6. ROI Calculator v2
    const spendSlider = document.getElementById('ad-spend');
    const toolsSlider = document.getElementById('tools-cost');
    const spendDisplay = document.getElementById('spend-display');
    const toolsDisplay = document.getElementById('tools-display');
    const mSaving = document.getElementById('m-saving');
    const aRoi = document.getElementById('a-roi');
    const pPeriod = document.getElementById('p-period');

    let roiChart;
    const roiChartCtx = document.getElementById('roiChart');
    if (roiChartCtx) {
        roiChart = new Chart(roiChartCtx, {
            type: 'bar',
            data: {
                labels: ['Current Wasted', 'Pulse Scout Saving', 'Net ROI'],
                datasets: [{
                    data: [10000, 12500, 10500],
                    backgroundColor: ['rgba(239, 68, 68, 0.8)', 'rgba(16, 185, 129, 0.8)', 'rgba(59, 130, 246, 0.8)'], borderColor: ['#ef4444', '#10b981', '#3b82f6'], borderWidth: 1,
                    borderRadius: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: { y: { beginAtZero: true } }
            }
        });
    }

    function updateROI() {
        if (!spendSlider || !toolsSlider) return;
        const spend = parseInt(spendSlider.value);
        const tools = parseInt(toolsSlider.value);
        if (spendDisplay) spendDisplay.innerText = spend.toLocaleString();
        if (toolsDisplay) toolsDisplay.innerText = tools.toLocaleString();

        const wasted = spend * 0.15;
        const saving = spend * 0.25;
        const net = saving - tools;

        if (mSaving) mSaving.innerText = saving.toLocaleString();
        if (aRoi) aRoi.innerText = (net * 12).toLocaleString();
        if (pPeriod) pPeriod.innerText = Math.max(1, Math.ceil(tools / (saving / 4)));

        if (roiChart) {
            roiChart.data.datasets[0].data = [wasted, saving, net];
            roiChart.update();
        }
    }

    if (spendSlider) {
        spendSlider.addEventListener('input', updateROI);
        toolsSlider.addEventListener('input', updateROI);
        updateROI();
    }

    // 7. Interactive Capabilities Strip Logic
    const stripTabs = document.querySelectorAll('.strip-tab');
    const stripPreviews = document.querySelectorAll('.strip-preview');
    stripTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.getAttribute('data-tab');
            stripTabs.forEach(t => t.classList.remove('active'));
            stripPreviews.forEach(p => p.classList.remove('active'));
            tab.classList.add('active');
            const targetPreview = document.getElementById(`${target}-preview`);
            if (targetPreview) targetPreview.classList.add('active');
        });
    });

    // Strip Previews Charts
    const stripDisplayCtx = document.getElementById('stripDisplayChart');
    if (stripDisplayCtx) {
        new Chart(stripDisplayCtx, {
            type: 'bar',
            data: {
                labels: ['Brand A', 'Brand B', 'Brand C', 'Others'],
                datasets: [{ data: [45, 25, 20, 10], backgroundColor: primaryColor }]
            },
            options: { indexAxis: 'y', plugins: { legend: { display: false } } }
        });
    }
    const stripContentCtx = document.getElementById('stripContentChart');
    if (stripContentCtx) {
        new Chart(stripContentCtx, {
            type: 'doughnut',
            data: {
                labels: ['Pos', 'Neu', 'Neg'],
                datasets: [{ data: [68, 17, 15], backgroundColor: ['#10b981', '#9ca3af', '#ef4444'] }]
            },
            options: { maintainAspectRatio: false, cutout: '70%', plugins: { legend: { position: 'right' } } }
        });
    }
    const stripCreativeCtx = document.getElementById('stripCreativeChart');
    if (stripCreativeCtx) {
        new Chart(stripCreativeCtx, {
            type: 'bar',
            data: {
                labels: ['Awareness', 'Headline', 'Brand', 'CTA', 'Perf'],
                datasets: [{ data: [88, 94, 91, 89, 92], backgroundColor: primaryColor }]
            },
            options: { plugins: { legend: { display: false } }, scales: { y: { beginAtZero: true, max: 100 } } }
        });
    }

    // 8. Module Previews Initialization
    const displayPrevCtx = document.getElementById('displayPreviewChart');
    if (displayPrevCtx) {
        new Chart(displayPrevCtx, {
            type: 'bar',
            data: {
                labels: ['P1', 'P2', 'P3', 'P4', 'P5'],
                datasets: [{ data: [30, 25, 20, 15, 10], backgroundColor: primaryColor }]
            },
            options: { indexAxis: 'y', plugins: { legend: { display: false } }, scales: { x: { display: false }, y: { display: false } } }
        });
    }
    const sentimentPrevCtx = document.getElementById('sentimentPreviewChart');
    if (sentimentPrevCtx) {
        new Chart(sentimentPrevCtx, {
            type: 'doughnut',
            data: {
                labels: ['Pos', 'Neu', 'Neg'],
                datasets: [{ data: [68, 17, 15], backgroundColor: ['#10b981', '#9ca3af', '#ef4444'] }]
            },
            options: { plugins: { legend: { display: false } }, cutout: '60%' }
        });
    }
    const creativePrevCtx = document.getElementById('creativePreviewChart');
    if (creativePrevCtx) {
        new Chart(creativePrevCtx, {
            type: 'radar',
            data: {
                labels: ['AW', 'HL', 'BR', 'CTA', 'PF'],
                datasets: [{ data: [85, 90, 75, 80, 95], backgroundColor: 'rgba(247, 148, 29, 0.2)', borderColor: primaryColor }]
            },
            options: { plugins: { legend: { display: false } }, scales: { r: { ticks: { display: false } } } }
        });
    }

    // 9. Mouse Glow & Global Effects
    const mouseGlow = document.getElementById('mouse-glow');
    if (mouseGlow) {
        window.addEventListener('mousemove', (e) => {
            mouseGlow.style.left = e.clientX + 'px';
            mouseGlow.style.top = e.clientY + 'px';
        });
    }
});

// Modal Logic (Global)
function openModal() { 
    const modal = document.getElementById('roiModal');
    if (modal) modal.style.display = 'block'; 
}
function closeModal() { 
    const modal = document.getElementById('roiModal');
    if (modal) modal.style.display = 'none'; 
}
window.onclick = function(event) {
    const modal = document.getElementById('roiModal');
    if (event.target == modal) closeModal();
}

    // --- v2 Upgrade Logic ---

    // 10. Scroll Progress Bar
    const scrollProgress = document.getElementById('scrollProgress');
    window.addEventListener('scroll', () => {
        const h = document.documentElement;
        const b = document.body;
        const st = 'scrollTop';
        const sh = 'scrollHeight';
        const percent = (h[st] || b[st]) / ((h[sh] || b[sh]) - h.clientHeight) * 100;
        if (scrollProgress) {
            scrollProgress.style.width = percent + '%';
            scrollProgress.style.opacity = (h[st] || b[st]) > 100 ? '1' : '0';
        }

        // Sticky Nav logic
        const nav = document.getElementById('navbar');
        if (nav) {
            if (window.scrollY > 50) nav.classList.add('scrolled');
            else nav.classList.remove('scrolled');
        }

        // Back to top
        const btt = document.getElementById('backToTop');
        if (btt) {
            if (window.scrollY > 400) btt.style.display = 'flex';
            else btt.style.display = 'none';
        }
    });

    // 11. Mobile Menu Toggle
    const menuToggle = document.getElementById('menuToggle');
    const mobileNav = document.getElementById('mobileNav');
    if (menuToggle && mobileNav) {
        menuToggle.addEventListener('click', () => {
            mobileNav.classList.toggle('open');
            const icon = menuToggle.querySelector('i');
            if (mobileNav.classList.contains('open')) {
                icon.className = 'ph ph-x';
            } else {
                icon.className = 'ph ph-list';
            }
        });

        // Close menu on link click
        mobileNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileNav.classList.remove('open');
                menuToggle.querySelector('i').className = 'ph ph-list';
            });
        });
    }

    // 12. Active Nav Highlighting (IntersectionObserver)
    const navSections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    const navObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === '#' + id) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, { threshold: 0.3 });
    navSections.forEach(section => navObserver.observe(section));

    // 13. Live Feed Random Stats
    const statMentions = document.getElementById('stat-mentions');
    const statSentiment = document.getElementById('stat-sentiment');
    const statTrending = document.getElementById('stat-trending');
    const trendingKeywords = ['#FMCG', '#AutoIndia', '#Fintech', '#EcomSales', '#BrandSafety', '#AdIntelligence'];

    setInterval(() => {
        if (statMentions) {
            let val = parseInt(statMentions.innerText.replace(/,/g, ''));
            val += Math.floor(Math.random() * 20 - 5);
            statMentions.innerText = val.toLocaleString();
        }
        if (statSentiment) {
            let val = parseInt(statSentiment.innerText);
            val += Math.floor(Math.random() * 3 - 1);
            statSentiment.innerText = Math.max(50, Math.min(95, val)) + '%';
        }
        if (Math.random() > 0.7 && statTrending) {
            statTrending.innerText = trendingKeywords[Math.floor(Math.random() * trendingKeywords.length)];
        }
    }, 5000);

    // 14. Smooth Scroll for all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Back to top click
    const btt = document.getElementById('backToTop');
    if (btt) {
        btt.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
