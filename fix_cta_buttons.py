import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's target all anchor tags and button tags that have bg-studio-600
    # and don't already have whitespace-nowrap
    
    def replacer(match):
        class_str = match.group(2)
        if 'whitespace-nowrap' not in class_str:
            new_class = class_str + ' whitespace-nowrap'
            return f'{match.group(1)}"{new_class}"'
        return match.group(0)

    # Regex to find class attribute in <a> or <button> tags with bg-studio-600
    new_content = re.sub(r'(<(?:a|button)[^>]*?class=)"([^"]*bg-studio-600[^"]*)"', replacer, content, flags=re.IGNORECASE)
    
    # Also target any "Explore Package" / "Explore Sessions" buttons that might have different backgrounds (like the secondary CTA in index.html)
    new_content = re.sub(r'(<(?:a|button)[^>]*?class=)"([^"]*bg-gray-50[^"]*hover:bg-studio-50[^"]*)"', replacer, new_content, flags=re.IGNORECASE)

    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Added whitespace-nowrap in ' + f)
