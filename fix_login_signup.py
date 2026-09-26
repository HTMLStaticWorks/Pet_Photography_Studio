import re

for filename in ['signup.html', 'login.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix the toggle password button
    content = content.replace('absolute inset-y-0 right-0 px-4', 'absolute inset-y-0 right-0 rtl:left-0 rtl:right-auto px-4')
    
    # Fix the checkbox gap
    # Instead of ml-2 rtl:mr-2 rtl:ml-0 on label, we put gap-x-2 on the parent.
    
    # login: <div class="flex items-center">
    # signup: <div class="flex items-start pt-2">
    content = content.replace('<div class="flex items-center">\n                    <input type="checkbox"', 
                              '<div class="flex items-center gap-x-2">\n                    <input type="checkbox"')
                              
    content = content.replace('<div class="flex items-start pt-2">\n                    <input type="checkbox"', 
                              '<div class="flex items-start gap-x-2 pt-2">\n                    <input type="checkbox"')
                              
    # Remove the margins from the label
    content = content.replace('class="ml-2 rtl:mr-2 rtl:ml-0 text-sm', 'class="text-sm')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated ' + filename)
