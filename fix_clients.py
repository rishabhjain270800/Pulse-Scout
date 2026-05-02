import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_section = """        <!-- BUILT FOR INDUSTRY -->
        <section class="industry" id="industry">
            <div class="container">
                <div class="section-header text-center">
                    <h2>Trusted by India's leading brands</h2>
                    <p>From FMCG giants to automotive leaders &mdash; Pulse Scout powers decisions at every level.</p>
                </div>

                <!-- Client Logo Strip -->
                <div class="client-logos">
                    <div class="client-logo"><i class="ph ph-whiskey-glass"></i><span>Radico Khaitan</span></div>
                    <div class="client-logo"><i class="ph ph-car"></i><span>Maruti Suzuki</span></div>
                    <div class="client-logo"><i class="ph ph-truck"></i><span>Eicher Motors</span></div>
                    <div class="client-logo"><i class="ph ph-bus"></i><span>Ashok Leyland</span></div>
                    <div class="client-logo"><i class="ph ph-bank"></i><span>IDFC First Bank</span></div>
                    <div class="client-logo"><i class="ph ph-graduation-cap"></i><span>LPU</span></div>
                </div>

                <!-- Use Case Tabs -->
                <div class="industry-tabs">
                    <button class="industry-tab active" data-industry="fmcg">Radico</button>
                    <button class="industry-tab" data-industry="auto">Maruti Suzuki</button>
                    <button class="industry-tab" data-industry="cv">Eicher &amp; Ashok</button>
                    <button class="industry-tab" data-industry="finance">IDFC First Bank</button>
                    <button class="industry-tab" data-industry="edu">LPU</button>
                </div>
                <div class="industry-content-wrapper">
                    <!-- Radico -->
                    <div class="industry-card glass-panel active" id="fmcg-card">
                        <div class="card-icon"><i class="ph ph-whiskey-glass"></i></div>
                        <div class="card-client-tag">Radico Khaitan &middot; FMCG / Spirits</div>
                        <div class="card-story">Radico used Pulse Scout's Display Intelligence to track competitor banner activity across 120+ publisher sites during the festive season. The team detected a competitor's 3-day flash push and reallocated display budget in real time &mdash; securing an <strong>18% SOV lead</strong> at peak buying intent.</div>
                        <div class="card-footer">
                            <span class="metric-badge">+18% SOV Gain</span>
                            <span class="metric-badge">120+ Publishers Tracked</span>
                            <button class="btn btn-primary btn-sm">See Display Module</button>
                        </div>
                    </div>
                    <!-- Maruti Suzuki -->
                    <div class="industry-card glass-panel" id="auto-card">
                        <div class="card-icon"><i class="ph ph-car"></i></div>
                        <div class="card-client-tag">Maruti Suzuki &middot; Automotive</div>
                        <div class="card-story">Maruti Suzuki used Pulse Scout's Search Intelligence to monitor keyword-level impression share across 5 competitor models during a new launch. The platform surfaced a critical gap in "compact SUV under 10 lakh" queries &mdash; enabling a targeted bid strategy that delivered a <strong>31% organic traffic lift</strong> within 3 weeks.</div>
                        <div class="card-footer">
                            <span class="metric-badge">+31% Organic Lift</span>
                            <span class="metric-badge">Search SOV Tracked</span>
                            <button class="btn btn-primary btn-sm">See Search Module</button>
                        </div>
                    </div>
                    <!-- Eicher & Ashok Leyland -->
                    <div class="industry-card glass-panel" id="cv-card">
                        <div class="card-icon"><i class="ph ph-truck"></i></div>
                        <div class="card-client-tag">Eicher Motors &amp; Ashok Leyland &middot; Commercial Vehicles</div>
                        <div class="card-story">Both CV brands used Pulse Scout to benchmark their Share of Voice in the commercial vehicle segment across Display and Search. Eicher identified 3 publisher categories with zero brand presence &mdash; and a targeted push increased their SOV by <strong>22% in 6 weeks</strong>.</div>
                        <div class="card-footer">
                            <span class="metric-badge">+22% Category SOV</span>
                            <span class="metric-badge">CV Segment Benchmarked</span>
                            <button class="btn btn-primary btn-sm">See Platform Modules</button>
                        </div>
                    </div>
                    <!-- IDFC First Bank -->
                    <div class="industry-card glass-panel" id="finance-card">
                        <div class="card-icon"><i class="ph ph-bank"></i></div>
                        <div class="card-client-tag">IDFC First Bank &middot; BFSI</div>
                        <div class="card-story">IDFC First Bank used Pulse Scout's Sentiment Intelligence to monitor brand mentions across 400+ financial forums and news sites. When a negative narrative began building around loan processing, the team received real-time alerts and responded <strong>within 4 hours</strong> &mdash; containing the shift before it went mainstream.</div>
                        <div class="card-footer">
                            <span class="metric-badge">4-Hour Crisis Response</span>
                            <span class="metric-badge">400+ Sources Monitored</span>
                            <button class="btn btn-primary btn-sm">See Sentiment Module</button>
                        </div>
                    </div>
                    <!-- LPU -->
                    <div class="industry-card glass-panel" id="edu-card">
                        <div class="card-icon"><i class="ph ph-graduation-cap"></i></div>
                        <div class="card-client-tag">LPU (Lovely Professional University) &middot; Education</div>
                        <div class="card-story">LPU used Pulse Scout's Creative Scoring module during their admission season. By scoring 80+ ad creatives across placement platforms, the team cut 12 underperforming banners and doubled down on top formats &mdash; delivering a <strong>28% reduction in CPL</strong> and record enrolment inquiries that quarter.</div>
                        <div class="card-footer">
                            <span class="metric-badge">-28% CPL</span>
                            <span class="metric-badge">80+ Creatives Scored</span>
                            <button class="btn btn-primary btn-sm">See Creative Module</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

match = re.search(r'        <!-- BUILT FOR INDUSTRY -->.*?        </section>', content, re.DOTALL)
if match:
    content = content[:match.start()] + new_section + content[match.end():]
    print('SUCCESS: Section replaced')
else:
    print('ERROR: Pattern not found')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
