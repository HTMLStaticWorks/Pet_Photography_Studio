import os
import re

directory = '.'

for filename in os.listdir(directory):
    if filename.endswith('.html') and filename != 'dashboard.html':
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex for Desktop Nav: look for <a href="index.html" ...>Home</a>
        # and insert Home 2 right after it.
        
        desktop_pattern = r'(<a href="index\.html"[^>]*>Home</a>)'
        # Before we insert, check if it's already there to avoid duplicates
        if 'href="home-2.html"' not in content:
            # wait, it might be in the mobile nav already. Let's just find the first desktop nav Home link.
            # Actually, let's just do a targeted replace for desktop nav
            content = re.sub(
                r'(<a href="index\.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium[^>]*>Home</a>)',
                r'\1\n                    <a href="home-2.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium transition-colors">Home 2</a>',
                content
            )
            
            # Mobile nav
            content = re.sub(
                r'(<a href="index\.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-200 hover:text-studio-600 hover:bg-studio-50 dark:hover:bg-neutral-800[^>]*>Home</a>)',
                r'\1\n                <a href="home-2.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-200 hover:text-studio-600 hover:bg-studio-50 dark:hover:bg-neutral-800 transition-colors">Home 2</a>',
                content
            )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed Home 2 in nav of {filename}")

print("Done.")
