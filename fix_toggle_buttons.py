import os
import re

directory = '.'

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # replace theme-toggle class
        content = re.sub(
            r'class="theme-toggle[^"]+"',
            'class="theme-toggle w-10 h-10 flex items-center justify-center text-gray-500 dark:text-gray-400 hover:text-studio-500 bg-white dark:bg-neutral-900 border border-gray-200 dark:border-neutral-700 shadow-sm hover:border-studio-300 dark:hover:border-studio-700 rounded-full transition-all focus:outline-none"',
            content
        )
        
        # replace rtl-toggle class
        content = re.sub(
            r'class="rtl-toggle[^"]+"',
            'class="rtl-toggle w-10 h-10 flex items-center justify-center text-gray-500 dark:text-gray-400 hover:text-studio-500 bg-white dark:bg-neutral-900 border border-gray-200 dark:border-neutral-700 shadow-sm hover:border-studio-300 dark:hover:border-studio-700 rounded-full font-bold text-xs transition-all focus:outline-none"',
            content
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done fixing toggle buttons.")
