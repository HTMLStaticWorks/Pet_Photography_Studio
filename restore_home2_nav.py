import os

directory = '.'

for filename in os.listdir(directory):
    if filename.endswith('.html') and filename != 'dashboard.html':
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add back to desktop nav
        content = content.replace(
            '<a href="index.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium transition-colors">Home</a>\n                    <a href="about.html"',
            '<a href="index.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium transition-colors">Home</a>\n                    <a href="home-2.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium transition-colors">Home 2</a>\n                    <a href="about.html"'
        )
        
        # Also it might be in mobile nav
        content = content.replace(
            '<a href="index.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-200 hover:text-studio-600 hover:bg-studio-50 dark:hover:bg-neutral-800 transition-colors">Home</a>\n                <a href="about.html"',
            '<a href="index.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-200 hover:text-studio-600 hover:bg-studio-50 dark:hover:bg-neutral-800 transition-colors">Home</a>\n                <a href="home-2.html" class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-200 hover:text-studio-600 hover:bg-studio-50 dark:hover:bg-neutral-800 transition-colors">Home 2</a>\n                <a href="about.html"'
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Restored Home 2 to navs in {filename}")

print("Done.")
