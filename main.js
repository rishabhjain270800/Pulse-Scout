document.addEventListener('DOMContentLoaded', () => {

    // 1. Scroll Reveal
    const revealEls = document.querySelectorAll('.reveal-el');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15 });
    revealEls.forEach(el => revealObserver.observe(el));

    // 2. Sticky Navbar
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (navbar) {
            navbar.classList.toggle('scrolled', window.scrollY > 60);
        }
    });

    // 3. Typing Animation
    const queries = [
        'Best SUVs under 15 lakhs India',
        'Maruti Suzuki competitor ads',
        'Top electric vehicles 2026',
        'Share of voice automotive',
        'Flipkart mobile sponsored ads',
        'Brand sentiment tracking tools',
        'Keyword ranking Google India'
    ];
    const typingText = document.getElementById('typingText');
    let queryIdx = 0;
    let charIdx = 0;
    let isDeleting = false;

    function typeLoop() {
        if (!typingText) return;
        const current = queries[queryIdx];

        if (!isDeleting) {
            typingText.textContent = current.slice(0, charIdx + 1);
            charIdx++;
            if (charIdx === current.length) {
                isDeleting = true;
                setTimeout(typeLoop, 2000);
                return;
            }
            setTimeout(typeLoop, 60 + Math.random() * 40);
        } else {
            typingText.textContent = current.slice(0, charIdx - 1);
            charIdx--;
            if (charIdx === 0) {
                isDeleting = false;
                queryIdx = (queryIdx + 1) % queries.length;
                setTimeout(typeLoop, 400);
                return;
            }
            setTimeout(typeLoop, 30);
        }
    }
    typeLoop();

    // 4. Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(a => {
        a.addEventListener('click', (e) => {
            const target = document.querySelector(a.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // 5. Globe dot particles (canvas-free, CSS-based)
    const globe = document.getElementById('heroGlobe');
    if (globe) {
        for (let i = 0; i < 40; i++) {
            const dot = document.createElement('span');
            dot.style.cssText = `
                position: absolute;
                width: ${3 + Math.random() * 6}px;
                height: ${3 + Math.random() * 6}px;
                background: rgba(255, 107, 0, ${0.15 + Math.random() * 0.4});
                border-radius: 50%;
                top: ${10 + Math.random() * 80}%;
                left: ${10 + Math.random() * 80}%;
                animation: dotFloat ${3 + Math.random() * 4}s ease-in-out infinite alternate;
                animation-delay: ${Math.random() * 3}s;
            `;
            globe.appendChild(dot);
        }

        // Add dotFloat keyframes
        const style = document.createElement('style');
        style.textContent = `
            @keyframes dotFloat {
                0% { transform: translate(0, 0) scale(1); opacity: 0.6; }
                100% { transform: translate(${Math.random() > 0.5 ? '' : '-'}${5 + Math.random() * 10}px, ${Math.random() > 0.5 ? '' : '-'}${5 + Math.random() * 10}px) scale(${0.8 + Math.random() * 0.4}); opacity: 1; }
            }
        `;
        document.head.appendChild(style);
    }
});
