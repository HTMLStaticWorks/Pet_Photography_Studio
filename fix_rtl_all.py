import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content
    
    # specific fix for the footer missing flex
    new_content = new_content.replace('class="space-x-4 mt-4 md:mt-0"', 'class="flex space-x-4 mt-4 md:mt-0"')
    
    # Global margin/padding replacements
    new_content = re.sub(r'\bmr-([0-9a-z\.]+)\b', r'me-\1', new_content)
    new_content = re.sub(r'\bml-([0-9a-z\.]+)\b', r'ms-\1', new_content)
    new_content = re.sub(r'\bpr-([0-9a-z\.]+)\b', r'pe-\1', new_content)
    new_content = re.sub(r'\bpl-([0-9a-z\.]+)\b', r'ps-\1', new_content)
    
    # Global space-x to gap-x replacements
    new_content = re.sub(r'\bspace-x-([0-9a-z\.]+)\b', r'gap-x-\1', new_content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Updated ' + f)
