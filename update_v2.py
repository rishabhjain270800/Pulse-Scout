import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. SEO & Meta Tags
seo_tags = '''
    <title>Pulse Scout | AI-Powered Ad Intelligence & Brand Monitoring Platform</title>
    <meta name="description" content="Track competitor ads, monitor brand sentiment, score creatives, and measure Share of Voice — all in one unified platform. Powered by Adglobal360.">
    <meta name="keywords" content="Display ad intelligence, brand monitoring, share of voice, competitive intelligence India, AI ad tracking, search SOV, sentiment analysis">
    <link rel="canonical" href="https://rishabhjain270800.github.io/Pulse-Scout/">
    <meta name="robots" content="index, follow">

    <!-- Open Graph -->
    <meta property="og:title" content="Pulse Scout | AI-Powered Ad Intelligence & Brand Monitoring Platform">
    <meta property="og:description" content="Track competitor ads, monitor brand sentiment, score creatives, and measure Share of Voice.">
    <meta property="og:image" content="https://rishabhjain270800.github.io/Pulse-Scout/og-image.jpg">
    <meta property="og:url" content="https://rishabhjain270800.github.io/Pulse-Scout/">
    <meta property="og:type" content="website">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Pulse Scout | AI-Powered Ad Intelligence">
    <meta name="twitter:description" content="Unified intelligence platform for modern brands.">

    <!-- Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Pulse Scout",
      "description": "AI-Powered Ad Intelligence & Brand Monitoring Platform",
      "applicationCategory": "BusinessApplication",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "INR"
      }
    }
    </script>
'''
html = html.replace('<title>Pulse Scout | AI-Powered Ad Intelligence</title>', seo_tags)
# Remove old description/og tags if redundant
html = html.replace('<meta name="description" content="Pulse Scout is a unified intelligence platform that shows you what your competitors are doing, how your brand is performing, and what actions you should take next.">', '')

# 2. Scroll Progress Bar
html = html.replace('<body>', '<body>\\n    <div class="scroll-progress" id="scrollProgress"></div>')

# 3. Upgraded Navbar (Add hamburger)
nav_replacement = '''
    <header class="navbar" id="navbar">
        <div class="nav-container">
            <div class="logo">
                <i class="ph-fill ph-pulse" aria-hidden="true"></i>
                <span>Pulse Scout</span>
            </div>
            <nav class="nav-links">
                <a href="#platform" class="nav-link">Platform</a>
                <a href="#modules" class="nav-link">Modules</a>
                <a href="#impact" class="nav-link">Impact</a>
                <a href="#pricing" class="nav-link">Pricing</a>
            </nav>
            <div class="nav-actions">
                <button class="btn btn-secondary magnetic hide-mobile">Log In</button>
                <button class="btn btn-primary magnetic pulse-btn">Get a Demo</button>
                <button class="mobile-menu-toggle" id="menuToggle"><i class="ph ph-list"></i></button>
            </div>
        </div>
        <div class="mobile-nav" id="mobileNav">
            <a href="#platform">Platform</a>
            <a href="#modules">Modules</a>
            <a href="#impact">Impact</a>
            <a href="#pricing">Pricing</a>
        </div>
    </header>
'''
html = re.sub(r'<header class="navbar">.*?</header>', nav_replacement, html, flags=re.DOTALL)

# 4. Upgraded Live Signal Ticker (India-specific)
ticker_replacement = '''
    <!-- LIVE SIGNAL TICKER -->
    <div class="sentiment-ticker-wrapper">
        <div class="ticker-content">
            <span class="ticker-item"><span class="dot orange"></span> Maruti Suzuki: 3 new display creatives detected on CarWale.com</span>
            <span class="ticker-item"><span class="dot blue"></span> Flipkart: Search SOV increased +14% on 'mobile under 20000' — 2 hrs ago</span>
            <span class="ticker-item"><span class="dot red"></span> Zomato: Negative sentiment spike on Twitter — 847 mentions in last hour</span>
            <span class="ticker-item"><span class="dot orange"></span> HDFC Bank: Competitor launched new loan campaign on 8 publisher sites</span>
            <span class="ticker-item"><span class="dot red"></span> Airtel: Creative Score dropped to 71 — headline clarity flagged by AI</span>
            <span class="ticker-item"><span class="dot teal"></span> Myntra: Share of Voice at 34% in Fashion category — highest this week</span>
            <span class="ticker-item"><span class="dot blue"></span> Tata Motors: Organic rank improved from #5 to #2 for 'electric cars India'</span>
            <!-- Loop -->
            <span class="ticker-item"><span class="dot orange"></span> Maruti Suzuki: 3 new display creatives detected</span>
        </div>
    </div>
'''
html = re.sub(r'<!-- LIVE SENTIMENT TICKER -->.*?</div>\s*</div>', ticker_replacement, html, flags=re.DOTALL)

