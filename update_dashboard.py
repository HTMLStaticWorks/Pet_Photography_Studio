import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Sidebar Navigation
old_nav = r'''<nav class="space-y-2">
                    <a href="#" class="flex items-center px-4 py-3 text-sm font-medium rounded-xl bg-studio-50 text-studio-700 dark:bg-studio-900/30 dark:text-studio-400">
                        <i class="fas fa-home w-5 mr-3"></i> Dashboard
                    </a>
                    <a href="#" class="flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">
                        <i class="fas fa-calendar-alt w-5 mr-3"></i> Book a Session
                    </a>
                    <a href="#" class="flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">
                        <i class="fas fa-camera w-5 mr-3"></i> My Sessions
                    </a>
                    <a href="#" class="flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors flex justify-between">
                        <div class="flex items-center"><i class="fas fa-images w-5 mr-3"></i> Proof Galleries</div>
                        <span class="bg-studio-100 text-studio-700 dark:bg-studio-900/50 dark:text-studio-400 text-xs py-0.5 px-2 rounded-full">1 New</span>
                    </a>
                </nav>'''

new_nav = '''<nav class="space-y-2">
                    <button onclick="switchTab('dashboard')" id="nav-dashboard" class="w-full flex items-center px-4 py-3 text-sm font-medium rounded-xl bg-studio-50 text-studio-700 dark:bg-studio-900/30 dark:text-studio-400 transition-colors">
                        <i class="fas fa-home w-5 mr-3 text-left"></i> Dashboard
                    </button>
                    <button onclick="switchTab('book')" id="nav-book" class="w-full flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">
                        <i class="fas fa-calendar-alt w-5 mr-3 text-left"></i> Book a Session
                    </button>
                    <button onclick="switchTab('sessions')" id="nav-sessions" class="w-full flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">
                        <i class="fas fa-camera w-5 mr-3 text-left"></i> My Sessions
                    </button>
                    <button onclick="switchTab('galleries')" id="nav-galleries" class="w-full flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors flex justify-between">
                        <div class="flex items-center"><i class="fas fa-images w-5 mr-3 text-left"></i> Proof Galleries</div>
                        <span class="bg-studio-100 text-studio-700 dark:bg-studio-900/50 dark:text-studio-400 text-xs py-0.5 px-2 rounded-full">1 New</span>
                    </button>
                </nav>'''

content = content.replace(old_nav, new_nav)

# Replace Dashboard Content
old_content_start = r'<div class="max-w-6xl mx-auto space-y-8">'

new_content_start = '''<div class="max-w-6xl mx-auto">
                    
                    <!-- Tab: Dashboard -->
                    <div id="tab-dashboard" class="space-y-8 block">'''

content = content.replace(old_content_start, new_content_start)

# Finding the end of the Dashboard content (before `</div></div></main>`)
old_content_end = r'                        </div>\n                    </div>\n\n                </div>\n            </div>\n        </main>'

