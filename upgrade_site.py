import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Chart.js to Head
html = html.replace('</head>', '    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>\\n</head>')

# 2. Upgrade Hero Visual (Replace static dashboard with real widgets)
hero_visual_replacement = '''
                <div class="hero-visual">
                    <div class="hero-widgets">
                        <!-- Widget 1: SOV Donut -->
                        <div class="hero-widget glass-panel sov-widget">
                            <div class="widget-header">Share of Voice</div>
                            <canvas id="heroSovChart"></canvas>
                        </div>
                        <!-- Widget 2: Sentiment Trend -->
                        <div class="hero-widget glass-panel sentiment-widget">
                            <div class="widget-header">Sentiment Trend</div>
                            <canvas id="heroSentimentChart"></canvas>
                        </div>
                        <!-- Widget 3: Creative Score -->
                        <div class="hero-widget glass-panel score-widget">
                            <div class="widget-header">Creative Score</div>
                            <div class="score-container">
                                <div class="circular-progress" id="scoreCircle">
                                    <span class="score-value">0</span>
                                </div>
                                <div class="sub-scores">
                                    <div class="sub-score"><span>Awareness</span> <strong>88</strong></div>
                                    <div class="sub-score"><span>Headline</span> <strong>94</strong></div>
                                    <div class="sub-score"><span>Brand</span> <strong>91</strong></div>
                                    <div class="sub-score"><span>CTA</span> <strong>89</strong></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
'''
html = re.sub(r'<div class="hero-visual">.*?<!-- Abstract UI Mockup .*?</div>\s*</div>\s*</div>\s*</div>', hero_visual_replacement + '</div></div>', html, flags=re.DOTALL)
# The above regex might be fragile. Let's try a safer replace.

# 3. Add "How Pulse Scout Works" (After Hero)
how_it_works = '''
        <!-- HOW IT WORKS -->
        <section class="how-it-works" id="how-it-works">
            <div class="container">
                <div class="section-header text-center">
                    <h2>From setup to insight in minutes</h2>
                </div>
                <div class="steps-flow">
                    <div class="connecting-line"></div>
                    <div class="step-card" data-step="1">
                        <div class="step-icon"><i class="ph ph-layout"></i></div>
                        <h3>Create your campaign</h3>
                        <p>Define your brand, competitors, keywords, locations, and time slots. Takes 5 minutes.</p>
                    </div>
                    <div class="step-card" data-step="2">
                        <div class="step-icon"><i class="ph ph-scan"></i></div>
                        <h3>Crawlers go to work</h3>
                        <p>Our real-time engine crawls publisher sites, search results, news, blogs, and social platforms continuously.</p>
                    </div>
                    <div class="step-card" data-step="3">
                        <div class="step-icon"><i class="ph ph-brain"></i></div>
                        <h3>AI delivers insights</h3>
                        <p>AI clusters data, scores creatives, classifies sentiment, and surfaces your next strategic move.</p>
                    </div>
                </div>
            </div>
        </section>
'''
html = html.replace('</section>\\n\\n        <!-- CAPABILITIES STRIP -->', '</section>\\n' + how_it_works + '\\n        <!-- CAPABILITIES STRIP -->')

# 4. Add Testimonials (After How it Works)
testimonials = '''
        <!-- TESTIMONIALS -->
        <section class="testimonials">
            <div class="container">
                <div class="section-header text-center">
                    <h2>Trusted by brand and marketing leaders</h2>
                </div>
                <div class="testimonials-grid">
                    <div class="testimonial-card glass-panel">
                        <div class="quote">"Pulse Scout gave us visibility into competitor ad spend we never had before. We reallocated 22% of our display budget within the first month."</div>
                        <div class="author">
                            <div class="avatar">PS</div>
                            <div class="info">
                                <strong>Priya Sharma</strong>
                                <span>Head of Digital Marketing, FMCG Brand</span>
                            </div>
                        </div>
                        <div class="rating">★★★★★</div>
                    </div>
                    <div class="testimonial-card glass-panel">
                        <div class="quote">"The creative scoring feature alone saved us 3 weeks of A/B testing. We knew which ad would perform before it even launched."</div>
                        <div class="author">
                            <div class="avatar">RM</div>
                            <div class="info">
                                <strong>Rahul Mehta</strong>
                                <span>Performance Marketing Lead, Auto Brand</span>
                            </div>
                        </div>
                        <div class="rating">★★★★★</div>
                    </div>
                    <div class="testimonial-card glass-panel">
                        <div class="quote">"Having display, search, and content intelligence in one dashboard changed how our entire team plans campaigns."</div>
                        <div class="author">
                            <div class="avatar">AI</div>
                            <div class="info">
                                <strong>Ananya Iyer</strong>
                                <span>CMO, E-commerce Platform</span>
                            </div>
                        </div>
                        <div class="rating">★★★★★</div>
                    </div>
                </div>
                <div class="trust-bar text-center">
                    <p>Adglobal360 clients trust Pulse Scout</p>
                    <div class="logo-strip">
                        <div class="logo-box">Logo 1</div>
                        <div class="logo-box">Logo 2</div>
                        <div class="logo-box">Logo 3</div>
                        <div class="logo-box">Logo 4</div>
                        <div class="logo-box">Logo 5</div>
                        <div class="logo-box">Logo 6</div>
                    </div>
                </div>
            </div>
        </section>
'''
html = html.replace(how_it_works, how_it_works + testimonials)

