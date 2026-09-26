import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if home-2.html is already in the mobile menu
    if 'href="home-2.html"' not in content or 'mobile-menu' not in content:
        # It might be in the desktop menu, we need to make sure it's in the mobile menu.
        pass
    
    # Find the mobile menu block
    start_mobile = content.find('id="mobile-menu"')
    if start_mobile == -1:
        continue
        
    end_mobile = content.find('</header>', start_mobile)
    if end_mobile == -1:
        # dashboard uses different structure maybe?
        end_mobile = content.find('</nav>', start_mobile)
        if end_mobile == -1:
            end_mobile = start_mobile + 2000
    
    mobile_menu = content[start_mobile:end_mobile]
    
    if 'href="home-2.html"' not in mobile_menu:
        # Let's find the Home link in the mobile menu
        pattern = re.compile(r'(<a\s+href="index\.html"[^>]*>Home</a>)', re.DOTALL)
        
        insert_str = '\n                <a href="home-2.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">Home 2</a>'
        
        # We only want to replace the FIRST occurrence in the mobile_menu
        new_mobile_menu = pattern.sub(r'\1' + insert_str, mobile_menu, count=1)
        
        new_content = content[:start_mobile] + new_mobile_menu + content[end_mobile:]
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print('Updated ' + f)
