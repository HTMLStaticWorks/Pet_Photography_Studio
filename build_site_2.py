import os

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

common_head = """
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        studio: {
                            50: '#faf6f3',
                            100: '#f4ede6',
                            200: '#ebd9cd',
                            300: '#dfbcab',
                            400: '#cf9881',
                            500: '#c27b60',
                            600: '#b5644a',
                            700: '#98503b',
                            800: '#7f4433',
                            900: '#67392c',
                            950: '#361b14',
                        }
                    }
                }
            }
        }
    </script>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
"""

header_html = """
    <header class="fixed w-full top-0 z-50 bg-white/90 dark:bg-neutral-900/90 backdrop-blur-md border-b border-gray-100 dark:border-neutral-800 transition-colors">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20 items-center">
                <div class="flex-shrink-0 flex items-center">
                    <a href="index.html" class="text-2xl font-bold text-studio-900 dark:text-studio-200">
                        Paws & <span class="text-studio-500">Pose</span>
                    </a>
                </div>
                <nav class="hidden md:flex space-x-8">
                    <a href="index.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium">Home</a>
                    <a href="about.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium">About</a>
                    <a href="blog.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium">Blog</a>
                    <a href="contact.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 dark:hover:text-studio-400 font-medium">Contact</a>
                </nav>
                <div class="hidden md:flex items-center space-x-4">
                    <button class="theme-toggle text-gray-500 dark:text-gray-400 hover:text-studio-500 focus:outline-none">
                        <i class="fas fa-moon dark:hidden"></i>
                        <i class="fas fa-sun hidden dark:block"></i>
                    </button>
                    <button class="rtl-toggle text-gray-500 dark:text-gray-400 hover:text-studio-500 font-medium">RTL</button>
                    <a href="login.html" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 font-medium">Login</a>
                    <a href="signup.html" class="bg-studio-600 hover:bg-studio-700 text-white px-5 py-2.5 rounded-full font-medium transition-colors">Sign Up</a>
                </div>
                <div class="md:hidden flex items-center">
                    <button id="mobile-menu-btn" class="text-gray-600 dark:text-gray-300 hover:text-studio-500 focus:outline-none">
                        <i class="fas fa-bars text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden md:hidden bg-white dark:bg-neutral-900 border-b border-gray-100 dark:border-neutral-800">
            <div class="px-4 pt-2 pb-6 space-y-1">
                <a href="index.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">Home</a>
                <a href="about.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">About</a>
                <a href="blog.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">Blog</a>
                <a href="contact.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 dark:hover:bg-neutral-800 rounded-md">Contact</a>
                <div class="border-t border-gray-100 dark:border-neutral-800 pt-4 pb-2">
                    <a href="login.html" class="block px-3 py-2 text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-studio-50 hover:text-studio-600 rounded-md">Login</a>
                    <a href="signup.html" class="block px-3 py-2 text-base font-medium text-studio-600 dark:text-studio-400 hover:bg-studio-50 rounded-md">Sign Up</a>
                </div>
                <div class="flex space-x-4 px-3 py-2">
                    <button class="theme-toggle text-gray-500 dark:text-gray-400"><i class="fas fa-adjust"></i> Theme</button>
                    <button class="rtl-toggle text-gray-500 dark:text-gray-400"><i class="fas fa-exchange-alt"></i> RTL</button>
                </div>
            </div>
        </div>
    </header>
"""

