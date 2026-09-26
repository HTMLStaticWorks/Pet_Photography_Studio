with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the 3rd card
# Card 1 has title: 5 Tips for a Stress-Free Pet Photo Session
# Card 2 has title: The Importance of Lighting in Pet Photography
# Card 3 has title: What to Wear to Your Pet's Photo Session

import re
content = re.sub(
    r'(<div class="bg-white dark:bg-neutral-900 rounded-3xl overflow-hidden shadow-sm border border-gray-100 dark:border-neutral-800 hover:shadow-md transition-shadow group)([^>]*>\s*<div class="relative h-64 overflow-hidden">\s*<img src="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba)',
    r'\1 md:col-span-2 md:w-[calc(50%-1.25rem)] md:mx-auto lg:col-span-1 lg:w-full lg:mx-0\2',
    content
)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated blog.html")
