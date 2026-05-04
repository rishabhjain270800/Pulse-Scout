document.addEventListener('DOMContentLoaded', () => {
    const primaryColor = '#FF6B00';
    const accentColor = '#FF8533';
    const darkBg = '#0A0A0B';
    const textColor = '#FFFFFF';
    const mutedColor = '#A0A0A0';

    // Set Chart.js defaults for dark mode
    if (typeof Chart !== 'undefined') {
        Chart.defaults.color = mutedColor;
        Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.1)';
        Chart.defaults.font.family = "'Inter', sans-serif";
    }

    // 1. Scroll Reveal Logic
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15 });

    document.querySelectorAll('section').forEach(section => {
        revealObserver.observe(section);
    });

    // 2. Impact Counters
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

    // 3. Demo Tab Switching
    const demoTabs = document.querySelectorAll('.demo-tab');
    const demoContents = document.querySelectorAll('.demo-content');
    demoTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.getAttribute('data-tab');
            demoTabs.forEach(t => t.classList.remove('active'));
            demoContents.forEach(c => c.classList.remove('active'));
            tab.classList.add('active');
            const targetContent = document.getElementById(`${target}-demo`);
            if (targetContent) targetContent.classList.add('active');
            
            // Re-init charts if needed
            if (target === 'search') initSearchChart();
            if (target === 'content') initContentChart();
        });
    });

    // 4. Repo Search Simulation
    const repoInput = document.querySelector('.repo-search-bar input');
    const repoBtn = document.querySelector('.repo-search-bar button');
    const repoItems = document.querySelectorAll('.repo-item');

    if (repoBtn && repoInput) {
        repoBtn.addEventListener('click', () => {
            const query = repoInput.value.toLowerCase();
            repoItems.forEach(item => {
                const text = item.innerText.toLowerCase();
                if (text.includes(query)) {
                    item.style.display = 'block';
                    item.style.animation = 'fadeIn 0.5s ease';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    }

    // 5. Hero Charts
    const heroSovCtx = document.getElementById('heroSovChart');
    if (heroSovCtx) {
        new Chart(heroSovCtx, {
            type: 'doughnut',
            data: {
                labels: ['Brand A', 'Brand B', 'Brand C', 'Others'],
                datasets: [{
                    data: [42, 28, 18, 12],
                    backgroundColor: [primaryColor, '#FF8533', '#FFA366', '#333'],
                    borderWidth: 0
                }]
            },
            options: { 
                responsive: true, 
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                cutout: '75%'
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
                    { label: 'Positive', data: [65, 72, 68, 80, 85, 78, 90, 88, 92, 95, 90, 88, 94, 92], borderColor: '#3b82f6', tension: 0.4, pointRadius: 0, fill: false },
                    { label: 'Negative', data: [15, 10, 10, 5, 5, 7, 2, 2, 3, 1, 2, 2, 1, 2], borderColor: '#ef4444', tension: 0.4, pointRadius: 0, fill: false }
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
            if (circle) circle.style.background = `conic-gradient(${primaryColor} ${count}%, rgba(255,255,255,0.05) 0%)`;
            if (count >= 92) clearInterval(interval);
        }, 15);
    }
    const kwChartCtx = document.getElementById('keywordDeepChart');
    if (kwChartCtx) {
        new Chart(kwChartCtx, {
            type: 'line',
            data: {
                labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6'],
                datasets: [{
                    label: 'Keyword Rank',
                    data: [12, 8, 5, 3, 2, 1],
                    borderColor: primaryColor,
                    backgroundColor: 'rgba(255, 107, 0, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: { reverse: true, min: 1, max: 15 }
                },
                plugins: { legend: { display: false } }
            }
        });
    }

    const compChartCtx = document.getElementById('compDeepChart');
    if (compChartCtx) {
        new Chart(compChartCtx, {
            type: 'bar',
            data: {
                labels: ['Display', 'Search', 'Social', 'News'],
                datasets: [{
                    label: 'Share of Voice',
                    data: [65, 42, 58, 35],
                    backgroundColor: primaryColor,
                    borderRadius: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } }
            }
        });
    }

    // 7. Mouse Glow & Global Effects
    const mouseGlow = document.getElementById('mouse-glow');
    if (mouseGlow) {
        window.addEventListener('mousemove', (e) => {
            mouseGlow.style.left = e.clientX + 'px';
            mouseGlow.style.top = e.clientY + 'px';
        });
    }

    // Magnetic Buttons
    const magneticBtns = document.querySelectorAll('.magnetic');
    magneticBtns.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
        });
        btn.addEventListener('mouseleave', () => {
            btn.style.transform = `translate(0, 0)`;
        });
    });

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
    }

    // Back to top click
    const btt = document.getElementById('backToTop');
    if (btt) {
        btt.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});

// Modal Logic
function openModal() { 
    const modal = document.getElementById('roiModal');
    if (modal) modal.style.display = 'block'; 
}
function closeModal() { 
    const modal = document.getElementById('roiModal');
    if (modal) modal.style.display = 'none'; 
}
