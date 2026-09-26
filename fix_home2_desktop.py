import os

directory = '.'

for filename in os.listdir(directory):
    if filename.endswith('.html') and filename != 'dashboard.html':
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        old_str = '''<a href="index.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium">Home</a>
                    
                    <a href="about.html"'''
                    
        new_str = '''<a href="index.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium transition-colors">Home</a>
                    <a href="home-2.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium transition-colors">Home 2</a>
                    <a href="about.html"'''
                    
        content = content.replace(old_str, new_str)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done.")
