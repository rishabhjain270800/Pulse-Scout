with open('index.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- Massive Upgrade Styles --- */

/* Hero Widgets */
.hero-visual { display: flex; align-items: center; justify-content: center; }
.hero-widgets {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    width: 100%;
}
.hero-widget {
    padding: 1.2rem;
    height: 220px;
    display: flex;
    flex-direction: column;
}
.widget-header {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-muted);
    margin-bottom: 1rem;
}
.score-widget { grid-column: span 2; height: 180px; }
.score-container { display: flex; align-items: center; gap: 3rem; }
.circular-progress {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background: conic-gradient(var(--primary) 0%, rgba(255,255,255,0.05) 0%);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}
.circular-progress::before {
    content: "";
    position: absolute;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: #ffffff; /* Match light theme bg */
}
.score-value { position: relative; font-size: 2rem; font-weight: 800; color: var(--text-main); }
.sub-scores { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; flex: 1; }
.sub-score { display: flex; flex-direction: column; }
.sub-score span { font-size: 0.75rem; color: var(--text-muted); }
.sub-score strong { font-size: 1.1rem; color: var(--primary); }

/* How It Works */
.how-it-works { padding: 8rem 0; background: #f8f9fb; }
.steps-flow {
    display: flex;
    justify-content: space-between;
    position: relative;
    margin-top: 4rem;
}
.connecting-line {
    position: absolute;
    top: 30px;
    left: 10%;
    width: 80%;
    height: 2px;
    background: repeating-linear-gradient(to right, var(--primary) 0, var(--primary) 10px, transparent 10px, transparent 20px);
    z-index: 1;
    background-size: 200% 100%;
    animation: dash 20s linear infinite;
}
@keyframes dash { to { background-position: 100% 0; } }
.step-card {
    flex: 1;
    text-align: center;
    padding: 0 2rem;
    position: relative;
    z-index: 2;
    opacity: 0;
    transform: translateY(20px);
}
.step-card.animate { opacity: 1; transform: translateY(0); transition: all 0.6s ease; }
.step-icon {
    width: 60px;
    height: 60px;
    background: var(--primary);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    margin: 0 auto 1.5rem;
    box-shadow: 0 0 20px rgba(247, 148, 29, 0.4);
}

/* Testimonials */
.testimonials { padding: 8rem 0; }
.testimonials-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2.5rem;
    margin-bottom: 5rem;
}
.testimonial-card { padding: 2.5rem; display: flex; flex-direction: column; gap: 1.5rem; }
.quote { font-style: italic; font-size: 1.1rem; color: var(--text-main); line-height: 1.7; }
.author { display: flex; align-items: center; gap: 1rem; }
.avatar {
    width: 50px;
    height: 50px;
    background: var(--primary);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
}
.info strong { display: block; font-size: 1rem; }
.info span { font-size: 0.85rem; color: var(--text-muted); }
.rating { color: #f59e0b; font-size: 1.2rem; }
.logo-strip {
    display: flex;
    justify-content: center;
    gap: 3rem;
    flex-wrap: wrap;
    opacity: 0.5;
    margin-top: 2rem;
}
.logo-box { padding: 1rem 2rem; border: 1px solid var(--border-color); border-radius: 8px; font-weight: 700; color: var(--text-muted); }

/* Industry Tabs */
.industry { padding: 8rem 0; background: #f8f9fb; }
.industry-tabs {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 3rem;
}
.industry-tab {
    padding: 0.8rem 2rem;
    border-radius: 30px;
    border: none;
    background: transparent;
    color: var(--text-muted);
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
}
.industry-tab.active { background: white; color: var(--primary); box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
.industry-card { display: none; padding: 4rem; text-align: center; max-width: 800px; margin: 0 auto; flex-direction: column; gap: 2rem; }
.industry-card.active { display: flex; animation: fadeIn 0.5s ease; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.card-icon { font-size: 4rem; color: var(--primary); }
.card-story { font-size: 1.4rem; font-weight: 500; color: var(--text-main); }
.card-footer { display: flex; align-items: center; justify-content: center; gap: 2rem; }
.metric-badge { background: rgba(247, 148, 29, 0.1); color: var(--primary); padding: 0.5rem 1.2rem; border-radius: 20px; font-weight: 700; }

/* Live Action Section */
.live-action { padding: 8rem 0; background: #0d0d1a; color: white; }
.live-action .section-header h2 { color: white; }
.live-chart-wrapper { padding: 3rem; position: relative; margin-top: 3rem; }
.timestamp { position: absolute; bottom: 1rem; right: 2rem; font-size: 0.8rem; color: rgba(255,255,255,0.4); }
.insight-chips { display: flex; justify-content: center; gap: 1rem; margin-top: 2rem; flex-wrap: wrap; }
.insight-chip { background: rgba(255,255,255,0.05); padding: 0.8rem 1.5rem; border-radius: 30px; border: 1px solid rgba(255,255,255,0.1); font-size: 0.9rem; }
.insight-chip.highlight { border-color: var(--primary); color: var(--primary); box-shadow: 0 0 15px rgba(247, 148, 29, 0.2); }

/* ROI Calculator v2 */
.calc-chart { display: flex; flex-direction: column; gap: 2rem; }
.m-card { background: white; padding: 1.5rem; border-radius: 12px; border: 1px solid var(--border-color); flex: 1; text-align: center; }
.m-card strong { font-size: 1.8rem; color: var(--primary); display: block; }
.m-card span { font-size: 0.8rem; color: var(--text-muted); }
.metric-cards { display: flex; gap: 1rem; }
.footnote { font-size: 0.8rem; color: var(--text-muted); font-style: italic; }

/* Modal */
.modal { display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); backdrop-filter: blur(5px); }
.modal-content { position: relative; margin: 10% auto; padding: 3rem; width: 400px; text-align: center; }
.close { position: absolute; right: 1.5rem; top: 1rem; font-size: 2rem; cursor: pointer; }
.form-group { margin-bottom: 1.5rem; }
.form-group input { width: 100%; padding: 1rem; border-radius: 8px; border: 1px solid var(--border-color); }

/* Comparison v2 */
.comparison-table th.highlight { background: var(--primary); color: white; }
.footnote { opacity: 0.7; }
''')
