import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

upgraded_modules = '''
                <div class="modules-grid">
                    <!-- Module 1 -->
                    <div class="module-card glass-panel" data-module="display">
                        <div class="module-icon" style="color: #3b82f6;">
                            <i class="ph ph-browser"></i>
                        </div>
                        <h3>Display Intelligence</h3>
                        <p>Track banner ads across publisher websites in real-time. Uncover Share of Voice (SOV), publisher dominance, and competitor presence.</p>
                        <div class="module-preview">
                            <canvas id="displayPreviewChart"></canvas>
                        </div>
                    </div>

                    <!-- Module 2 -->
                    <div class="module-card glass-panel" data-module="search">
                        <div class="module-icon" style="color: #a855f7;">
                            <i class="ph ph-magnifying-glass-plus"></i>
                        </div>
                        <h3>Search Intelligence</h3>
                        <p>Track Paid + Organic search ads based on keywords. Monitor rankings, Impression Share, and region-based search simulations.</p>
                        <div class="module-preview">
                            <table class="mini-table">
                                <thead><tr><th>Keyword</th><th>Pos</th><th>Type</th></tr></thead>
                                <tbody>
                                    <tr><td>Ad Intelligence</td><td>1</td><td>Paid</td></tr>
                                    <tr><td>Brand Monitor</td><td>3</td><td>Org</td></tr>
                                    <tr><td>Competitor Tool</td><td>7</td><td>Paid</td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- Module 3 -->
                    <div class="module-card glass-panel" data-module="sentiment">
                        <div class="module-icon" style="color: #10b981;">
                            <i class="ph ph-chats-circle"></i>
                        </div>
                        <h3>Content & Sentiment</h3>
                        <p>Analyze brand mentions across web content, news, and forums. Group by keywords and classify sentiment using advanced AI.</p>
                        <div class="module-preview">
                            <canvas id="sentimentPreviewChart"></canvas>
                        </div>
                    </div>

                    <!-- Module 4 -->
                    <div class="module-card glass-panel" data-module="creative">
                        <div class="module-icon" style="color: #ef4444;">
                            <i class="ph ph-target"></i>
                        </div>
                        <h3>Creative Scoring</h3>
                        <p>Evaluate ad creatives using AI. Score based on Awareness, Imagery, Headline, Brand Visibility, and Performance.</p>
                        <div class="module-preview">
                            <canvas id="creativePreviewChart"></canvas>
                        </div>
                    </div>

                    <!-- Module 5 -->
                    <div class="module-card glass-panel" data-module="social">
                        <div class="module-icon" style="color: #f59e0b;">
                            <i class="ph ph-users-three"></i>
                        </div>
                        <h3>Social Listening</h3>
                        <p>Track brand conversations across social platforms. Understand sentiment trends, engagement metrics, and influencer insights.</p>
                        <div class="module-preview">
                            <div class="mini-chips">
                                <div class="mini-chip"><strong>12.4K</strong> <span>Mentions</span></div>
                                <div class="mini-chip"><strong>68%</strong> <span>Positive</span></div>
                                <div class="mini-chip"><strong>#FMCG</strong> <span>Trending</span></div>
                            </div>
                        </div>
                    </div>
                </div>
'''
html = re.sub(r'<div class="modules-grid">.*?</div>\s*</div>\s*</section>', upgraded_modules + '</div></section>', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
