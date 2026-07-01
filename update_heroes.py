import os
import re

files = {
    'index.html': 'hero_sharpening.png',
    'home2.html': 'mobile_workshop.png',
    'about.html': 'Ab1.jpg',
    'service.html': 'sharping.jpg',
    'repair.html': 'knife_bef.jpg',
    'pricing.html': 'knife.jpg',
    'gallery.html': 'polish.jpg',
    'doorstep.html': 'doorstep_van.png',
    'contact.html': 'explore_services.png',
    'book.html': 'Ab2.jpg'
}

for f, img in files.items():
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if f == 'home2.html':
        content = re.sub(
            r'<section class=\"relative min-h-screen flex items-center pt-28 pb-16 overflow-hidden hero-section\">',
            f'<section class="relative min-h-screen flex items-center pt-28 pb-16 overflow-hidden bg-cover bg-center" style="background-image: linear-gradient(rgba(11, 26, 46, 0.7), rgba(11, 26, 46, 0.9)), url(\'assests/{img}\');">',
            content
        )
    else:
        content = re.sub(
            r'<section class=\"(relative pt-40 pb-28 md:pt-52 md:pb-36 overflow-hidden) bg-gradient-to-br from-edge-primary via-edge-primary to-edge-dark\">',
            f'<section class="\\1 bg-cover bg-center" style="background-image: linear-gradient(rgba(11, 26, 46, 0.7), rgba(11, 26, 46, 0.9)), url(\'assests/{img}\');">',
            content
        )
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Hero backgrounds updated successfully.")
