import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add logo images to each card's icon area
cards = {
    'fmcg-card': ('https://logo.clearbit.com/radico.co.in', 'RK', 'Radico Khaitan'),
    'auto-card': ('https://logo.clearbit.com/marutisuzuki.com', 'MS', 'Maruti Suzuki'),
    'cv-card': ('https://logo.clearbit.com/eichermotors.com', 'EM', 'Eicher + Ashok Leyland'),
    'finance-card': ('https://logo.clearbit.com/idfcfirstbank.com', 'IDFC', 'IDFC First Bank'),
    'edu-card': ('https://logo.clearbit.com/lpu.in', 'LPU', 'LPU'),
}

for card_id, (logo_url, initials, name) in cards.items():
    # Find the card icon area and replace with logo image
    old_pattern = f'id="{card_id}">\n                        <div class="card-icon"><i class="ph ph-'
    # Use regex to find and replace the icon in each card
    pattern = rf'(id="{card_id}">[\s\n]+)<div class="card-icon"><i class="[^"]+"></i></div>'
    replacement = rf'\1<div class="card-logo-header"><img src="{logo_url}" onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'" alt="{name}" class="card-client-logo"><span class="card-logo-fallback">{initials}</span></div>'
    content = re.sub(pattern, replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Card logos updated')
