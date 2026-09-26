import os
import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacement for Header/Dashboard
    old_logo_1 = r'<a href="index.html" class="text-2xl font-bold text-studio-900 dark:text-studio-200">\s*Paws & <span class="text-studio-500">Pose</span>\s*</a>'
    new_logo_1 = r'''<a href="index.html" class="flex items-center text-2xl font-bold text-studio-900 dark:text-studio-200">
                        <i class="fas fa-paw text-studio-500 mr-2 text-2xl"></i>
                        Paws & <span class="text-studio-500 ml-1">Pose</span>
                    </a>'''
    
    # Replacement for Login/Signup block
    old_logo_2 = r'<a href="index.html" class="text-3xl font-bold text-studio-900 dark:text-studio-200 mb-2 block">\s*Paws & <span class="text-studio-500">Pose</span>\s*</a>'
    new_logo_2 = r'''<a href="index.html" class="flex items-center justify-center lg:justify-start text-3xl font-bold text-studio-900 dark:text-studio-200 mb-2 block">
                    <i class="fas fa-paw text-studio-500 mr-2 text-3xl"></i>
                    Paws & <span class="text-studio-500 ml-1">Pose</span>
                </a>'''

    # Replacement for Login/Signup inline-block (if any)
    old_logo_3 = r'<a href="index.html" class="text-3xl font-bold text-studio-900 dark:text-studio-200 mb-2 inline-block">\s*Paws & <span class="text-studio-500">Pose</span>\s*</a>'
    new_logo_3 = r'''<a href="index.html" class="flex items-center justify-center lg:justify-start text-3xl font-bold text-studio-900 dark:text-studio-200 mb-2 inline-block">
                    <i class="fas fa-paw text-studio-500 mr-2 text-3xl"></i>
                    Paws & <span class="text-studio-500 ml-1">Pose</span>
                </a>'''

    # Footer logo replacement
    old_footer_logo = r'<a href="index.html" class="text-2xl font-bold text-white">\s*Paws & <span class="text-studio-400">Pose</span>\s*</a>'
    new_footer_logo = r'''<a href="index.html" class="flex items-center text-2xl font-bold text-white">
                        <i class="fas fa-paw text-studio-400 mr-2 text-2xl"></i>
                        Paws & <span class="text-studio-400 ml-1">Pose</span>
                    </a>'''

    content = re.sub(old_logo_1, new_logo_1, content)
    content = re.sub(old_logo_2, new_logo_2, content)
    content = re.sub(old_logo_3, new_logo_3, content)
    content = re.sub(old_footer_logo, new_footer_logo, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Logos updated successfully.")
