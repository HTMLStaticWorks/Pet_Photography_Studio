import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace('mr-2 text-2xl', 'me-2 text-2xl')
    new_content = new_content.replace('mr-2 text-3xl', 'me-2 text-3xl')
    new_content = new_content.replace('ml-1">Pose', 'ms-1">Pose')
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Updated ' + f)
