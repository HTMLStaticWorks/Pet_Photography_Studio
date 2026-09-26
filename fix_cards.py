import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Card 1
content = content.replace(
    '<h4 class="font-bold text-lg mb-2">Studio Signature</h4>\n                                    <p class="text-sm text-gray-500 mb-4">1 Hour • 15 Photos</p>\n                                    <button\n                                        class="w-full mt-auto bg-gray-100 dark:bg-neutral-900 text-sm font-semibold py-2 rounded-xl">Select</button>',
    '<h4 class="font-bold text-lg mb-2">Studio Signature</h4>\n                                    <div class="mt-auto w-full">\n                                        <p class="text-sm text-gray-500 mb-4">1 Hour • 15 Photos</p>\n                                        <button\n                                            class="w-full bg-gray-100 dark:bg-neutral-900 text-sm font-semibold py-2 rounded-xl">Select</button>\n                                    </div>'
)

# Card 2
content = content.replace(
    '<h4 class="font-bold text-lg mb-2">The Great Outdoors</h4>\n                                    <p class="text-sm text-gray-500 mb-4">2 Hours • 30 Photos</p>\n                                    <button\n                                        class="w-full mt-auto bg-studio-600 text-white text-sm font-semibold py-2 rounded-xl">Selected</button>',
    '<h4 class="font-bold text-lg mb-2">The Great Outdoors</h4>\n                                    <div class="mt-auto w-full">\n                                        <p class="text-sm text-gray-500 mb-4">2 Hours • 30 Photos</p>\n                                        <button\n                                            class="w-full bg-studio-600 text-white text-sm font-semibold py-2 rounded-xl">Selected</button>\n                                    </div>'
)

# Card 3
content = content.replace(
    '<h4 class="font-bold text-lg mb-2">Lifestyle Home</h4>\n                                    <p class="text-sm text-gray-500 mb-4">1.5 Hours • 20 Photos</p>\n                                    <button\n                                        class="w-full mt-auto bg-gray-100 dark:bg-neutral-900 text-sm font-semibold py-2 rounded-xl">Select</button>',
    '<h4 class="font-bold text-lg mb-2">Lifestyle Home</h4>\n                                    <div class="mt-auto w-full">\n                                        <p class="text-sm text-gray-500 mb-4">1.5 Hours • 20 Photos</p>\n                                        <button\n                                            class="w-full bg-gray-100 dark:bg-neutral-900 text-sm font-semibold py-2 rounded-xl">Select</button>\n                                    </div>'
)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated dashboard cards")
