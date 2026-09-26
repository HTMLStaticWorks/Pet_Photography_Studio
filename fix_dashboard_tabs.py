import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's see if tab-book exists
if 'id="tab-book"' not in content:
    # We need to insert the missing tabs right before </main>
    # Find </main>
    
    missing_tabs = """
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
"""
    
    # We find the end of tab-dashboard:
    content = content.replace(
        '                </div>\n            </div>\n        </main>',
        missing_tabs + '\n                </div>\n            </div>\n        </main>'
    )
    
    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Missing tabs injected!")
else:
    print("Tabs already exist.")
