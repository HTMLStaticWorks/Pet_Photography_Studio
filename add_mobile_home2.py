import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to find the mobile menu Home link and insert Home 2 after it.
    # We'll specifically look for:
    # <a href="index.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">Home</a>
    
    search_str = '<a href="index.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">Home</a>'
    insert_str = '\n                <a href="home-2.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">Home 2</a>'
    
    # But wait, index.html might have active classes for Home depending on the page?
    # Actually, script.js handles the active classes for BOTH desktop and mobile dynamically!
    # So the HTML just has the default classes for all links.
    
    if search_str in content and 'href="home-2.html"' not in content.split(search_str)[1][:200]:
        new_content = content.replace(search_str, search_str + insert_str)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Updated ' + f)