# 5. Add Built for Industry (After Testimonials)
industry = '''
        <!-- BUILT FOR INDUSTRY -->
        <section class="industry" id="industry">
            <div class="container">
                <div class="section-header text-center">
                    <h2>Every industry. One platform.</h2>
                </div>
                <div class="industry-tabs">
                    <button class="industry-tab active" data-industry="fmcg">FMCG</button>
                    <button class="industry-tab" data-industry="auto">Automotive</button>
                    <button class="industry-tab" data-industry="finance">Finance</button>
                    <button class="industry-tab" data-industry="ecommerce">E-commerce</button>
                </div>
                <div class="industry-content-wrapper">
                    <div class="industry-card glass-panel active" id="fmcg-card">
                        <div class="card-icon"><i class="ph ph-shopping-cart"></i></div>
                        <div class="card-story">A leading FMCG brand used Pulse Scout to detect a competitor\'s 3-day flash campaign before it peaked — and reallocated display budget in real time. Result: 18% SOV gain.</div>
                        <div class="card-footer">
                            <span class="metric-badge">18% SOV gain</span>
                            <button class="btn btn-primary btn-sm">See this module</button>
                        </div>
                    </div>
                    <div class="industry-card glass-panel" id="auto-card">
                        <div class="card-icon"><i class="ph ph-car"></i></div>
                        <div class="card-story">An automotive brand tracked competitor search impressions during a new model launch. Pulse Scout identified keyword gaps that drove a 31% organic lift.</div>
                        <div class="card-footer">
                            <span class="metric-badge">31% Organic Lift</span>
                            <button class="btn btn-primary btn-sm">See this module</button>
                        </div>
                    </div>
                    <div class="industry-card glass-panel" id="finance-card">
                        <div class="card-icon"><i class="ph ph-bank"></i></div>
                        <div class="card-story">A fintech brand monitored negative brand sentiment across 400+ forums during a product crisis, enabling same-day PR response and limiting reputation damage.</div>
                        <div class="card-footer">
                            <span class="metric-badge">Reputation Shield</span>
                            <button class="btn btn-primary btn-sm">See this module</button>
                        </div>
                    </div>
                    <div class="industry-card glass-panel" id="ecommerce-card">
                        <div class="card-icon"><i class="ph ph-storefront"></i></div>
                        <div class="card-story">A marketplace brand scored 200 ad creatives in one crawl cycle — identifying 4 top performers and eliminating 3 underperformers before peak season.</div>
                        <div class="card-footer">
                            <span class="metric-badge">Creative ROI x3</span>
                            <button class="btn btn-primary btn-sm">See this module</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''
html = html.replace(testimonials, testimonials + industry)

# 6. Add See it in Action (Between Modules and Platform)
action_section = '''
        <!-- SEE IT IN ACTION -->
        <section class="live-action" id="action">
            <div class="container">
                <div class="section-header text-center">
                    <h2>Watch brands fight for share of voice — live</h2>
                    <p>This is real Pulse Scout data. Updated every few seconds.</p>
                </div>
                <div class="live-chart-wrapper glass-panel">
                    <canvas id="liveSovChart"></canvas>
                    <div class="timestamp">Last updated: <span id="time-ago">0</span> seconds ago</div>
                </div>
                <div class="insight-chips">
                    <div class="insight-chip" id="chip-1">Maruti gained 4% SOV in the last hour</div>
                    <div class="insight-chip" id="chip-2">Zomato running 3 new creatives today</div>
                    <div class="insight-chip" id="chip-3">Flipkart dominance in Search Ads</div>
                </div>
                <div class="text-center mt-4">
                    <a href="#demo" class="btn btn-primary btn-lg">Track your brand</a>
                </div>
            </div>
        </section>
