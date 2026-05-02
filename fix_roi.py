import re

with open('index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix slider alignment and widths
roi_fix_css = '''
/* ROI Calculator Fixes */
.roi-calculator { padding: 4rem 0 !important; } /* Reduced from 8rem */
.calculator-grid { display: grid; grid-template-columns: 1fr 1.2fr; gap: 4rem; padding: 4rem; align-items: start; }
.calc-input { display: flex; flex-direction: column; gap: 2rem; }
.calc-input h2 { margin-bottom: 0.5rem; }
.input-group { width: 100%; display: flex; flex-direction: column; gap: 0.8rem; }
.input-group input[type="range"] { width: 100%; height: 6px; -webkit-appearance: none; background: #e5e7eb; border-radius: 5px; outline: none; }
.input-group input[type="range"]::-webkit-slider-thumb { -webkit-appearance: none; width: 24px; height: 24px; background: var(--primary); border-radius: 50%; cursor: pointer; border: 4px solid white; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
.spend-value { font-size: 1.5rem; font-weight: 800; color: var(--primary); margin-top: 0.5rem; }

.calc-chart { background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); height: 100%; display: flex; flex-direction: column; }
.calc-chart canvas { max-height: 300px; margin-bottom: 2rem; }

.metric-cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: auto; }
.m-card { padding: 1.5rem 1rem; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 12px; text-align: center; }
.m-card strong { font-size: 1.2rem; color: var(--primary); display: block; margin-bottom: 0.3rem; }
.m-card span { font-size: 0.75rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }

@media (max-width: 968px) {
    .calculator-grid { grid-template-columns: 1fr; padding: 2rem; gap: 3rem; }
    .metric-cards { grid-template-columns: 1fr; }
}
'''

# Replace or append ROI styles
if '.roi-calculator {' in css:
    # Find the block and replace it
    pattern = r'\.roi-calculator \{.*?\}'
    css = re.sub(pattern, '', css, flags=re.DOTALL)
    # Also clean up other related classes if they exist
    css = re.sub(r'\.calculator-grid \{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'\.calc-input \{.*?\}', '', css, flags=re.DOTALL)
    css = re.sub(r'\.m-card \{.*?\}', '', css, flags=re.DOTALL)

css += roi_fix_css

with open('index.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Fix main.js Chart logic (Ensure bars are visible)
with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make sure Chart.js uses explicit colors and updates correctly
js = js.replace("backgroundColor: ['#ef4444', '#10b981', '#3b82f6']", "backgroundColor: ['rgba(239, 68, 68, 0.8)', 'rgba(16, 185, 129, 0.8)', 'rgba(59, 130, 246, 0.8)'], borderColor: ['#ef4444', '#10b981', '#3b82f6'], borderWidth: 1")

# Also ensure updateROI is called after chart init
if 'updateROI();' not in js:
    js = js.replace('if (spendSlider) {', 'if (spendSlider) {\\n        updateROI();')

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(js)
