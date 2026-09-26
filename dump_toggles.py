import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

buttons = re.findall(r'<button class="[^"]*(?:theme-toggle|rtl-toggle)[^"]*".*?</button>', content, re.DOTALL)
for i, b in enumerate(buttons):
    print(f'Button {i}:')
    print(b)
    print('-'*20)
