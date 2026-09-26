import re

with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the main card flex flex-col
old_card_class = r'class="group bg-gray-50 dark:bg-neutral-950 rounded-2xl overflow-hidden border border-gray-100 dark:border-neutral-800 hover:shadow-lg transition-all duration-300"'
new_card_class = r'class="group bg-gray-50 dark:bg-neutral-950 rounded-2xl overflow-hidden border border-gray-100 dark:border-neutral-800 hover:shadow-lg transition-all duration-300 flex flex-col"'
content = content.replace(
    'class="group bg-gray-50 dark:bg-neutral-950 rounded-2xl overflow-hidden border border-gray-100 dark:border-neutral-800 hover:shadow-lg transition-all duration-300"',
    'class="group bg-gray-50 dark:bg-neutral-950 rounded-2xl overflow-hidden border border-gray-100 dark:border-neutral-800 hover:shadow-lg transition-all duration-300 flex flex-col"'
)

# Make the padding div flex-1 flex flex-col
content = content.replace(
    '<div class="p-8">',
    '<div class="p-8 flex-1 flex flex-col">'
)

# Push the "Read More" button down
content = content.replace(
    '<a href="#" class="text-studio-600 dark:text-studio-400 font-semibold text-sm hover:underline flex items-center">Read More',
    '<a href="#" class="text-studio-600 dark:text-studio-400 font-semibold text-sm hover:underline flex items-center mt-auto">Read More'
)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Blog cards aligned properly.")
