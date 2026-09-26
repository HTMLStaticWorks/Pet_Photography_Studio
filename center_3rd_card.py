import glob

# For index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('grid grid-cols-1 md:grid-cols-3 gap-8', 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8')
# The 3rd card in index starts with: <div class="bg-white dark:bg-neutral-900 rounded-3xl p-10 shadow-lg border border-gray-100 dark:border-neutral-800 hover:-translate-y-2 transition-transform duration-300 flex flex-col h-full">
content = content.replace(
    '<div class="bg-white dark:bg-neutral-900 rounded-3xl p-10 shadow-lg border border-gray-100 dark:border-neutral-800 hover:-translate-y-2 transition-transform duration-300 flex flex-col h-full">',
    '<div class="bg-white dark:bg-neutral-900 rounded-3xl p-10 shadow-lg border border-gray-100 dark:border-neutral-800 hover:-translate-y-2 transition-transform duration-300 flex flex-col h-full md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto lg:col-span-1 lg:w-full lg:mx-0">'
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


# For home-2.html
with open('home-2.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('grid grid-cols-1 md:grid-cols-3 gap-8', 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8')
content = content.replace(
    '<div class="bg-white dark:bg-neutral-900 rounded-3xl p-10 shadow-lg border border-gray-100 dark:border-neutral-800 hover:-translate-y-2 transition-transform duration-300 flex flex-col h-full">',
    '<div class="bg-white dark:bg-neutral-900 rounded-3xl p-10 shadow-lg border border-gray-100 dark:border-neutral-800 hover:-translate-y-2 transition-transform duration-300 flex flex-col h-full md:col-span-2 md:w-[calc(50%-1rem)] md:mx-auto lg:col-span-1 lg:w-full lg:mx-0">'
)
with open('home-2.html', 'w', encoding='utf-8') as f:
    f.write(content)


# For dashboard.html
with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('grid grid-cols-1 md:grid-cols-3 gap-6', 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6')
# In dashboard.html the 3rd card is Lifestyle Home: <div class="border border-gray-200 dark:border-neutral-800 rounded-2xl p-6 hover:border-studio-500 cursor-pointer transition-colors flex flex-col h-full">
# BUT wait, the 1st card also has that exact same class string!
content = content.replace(
    '<h4 class="font-bold text-lg mb-2">Lifestyle Home</h4>',
    '__LIFESTYLE_HOME_MARKER__'
)
# Since we need to modify the parent, let's use regex for dashboard.html
import re
content = re.sub(
    r'<div class="border border-gray-200 dark:border-neutral-800 rounded-2xl p-6 hover:border-studio-500 cursor-pointer transition-colors flex flex-col h-full">\s*__LIFESTYLE_HOME_MARKER__',
    '<div class="border border-gray-200 dark:border-neutral-800 rounded-2xl p-6 hover:border-studio-500 cursor-pointer transition-colors flex flex-col h-full md:col-span-2 md:w-[calc(50%-0.75rem)] md:mx-auto lg:col-span-1 lg:w-full lg:mx-0">\n                                    <h4 class="font-bold text-lg mb-2">Lifestyle Home</h4>',
    content
)
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)


# For about.html
with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('grid grid-cols-1 md:grid-cols-3 gap-12', 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12')
# The 3rd card contains "Step 3"
content = content.replace(
    '<span class="text-6xl font-bold text-gray-100 dark:text-neutral-800/50 absolute -top-6 -left-6 z-0">03</span>',
    '__STEP3_MARKER__'
)
content = re.sub(
    r'<div class="relative bg-white dark:bg-neutral-900 p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800 text-center">\s*__STEP3_MARKER__',
    '<div class="relative bg-white dark:bg-neutral-900 p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800 text-center md:col-span-2 md:w-[calc(50%-1.5rem)] md:mx-auto lg:col-span-1 lg:w-full lg:mx-0">\n                        <span class="text-6xl font-bold text-gray-100 dark:text-neutral-800/50 absolute -top-6 -left-6 z-0">03</span>',
    content
)
with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated all grids")
