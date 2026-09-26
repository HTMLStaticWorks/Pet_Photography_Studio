import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for index.html cards
# They look like:
# <h3 class="...">Title</h3>
# <p class="...">...</p>
# <ul class="...">...</ul>
# <a class="... mt-auto ...">...</a>

# I'll use a regex replacement to wrap the p, ul, and a tags in an mt-auto div.

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
    # Remove mt-auto from the anchor since we put it on the wrapper
    a_fixed = a.replace('mt-auto ', '')
    return f'{h3}\n                        <div class="mt-auto w-full">\n                            {p}\n                            {ul}\n                            {a_fixed}\n                        </div>'

new_content = pattern.sub(replacer, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html cards")
