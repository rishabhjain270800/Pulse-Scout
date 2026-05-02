with open('main.js', 'a', encoding='utf-8') as f:
    f.write('''
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
''')