new_content_end = '''                        </div>
                    </div>
                    </div> <!-- End Tab Dashboard -->

                    <!-- Tab: Book a Session -->
                    <div id="tab-book" class="hidden space-y-8">
                        <h2 class="text-3xl font-bold mb-6">Book a Session</h2>
                        <div class="bg-white dark:bg-neutral-950 p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800">
                            <p class="text-gray-500 mb-6">Select a session type to view available dates and times.</p>
                            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                                <div class="border border-gray-200 dark:border-neutral-800 rounded-2xl p-6 hover:border-studio-500 cursor-pointer transition-colors">
                                    <h4 class="font-bold text-lg mb-2">Studio Signature</h4>
                                    <p class="text-sm text-gray-500 mb-4">1 Hour • 15 Photos</p>
                                    <button class="w-full bg-gray-100 dark:bg-neutral-900 text-sm font-semibold py-2 rounded-xl">Select</button>
                                </div>
                                <div class="border border-studio-500 rounded-2xl p-6 bg-studio-50 dark:bg-studio-900/10 cursor-pointer transition-colors relative">
                                    <span class="absolute top-0 right-0 bg-studio-500 text-white text-[10px] font-bold px-2 py-1 rounded-bl-xl rounded-tr-xl">POPULAR</span>
                                    <h4 class="font-bold text-lg mb-2">The Great Outdoors</h4>
                                    <p class="text-sm text-gray-500 mb-4">2 Hours • 30 Photos</p>
                                    <button class="w-full bg-studio-600 text-white text-sm font-semibold py-2 rounded-xl">Selected</button>
                                </div>
                                <div class="border border-gray-200 dark:border-neutral-800 rounded-2xl p-6 hover:border-studio-500 cursor-pointer transition-colors">
                                    <h4 class="font-bold text-lg mb-2">Lifestyle Home</h4>
                                    <p class="text-sm text-gray-500 mb-4">1.5 Hours • 20 Photos</p>
                                    <button class="w-full bg-gray-100 dark:bg-neutral-900 text-sm font-semibold py-2 rounded-xl">Select</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Tab: My Sessions -->
                    <div id="tab-sessions" class="hidden space-y-8">
                        <h2 class="text-3xl font-bold mb-6">My Sessions</h2>
                        <div class="bg-white dark:bg-neutral-950 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800 overflow-hidden">
                            <table class="w-full text-left">
                                <thead class="bg-gray-50 dark:bg-neutral-900/50">
                                    <tr>
                                        <th class="px-6 py-4 text-xs font-semibold text-gray-500 uppercase">Session Type</th>
                                        <th class="px-6 py-4 text-xs font-semibold text-gray-500 uppercase">Date</th>
                                        <th class="px-6 py-4 text-xs font-semibold text-gray-500 uppercase">Pet Name</th>
                                        <th class="px-6 py-4 text-xs font-semibold text-gray-500 uppercase">Status</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-gray-100 dark:divide-neutral-800">
                                    <tr>
                                        <td class="px-6 py-4 font-medium">The Great Outdoors</td>
                                        <td class="px-6 py-4 text-gray-500">Oct 12, 2026</td>
                                        <td class="px-6 py-4 text-gray-500">Charlie</td>
                                        <td class="px-6 py-4"><span class="bg-green-100 text-green-700 text-xs font-bold px-3 py-1 rounded-full">Completed</span></td>
                                    </tr>
                                    <tr>
                                        <td class="px-6 py-4 font-medium">Studio Signature</td>
                                        <td class="px-6 py-4 text-gray-500">May 05, 2025</td>
                                        <td class="px-6 py-4 text-gray-500">Charlie</td>
                                        <td class="px-6 py-4"><span class="bg-gray-100 text-gray-700 dark:bg-neutral-800 dark:text-gray-300 text-xs font-bold px-3 py-1 rounded-full">Archived</span></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- Tab: Proof Galleries -->
                    <div id="tab-galleries" class="hidden space-y-8">
                        <h2 class="text-3xl font-bold mb-6">Proof Galleries</h2>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="bg-white dark:bg-neutral-950 p-6 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800">
                                <div class="flex justify-between items-end mb-4">
                                    <div>
                                        <h4 class="font-semibold text-lg">Charlie's Autumn Adventure</h4>
                                        <p class="text-sm text-gray-500">45 Photos</p>
                                    </div>
                                    <span class="px-3 py-1 bg-yellow-100 text-yellow-700 text-xs font-bold rounded-full">Select 15 More</span>
                                </div>
                                <img src="https://images.unsplash.com/photo-1548199973-03cce0bbc87b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Cover" class="w-full h-48 object-cover rounded-xl mb-4">
                                <button class="w-full py-3 bg-studio-600 text-white font-semibold rounded-xl hover:bg-studio-700 transition-colors">Enter Gallery</button>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </main>'''

content = content.replace(old_content_end, new_content_end)

# Add Script to the bottom of the body
script_addition = '''
    <script>
        function switchTab(tabId) {
            // Hide all tabs
            document.getElementById('tab-dashboard').classList.add('hidden');
            document.getElementById('tab-dashboard').classList.remove('block');
            document.getElementById('tab-book').classList.add('hidden');
            document.getElementById('tab-book').classList.remove('block');
            document.getElementById('tab-sessions').classList.add('hidden');
            document.getElementById('tab-sessions').classList.remove('block');
            document.getElementById('tab-galleries').classList.add('hidden');
            document.getElementById('tab-galleries').classList.remove('block');
            
            // Show selected tab
            document.getElementById('tab-' + tabId).classList.remove('hidden');
            document.getElementById('tab-' + tabId).classList.add('block');
            
            // Reset nav buttons
            const navIds = ['nav-dashboard', 'nav-book', 'nav-sessions', 'nav-galleries'];
            navIds.forEach(id => {
                const el = document.getElementById(id);
                el.classList.remove('bg-studio-50', 'text-studio-700', 'dark:bg-studio-900/30', 'dark:text-studio-400');
                el.classList.add('text-gray-600', 'dark:text-gray-400', 'hover:bg-gray-50', 'dark:hover:bg-neutral-900');
            });
            
            // Highlight selected nav button
            const selectedBtn = document.getElementById('nav-' + tabId);
            selectedBtn.classList.remove('text-gray-600', 'dark:text-gray-400', 'hover:bg-gray-50', 'dark:hover:bg-neutral-900');
            selectedBtn.classList.add('bg-studio-50', 'text-studio-700', 'dark:bg-studio-900/30', 'dark:text-studio-400');
        }
    </script>
'''

content = content.replace('</body>', script_addition + '\n</body>')

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Dashboard tabs updated.")
