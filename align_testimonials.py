import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the cards flex columns
old_card_class = r'class="bg-white dark:bg-neutral-900 p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800 hover:-translate-y-1 transition-transform duration-300"'
new_card_class = r'class="bg-white dark:bg-neutral-900 p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800 hover:-translate-y-1 transition-transform duration-300 flex flex-col"'

content = content.replace(
    'bg-white dark:bg-neutral-900 p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800 hover:-translate-y-1 transition-transform duration-300"',
    'bg-white dark:bg-neutral-900 p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800 hover:-translate-y-1 transition-transform duration-300 flex flex-col"'
)

# Push the avatar container to the bottom
content = content.replace(
    '<div class="flex items-center">',
    '<div class="flex items-center mt-auto">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Testimonials aligned properly.")