'''
html = html.replace('</section>\\n\\n        <!-- PLATFORM CAPABILITIES -->', '</section>\\n' + action_section + '\\n        <!-- PLATFORM CAPABILITIES -->')

# 7. Upgrade Comparison Matrix
upgraded_comparison = '''
        <!-- COMPARISON MATRIX -->
        <section class="comparison" id="comparison">
            <div class="container">
                <div class="section-header text-center">
                    <h2>Pulse Scout vs. The Rest</h2>
                    <p>Why brands choose the unified intelligence platform.</p>
                </div>
                <div class="comparison-table-wrapper glass-panel">
                    <table class="comparison-table">
                        <thead>
                            <tr>
                                <th>Feature</th>
                                <th class="highlight">Pulse Scout</th>
                                <th>SEMrush</th>
                                <th>SimilarWeb</th>
                                <th>Brandwatch</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Display Ad Tracking</td>
                                <td class="highlight"><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                                <td><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                            </tr>
                            <tr>
                                <td>Real-time Hourly Tracking</td>
                                <td class="highlight"><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                            </tr>
                            <tr>
                                <td>AI Creative Scoring (0-100)</td>
                                <td class="highlight"><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                            </tr>
                            <tr>
                                <td>Cross-channel Unified View</td>
                                <td class="highlight"><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph ph-minus-circle"></i></td>
                                <td><i class="ph ph-minus-circle"></i></td>
                                <td><i class="ph ph-minus-circle"></i></td>
                            </tr>
                            <tr>
                                <td>Indian Publisher Coverage</td>
                                <td class="highlight"><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph ph-minus-circle"></i></td>
                                <td><i class="ph ph-minus-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                            </tr>
                            <tr>
                                <td>PayU / Local Billing</td>
                                <td class="highlight"><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                            </tr>
                            <tr>
                                <td>Dedicated Account Manager</td>
                                <td class="highlight"><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                                <td><i class="ph ph-minus-circle"></i></td>
                                <td><i class="ph ph-minus-circle"></i></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <p class="footnote text-center">Comparison based on publicly available feature documentation, May 2026</p>
            </div>
        </section>
'''
html = re.sub(r'<!-- COMPARISON MATRIX -->.*?<!-- IMPACT \(NUMBERS\) -->', upgraded_comparison + '\\n\\n        <!-- IMPACT (NUMBERS) -->', html, flags=re.DOTALL)

# 8. Upgrade ROI Calculator
upgraded_roi = '''
        <!-- ROI CALCULATOR -->
        <section class="roi-calculator" id="roi">
            <div class="container">
                <div class="calculator-grid glass-panel">
                    <div class="calc-input">
                        <h2>Calculate Your Lift</h2>
                        <p>See how much you can save with Pulse Scout intelligence.</p>
                        <div class="input-group">
                            <label for="ad-spend">Monthly Media Spend ($)</label>
                            <input type="range" id="ad-spend" min="10000" max="500000" step="10000" value="50000">
                            <div class="spend-value">$<span id="spend-display">50,000</span></div>
                        </div>
                        <div class="input-group mt-3">
                            <label for="tools-cost">Current Tools Cost ($)</label>
                            <input type="range" id="tools-cost" min="0" max="20000" step="500" value="2000">
                            <div class="spend-value">$<span id="tools-display">2,000</span></div>
                        </div>
                    </div>
                    <div class="calc-chart">
                        <canvas id="roiChart"></canvas>
                        <div class="metric-cards mt-4">
                            <div class="m-card">
                                <strong>$<span id="m-saving">12,500</span></strong>
                                <span>Monthly Saving</span>
                            </div>
                            <div class="m-card">
                                <strong>$<span id="a-roi">150,000</span></strong>
                                <span>Annual ROI</span>
                            </div>
                            <div class="m-card">
                                <strong><span id="p-period">4</span> Weeks</strong>
                                <span>Payback Period</span>
                            </div>
                        </div>
                        <div class="text-center mt-3">
                            <button class="btn btn-primary" onclick="openModal()">Get my full ROI report</button>
                        </div>
                        <p class="footnote text-center mt-2">Based on avg 15–25% media efficiency improvement across Pulse Scout clients</p>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- ROI MODAL -->
        <div class="modal" id="roiModal">
            <div class="modal-content glass-panel">
                <span class="close" onclick="closeModal()">&times;</span>
                <h3>Get Your Full ROI Report</h3>
                <form id="roiForm">
                    <div class="form-group">
                        <input type="text" placeholder="Your Name" required>
                    </div>
                    <div class="form-group">
                        <input type="email" placeholder="Work Email" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Send Report</button>
                </form>
            </div>
        </div>
'''
html = re.sub(r'<!-- ROI CALCULATOR -->.*?<!-- CTA SECTION -->', upgraded_roi + '\\n        \\n        <!-- CTA SECTION -->', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
