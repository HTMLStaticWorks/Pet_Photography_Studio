import os
import re

directory = '.'

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # We will look for Home 2 link inside the footer. It is probably in the Quick Links list.
        # The exact string depends on what it was. 
        # Let's use a regex to find 'Home 2' in the footer area. Or just simply replace the list item.
        # It's likely something like: <li><a href="home-2.html" class="hover:text-studio-400 transition-colors">Home 2</a></li>
        
        # Let's remove any line containing "Home 2" that is within a list (<li>) in the footer
        # A simpler approach: remove the exact string.
        # Let's check what it looks like exactly.
        
        # We can just remove: <li><a href="home-2.html" class="text-gray-400 hover:text-white transition-colors">Home 2</a></li>
        # or similar.
        
        # Let's replace any `<li><a href="home-2.html"...>Home 2</a></li>` in the file.
        new_content = re.sub(r'<li[^>]*>\s*<a[^>]*href="home-2\.html"[^>]*>Home 2</a>\s*</li>', '', content)
        
        # Wait, if they just added it as `<li><a href="home-2.html"...>Home 2</a></li>`, the regex will match.
        # Let's also check if it's on the same line as Home. Sometimes it's `<li><a href="index.html">Home</a></li> <li><a href="home-2.html">Home 2</a></li>`
        # Wait! The previous screenshot showed "Home Home 2" as Quick Links!
        # Ah, in my earlier `add_nav_links.py` I might have just replaced `Home` with `Home Home 2`!
        new_content = re.sub(r'<a href="home-2\.html"[^>]*>Home 2</a>', '', new_content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed Home 2 from {filename}")

print("Done.")