footer_html = """
    <footer class="bg-neutral-900 text-white pt-16 pb-8 border-t border-neutral-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-12">
                <div class="space-y-4">
                    <a href="index.html" class="text-2xl font-bold text-white">
                        Paws & <span class="text-studio-400">Pose</span>
                    </a>
                    <p class="text-gray-400 text-sm leading-relaxed">
                        Capturing the unique personality and soul of your beloved pets through premium studio and lifestyle photography.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i class="fab fa-instagram text-xl"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i class="fab fa-facebook text-xl"></i></a>
                        <a href="#" class="text-gray-400 hover:text-white transition-colors"><i class="fab fa-pinterest text-xl"></i></a>
                    </div>
                </div>
                <div>
                    <h3 class="text-lg font-semibold mb-4">Quick Links</h3>
                    <ul class="space-y-2">
                        <li><a href="index.html" class="text-gray-400 hover:text-white transition-colors text-sm">Home</a></li>
                        <li><a href="home-2.html" class="text-gray-400 hover:text-white transition-colors text-sm">Editorial Home</a></li>
                        <li><a href="about.html" class="text-gray-400 hover:text-white transition-colors text-sm">About Us</a></li>
                        <li><a href="blog.html" class="text-gray-400 hover:text-white transition-colors text-sm">Journal</a></li>
                        <li><a href="contact.html" class="text-gray-400 hover:text-white transition-colors text-sm">Contact</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-semibold mb-4">Services</h3>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-white transition-colors text-sm">Studio Sessions</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white transition-colors text-sm">Outdoor Adventures</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white transition-colors text-sm">Puppy Milestones</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white transition-colors text-sm">Fine Art Prints</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-semibold mb-4">Contact</h3>
                    <ul class="space-y-3">
                        <li class="flex items-start text-gray-400 text-sm">
                            <i class="fas fa-map-marker-alt mt-1 mr-3 text-studio-400"></i>
                            123 Creative Studio Ave,<br>Art District, NY 10001
                        </li>
                        <li class="flex items-center text-gray-400 text-sm">
                            <i class="fas fa-phone mr-3 text-studio-400"></i>
                            +1 (555) 123-4567
                        </li>
                        <li class="flex items-center text-gray-400 text-sm">
                            <i class="fas fa-envelope mr-3 text-studio-400"></i>
                            hello@pawspose.com
                        </li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-neutral-800 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center text-gray-500 text-sm">
                <p>&copy; 2026 Paws & Pose Photography. All rights reserved.</p>
                <div class="space-x-4 mt-4 md:mt-0">
                    <a href="#" class="hover:text-white">Privacy Policy</a>
                    <a href="#" class="hover:text-white">Terms & Conditions</a>
                </div>
            </div>
        </div>
    </footer>
"""

back_to_top = """
    <button id="back-to-top" class="hidden fixed bottom-8 right-8 z-50 bg-studio-600 hover:bg-studio-700 text-white rounded-full w-12 h-12 flex items-center justify-center shadow-lg transition-transform hover:-translate-y-1 focus:outline-none">
        <i class="fas fa-arrow-up"></i>
    </button>
    <script src="script.js"></script>
"""

pages = {}

pages['about.html'] = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {common_head}
    <title>About Us - Paws & Pose | Pet Photography Studio</title>
