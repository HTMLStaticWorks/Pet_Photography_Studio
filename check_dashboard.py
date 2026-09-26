import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.finditer(r'<h4 class="font-bold text-lg mb-2">(.*?)</h4>(.*?)</button>', content, re.DOTALL)
for m in matches:
    print('---', m.group(1), '---')
    print(m.group(2))
