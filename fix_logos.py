import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_logos = """                <!-- Client Logo Strip -->
                <div class="client-logos">
                    <div class="client-logo"><i class="ph ph-whiskey-glass"></i><span>Radico Khaitan</span></div>
                    <div class="client-logo"><i class="ph ph-car"></i><span>Maruti Suzuki</span></div>
                    <div class="client-logo"><i class="ph ph-truck"></i><span>Eicher Motors</span></div>
                    <div class="client-logo"><i class="ph ph-bus"></i><span>Ashok Leyland</span></div>
                    <div class="client-logo"><i class="ph ph-bank"></i><span>IDFC First Bank</span></div>
                    <div class="client-logo"><i class="ph ph-graduation-cap"></i><span>LPU</span></div>
                </div>"""

new_logos = """                <!-- Client Logo Strip -->
                <div class="client-logos-grid">
                    <a class="client-logo-card" href="#fmcg-card" data-tab="fmcg">
                        <div class="client-logo-img-wrap">
                            <img src="https://logo.clearbit.com/radico.co.in"
                                 onerror="this.onerror=null;this.src='';this.parentElement.innerHTML='<span class=logo-fallback>RK</span>'"
                                 alt="Radico Khaitan" loading="lazy">
                        </div>
                        <span class="client-logo-name">Radico Khaitan</span>
                        <span class="client-logo-sector">FMCG &amp; Spirits</span>
                    </a>
                    <a class="client-logo-card" href="#auto-card" data-tab="auto">
                        <div class="client-logo-img-wrap">
                            <img src="https://logo.clearbit.com/marutisuzuki.com"
                                 onerror="this.onerror=null;this.src='';this.parentElement.innerHTML='<span class=logo-fallback>MS</span>'"
                                 alt="Maruti Suzuki" loading="lazy">
                        </div>
                        <span class="client-logo-name">Maruti Suzuki</span>
                        <span class="client-logo-sector">Automotive</span>
                    </a>
                    <a class="client-logo-card" href="#cv-card" data-tab="cv">
                        <div class="client-logo-img-wrap">
                            <img src="https://logo.clearbit.com/eichermotors.com"
                                 onerror="this.onerror=null;this.src='';this.parentElement.innerHTML='<span class=logo-fallback>EM</span>'"
                                 alt="Eicher Motors" loading="lazy">
                        </div>
                        <span class="client-logo-name">Eicher Motors</span>
                        <span class="client-logo-sector">Commercial Vehicles</span>
                    </a>
                    <a class="client-logo-card" href="#cv-card" data-tab="cv">
                        <div class="client-logo-img-wrap">
                            <img src="https://logo.clearbit.com/ashokleyland.com"
                                 onerror="this.onerror=null;this.src='';this.parentElement.innerHTML='<span class=logo-fallback>AL</span>'"
                                 alt="Ashok Leyland" loading="lazy">
                        </div>
                        <span class="client-logo-name">Ashok Leyland</span>
                        <span class="client-logo-sector">Commercial Vehicles</span>
                    </a>
                    <a class="client-logo-card" href="#finance-card" data-tab="finance">
                        <div class="client-logo-img-wrap">
                            <img src="https://logo.clearbit.com/idfcfirstbank.com"
                                 onerror="this.onerror=null;this.src='';this.parentElement.innerHTML='<span class=logo-fallback>IDFC</span>'"
                                 alt="IDFC First Bank" loading="lazy">
                        </div>
                        <span class="client-logo-name">IDFC First Bank</span>
                        <span class="client-logo-sector">BFSI</span>
                    </a>
                    <a class="client-logo-card" href="#edu-card" data-tab="edu">
                        <div class="client-logo-img-wrap">
                            <img src="https://logo.clearbit.com/lpu.in"
                                 onerror="this.onerror=null;this.src='';this.parentElement.innerHTML='<span class=logo-fallback>LPU</span>'"
                                 alt="LPU" loading="lazy">
                        </div>
                        <span class="client-logo-name">LPU</span>
                        <span class="client-logo-sector">Education</span>
                    </a>
                </div>"""

if old_logos in content:
    content = content.replace(old_logos, new_logos)
    print('SUCCESS: Logo strip updated')
else:
    print('ERROR: Could not find logo strip')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
