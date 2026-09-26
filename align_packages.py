import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update first card
content = content.replace(
    'class="bg-white dark:bg-neutral-900 rounded-3xl p-10 shadow-lg border border-gray-100 dark:border-neutral-800 hover:-translate-y-2 transition-transform duration-300"',
    'class="bg-white dark:bg-neutral-900 rounded-3xl p-10 shadow-lg border border-gray-100 dark:border-neutral-800 hover:-translate-y-2 transition-transform duration-300 flex flex-col"'
)

# 2. Update second card
content = content.replace(
    'class="bg-neutral-900 dark:bg-neutral-950 rounded-3xl p-10 shadow-xl border border-neutral-800 relative transform md:-translate-y-4"',
    'class="bg-neutral-900 dark:bg-neutral-950 rounded-3xl p-10 shadow-xl border border-neutral-800 relative hover:-translate-y-2 transition-transform duration-300 flex flex-col"'
)

# 3. Update third card
content = content.replace(
    'class="bg-white dark:bg-neutral-900 rounded-3xl p-10 shadow-lg border border-gray-100 dark:border-neutral-800 hover:-translate-y-2 transition-transform duration-300"',
    'class="bg-white dark:bg-neutral-900 rounded-3xl p-10 shadow-lg border border-gray-100 dark:border-neutral-800 hover:-translate-y-2 transition-transform duration-300 flex flex-col"'
)

# 4. Push the buttons to the bottom by giving the ul mb-auto OR button mt-auto
content = content.replace(
    '<a href="dashboard.html" class="block w-full py-3 px-4 bg-gray-50 dark:bg-neutral-800 hover:bg-studio-50 text-center font-medium rounded-xl transition-colors text-studio-600 dark:text-studio-400 border border-gray-200 dark:border-neutral-700">Explore Package</a>',
    '<a href="dashboard.html" class="block w-full py-3 px-4 mt-auto bg-gray-50 dark:bg-neutral-800 hover:bg-studio-50 text-center font-medium rounded-xl transition-colors text-studio-600 dark:text-studio-400 border border-gray-200 dark:border-neutral-700">Explore Package</a>'
)

content = content.replace(
    '<a href="dashboard.html" class="block w-full py-3 px-4 bg-studio-600 hover:bg-studio-700 text-white text-center font-medium rounded-xl transition-colors">Explore Package</a>',
    '<a href="dashboard.html" class="block w-full py-3 px-4 mt-auto bg-studio-600 hover:bg-studio-700 text-white text-center font-medium rounded-xl transition-colors">Explore Package</a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Packages aligned properly.")
