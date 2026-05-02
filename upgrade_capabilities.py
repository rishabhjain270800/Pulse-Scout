import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

interactive_strip = '''
        <!-- INTERACTIVE CAPABILITIES STRIP -->
        <section class="capabilities-strip" id="capabilities">
            <div class="container">
                <p class="strip-title">Unified Intelligence Across Every Channel</p>
                <div class="strip-tabs">
                    <button class="strip-tab active" data-tab="display"><i class="ph ph-desktop"></i> Display Ads</button>
                    <button class="strip-tab" data-tab="search"><i class="ph ph-magnifying-glass"></i> Search Ads</button>
                    <button class="strip-tab" data-tab="content"><i class="ph ph-article"></i> Content & Blogs</button>
                    <button class="strip-tab" data-tab="social"><i class="ph ph-share-network"></i> Social Listening</button>
                    <button class="strip-tab" data-tab="creative"><i class="ph ph-paint-brush"></i> Creatives</button>
                </div>
                <div class="strip-preview-panel glass-panel">
                    <div class="strip-preview active" id="display-preview">
                        <div class="preview-content">
                            <h4>Display Ad Share of Voice</h4>
                            <canvas id="stripDisplayChart"></canvas>
                        </div>
                    </div>
                    <div class="strip-preview" id="search-preview">
                        <div class="preview-content">
                            <h4>Keyword Rankings</h4>
                            <table class="mini-table">
                                <thead><tr><th>Keyword</th><th>Rank</th><th>Trend</th></tr></thead>
                                <tbody>
                                    <tr><td>Ad Intelligence</td><td>#1</td><td><i class="ph ph-trend-up text-success"></i></td></tr>
                                    <tr><td>Brand Monitor</td><td>#3</td><td><i class="ph ph-trend-up text-success"></i></td></tr>
                                    <tr><td>Market Insights</td><td>#5</td><td><i class="ph ph-trend-down text-danger"></i></td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div class="strip-preview" id="content-preview">
                        <div class="preview-content">
                            <h4>Sentiment Distribution</h4>
                            <div style="height: 150px;"><canvas id="stripContentChart"></canvas></div>
                        </div>
                    </div>
                    <div class="strip-preview" id="social-preview">
                        <div class="preview-content">
                            <h4>Engagement Metrics</h4>
                            <div class="mini-chips">
                                <div class="mini-chip"><strong>1.2M</strong> <span>Reach</span></div>
                                <div class="mini-chip"><strong>45K</strong> <span>Engagements</span></div>
                                <div class="mini-chip"><strong>+12%</strong> <span>Growth</span></div>
                            </div>
                        </div>
                    </div>
                    <div class="strip-preview" id="creative-preview">
                        <div class="preview-content">
                            <h4>Creative Score Breakdown</h4>
                            <canvas id="stripCreativeChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''
html = re.sub(r'<!-- CAPABILITIES STRIP -->.*?<!-- MODULES SHOWCASE -->', interactive_strip + '\\n\\n        <!-- MODULES SHOWCASE -->', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
