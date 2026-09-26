import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Gallery - 3rd item starts with '<img src="https://images.unsplash.com/photo-1548199973-03cce0bbc87b'
# Let's find that 3rd card's opening div:
content = re.sub(
    r'(<div class="group relative rounded-3xl overflow-hidden aspect-\[4/5\] shadow-xl)(">\s*<img src="https://images.unsplash.com/photo-1548199973-03cce0bbc87b)',
    r'\1 md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto lg:col-span-1 lg:w-full lg:mx-0\2',
    content
)

# 2. Testimonials - 3rd item starts with '<p class="text-gray-600 dark:text-gray-400 mb-6 italic">"The lifestyle session at our home was perfect.'
content = re.sub(
    r'(<div class="bg-white dark:bg-neutral-900 p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800 hover:-translate-y-1 transition-transform duration-300 flex flex-col h-full)(">\s*<div class="flex text-yellow-400 mb-4">\s*<i class="fas fa-star"></i>\s*<i class="fas fa-star"></i>\s*<i class="fas fa-star"></i>\s*<i class="fas fa-star"></i>\s*<i class="fas fa-star"></i>\s*</div>\s*<p class="text-gray-600 dark:text-gray-400 mb-6 italic">"The lifestyle session at our home was perfect.)',
    r'\1 md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto lg:col-span-1 lg:w-full lg:mx-0\2',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html grids")
