import re

for filename in ['index.html', 'home-2.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # First, let's remove the centering classes from ALL cards in the pricing grid just to be safe.
    # The centering string is: ` md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto lg:col-span-1 lg:w-full lg:mx-0`
    content = content.replace(' md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto lg:col-span-1 lg:w-full lg:mx-0', '')

    # Now, we specifically want to add it ONLY to the 3rd card (The Lifestyle Home).
    # The Lifestyle Home starts with:
    marker = 'h-full">\n                        <div class="w-16 h-16 bg-studio-100 dark:bg-studio-900/30 rounded-2xl flex items-center justify-center mb-6">\n                            <i class="fas fa-home'
    
    replacement = 'h-full md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto lg:col-span-1 lg:w-full lg:mx-0">\n                        <div class="w-16 h-16 bg-studio-100 dark:bg-studio-900/30 rounded-2xl flex items-center justify-center mb-6">\n                            <i class="fas fa-home'
    
    content = content.replace(marker, replacement)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed pricing cards centering")
