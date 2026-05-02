import sys
import re

with open('index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update variables for Light Theme (White & Orange)
css = css.replace('--bg-dark: #050505;', '--bg-dark: #ffffff;')
css = css.replace('--bg-card: rgba(20, 20, 25, 0.6);', '--bg-card: rgba(255, 255, 255, 0.7);')
css = css.replace('--border-color: rgba(255, 255, 255, 0.08);', '--border-color: rgba(0, 0, 0, 0.06);')
css = css.replace('--text-main: #f3f4f6;', '--text-main: #1a1a1a;')
css = css.replace('--text-muted: #9ca3af;', '--text-muted: #6b7280;')

# Accents (Orange)
css = css.replace('--primary: #6366f1;', '--primary: #ff7043;') # Orange-Red
css = css.replace('--primary-hover: #4f46e5;', '--primary-hover: #f4511e;')
css = css.replace('--secondary: #8b5cf6;', '--secondary: #ffa726;') # Orange-Yellow
css = css.replace('--accent: #ec4899;', '--accent: #ff6d00;') # Vivid Orange

# 2. Update Hardcoded Colors in Gradients
css = css.replace('rgba(99, 102, 241, 0.15)', 'rgba(255, 112, 67, 0.12)') # Glow 1
css = css.replace('rgba(236, 72, 153, 0.1)', 'rgba(255, 109, 0, 0.08)') # Glow 2
css = css.replace('rgba(5, 5, 5, 0)', 'rgba(255, 255, 255, 0)') # Gradient end

# 3. Update Navbar and Buttons for Light Theme
css = css.replace('background: rgba(5, 5, 5, 0.85);', 'background: rgba(255, 255, 255, 0.9);')
css = css.replace('background: rgba(255, 255, 255, 0.05);', 'background: rgba(0, 0, 0, 0.05);')
css = css.replace('background: rgba(255, 255, 255, 0.1);', 'background: rgba(0, 0, 0, 0.08);')
css = css.replace('background: rgba(255, 255, 255, 0.2);', 'background: rgba(0, 0, 0, 0.12);')

# 4. Update Dashboard Mockup (invert colors)
css = css.replace('background: rgba(255,255,255,0.02);', 'background: rgba(0,0,0,0.02);')
css = css.replace('background: rgba(255,255,255,0.01);', 'background: rgba(0,0,0,0.01);')
css = css.replace('background: rgba(255,255,255,0.03);', 'background: rgba(0,0,0,0.03);')
css = css.replace('border: 1px solid rgba(255,255,255,0.05);', 'border: 1px solid rgba(0,0,0,0.05);')
css = css.replace('background: rgba(255,255,255,0.1);', 'background: rgba(0,0,0,0.05);')
css = css.replace('border-bottom: 1px solid rgba(255,255,255,0.1);', 'border-bottom: 1px solid rgba(0,0,0,0.05);')
css = css.replace('background: rgba(255,255,255,0.05);', 'background: rgba(0,0,0,0.05);')
css = css.replace('border-radius: 6px;', 'border-radius: 6px; background: rgba(0,0,0,0.1);') # Fix sidebar nav item background

# 5. Update Footer and other sections
css = css.replace('background: #000;', 'background: #f9fafb;')
css = css.replace('color: #fff;', 'color: #1a1a1a;')
css = css.replace('border-top: 1px solid rgba(255,255,255,0.05);', 'border-top: 1px solid rgba(0,0,0,0.05);')
css = css.replace('background: rgba(0,0,0,0.3);', 'background: rgba(255,255,255,0.8);') # Feature row

# 6. Mouse Glow update
css = css.replace('rgba(99, 102, 241, 0.08)', 'rgba(255, 112, 67, 0.08)')

with open('index.css', 'w', encoding='utf-8') as f:
    f.write(css)
