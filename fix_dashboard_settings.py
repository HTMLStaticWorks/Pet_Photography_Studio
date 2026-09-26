import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the Settings and Support links with buttons
old_settings = r'<a href="#" class="flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">\s*<i class="fas fa-cog w-5 mr-3"></i> Account Settings\s*</a>'
new_settings = r'''<button onclick="switchTab('settings')" id="nav-settings" class="w-full flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">
                    <i class="fas fa-cog w-5 mr-3 text-left"></i> Account Settings
                </button>'''

old_support = r'<a href="#" class="flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">\s*<i class="fas fa-question-circle w-5 mr-3"></i> Help & Support\s*</a>'
new_support = r'''<button onclick="switchTab('support')" id="nav-support" class="w-full flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">
                    <i class="fas fa-question-circle w-5 mr-3 text-left"></i> Help & Support
                </button>'''

content = re.sub(old_settings, new_settings, content)
content = re.sub(old_support, new_support, content)

# 2. Inject tabs HTML
if 'id="tab-settings"' not in content:
    tabs_html = """
                    <!-- Tab: Settings -->
                    <div id="tab-settings" class="hidden space-y-8">
                        <h2 class="text-3xl font-bold mb-6">Account Settings</h2>
                        <div class="bg-white dark:bg-neutral-950 p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800">
                            <h3 class="text-xl font-bold mb-4">Profile Information</h3>
                            <div class="space-y-4 max-w-md">
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Full Name</label>
                                    <input type="text" value="Emily Davis" class="w-full px-4 py-2 rounded-lg border border-gray-200 dark:border-neutral-700 bg-gray-50 dark:bg-neutral-900 outline-none focus:border-studio-500">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Email Address</label>
                                    <input type="email" value="emily.davis@example.com" class="w-full px-4 py-2 rounded-lg border border-gray-200 dark:border-neutral-700 bg-gray-50 dark:bg-neutral-900 outline-none focus:border-studio-500">
                                </div>
                                <button class="px-6 py-2 bg-studio-600 text-white rounded-lg font-medium hover:bg-studio-700 transition-colors mt-4">Save Changes</button>
                            </div>
                        </div>
                    </div>

                    <!-- Tab: Support -->
                    <div id="tab-support" class="hidden space-y-8">
                        <h2 class="text-3xl font-bold mb-6">Help & Support</h2>
                        <div class="bg-white dark:bg-neutral-950 p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800">
                            <h3 class="text-xl font-bold mb-4">Frequently Asked Questions</h3>
                            <div class="space-y-4">
                                <details class="p-4 border border-gray-100 dark:border-neutral-800 rounded-lg bg-gray-50 dark:bg-neutral-900/50">
                                    <summary class="font-medium cursor-pointer">How long does it take to receive my gallery?</summary>
                                    <p class="mt-2 text-gray-500 text-sm">Typically, proof galleries are ready within 1-2 weeks after your session.</p>
                                </details>
                                <details class="p-4 border border-gray-100 dark:border-neutral-800 rounded-lg bg-gray-50 dark:bg-neutral-900/50">
                                    <summary class="font-medium cursor-pointer">Can I order more prints later?</summary>
                                    <p class="mt-2 text-gray-500 text-sm">Yes! Your gallery will remain active for 6 months for any additional orders.</p>
                                </details>
                            </div>
                            <h3 class="text-xl font-bold mt-8 mb-4">Contact Studio</h3>
                            <p class="text-gray-500 mb-4">Need immediate assistance? Reach out to us directly.</p>
                            <button class="px-6 py-2 bg-gray-900 dark:bg-white text-white dark:text-gray-900 rounded-lg font-medium hover:bg-gray-800 dark:hover:bg-gray-100 transition-colors">Contact Us</button>
                        </div>
                    </div>
"""
    content = content.replace(
        '                </div>\n            </div>\n        </main>',
        tabs_html + '\n                </div>\n            </div>\n        </main>'
    )

# 3. Update the script
if "document.getElementById('tab-settings').classList.add('hidden');" not in content:
    content = content.replace(
        "document.getElementById('tab-galleries').classList.remove('block');",
        "document.getElementById('tab-galleries').classList.remove('block');\n            document.getElementById('tab-settings').classList.add('hidden');\n            document.getElementById('tab-settings').classList.remove('block');\n            document.getElementById('tab-support').classList.add('hidden');\n            document.getElementById('tab-support').classList.remove('block');"
    )
    content = content.replace(
        "['nav-dashboard', 'nav-book', 'nav-sessions', 'nav-galleries']",
        "['nav-dashboard', 'nav-book', 'nav-sessions', 'nav-galleries', 'nav-settings', 'nav-support']"
    )

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Settings and Support tabs fixed.")
