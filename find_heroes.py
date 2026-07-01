import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        hero_match = re.search(r'<section class=\"(.*?bg-gradient.*?)\"', content)
        if hero_match:
            print(f'File: {f}')
            print(f'Match: {hero_match.group(1)}')
