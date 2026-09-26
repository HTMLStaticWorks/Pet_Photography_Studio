import os
import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop Nav update
    desktop_nav_search = r'(<a href="index.html" class="[^"]*">Home</a>)'
    desktop_nav_replace = r'\1\n                    <a href="home-2.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium">Home 2</a>\n                    <a href="dashboard.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium">Dashboard</a>'
    
    # Mobile Nav update
    mobile_nav_search = r'(<a href="index.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">Home</a>)'
    mobile_nav_replace = r'\1\n                <a href="home-2.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">Home 2</a>\n                <a href="dashboard.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">Dashboard</a>'

    content = re.sub(desktop_nav_search, desktop_nav_replace, content)
    content = re.sub(mobile_nav_search, mobile_nav_replace, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Nav links updated successfully.")
