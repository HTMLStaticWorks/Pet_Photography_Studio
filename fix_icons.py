import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for the old theme toggle in normal nav bar
    old_theme = r'<button class="theme-toggle text-gray-500 dark:text-gray-400 hover:text-studio-500 focus:outline-none">\s*<i class="fas fa-moon dark:hidden"></i>\s*<i class="fas fa-sun hidden dark:block"></i>\s*</button>'
    new_theme = r'''<button class="theme-toggle w-10 h-10 flex items-center justify-center text-gray-500 dark:text-gray-400 hover:text-studio-500 hover:bg-gray-100 dark:hover:bg-neutral-800 rounded-full transition-colors focus:outline-none">
                        <i class="fas fa-moon text-lg dark:hidden"></i>
                        <i class="fas fa-sun text-lg hidden dark:block"></i>
                    </button>'''

    # Pattern for the old RTL toggle in normal nav bar
    old_rtl = r'<button class="rtl-toggle text-gray-500 dark:text-gray-400 hover:text-studio-500 font-medium">RTL</button>'
    new_rtl = r'''<button class="rtl-toggle w-10 h-10 flex items-center justify-center text-gray-500 dark:text-gray-400 hover:text-studio-500 hover:bg-gray-100 dark:hover:bg-neutral-800 rounded-full font-bold text-sm transition-colors focus:outline-none">RTL</button>'''

    content = re.sub(old_theme, new_theme, content)
    content = re.sub(old_rtl, new_rtl, content)

    # Let's also fix login/signup which had a slightly different markup
    old_login_theme = r'<button class="theme-toggle text-gray-500 hover:text-studio-500"><i class="fas fa-adjust"></i></button>'
    new_login_theme = r'''<button class="theme-toggle w-10 h-10 flex items-center justify-center text-gray-500 hover:text-studio-500 hover:bg-gray-100 dark:hover:bg-neutral-800 rounded-full transition-colors focus:outline-none">
            <i class="fas fa-moon text-lg dark:hidden"></i>
            <i class="fas fa-sun text-lg hidden dark:block"></i>
        </button>'''
    
    old_login_rtl = r'<button class="rtl-toggle text-gray-500 font-semibold text-xs hover:text-studio-500">RTL</button>'
    new_login_rtl = r'''<button class="rtl-toggle w-10 h-10 flex items-center justify-center text-gray-500 hover:text-studio-500 hover:bg-gray-100 dark:hover:bg-neutral-800 rounded-full font-bold text-sm transition-colors focus:outline-none">RTL</button>'''

    content = re.sub(old_login_theme, new_login_theme, content)
    content = re.sub(old_login_rtl, new_login_rtl, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Icons size fixed.")