</head>
<body class="bg-white dark:bg-neutral-900 text-gray-900 dark:text-gray-100 transition-colors pt-20">
    {header_html}
    
    <main>
        <!-- Hero Section -->
        <section class="relative min-h-[60vh] flex items-center overflow-hidden">
            <div class="absolute inset-0">
                <img src="https://images.unsplash.com/photo-1555685812-4b943f1cb0eb?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80" alt="Photographer with dog in studio" class="w-full h-full object-cover opacity-90 dark:opacity-40">
                <div class="absolute inset-0 bg-gradient-to-r from-white/95 dark:from-neutral-900/95 via-white/70 dark:via-neutral-900/70 to-transparent"></div>
            </div>
            <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full py-24">
                <div class="max-w-2xl">
                    <span class="text-studio-600 dark:text-studio-400 font-semibold tracking-wider uppercase text-sm mb-4 block">Our Story</span>
                    <h1 class="text-5xl md:text-6xl font-bold mb-6 text-neutral-900 dark:text-white">For the Love of <br><span class="text-studio-600 dark:text-studio-400">Paws & Whiskers</span></h1>
                    <p class="text-lg text-neutral-700 dark:text-gray-300 leading-relaxed">We believe every pet has a unique soul that deserves to be celebrated. Our studio is dedicated to capturing the fleeting moments, the goofy smiles, and the quiet affection that makes your pet family.</p>
                </div>
            </div>
        </section>

        <!-- The Photographer -->
        <section class="py-24 bg-studio-50 dark:bg-neutral-800">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex flex-col lg:flex-row items-center gap-16">
                    <div class="w-full lg:w-1/2">
                        <div class="relative">
                            <img src="https://images.unsplash.com/photo-1581456495146-65a71b2c8e52?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Lead Photographer" class="rounded-3xl shadow-xl relative z-10">
                            <div class="absolute -bottom-8 -right-8 w-64 h-64 bg-studio-200 dark:bg-studio-900/50 rounded-full mix-blend-multiply filter blur-2xl opacity-70 z-0"></div>
                        </div>
                    </div>
                    <div class="w-full lg:w-1/2 space-y-6">
                        <h2 class="text-4xl font-bold">Meet Jessica, Your Lead Photographer</h2>
                        <h3 class="text-xl text-studio-600 dark:text-studio-400 font-medium">Over 10 years of capturing wagging tails and purrs.</h3>
                        <p class="text-gray-600 dark:text-gray-400 leading-relaxed">"My journey into pet photography started with my own rescue pup, Barnaby. I realized that the photos I had of him were my most treasured possessions. I wanted to give other pet parents that same gift—high-quality, artistic images that capture the essence of their best friends."</p>
                        <p class="text-gray-600 dark:text-gray-400 leading-relaxed">With a background in fine art portraiture and animal behavior, Jessica knows exactly how to make your pet comfortable, ensuring their true personality shines through the lens.</p>
                        <div class="pt-4">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Signature_of_author.svg" alt="Signature" class="h-12 opacity-50 dark:invert">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Our Philosophy -->
        <section class="py-24 bg-white dark:bg-neutral-900">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <h2 class="text-4xl font-bold mb-16">Our Photography Philosophy</h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
                    <div class="space-y-4">
                        <div class="w-20 h-20 mx-auto bg-studio-50 dark:bg-studio-900/30 rounded-full flex items-center justify-center text-studio-600 dark:text-studio-400">
                            <i class="fas fa-heart text-3xl"></i>
                        </div>
                        <h3 class="text-2xl font-semibold">Patience Above All</h3>
                        <p class="text-gray-600 dark:text-gray-400">We work on your pet's schedule. There's no rushing. We wait for the moment they feel safe, relaxed, and ready to show their true colors.</p>
                    </div>
                    <div class="space-y-4">
                        <div class="w-20 h-20 mx-auto bg-studio-50 dark:bg-studio-900/30 rounded-full flex items-center justify-center text-studio-600 dark:text-studio-400">
                            <i class="fas fa-paint-brush text-3xl"></i>
                        </div>
                        <h3 class="text-2xl font-semibold">Artistic Intent</h3>
                        <p class="text-gray-600 dark:text-gray-400">Every session is styled and lit with purpose. We aren't just taking snapshots; we are creating heirloom artwork for your walls.</p>
                    </div>
                    <div class="space-y-4">
                        <div class="w-20 h-20 mx-auto bg-studio-50 dark:bg-studio-900/30 rounded-full flex items-center justify-center text-studio-600 dark:text-studio-400">
                            <i class="fas fa-paw text-3xl"></i>
                        </div>
                        <h3 class="text-2xl font-semibold">Safety First</h3>
                        <p class="text-gray-600 dark:text-gray-400">Whether in the studio or outdoors, your pet's physical and emotional safety is our absolute priority throughout the entire process.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- The Studio Experience -->
        <section class="py-24 bg-neutral-950 text-white relative overflow-hidden">
            <div class="absolute inset-0 opacity-20">
                <img src="https://images.unsplash.com/photo-1516222338250-863216ce01ea?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80" alt="Studio Setup" class="w-full h-full object-cover">
            </div>
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                    <div class="space-y-8">
                        <h2 class="text-4xl font-bold">The Studio Experience</h2>
                        <p class="text-gray-400 text-lg">Our custom-designed studio is built specifically for pets. From non-slip floors to quiet lighting equipment and an endless supply of treats, we've created an environment where magic happens.</p>
                        <ul class="space-y-4 text-gray-300">
                            <li class="flex items-start"><i class="fas fa-check-circle text-studio-400 mt-1 mr-4"></i> Secure, enclosed space to prevent escapes.</li>
                            <li class="flex items-start"><i class="fas fa-check-circle text-studio-400 mt-1 mr-4"></i> Professional grade, fast-sync strobes that don't frighten animals.</li>
                            <li class="flex items-start"><i class="fas fa-check-circle text-studio-400 mt-1 mr-4"></i> A wardrobe of premium bandanas, bows, and collars.</li>
                        </ul>
                        <a href="contact.html" class="inline-block mt-4 bg-studio-600 hover:bg-studio-700 text-white px-8 py-4 rounded-full font-semibold transition-colors">Visit the Studio</a>
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <img src="https://images.unsplash.com/photo-1541364983171-a8ba01e95cfc?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Dog in studio" class="rounded-2xl w-full h-64 object-cover">
                        <img src="https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Cat in studio" class="rounded-2xl w-full h-64 object-cover mt-8">
                    </div>
                </div>
            </div>
        </section>

        <!-- Behind The Scenes -->
        <section class="py-24 bg-studio-50 dark:bg-neutral-800">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <h2 class="text-4xl font-bold mb-4">Behind the Lens</h2>
                <p class="text-gray-600 dark:text-gray-400 mb-16 max-w-2xl mx-auto">A sneak peek into the beautiful chaos of a typical pet portrait session.</p>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <img src="https://images.unsplash.com/photo-1551730459-92db2a308d6a?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" alt="BTS 1" class="rounded-xl aspect-square object-cover shadow-sm hover:scale-105 transition-transform duration-300">
                    <img src="https://images.unsplash.com/photo-1583337130417-3346a1be7dee?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" alt="BTS 2" class="rounded-xl aspect-square object-cover shadow-sm hover:scale-105 transition-transform duration-300">
                    <img src="https://images.unsplash.com/photo-1591160690555-5debfba289f0?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" alt="BTS 3" class="rounded-xl aspect-square object-cover shadow-sm hover:scale-105 transition-transform duration-300">
                    <img src="https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" alt="BTS 4" class="rounded-xl aspect-square object-cover shadow-sm hover:scale-105 transition-transform duration-300">
                </div>
            </div>
        </section>

    </main>
    
    {footer_html}
    {back_to_top}
