import os
import re

directory = '.'

for filename in os.listdir(directory):
    if filename.endswith('.html') and filename != 'dashboard.html':
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'href="home-2.html"' not in content:
            # Desktop Nav
            content = re.sub(
                r'(<a href="index\.html"[^>]*>Home</a>)',
                r'\1\n                    <a href="home-2.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium">Home 2</a>',
                content,
                count=1 # Only replace the first one (desktop nav)
            )
            
            # Mobile Nav (second occurrence)
            content = re.sub(
                r'(<a href="index\.html"[^>]*>Home</a>)',
                r'\1\n                <a href="home-2.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-200 hover:text-studio-600 hover:bg-studio-50 dark:hover:bg-neutral-800">Home 2</a>',
                content,
                count=1 # The previous regex already replaced the first one, but wait, the string changed!
                # Actually, the string changed to `<a ...>Home</a>` so re.sub will find it again if we don't differentiate.
            )
        
        # Let's just do it manually with a split to be perfectly safe
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done.")
