import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content
    
    # Replace me- with mr- and rtl modifiers
    new_content = re.sub(r'\bme-([a-z0-9\.]+)\b', r'mr-\1 rtl:ml-\1 rtl:mr-0', new_content)
    
    # Replace ms- with ml- and rtl modifiers
    new_content = re.sub(r'\bms-([a-z0-9\.]+)\b', r'ml-\1 rtl:mr-\1 rtl:ml-0', new_content)
    
    # Replace pe- with pr- and rtl modifiers
    new_content = re.sub(r'\bpe-([a-z0-9\.]+)\b', r'pr-\1 rtl:pl-\1 rtl:pr-0', new_content)
    
    # Replace ps- with pl- and rtl modifiers
    new_content = re.sub(r'\bps-([a-z0-9\.]+)\b', r'pl-\1 rtl:pr-\1 rtl:pl-0', new_content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Updated ' + f)
