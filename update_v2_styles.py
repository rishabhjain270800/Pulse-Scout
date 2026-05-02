with open('index.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- v2 Massive Upgrade Styles --- */

/* Scroll Progress Bar */
.scroll-progress {
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: var(--primary);
    width: 0;
    z-index: 10001;
    transition: opacity 0.3s;
    opacity: 0;
}

/* Sticky Nav & Hamburger */
.navbar { position: fixed; top: 0; width: 100%; transition: all 0.3s; z-index: 10000; }
.navbar.scrolled { background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(0,0,0,0.05); }
.nav-link.active { color: var(--primary) !important; font-weight: 700; }
.pulse-btn { animation: pulse 4s infinite; }
@keyframes pulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(247, 148, 29, 0.4); }
    50% { box-shadow: 0 0 0 15px rgba(247, 148, 29, 0); }
}

.mobile-menu-toggle { display: none; background: none; border: none; font-size: 1.8rem; cursor: pointer; color: var(--text-main); }
.mobile-nav {
    position: fixed;
    top: 0;
    right: -300px;
    width: 300px;
    height: 100vh;
    background: white;
    padding: 6rem 2rem;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    box-shadow: -10px 0 30px rgba(0,0,0,0.1);
    transition: right 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    z-index: 9999;
}
.mobile-nav.open { right: 0; }
.mobile-nav a { font-size: 1.5rem; font-weight: 600; color: var(--text-main); text-decoration: none; }

/* India-specific Ticker Dot */
.ticker-item .dot { width: 8px; height: 8px; border-radius: 50%; display: inline-block; margin-right: 8px; }
.dot.orange { background: var(--primary); }
.dot.blue { background: #3b82f6; }
.dot.red { background: #ef4444; }
.dot.teal { background: #10b981; }

/* Problem Section */
.problem { padding: 8rem 0; background: #fff; }
.problem-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; margin-top: 4rem; }
.pain-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
.pain-card { padding: 2rem; background: #fff1f0; border-radius: 16px; text-align: center; }
.pain-card i { font-size: 2.5rem; color: #ef4444; margin-bottom: 1rem; }
.pain-card h4 { font-size: 1rem; color: #7c2d12; line-height: 1.4; }

.split-view { padding: 3rem; display: flex; align-items: center; justify-content: space-between; position: relative; }
.split-col { flex: 1; }
.split-col h5 { font-size: 1.2rem; margin-bottom: 2rem; text-transform: uppercase; letter-spacing: 1px; }
.split-col ul { list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1rem; }
.split-col ul li { font-weight: 600; display: flex; align-items: center; gap: 0.5rem; }
.split-arrow { font-size: 2rem; color: var(--text-muted); opacity: 0.5; }

/* Live Feed Section */
.live-feed { padding: 8rem 0; background: #0d0d1a; color: white; overflow: hidden; }
.live-feed h2 { color: white; }
.feed-layout { display: grid; grid-template-columns: 2fr 1fr; gap: 4rem; margin-top: 4rem; }
.feed-container-outer { position: relative; height: 500px; overflow: hidden; }
.feed-scroll-container {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    animation: feedScroll 40s linear infinite;
}
@keyframes feedScroll {
    from { transform: translateY(0); }
    to { transform: translateY(-50%); }
}
.mention-card { padding: 2rem; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; }
.mention-card .badge { padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; margin-bottom: 1rem; display: inline-block; }
.badge.pos { background: rgba(16, 185, 129, 0.2); color: #10b981; }
.badge.neg { background: rgba(239, 68, 68, 0.2); color: #ef4444; }
.badge.neu { background: rgba(156, 163, 175, 0.2); color: #9ca3af; }
.mention-card strong { font-size: 1.2rem; display: block; margin-bottom: 0.5rem; }
.mention-card p { font-size: 0.95rem; color: rgba(255,255,255,0.7); line-height: 1.6; }
.card-meta { display: flex; justify-content: space-between; margin-top: 1.5rem; font-size: 0.8rem; color: rgba(255,255,255,0.4); }
.feed-overlay-bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 150px;
    background: linear-gradient(to top, #0d0d1a, transparent);
    pointer-events: none;
    z-index: 2;
}

.live-stats-col { display: flex; flex-direction: column; gap: 1.5rem; }
.live-stat-card { padding: 2rem; }
.live-stat-card .label { font-size: 0.9rem; color: rgba(255,255,255,0.5); display: block; margin-bottom: 0.5rem; }
.live-stat-card strong { font-size: 2.2rem; color: var(--primary); }

/* Integrations Marquee */
.integrations { padding: 8rem 0; background: #f8f9fb; overflow: hidden; }
.marquee-wrapper { display: flex; flex-direction: column; gap: 1.5rem; margin-top: 3rem; }
.marquee { display: flex; gap: 1.5rem; animation: marquee 30s linear infinite; width: max-content; }
.marquee.row-2 { animation-direction: reverse; }
@keyframes marquee { from { transform: translateX(0); } to { transform: translateX(-50%); } }
.pill {
    padding: 0.8rem 1.5rem;
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 30px;
    display: flex;
    align-items: center;
    gap: 0.8rem;
    font-weight: 600;
    white-space: nowrap;
}
.pill .dot { width: 12px; height: 12px; border-radius: 50%; }

/* Pricing Section */
.pricing { padding: 8rem 0; background: #fff; }
.pricing-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2.5rem;
    margin-top: 4rem;
}
.pricing-card { padding: 3rem 2.5rem; text-align: center; display: flex; flex-direction: column; gap: 1.5rem; position: relative; }
.pricing-card.popular { border: 2px solid var(--primary); transform: scale(1.05); z-index: 10; }
.popular-badge {
    position: absolute;
    top: -15px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--primary);
    color: white;
    padding: 0.4rem 1.2rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
}
.pricing-card h3 { font-size: 1.8rem; color: var(--primary); }
.price { font-size: 1.2rem; font-weight: 700; color: var(--text-main); }
.pricing-card ul { list-style: none; padding: 0; text-align: left; display: flex; flex-direction: column; gap: 1rem; }
.pricing-card ul li { font-size: 0.95rem; display: flex; align-items: center; gap: 0.8rem; }
.pricing-card ul li i { color: #10b981; font-size: 1.2rem; }

/* Back to Top */
.back-to-top {
    position: fixed;
    bottom: 24px;
    right: 24px;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: var(--primary);
    color: white;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(247, 148, 29, 0.4);
    display: none;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    z-index: 9998;
    transition: all 0.3s;
}
.back-to-top:hover { transform: scale(1.1); box-shadow: 0 6px 20px rgba(247, 148, 29, 0.6); }

@media (max-width: 968px) {
    .problem-grid, .feed-layout { grid-template-columns: 1fr; }
    .mobile-menu-toggle { display: block; }
    .nav-links, .hide-mobile { display: none; }
    .pricing-card.popular { transform: scale(1); }
}
''')
