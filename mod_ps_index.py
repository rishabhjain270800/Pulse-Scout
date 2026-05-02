import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Meta Tags
html = html.replace(
    '<meta name="description" content="Pulse Scout is a unified intelligence platform that shows you what your competitors are doing, how your brand is performing, and what actions you should take next.">',
    '''<meta name="description" content="Pulse Scout is a unified intelligence platform that shows you what your competitors are doing, how your brand is performing, and what actions you should take next.">
    <!-- Open Graph -->
    <meta property="og:title" content="Pulse Scout | AI-Powered Ad Intelligence">
    <meta property="og:description" content="Unified intelligence platform for modern brands.">
    <meta property="og:type" content="website">'''
)

# 2. Mouse Glow
html = html.replace(
    '<body>',
    '<body>\\n    <div class=\"mouse-glow\" id=\"mouse-glow\"></div>'
)

# 3. Magnetic Buttons
# Replace button classes to include magnetic
html = html.replace('class="btn btn-secondary"', 'class="btn btn-secondary magnetic" aria-label="Log In"')
html = html.replace('class="btn btn-primary"', 'class="btn btn-primary magnetic" aria-label="Get a Demo"')
html = html.replace('class="btn btn-primary btn-lg"', 'class="btn btn-primary btn-lg magnetic" aria-label="Start Monitoring"')
html = html.replace('class="btn btn-outline btn-lg"', 'class="btn btn-outline btn-lg magnetic" aria-label="See How It Works"')

# 4. Accessibility for footer icons
html = html.replace('class="ph-fill ph-pulse"', 'class="ph-fill ph-pulse" aria-hidden="true"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
