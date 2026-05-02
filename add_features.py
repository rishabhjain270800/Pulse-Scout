import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Sentiment Ticker (Top bar below nav)
ticker_html = '''
    <!-- LIVE SENTIMENT TICKER -->
    <div class="sentiment-ticker-wrapper">
        <div class="ticker-content">
            <span class="ticker-item"><i class="ph-fill ph-chat-circle-dots"></i> Apple: Positive Sentiment (+82)</span>
            <span class="ticker-item"><i class="ph-fill ph-chat-circle-dots"></i> Nike: Competitive Move Detected</span>
            <span class="ticker-item"><i class="ph-fill ph-chat-circle-dots"></i> Amazon: Search SOV Increase (+12%)</span>
            <span class="ticker-item"><i class="ph-fill ph-chat-circle-dots"></i> Tesla: Creative Score 94/100</span>
            <span class="ticker-item"><i class="ph-fill ph-chat-circle-dots"></i> Microsoft: New Banner Campaign Live</span>
            <!-- Repeat for loop -->
            <span class="ticker-item"><i class="ph-fill ph-chat-circle-dots"></i> Apple: Positive Sentiment (+82)</span>
            <span class="ticker-item"><i class="ph-fill ph-chat-circle-dots"></i> Nike: Competitive Move Detected</span>
            <span class="ticker-item"><i class="ph-fill ph-chat-circle-dots"></i> Amazon: Search SOV Increase (+12%)</span>
        </div>
    </div>
'''
html = html.replace('</header>', '</header>\\n' + ticker_html)

# 2. Add Comparison Matrix
comparison_html = '''
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
                                <th>Point Solutions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Display Ad Tracking</td>
                                <td class="highlight"><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph-fill ph-check-circle"></i></td>
                            </tr>
                            <tr>
                                <td>Search SOV Analysis</td>
                                <td class="highlight"><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph-fill ph-check-circle"></i></td>
                            </tr>
                            <tr>
                                <td>AI Creative Scoring</td>
                                <td class="highlight"><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                            </tr>
                            <tr>
                                <td>Cross-Channel Sentiment</td>
                                <td class="highlight"><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                            </tr>
                            <tr>
                                <td>Unified ROI Dashboard</td>
                                <td class="highlight"><i class="ph-fill ph-check-circle"></i></td>
                                <td><i class="ph ph-x-circle"></i></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>
'''
html = html.replace('</section>\\n\\n        <!-- IMPACT (NUMBERS) -->', comparison_html + '\\n\\n        <!-- IMPACT (NUMBERS) -->')

# 3. Add ROI Calculator
calculator_html = '''
        <!-- ROI CALCULATOR -->
        <section class="roi-calculator" id="roi">
            <div class="container">
                <div class="calculator-grid glass-panel">
                    <div class="calc-input">
                        <h2>Calculate Your Lift</h2>
                        <p>See how much you can save with Pulse Scout intelligence.</p>
                        <div class="input-group">
                            <label for="ad-spend">Monthly Media Spend ($)</label>
                            <input type="range" id="ad-spend" min="10000" max="1000000" step="10000" value="50000">
                            <div class="spend-value">$<span id="spend-display">50,000</span></div>
                        </div>
                    </div>
                    <div class="calc-results">
                        <div class="result-card">
                            <span class="result-label">Potential Efficiency Gain</span>
                            <span class="result-value text-gradient">$<span id="savings-display">10,000</span></span>
                            <span class="result-sub">Estimated Monthly ROI</span>
                        </div>
                        <div class="result-card">
                            <span class="result-label">Media Planning Speed</span>
                            <span class="result-value text-gradient">60%</span>
                            <span class="result-sub">Faster Resource Allocation</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''
html = html.replace('</section>\\n        \\n        <!-- CTA SECTION -->', calculator_html + '\\n        \\n        <!-- CTA SECTION -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
