import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content
    
    # We will search for any button that has `theme-toggle` or `rtl-toggle` and also has text like `Theme` or `RTL` inside it
    # Then we replace `w-10 h-10` with `w-auto h-10 px-4 gap-x-2`
    
    # Let's define a function to replace w-10 h-10
    def replacer(match):
        button_tag = match.group(0)
        # If the button contains text "Theme" or "RTL"
        if re.search(r'>\s*(?:<[^>]+>\s*)*Theme\s*</button>', button_tag, re.IGNORECASE) or \
           re.search(r'>\s*(?:<[^>]+>\s*)*RTL\s*</button>', button_tag, re.IGNORECASE):
            # Replace w-10 h-10
            return re.sub(r'\bw-10\s+h-10\b', 'w-auto h-10 px-4 gap-x-2', button_tag)
        return button_tag

    new_content = re.sub(r'<button class="[^"]*(?:theme-toggle|rtl-toggle)[^"]*".*?</button>', replacer, new_content, flags=re.DOTALL)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Updated mobile toggles in ' + f)