# 5. "The problem every brand faces" (After Hero)
problem_section = '''
        <!-- THE PROBLEM -->
        <section class="problem" id="problem">
            <div class="container">
                <div class="section-header text-center">
                    <h2>Flying blind in a competitive market?</h2>
                </div>
                <div class="problem-grid">
                    <div class="pain-cards">
                        <div class="pain-card">
                            <i class="ph ph-eye-slash"></i>
                            <h4>Don't know where competitors advertise</h4>
                        </div>
                        <div class="pain-card">
                            <i class="ph ph-dice"></i>
                            <h4>Guessing which creatives perform</h4>
                        </div>
                        <div class="pain-card">
                            <i class="ph ph-bell-ringing"></i>
                            <h4>Sentiment crises catch you off guard</h4>
                        </div>
                        <div class="pain-card">
                            <i class="ph ph-money-wavy"></i>
                            <h4>Budget leaks to low-impact publishers</h4>
                        </div>
                    </div>
                    <div class="split-view glass-panel">
                        <div class="split-col before">
                            <h5>Before Pulse Scout</h5>
                            <ul>
                                <li class="text-danger"><i class="ph ph-x"></i> Scattered Data</li>
                                <li class="text-danger"><i class="ph ph-x"></i> Reactive Decisions</li>
                                <li class="text-danger"><i class="ph ph-x"></i> Wasted Spend</li>
                                <li class="text-danger"><i class="ph ph-x"></i> Blind Gaps</li>
                            </ul>
                        </div>
                        <div class="split-arrow"><i class="ph ph-arrow-right"></i></div>
                        <div class="split-col after">
                            <h5>After Pulse Scout</h5>
                            <ul>
                                <li class="text-success"><i class="ph ph-check"></i> Unified View</li>
                                <li class="text-success"><i class="ph ph-check"></i> Real-time Alerts</li>
                                <li class="text-success"><i class="ph ph-check"></i> Optimised Spend</li>
                                <li class="text-success"><i class="ph ph-check"></i> Full Visibility</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="text-center mt-5">
                    <h3>Stop guessing. Start knowing.</h3>
                    <a href="#how-it-works" class="btn btn-outline btn-lg mt-3">See how Pulse Scout solves this</a>
                </div>
            </div>
        </section>
'''
html = html.replace('</section>\\n\\n        <!-- HOW IT WORKS -->', '</section>\\n' + problem_section + '\\n        <!-- HOW IT WORKS -->')

# 6. "Live brand mention feed" (After How it Works)
live_feed = '''
        <!-- LIVE MENTION FEED -->
        <section class="live-feed" id="live-feed">
            <div class="container">
                <div class="section-header text-center">
                    <h2>See what the web is saying — right now</h2>
                </div>
                <div class="feed-layout">
                    <div class="feed-container-outer">
                        <div class="feed-scroll-container" id="feedScroll">
                            <!-- Cards will be populated/duplicated in JS for seamless scroll if needed, but we'll put 10 here for CSS scroll -->
                            <div class="mention-card">
                                <span class="badge pos">Positive</span>
                                <strong>Maruti Suzuki</strong>
                                <p>"The new Maruti Brezza feels incredibly solid and the fuel efficiency is just unbeatable in this segment."</p>
                                <div class="card-meta"><span>team-bhp.com</span> <span>2 hours ago</span></div>
                            </div>
                            <div class="mention-card">
                                <span class="badge neg">Negative</span>
                                <strong>Zomato</strong>
                                <p>"Extremely disappointed with the delivery time today. 90 minutes for a 2km distance? Unacceptable."</p>
                                <div class="card-meta"><span>twitter.com</span> <span>1 hour ago</span></div>
                            </div>
                            <div class="mention-card">
                                <span class="badge neu">Neutral</span>
                                <strong>HDFC Bank</strong>
                                <p>"Comparing HDFC and ICICI home loan rates for my new apartment. Both seem competitive this quarter."</p>
                                <div class="card-meta"><span>moneycontrol.com</span> <span>3 hours ago</span></div>
                            </div>
                            <div class="mention-card">
                                <span class="badge pos">Positive</span>
                                <strong>Flipkart</strong>
                                <p>"Amazing experience with Flipkart Minutes! Got my groceries in less than 15 minutes. Game changer."</p>
                                <div class="card-meta"><span>facebook.com</span> <span>30 mins ago</span></div>
                            </div>
                            <!-- Repeat for smooth scroll -->
                        </div>
                        <div class="feed-overlay-bottom"></div>
                        <div class="text-center mt-4">
                            <button class="btn btn-primary">View full feed in Pulse Scout</button>
                        </div>
                    </div>
                    <div class="live-stats-col">
                        <div class="live-stat-card glass-panel">
                            <span class="label">Total Mentions Today</span>
                            <strong id="stat-mentions">12,482</strong>
                        </div>
                        <div class="live-stat-card glass-panel">
                            <span class="label">Positive Sentiment %</span>
                            <strong id="stat-sentiment">68%</strong>
                        </div>
                        <div class="live-stat-card glass-panel">
                            <span class="label">Trending Keyword</span>
                            <strong id="stat-trending">#FMCG</strong>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''
html = html.replace('</section>\\n\\n        <!-- TESTIMONIALS -->', '</section>\\n' + live_feed + '\\n        <!-- TESTIMONIALS -->')

# 7. Integrations Marquee (Below Platform Capabilities)
integrations = '''
        <!-- INTEGRATIONS -->
        <section class="integrations">
            <div class="container">
                <div class="section-header text-center">
                    <h2>Works with the tools and platforms you rely on</h2>
                </div>
                <div class="marquee-wrapper">
                    <div class="marquee row-1">
                        <div class="pill"><span class="dot" style="background:#4285F4"></span> Google Search</div>
                        <div class="pill"><span class="dot" style="background:#EA4335"></span> Google Display</div>
                        <div class="pill"><span class="dot" style="background:#00A4EF"></span> Microsoft Bing</div>
                        <div class="pill"><span class="dot" style="background:#1877F2"></span> Meta</div>
                        <div class="pill"><span class="dot" style="background:#FF0000"></span> YouTube</div>
                        <div class="pill"><span class="dot" style="background:#E4405F"></span> Instagram</div>
                        <!-- Repeat -->
                    </div>
                    <div class="marquee row-2">
                        <div class="pill"><span class="dot" style="background:#1D6F42"></span> Excel</div>
                        <div class="pill"><span class="dot" style="background:#F40F02"></span> PDF Reports</div>
                        <div class="pill"><span class="dot" style="background:#F7941D"></span> PayU</div>
                        <div class="pill"><span class="dot" style="background:#4A154B"></span> Slack Alerts</div>
                        <div class="pill"><span class="dot" style="background:#D44638"></span> Email</div>
                        <div class="pill"><span class="dot" style="background:#3b82f6"></span> REST API</div>
                    </div>
                </div>
                <p class="text-center mt-4">Don't see your platform? <a href="#">We integrate on request.</a> <a href="#" class="text-gradient">Contact us</a></p>
            </div>
        </section>
