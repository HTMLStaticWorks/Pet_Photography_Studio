import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content
    
    # Let's fix the theme toggle in the mobile menu (Button 2)
    new_content = re.sub(
        r'<button class="theme-toggle w-10 h-10([^"]*)"([^>]*)><i class="fas fa-adjust"></i> Theme</button>',
        r'<button class="theme-toggle w-auto h-10 px-4 gap-x-2\1"\2><i class="fas fa-adjust"></i> Theme</button>',
        new_content
    )
    
    # Let's fix the RTL toggle in the mobile menu (Button 3)
    new_content = re.sub(
        r'<button class="rtl-toggle w-10 h-10([^"]*)"([^>]*)><i class="fas fa-exchange-alt"></i> RTL</button>',
        r'<button class="rtl-toggle w-auto h-10 px-4 gap-x-2\1"\2><i class="fas fa-exchange-alt"></i> RTL</button>',
        new_content
    )
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Updated mobile toggles in ' + f)