</body>
</html>"""

pages['blog.html'] = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {common_head}
    <title>Journal - Paws & Pose | Pet Photography</title>
</head>
<body class="bg-[#f9f8f6] dark:bg-neutral-900 text-gray-900 dark:text-gray-100 transition-colors pt-20">
    {header_html}
    
    <main>
        <!-- Blog Hero -->
        <section class="py-20 bg-white dark:bg-neutral-950 border-b border-gray-100 dark:border-neutral-800">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <h1 class="text-5xl md:text-6xl font-serif font-bold mb-6">The Pet Portrait Journal</h1>
                <p class="text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">Stories from the studio, photography tips for pet parents, and behind-the-scenes magic.</p>
            </div>
        </section>

        <!-- Featured Article -->
        <section class="py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="bg-white dark:bg-neutral-950 rounded-3xl overflow-hidden shadow-xl border border-gray-100 dark:border-neutral-800 flex flex-col md:flex-row group">
                    <div class="w-full md:w-1/2 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1552053831-71594a27632d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Golden Retriever outdoors" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                    </div>
                    <div class="w-full md:w-1/2 p-10 lg:p-16 flex flex-col justify-center">
                        <div class="flex items-center space-x-4 mb-4">
                            <span class="text-studio-600 dark:text-studio-400 font-semibold text-sm uppercase tracking-wider">Featured Guide</span>
                            <span class="text-gray-400 text-sm">October 24, 2026</span>
                        </div>
                        <h2 class="text-3xl lg:text-4xl font-bold mb-6 hover:text-studio-600 dark:hover:text-studio-400 transition-colors cursor-pointer">How to Prepare Your Dog for an Outdoor Photography Session</h2>
                        <p class="text-gray-600 dark:text-gray-400 mb-8 leading-relaxed">Outdoor sessions offer beautiful natural light and a playground for your dog. But they also come with distractions. Here's our comprehensive guide to getting your pup ready for their big day out.</p>
                        <a href="#" class="inline-block bg-studio-900 dark:bg-white text-white dark:text-neutral-900 px-8 py-3 rounded-full font-medium hover:bg-studio-800 dark:hover:bg-gray-200 transition-colors w-max">Read the Article</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Latest Articles Grid -->
        <section class="py-16 bg-white dark:bg-neutral-900">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <h3 class="text-3xl font-bold mb-12">Latest Stories</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
                    
                    <!-- Article Card 1 -->
                    <div class="group bg-gray-50 dark:bg-neutral-950 rounded-2xl overflow-hidden border border-gray-100 dark:border-neutral-800 hover:shadow-lg transition-all duration-300">
                        <div class="aspect-video overflow-hidden">
                            <img src="https://images.unsplash.com/photo-1573865526739-10659fec78a5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Cat in studio" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <div class="p-8">
                            <div class="flex justify-between items-center mb-4">
                                <span class="text-studio-600 dark:text-studio-400 text-xs font-bold uppercase">Studio Secrets</span>
                                <span class="text-gray-400 text-xs">Oct 18, 2026</span>
                            </div>
                            <h4 class="text-xl font-bold mb-3 group-hover:text-studio-600 dark:group-hover:text-studio-400 transition-colors">Lighting Techniques for Black Cats</h4>
                            <p class="text-gray-600 dark:text-gray-400 text-sm mb-6 line-clamp-3">Photographing black fur can be challenging. Discover how we use rim lighting to capture the beautiful texture of dark-coated feline friends.</p>
                            <a href="#" class="text-studio-600 dark:text-studio-400 font-semibold text-sm hover:underline flex items-center">Read More <i class="fas fa-arrow-right ml-2 text-xs"></i></a>
                        </div>
                    </div>

                    <!-- Article Card 2 -->
                    <div class="group bg-gray-50 dark:bg-neutral-950 rounded-2xl overflow-hidden border border-gray-100 dark:border-neutral-800 hover:shadow-lg transition-all duration-300">
                        <div class="aspect-video overflow-hidden">
                            <img src="https://images.unsplash.com/photo-1583337130417-3346a1be7dee?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Puppy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <div class="p-8">
                            <div class="flex justify-between items-center mb-4">
                                <span class="text-studio-600 dark:text-studio-400 text-xs font-bold uppercase">Client Spotlight</span>
                                <span class="text-gray-400 text-xs">Oct 10, 2026</span>
                            </div>
                            <h4 class="text-xl font-bold mb-3 group-hover:text-studio-600 dark:group-hover:text-studio-400 transition-colors">Meet Barnaby: A Rescue Story</h4>
                            <p class="text-gray-600 dark:text-gray-400 text-sm mb-6 line-clamp-3">See the heartwarming gallery from our recent session with Barnaby, a rescue pup who found his forever home just in time for the holidays.</p>
                            <a href="#" class="text-studio-600 dark:text-studio-400 font-semibold text-sm hover:underline flex items-center">Read More <i class="fas fa-arrow-right ml-2 text-xs"></i></a>
                        </div>
                    </div>

                    <!-- Article Card 3 -->
                    <div class="group bg-gray-50 dark:bg-neutral-950 rounded-2xl overflow-hidden border border-gray-100 dark:border-neutral-800 hover:shadow-lg transition-all duration-300">
                        <div class="aspect-video overflow-hidden">
                            <img src="https://images.unsplash.com/photo-1501820488136-72669149e0d4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Dog owners" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <div class="p-8">
                            <div class="flex justify-between items-center mb-4">
                                <span class="text-studio-600 dark:text-studio-400 text-xs font-bold uppercase">Tips & Tricks</span>
                                <span class="text-gray-400 text-xs">Oct 02, 2026</span>
                            </div>
                            <h4 class="text-xl font-bold mb-3 group-hover:text-studio-600 dark:group-hover:text-studio-400 transition-colors">What to Wear to Your Pet's Photo Session</h4>
                            <p class="text-gray-600 dark:text-gray-400 text-sm mb-6 line-clamp-3">Coordinating with your furry best friend doesn't have to be hard. Here are our top styling tips for pet parents.</p>
                            <a href="#" class="text-studio-600 dark:text-studio-400 font-semibold text-sm hover:underline flex items-center">Read More <i class="fas fa-arrow-right ml-2 text-xs"></i></a>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- Newsletter CTA -->
        <section class="py-24 bg-studio-600 dark:bg-studio-900 text-white">
            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <h2 class="text-4xl font-bold mb-4">Join the Pack</h2>
                <p class="text-studio-100 mb-8 text-lg">Subscribe to our newsletter for exclusive photography tips, studio updates, and seasonal mini-session announcements.</p>
                <form class="flex flex-col sm:flex-row gap-4 justify-center">
                    <input type="email" placeholder="Enter your email address" class="px-6 py-4 rounded-full w-full sm:w-96 text-gray-900 focus:outline-none focus:ring-2 focus:ring-white">
                    <button type="submit" class="bg-neutral-900 hover:bg-neutral-800 text-white px-8 py-4 rounded-full font-bold transition-colors">Subscribe</button>
                </form>
            </div>
        </section>

    </main>
    
    {footer_html}
    {back_to_top}
</body>
</html>"""


