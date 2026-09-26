import os
import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Move Dashboard before Contact in desktop nav
    # Current sequence has Dashboard before About
    # We will just extract Dashboard link, remove it, and insert it before Contact
    
    dashboard_desktop_link_pattern = r'\n\s*<a href="dashboard\.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium">Dashboard</a>'
    
    if re.search(dashboard_desktop_link_pattern, content):
        dashboard_desktop_match = re.search(dashboard_desktop_link_pattern, content).group(0)
        content = re.sub(dashboard_desktop_link_pattern, '', content)
        
        contact_desktop_pattern = r'(<a href="contact\.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium">Contact</a>)'
        content = re.sub(contact_desktop_pattern, dashboard_desktop_match.lstrip('\n') + r'\n                    \1', content)

    
    dashboard_mobile_link_pattern = r'\n\s*<a href="dashboard\.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">Dashboard</a>'
    
    if re.search(dashboard_mobile_link_pattern, content):
        dashboard_mobile_match = re.search(dashboard_mobile_link_pattern, content).group(0)
        content = re.sub(dashboard_mobile_link_pattern, '', content)
        
        contact_mobile_pattern = r'(<a href="contact\.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">Contact</a>)'
        content = re.sub(contact_mobile_pattern, dashboard_mobile_match.lstrip('\n') + r'\n                \1', content)
        

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Nav links reordered successfully.")
