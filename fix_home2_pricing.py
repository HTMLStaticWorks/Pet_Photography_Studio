import re

with open('home-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(
    r'(<h3 class="text-2xl font-semibold mb-4[^>]*>[^<]+</h3>)\s*'
    r'(<p class="[^"]*mb-6[^"]*">.*?</p>)\s*'
    r'(<ul class="space-y-3 mb-8[^"]*">.*?</ul>)\s*'
    r'(<a href="dashboard\.html" class="block w-full py-3 px-4 mt-auto [^"]+">Explore Package</a>)',
    re.DOTALL
)

def replacer(match):
    h3 = match.group(1)
    p = match.group(2)
    ul = match.group(3)
    a = match.group(4)
    a_fixed = a.replace('mt-auto ', '')
    return f'{h3}\n                        <div class="mt-auto w-full">\n                            {p}\n                            {ul}\n                            {a_fixed}\n                        </div>'

content = pattern.sub(replacer, content)

with open('home-2.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed home-2.html pricing cards")
