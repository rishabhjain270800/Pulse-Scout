// Navbar Scroll Effect
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Number Counter Animation for Impact Section
const animateNumbers = () => {
    const numbers = document.querySelectorAll('.metric-number');
    const speed = 200; // lower is faster

    numbers.forEach(num => {
        const target = +num.getAttribute('data-target');
        const count = +num.innerText;
        const inc = target / speed;

        if (count < target) {
            num.innerText = Math.ceil(count + inc);
            setTimeout(animateNumbers, 20);
        } else {
            num.innerText = target;
        }
    });
};

// Intersection Observer for Animations on Scroll
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            if (entry.target.classList.contains('impact')) {
                animateNumbers();
            }
            // Add a simple fade-in class if we want to expand animations
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe impact section for number counting
const impactSection = document.querySelector('.impact');
if (impactSection) {
    observer.observe(impactSection);
}

// Optional: Initial state for scroll animations
document.querySelectorAll('.module-card, .metric-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});

// Mouse Glow Tracking
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
        btn.style.transform = 'translate(0px, 0px)';
    });
});

// Dashboard Mockup 3D Parallax
const mockup = document.querySelector('.dashboard-mockup');
if (mockup) {
    window.addEventListener('mousemove', (e) => {
        const xAxis = (window.innerWidth / 2 - e.clientX) / 25;
        const yAxis = (window.innerHeight / 2 - e.clientY) / 25;
        mockup.style.transform = `perspective(1000px) rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
    });
    
    window.addEventListener('mouseleave', () => {
        mockup.style.transform = perspective(1000px) rotateY(-5deg) rotateX(5deg);
    });
}

// ROI Calculator Logic
const spendSlider = document.getElementById('ad-spend');
const spendDisplay = document.getElementById('spend-display');
const savingsDisplay = document.getElementById('savings-display');

if (spendSlider && spendDisplay && savingsDisplay) {
    spendSlider.addEventListener('input', (e) => {
        const val = parseInt(e.target.value);
        spendDisplay.innerText = val.toLocaleString();
        
        // Calculation: 20% efficiency gain (average of 15-25%)
        const savings = Math.ceil(val * 0.20);
        savingsDisplay.innerText = savings.toLocaleString();
    });
}
