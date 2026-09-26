import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace('class="hidden md:flex space-x-8"', 'class="hidden lg:flex space-x-8"')
    new_content = new_content.replace('class="hidden md:flex items-center space-x-4"', 'class="hidden lg:flex items-center space-x-4"')
    new_content = new_content.replace('class="md:hidden flex items-center"', 'class="lg:hidden flex items-center"')
    new_content = new_content.replace('class="hidden md:hidden', 'class="hidden lg:hidden')
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Updated ' + f)
