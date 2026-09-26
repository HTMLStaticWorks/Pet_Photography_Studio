import glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to group the <p> and <a> inside blog cards inside a div.mt-auto w-full.
    # We need to make sure the card content wrapper has `flex flex-col h-full`.
    
    # The blog card structure:
    # <div class="bg-white ... group">
    #     <div class="relative h-64 overflow-hidden">...</div>
    #     <div class="p-8">
    #        <div class="...">...</div>
    #        <h3 class="...">...</h3>
    #        <p class="...">...</p>
    #        <a href="...">...</a>
    #     </div>
    # </div>
    
    # Let's change `<div class="p-8">` to `<div class="p-8 flex flex-col h-full">`
    # Actually wait. The parent `<div class="bg-white ... group">` must have `flex flex-col h-full`.
    # And the image wrapper `<div class="relative h-64 overflow-hidden">` has a fixed height, so `h-full` on the card will stretch it, and `flex-grow` on `<div class="p-8">` is needed.
    
    # Let's replace the blog card outer div:
    content = re.sub(
        r'(<div class="bg-white dark:bg-neutral-900 rounded-3xl overflow-hidden shadow-sm border border-gray-100 dark:border-neutral-800 hover:shadow-md transition-shadow group)([^"]*">)',
        r'\1 flex flex-col h-full\2',
        content
    )
    
    # Let's replace `<div class="p-8">` with `<div class="p-8 flex flex-col flex-grow">`
    # But only inside the blog grid!
    # A safer regex:
    # find all block components:
    
    def replace_card(m):
        card = m.group(0)
        # replace p-8
        card = re.sub(r'<div class="p-8">', r'<div class="p-8 flex flex-col flex-grow">', card)
        
        # wrap the paragraph and a link in mt-auto w-full
        card = re.sub(
            r'(<p class="text-gray-600 dark:text-gray-400 mb-6">.*?</p>\s*<a href="[^"]+" class="inline-flex items-center text-studio-600[^"]+">.*?</a>)',
            r'<div class="mt-auto w-full">\n\1\n</div>',
            card,
            flags=re.DOTALL
        )
        return card

    content = re.sub(
        r'<div class="bg-white dark:bg-neutral-900 rounded-3xl overflow-hidden shadow-sm border border-gray-100 dark:border-neutral-800 hover:shadow-md transition-shadow group.*?</article>\s*</div>',
        replace_card,
        content,
        flags=re.DOTALL
    )

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
print("Updated blog cards")