pages['contact.html'] = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {common_head}
    <title>Contact Us - Paws & Pose | Pet Photography</title>
</head>
<body class="bg-white dark:bg-neutral-900 text-gray-900 dark:text-gray-100 transition-colors pt-20">
    {header_html}
    
    <main>
        <!-- Contact Hero -->
        <section class="relative py-24 bg-studio-50 dark:bg-neutral-800 overflow-hidden">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
                <h1 class="text-5xl md:text-6xl font-bold mb-6">Let's Photograph Your Pet</h1>
                <p class="text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">We'd love to hear about your furry best friend and discuss how we can create beautiful artwork together.</p>
            </div>
            <div class="absolute right-0 bottom-0 opacity-10 pointer-events-none">
                <i class="fas fa-camera text-[20rem]"></i>
            </div>
        </section>

        <!-- Contact Form & Info -->
        <section class="py-24">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
                    
                    <!-- Contact Form -->
                    <div class="bg-white dark:bg-neutral-950 p-10 rounded-3xl shadow-xl border border-gray-100 dark:border-neutral-800">
                        <h3 class="text-2xl font-bold mb-8">Send an Enquiry</h3>
                        <form class="space-y-6" id="contact-form">
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                <div>
                                    <label class="block text-sm font-medium mb-2">Your Name *</label>
                                    <input type="text" required class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-700 bg-gray-50 dark:bg-neutral-900 focus:outline-none focus:ring-2 focus:ring-studio-500">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium mb-2">Email Address *</label>
                                    <input type="email" required class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-700 bg-gray-50 dark:bg-neutral-900 focus:outline-none focus:ring-2 focus:ring-studio-500">
                                </div>
                            </div>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                <div>
                                    <label class="block text-sm font-medium mb-2">Phone Number</label>
                                    <input type="tel" class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-700 bg-gray-50 dark:bg-neutral-900 focus:outline-none focus:ring-2 focus:ring-studio-500">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium mb-2">Pet Name & Type *</label>
                                    <input type="text" placeholder="e.g. Luna (Golden Retriever)" required class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-700 bg-gray-50 dark:bg-neutral-900 focus:outline-none focus:ring-2 focus:ring-studio-500">
                                </div>
                            </div>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                <div>
                                    <label class="block text-sm font-medium mb-2">Preferred Session *</label>
                                    <select required class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-700 bg-gray-50 dark:bg-neutral-900 focus:outline-none focus:ring-2 focus:ring-studio-500">
                                        <option value="">Select a session</option>
                                        <option value="studio">Studio Signature</option>
                                        <option value="outdoor">The Great Outdoors</option>
                                        <option value="lifestyle">Lifestyle Home</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium mb-2">Preferred Date</label>
                                    <input type="date" class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-700 bg-gray-50 dark:bg-neutral-900 focus:outline-none focus:ring-2 focus:ring-studio-500">
                                </div>
                            </div>
                            <div>
                                <label class="block text-sm font-medium mb-2">Message *</label>
                                <textarea rows="4" required placeholder="Tell us a little bit about your pet's personality..." class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-700 bg-gray-50 dark:bg-neutral-900 focus:outline-none focus:ring-2 focus:ring-studio-500"></textarea>
                            </div>
                            <button type="submit" class="w-full bg-studio-600 hover:bg-studio-700 text-white font-bold py-4 rounded-xl transition-colors shadow-lg">Submit Enquiry</button>
                        </form>
                    </div>

                    <!-- Contact Info & Map -->
                    <div class="space-y-10">
                        <div>
                            <h3 class="text-3xl font-bold mb-6">Studio Information</h3>
                            <p class="text-gray-600 dark:text-gray-400 mb-8 leading-relaxed">Our studio is located in the heart of the Arts District, designed specifically for the comfort and safety of your pets. Consultations are by appointment only.</p>
                            
                            <div class="space-y-6">
                                <div class="flex items-start">
                                    <div class="w-12 h-12 bg-studio-100 dark:bg-studio-900/30 rounded-full flex items-center justify-center text-studio-600 dark:text-studio-400 shrink-0">
                                        <i class="fas fa-map-marker-alt"></i>
                                    </div>
                                    <div class="ml-4 pt-1">
                                        <h4 class="font-semibold text-lg">Studio Address</h4>
                                        <p class="text-gray-600 dark:text-gray-400 mt-1">123 Creative Studio Ave<br>Art District, NY 10001</p>
                                    </div>
                                </div>
                                <div class="flex items-start">
                                    <div class="w-12 h-12 bg-studio-100 dark:bg-studio-900/30 rounded-full flex items-center justify-center text-studio-600 dark:text-studio-400 shrink-0">
                                        <i class="fas fa-envelope"></i>
                                    </div>
                                    <div class="ml-4 pt-1">
                                        <h4 class="font-semibold text-lg">Email Us</h4>
                                        <a href="mailto:hello@pawspose.com" class="text-studio-600 dark:text-studio-400 hover:underline mt-1 block">hello@pawspose.com</a>
                                    </div>
                                </div>
                                <div class="flex items-start">
                                    <div class="w-12 h-12 bg-studio-100 dark:bg-studio-900/30 rounded-full flex items-center justify-center text-studio-600 dark:text-studio-400 shrink-0">
                                        <i class="fas fa-phone"></i>
                                    </div>
                                    <div class="ml-4 pt-1">
                                        <h4 class="font-semibold text-lg">Call Us</h4>
                                        <p class="text-gray-600 dark:text-gray-400 mt-1">+1 (555) 123-4567</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Embedded Map (Placeholder Image representing map for visual quality, as real iframe embeds can sometimes look messy without an API key, but using a generic map embed) -->
                        <div class="rounded-3xl overflow-hidden shadow-lg h-64 w-full bg-gray-200 dark:bg-neutral-800">
                            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d193595.15830869428!2d-74.119763973046!3d40.69766374874431!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2s!4v1680000000000!5m2!1sen!2s" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- FAQ Section -->
        <section class="py-24 bg-studio-50 dark:bg-neutral-800">
            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-bold mb-4">Frequently Asked Questions</h2>
                    <p class="text-gray-600 dark:text-gray-400">Everything you need to know before booking your session.</p>
                </div>
                <div class="space-y-6">
                    <div class="bg-white dark:bg-neutral-900 p-6 rounded-2xl shadow-sm">
                        <h4 class="text-xl font-bold mb-2">My dog is very energetic and won't sit still. Can you still photograph them?</h4>
                        <p class="text-gray-600 dark:text-gray-400">Absolutely! We specialize in capturing animals in motion and have plenty of tricks (and treats) to get their attention for those split-second portraits. Fast shutter speeds are our best friend.</p>
                    </div>
                    <div class="bg-white dark:bg-neutral-900 p-6 rounded-2xl shadow-sm">
                        <h4 class="text-xl font-bold mb-2">Can humans be in the photos too?</h4>
                        <p class="text-gray-600 dark:text-gray-400">Yes! While pets are the main focus, we encourage pet parents to step into a few shots. The bond between you and your pet is a beautiful thing to capture.</p>
                    </div>
                    <div class="bg-white dark:bg-neutral-900 p-6 rounded-2xl shadow-sm">
                        <h4 class="text-xl font-bold mb-2">How long after the session until I see the photos?</h4>
                        <p class="text-gray-600 dark:text-gray-400">Your proof gallery will be available in your Client Portal within 7-10 days after your session. From there, you can select your favorites for final retouching and printing.</p>
                    </div>
                </div>
            </div>
        </section>

    </main>
    
    {footer_html}
    {back_to_top}
    
    <script>
        document.getElementById('contact-form')?.addEventListener('submit', (e) => {{
            e.preventDefault();
            alert('Thank you for your enquiry! We will get back to you soon.');
        }});
    </script>
