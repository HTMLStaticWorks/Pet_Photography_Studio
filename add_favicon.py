import os
import glob
import urllib.request

html_files = glob.glob('d:/SEPT WEBSITES/Pet Photography Studio/*.html')

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="#c27b60" d="M226.5 92.9c14.3 7.3 22.9 23 22.9 40.5l0 1.6c0 17.5-8.6 33.2-22.9 40.5l-23.5 12c-19.1 9.8-42.2 2.2-51.9-16.9s-2.2-42.2 16.9-51.9l23.5-12c9.7-5 20.8-5 30.5 0l4.5 2.3zM256 512c-42.6 0-82.9-13.8-115.8-37.4C108.6 451.9 84 416.7 68.6 376.1c-8.9-23.7-3.9-50.5 13-69.6l25.3-28.4c17.1-19.1 44.5-24.8 67.4-14.1l25.4 11.9c19.1 8.9 40.5 8.9 59.6 0l25.4-11.9c22.9-10.7 50.3-5 67.4 14.1l25.3 28.4c16.9 19.1 21.9 45.9 13 69.6C374 416.7 349.4 451.9 315.8 474.6 282.9 498.2 242.6 512 256 512zm151.4-361.5c-19.1-9.7-21.3-32.8-11.6-51.9s32.8-21.3 51.9-11.6l23.5 12c14.3 7.3 22.9 23 22.9 40.5l0 1.6c0 17.5-8.6 33.2-22.9 40.5l-23.5 12c-9.7 5-20.8 5-30.5 0l-4.5-2.3-5.3-2.7zm-226.7-18.7c16.3-17 19.3-43 6.7-61.9l-13.1-19.7c-11.8-17.7-34.9-23.2-52.9-12.6C103.4-51 98-28 109.8-10.2l13.1 19.7c12.6 18.9 38.3 21.4 54.8 4.7zM402.2 62.1c-18-10.6-41.1-5.1-52.9 12.6l-13.1 19.7c-12.6 18.9-9.6 44.9 6.7 61.9c16.5 16.7 42.2 14.2 54.8-4.7l13.1-19.7c11.8-17.8 6.4-40.8-8.6-49.8z"/></svg>"""

with open('d:/SEPT WEBSITES/Pet Photography Studio/favicon.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

favicon_tag = '<link rel="icon" type="image/svg+xml" href="favicon.svg">'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<link rel="icon"' not in content:
        content = content.replace('</head>', f'    {favicon_tag}\n</head>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added favicon to {os.path.basename(filepath)}")
    else:
        print(f"Favicon already exists in {os.path.basename(filepath)}")
