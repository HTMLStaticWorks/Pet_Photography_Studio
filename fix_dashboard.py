import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Sidebar Gap
content = content.replace('</nav>\n            </div>\n\n            <div class="mt-auto p-6 border-t border-gray-100 dark:border-neutral-800 space-y-2">', 
                          '')
content = content.replace('                            New</span>\n                    </button>\n                </nav>', 
                          '                            New</span>\n                    </button>\n')

# Fix Recent Activity Line
content = content.replace('before:ml-2.5 rtl:mr-2.5 rtl:ml-0', 'before:ml-2.5 rtl:before:mr-2.5 rtl:before:ml-0')

# Fix Recent Activity Dots
content = content.replace('absolute -left-2 shrink-0', 'absolute -left-2 rtl:-right-2 rtl:left-auto shrink-0')

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