</body>
</html>"""

pages['signup.html'] = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {common_head}
    <title>Sign Up - Paws & Pose</title>
</head>
<body class="bg-white dark:bg-neutral-900 text-gray-900 dark:text-gray-100 min-h-screen flex">
    
    <!-- Signup Form Area -->
    <div class="w-full lg:w-1/2 flex flex-col justify-center items-center p-8 sm:p-12 lg:p-16 bg-white dark:bg-neutral-950 relative overflow-y-auto">
        
        <!-- Controls -->
        <div class="absolute top-8 left-8 lg:right-8 lg:left-auto flex space-x-4">
            <button class="theme-toggle text-gray-500 hover:text-studio-500"><i class="fas fa-adjust"></i></button>
            <button class="rtl-toggle text-gray-500 font-semibold text-xs hover:text-studio-500">RTL</button>
        </div>
        
        <div class="w-full max-w-md mt-12 lg:mt-0">
            <div class="mb-10 text-center lg:text-left">
                <a href="index.html" class="text-3xl font-bold text-studio-900 dark:text-studio-200 mb-2 inline-block">
                    Paws & <span class="text-studio-500">Pose</span>
                </a>
                <h1 class="text-2xl font-semibold mt-4">Create Client Account</h1>
                <p class="text-gray-500 text-sm mt-2">Join our studio to manage your sessions and galleries.</p>
            </div>
            
            <form class="space-y-5">
                <div>
                    <label class="block text-sm font-medium mb-1">Full Name</label>
                    <input type="text" class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-800 bg-transparent focus:outline-none focus:ring-2 focus:ring-studio-500 transition-shadow" placeholder="Jane Doe" required>
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Email Address</label>
                    <input type="email" class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-800 bg-transparent focus:outline-none focus:ring-2 focus:ring-studio-500 transition-shadow" placeholder="jane@example.com" required>
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Phone Number</label>
                    <input type="tel" class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-800 bg-transparent focus:outline-none focus:ring-2 focus:ring-studio-500 transition-shadow" placeholder="(555) 123-4567" required>
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Password</label>
                    <input type="password" class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-800 bg-transparent focus:outline-none focus:ring-2 focus:ring-studio-500 transition-shadow" placeholder="••••••••" required>
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">Confirm Password</label>
                    <input type="password" class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-800 bg-transparent focus:outline-none focus:ring-2 focus:ring-studio-500 transition-shadow" placeholder="••••••••" required>
                </div>
                
                <div class="flex items-start pt-2">
                    <input type="checkbox" id="terms" required class="mt-1 w-4 h-4 text-studio-600 border-gray-300 rounded focus:ring-studio-500">
                    <label for="terms" class="ml-2 text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
                        I agree to the <a href="#" class="text-studio-600 dark:text-studio-400 hover:underline">Terms & Conditions</a> and <a href="#" class="text-studio-600 dark:text-studio-400 hover:underline">Privacy Policy</a> for managing my photography assets.
                    </label>
                </div>
                
                <a href="dashboard.html" class="block w-full py-3.5 px-4 mt-4 bg-studio-600 hover:bg-studio-700 text-white text-center font-bold rounded-xl transition-colors shadow-lg shadow-studio-500/20">Create Account</a>
            </form>
            
            <p class="mt-8 text-center text-sm text-gray-600 dark:text-gray-400">
                Already have an account? <a href="login.html" class="font-bold text-studio-600 dark:text-studio-400 hover:underline">Log in</a>
            </p>
        </div>
    </div>

    <!-- Visual Area -->
    <div class="hidden lg:block lg:w-1/2 relative bg-studio-50">
        <img src="https://images.unsplash.com/photo-1533743983669-94fa5c4338ec?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Pet photography experience" class="absolute inset-0 w-full h-full object-cover">
        <div class="absolute inset-0 bg-gradient-to-t from-studio-900/90 via-studio-900/40 to-transparent flex flex-col justify-end p-16">
            <div class="bg-white/10 backdrop-blur-md p-8 rounded-3xl border border-white/20">
                <h3 class="text-white text-2xl font-bold mb-4">Client Portal Benefits</h3>
                <ul class="space-y-3 text-white/90">
                    <li class="flex items-center"><i class="fas fa-check-circle text-studio-400 mr-3"></i> Secure proof gallery viewing</li>
                    <li class="flex items-center"><i class="fas fa-check-circle text-studio-400 mr-3"></i> Easy photo selection for retouching</li>
                    <li class="flex items-center"><i class="fas fa-check-circle text-studio-400 mr-3"></i> Track your premium print orders</li>
                    <li class="flex items-center"><i class="fas fa-check-circle text-studio-400 mr-3"></i> Seamless session booking</li>
                </ul>
            </div>
        </div>
    </div>
    
    {back_to_top}
</body>
</html>"""


# Writing files
for filename, content in pages.items():
    write_file(filename, content)
    
print("Files generated successfully.")