'''
html = html.replace('</section>\\n\\n        <!-- COMPARISON MATRIX -->', '</section>\\n' + integrations + '\\n        <!-- COMPARISON MATRIX -->')

# 8. Pricing Section (Before CTA)
pricing = '''
        <!-- PRICING -->
        <section class="pricing" id="pricing">
            <div class="container">
                <div class="section-header text-center">
                    <h2>Simple, transparent plans</h2>
                </div>
                <div class="pricing-grid">
                    <div class="pricing-card glass-panel">
                        <h3>Starter</h3>
                        <div class="price">Contact for pricing</div>
                        <p>For brands getting started with ad intelligence</p>
                        <ul>
                            <li><i class="ph ph-check"></i> Up to 3 campaigns</li>
                            <li><i class="ph ph-check"></i> Display + Search modules</li>
                            <li><i class="ph ph-check"></i> Weekly reports (PDF/Excel)</li>
                            <li><i class="ph ph-check"></i> 1 user seat</li>
                            <li><i class="ph ph-check"></i> Email support</li>
                        </ul>
                        <button class="btn btn-outline w-100 mt-4">Start Free Trial</button>
                    </div>
                    <div class="pricing-card glass-panel popular">
                        <div class="popular-badge">Most Popular</div>
                        <h3>Growth</h3>
                        <div class="price">Contact for pricing</div>
                        <p>For active brands and agencies</p>
                        <ul>
                            <li><i class="ph ph-check"></i> Up to 15 campaigns</li>
                            <li><i class="ph ph-check"></i> All 5 modules</li>
                            <li><i class="ph ph-check"></i> Creative Scoring</li>
                            <li><i class="ph ph-check"></i> Daily reports + Alerts</li>
                            <li><i class="ph ph-check"></i> 5 user seats</li>
                        </ul>
                        <button class="btn btn-primary w-100 mt-4">Get a Demo</button>
                    </div>
                    <div class="pricing-card glass-panel">
                        <h3>Enterprise</h3>
                        <div class="price">Contact for pricing</div>
                        <p>For large brands needing full intelligence</p>
                        <ul>
                            <li><i class="ph ph-check"></i> Unlimited campaigns</li>
                            <li><i class="ph ph-check"></i> Custom crawl frequency</li>
                            <li><i class="ph ph-check"></i> Dedicated account manager</li>
                            <li><i class="ph ph-check"></i> API access</li>
                            <li><i class="ph ph-check"></i> Custom integrations</li>
                        </ul>
                        <button class="btn btn-outline w-100 mt-4">Contact Sales</button>
                    </div>
                </div>
            </div>
        </section>
'''
html = html.replace('<!-- CTA SECTION -->', pricing + '\\n\\n        <!-- CTA SECTION -->')

# 9. Back to top
html = html.replace('</body>', '    <button id="backToTop" class="back-to-top"><i class="ph ph-arrow-up"></i></button>\\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
