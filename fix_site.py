import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the broken Hero section and insert missing sections
hero_fix = '''
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
            </div>
        </section>

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

# Use regex to find the broken block and replace it
# From <div class="hero-visual"> to the end of the hero section
pattern = r'<div class="hero-visual">.*?</section>'
html = re.sub(pattern, hero_fix, html, flags=re.DOTALL)

# Insert "See it in Action" before platform capabilities if missing
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
if '<!-- SEE IT IN ACTION -->' not in html:
    html = html.replace('<!-- PLATFORM CAPABILITIES -->', action_section + '\\n\\n        <!-- PLATFORM CAPABILITIES -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
