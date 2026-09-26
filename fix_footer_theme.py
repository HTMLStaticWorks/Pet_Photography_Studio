import glob

def fix_footer(content):
    start = content.find('<footer')
    if start == -1: return content
    end = content.find('</footer>', start) + 9
    
    footer = content[start:end]
    
    # Footer tag
    footer = footer.replace('class="bg-neutral-900 text-white pt-16 pb-8 border-t border-neutral-800"', 
                            'class="bg-white dark:bg-neutral-900 text-neutral-900 dark:text-white pt-16 pb-8 border-t border-gray-100 dark:border-neutral-800 transition-colors"')
    
    # Logo text
    footer = footer.replace('text-2xl font-bold text-white"', 'text-2xl font-bold text-studio-900 dark:text-white"')
    
    # Brand icon / highlight
    footer = footer.replace('text-studio-400', 'text-studio-500 dark:text-studio-400')
    
    # Normal text
    footer = footer.replace('text-gray-400 text-sm', 'text-gray-600 dark:text-gray-400 text-sm')
    
    # Links
    footer = footer.replace('text-gray-400 hover:text-white', 'text-gray-500 dark:text-gray-400 hover:text-studio-600 dark:hover:text-white')
    
    # Bottom footer border
    footer = footer.replace('border-neutral-800 mt-12', 'border-gray-200 dark:border-neutral-800 mt-12')
    
    # Bottom footer text (copyright)
    footer = footer.replace('text-gray-500 text-sm', 'text-gray-500 dark:text-gray-400 text-sm')
    
    # Bottom footer links
    footer = footer.replace('hover:text-white">Privacy', 'text-gray-500 dark:text-gray-400 hover:text-studio-600 dark:hover:text-white">Privacy')
    footer = footer.replace('hover:text-white">Terms', 'text-gray-500 dark:text-gray-400 hover:text-studio-600 dark:hover:text-white">Terms')
    
    # Make sure we don't accidentally do hover:text-studio-600 dark:hover:text-white twice if running multiple times
    
    return content[:start] + footer + content[end:]

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = fix_footer(content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Updated ' + f)
