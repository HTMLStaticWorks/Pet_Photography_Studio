import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop Login link
    desktop_login_pattern = r'\s*<a href="login\.html"[^>]*>Login</a>'
    content = re.sub(desktop_login_pattern, '', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Login removed from nav bars.")
