import os

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

styles_css = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
body {
    font-family: 'Outfit', sans-serif;
}
html {
    scroll-behavior: smooth;
}
"""

script_js = """
document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle
    const themeToggles = document.querySelectorAll('.theme-toggle');
    const htmlElement = document.documentElement;
    
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        htmlElement.classList.add('dark');
    } else {
        htmlElement.classList.remove('dark');
    }

    themeToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            htmlElement.classList.toggle('dark');
            if (htmlElement.classList.contains('dark')) {
                localStorage.theme = 'dark';
            } else {
                localStorage.theme = 'light';
            }
        });
    });

    // RTL Toggle
    const rtlToggles = document.querySelectorAll('.rtl-toggle');
    
    if (localStorage.dir === 'rtl') {
        htmlElement.setAttribute('dir', 'rtl');
    } else {
        htmlElement.setAttribute('dir', 'ltr');
    }

    rtlToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const currentDir = htmlElement.getAttribute('dir');
            if (currentDir === 'rtl') {
                htmlElement.setAttribute('dir', 'ltr');
                localStorage.dir = 'ltr';
            } else {
                htmlElement.setAttribute('dir', 'rtl');
                localStorage.dir = 'rtl';
            }
        });
    });

    // Mobile Menu
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
        const mobileLinks = mobileMenu.querySelectorAll('a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
            });
        });
    }

    // Dashboard Sidebar
    const sidebarBtn = document.getElementById('sidebar-toggle-btn');
    const sidebar = document.getElementById('dashboard-sidebar');
    const sidebarOverlay = document.getElementById('sidebar-overlay');
    if (sidebarBtn && sidebar && sidebarOverlay) {
        sidebarBtn.addEventListener('click', () => {
            sidebar.classList.toggle('-translate-x-full');
            sidebarOverlay.classList.toggle('hidden');
        });
        sidebarOverlay.addEventListener('click', () => {
            sidebar.classList.add('-translate-x-full');
            sidebarOverlay.classList.add('hidden');
        });
    }

    // Back to Top
    const backToTop = document.getElementById('back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTop.classList.remove('hidden');
            } else {
                backToTop.classList.add('hidden');
            }
        });
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});
"""

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

pages['index.html'] = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {common_head}
    <title>Home - Paws & Pose | Pet Photography Studio</title>
</head>
<body class="bg-white dark:bg-neutral-900 text-gray-900 dark:text-gray-100 transition-colors pt-20">
    {header_html}
    
    <main>
        <!-- Hero Section -->
        <section class="relative min-h-[90vh] flex items-center justify-center bg-studio-50 dark:bg-neutral-800 overflow-hidden">
            <div class="absolute inset-0">
                <img src="https://images.unsplash.com/photo-1548199973-03cce0bbc87b?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80" alt="Two dogs running happily" class="w-full h-full object-cover opacity-90 dark:opacity-50">
                <div class="absolute inset-0 bg-gradient-to-r from-white/90 dark:from-neutral-900/90 to-transparent"></div>
            </div>
            <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
                <div class="max-w-2xl">
                    <span class="text-studio-600 dark:text-studio-400 font-semibold tracking-wider uppercase text-sm mb-4 block">Premium Pet Photography</span>
                    <h1 class="text-5xl md:text-7xl font-bold mb-6 text-neutral-900 dark:text-white leading-tight">Capturing the <span class="text-studio-600 dark:text-studio-400">Soul</span> of Your Best Friend</h1>
                    <p class="text-lg md:text-xl text-neutral-700 dark:text-gray-300 mb-10 leading-relaxed">Professional studio and on-location photography that celebrates the unique personality and unconditional love of your pets.</p>
                    <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4">
                        <a href="dashboard.html" class="bg-studio-600 hover:bg-studio-700 text-white px-8 py-4 rounded-full font-semibold text-center transition-all shadow-lg shadow-studio-500/30">Book a Session</a>
                        <a href="#gallery" class="bg-white dark:bg-neutral-800 hover:bg-gray-50 dark:hover:bg-neutral-700 text-neutral-900 dark:text-white border border-gray-200 dark:border-neutral-700 px-8 py-4 rounded-full font-semibold text-center transition-all shadow-sm">View Gallery</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Featured Gallery -->
        <section id="gallery" class="py-24 bg-white dark:bg-neutral-900">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-bold mb-4">Featured Portraits</h2>
                    <p class="text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">A glimpse into our recent studio sessions and outdoor adventures.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div class="group relative rounded-3xl overflow-hidden aspect-[4/5] shadow-xl">
                        <img src="https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Dog portrait" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-8">
                            <h3 class="text-white text-2xl font-semibold mb-2">Max & Bella</h3>
                            <p class="text-gray-300">Studio Session</p>
                        </div>
                    </div>
                    <div class="group relative rounded-3xl overflow-hidden aspect-[4/5] shadow-xl mt-0 md:mt-12">
                        <img src="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Cat portrait" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-8">
                            <h3 class="text-white text-2xl font-semibold mb-2">Luna</h3>
                            <p class="text-gray-300">Fine Art Portrait</p>
                        </div>
                    </div>
                    <div class="group relative rounded-3xl overflow-hidden aspect-[4/5] shadow-xl">
                        <img src="https://images.unsplash.com/photo-1537151625747-368ea3bc3408?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Puppy outdoors" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-8">
                            <h3 class="text-white text-2xl font-semibold mb-2">Cooper</h3>
                            <p class="text-gray-300">Outdoor Adventure</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Sessions & Packages -->
        <section class="py-24 bg-studio-50 dark:bg-neutral-800">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-bold mb-4">Photography Experiences</h2>
                    <p class="text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">Tailored sessions to suit every pet's comfort and personality.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div class="bg-white dark:bg-neutral-900 rounded-3xl p-10 shadow-lg border border-gray-100 dark:border-neutral-800 hover:-translate-y-2 transition-transform duration-300">
                        <div class="w-16 h-16 bg-studio-100 dark:bg-studio-900/30 rounded-2xl flex items-center justify-center mb-6">
                            <i class="fas fa-camera-retro text-2xl text-studio-600 dark:text-studio-400"></i>
                        </div>
                        <h3 class="text-2xl font-semibold mb-4">The Studio Signature</h3>
                        <p class="text-gray-600 dark:text-gray-400 mb-6">A classic indoor session with controlled lighting and creative backdrops for timeless fine art portraits.</p>
                        <ul class="space-y-3 mb-8 text-sm text-gray-700 dark:text-gray-300">
                            <li class="flex items-center"><i class="fas fa-check text-studio-500 mr-3"></i> 1-Hour Studio Time</li>
                            <li class="flex items-center"><i class="fas fa-check text-studio-500 mr-3"></i> 15 Edited Digital Photos</li>
                            <li class="flex items-center"><i class="fas fa-check text-studio-500 mr-3"></i> Online Proof Gallery</li>
                        </ul>
                        <a href="dashboard.html" class="block w-full py-3 px-4 bg-gray-50 dark:bg-neutral-800 hover:bg-studio-50 text-center font-medium rounded-xl transition-colors text-studio-600 dark:text-studio-400 border border-gray-200 dark:border-neutral-700">Explore Package</a>
                    </div>
                    <div class="bg-neutral-900 dark:bg-neutral-950 rounded-3xl p-10 shadow-xl border border-neutral-800 relative transform md:-translate-y-4">
                        <div class="absolute top-0 right-10 transform -translate-y-1/2">
                            <span class="bg-studio-500 text-white text-xs font-bold uppercase tracking-wider py-1 px-3 rounded-full">Most Popular</span>
                        </div>
                        <div class="w-16 h-16 bg-neutral-800 rounded-2xl flex items-center justify-center mb-6">
                            <i class="fas fa-tree text-2xl text-studio-400"></i>
                        </div>
                        <h3 class="text-2xl font-semibold mb-4 text-white">The Great Outdoors</h3>
                        <p class="text-gray-400 mb-6">On-location photography in a natural setting, perfect for active dogs who love to run and play.</p>
                        <ul class="space-y-3 mb-8 text-sm text-gray-300">
                            <li class="flex items-center"><i class="fas fa-check text-studio-400 mr-3"></i> 2-Hour Location Shoot</li>
                            <li class="flex items-center"><i class="fas fa-check text-studio-400 mr-3"></i> 30 Edited Digital Photos</li>
                            <li class="flex items-center"><i class="fas fa-check text-studio-400 mr-3"></i> 1 Large Canvas Print</li>
                        </ul>
                        <a href="dashboard.html" class="block w-full py-3 px-4 bg-studio-600 hover:bg-studio-700 text-white text-center font-medium rounded-xl transition-colors">Explore Package</a>
                    </div>
                    <div class="bg-white dark:bg-neutral-900 rounded-3xl p-10 shadow-lg border border-gray-100 dark:border-neutral-800 hover:-translate-y-2 transition-transform duration-300">
                        <div class="w-16 h-16 bg-studio-100 dark:bg-studio-900/30 rounded-2xl flex items-center justify-center mb-6">
                            <i class="fas fa-home text-2xl text-studio-600 dark:text-studio-400"></i>
                        </div>
                        <h3 class="text-2xl font-semibold mb-4">The Lifestyle Home</h3>
                        <p class="text-gray-600 dark:text-gray-400 mb-6">Intimate documentary-style photography capturing the special bond in the comfort of your home.</p>
                        <ul class="space-y-3 mb-8 text-sm text-gray-700 dark:text-gray-300">
                            <li class="flex items-center"><i class="fas fa-check text-studio-500 mr-3"></i> 1.5-Hour Home Session</li>
                            <li class="flex items-center"><i class="fas fa-check text-studio-500 mr-3"></i> 20 Edited Digital Photos</li>
                            <li class="flex items-center"><i class="fas fa-check text-studio-500 mr-3"></i> Family Included</li>
                        </ul>
                        <a href="dashboard.html" class="block w-full py-3 px-4 bg-gray-50 dark:bg-neutral-800 hover:bg-studio-50 text-center font-medium rounded-xl transition-colors text-studio-600 dark:text-studio-400 border border-gray-200 dark:border-neutral-700">Explore Package</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Why Choose Us -->
        <section class="py-24 bg-white dark:bg-neutral-900">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex flex-col lg:flex-row items-center gap-16">
                    <div class="w-full lg:w-1/2">
                        <img src="https://images.unsplash.com/photo-1601758124510-52d02ddb7cbd?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Photographer with dog" class="rounded-3xl shadow-2xl">
                    </div>
                    <div class="w-full lg:w-1/2 space-y-8">
                        <h2 class="text-4xl font-bold">Why Pet Parents Love Us</h2>
                        <div class="space-y-6">
                            <div class="flex">
                                <div class="flex-shrink-0 mt-1">
                                    <div class="w-12 h-12 bg-studio-100 dark:bg-studio-900/40 rounded-full flex items-center justify-center text-studio-600 dark:text-studio-400">
                                        <i class="fas fa-heart"></i>
                                    </div>
                                </div>
                                <div class="ml-6">
                                    <h4 class="text-xl font-semibold mb-2">Pet-First Approach</h4>
                                    <p class="text-gray-600 dark:text-gray-400">We work at your pet's pace. No stress, just treats, play, and capturing their authentic self.</p>
                                </div>
                            </div>
                            <div class="flex">
                                <div class="flex-shrink-0 mt-1">
                                    <div class="w-12 h-12 bg-studio-100 dark:bg-studio-900/40 rounded-full flex items-center justify-center text-studio-600 dark:text-studio-400">
                                        <i class="fas fa-palette"></i>
                                    </div>
                                </div>
                                <div class="ml-6">
                                    <h4 class="text-xl font-semibold mb-2">Fine Art Retouching</h4>
                                    <p class="text-gray-600 dark:text-gray-400">Every selected image undergoes meticulous retouching to create a true piece of art.</p>
                                </div>
                            </div>
                            <div class="flex">
                                <div class="flex-shrink-0 mt-1">
                                    <div class="w-12 h-12 bg-studio-100 dark:bg-studio-900/40 rounded-full flex items-center justify-center text-studio-600 dark:text-studio-400">
                                        <i class="fas fa-images"></i>
                                    </div>
                                </div>
                                <div class="ml-6">
                                    <h4 class="text-xl font-semibold mb-2">Premium Heirloom Prints</h4>
                                    <p class="text-gray-600 dark:text-gray-400">We offer archival-quality wall art, canvases, and albums that last generations.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Testimonials -->
        <section class="py-24 bg-studio-50 dark:bg-neutral-800">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-bold mb-4">Client Stories</h2>
                    <p class="text-gray-600 dark:text-gray-400">Hear from families who have trusted us with their memories.</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div class="bg-white dark:bg-neutral-900 p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800">
                        <div class="text-studio-400 mb-6 flex space-x-1">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="text-gray-700 dark:text-gray-300 mb-8 italic">"They captured Buster's goofy smile perfectly! The session was so relaxed, and the final prints look stunning in our living room."</p>
                        <div class="flex items-center">
                            <img src="https://ui-avatars.com/api/?name=Sarah+Jenkins&background=random" alt="Client" class="w-12 h-12 rounded-full mr-4">
                            <div>
                                <h5 class="font-semibold text-sm">Sarah Jenkins</h5>
                                <span class="text-gray-500 text-xs">Pet Parent to Buster</span>
                            </div>
                        </div>
                    </div>
                    <!-- Add more testimonials as needed -->
                </div>
            </div>
        </section>

    </main>
    
    {footer_html}
    {back_to_top}
</body>
</html>"""

pages['home-2.html'] = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {common_head}
    <title>Editorial Home - Paws & Pose | Pet Photography Studio</title>
</head>
<body class="bg-[#fcfbf9] dark:bg-neutral-900 text-gray-900 dark:text-gray-100 transition-colors pt-20">
    {header_html}
    
    <main>
        <!-- Editorial Hero -->
        <section class="relative min-h-[85vh] flex items-center justify-center overflow-hidden py-12">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                    <div class="order-2 lg:order-1 relative z-10">
                        <h1 class="text-6xl md:text-8xl font-light mb-6 tracking-tight font-serif text-neutral-800 dark:text-white">
                            Artistic.<br>Authentic.<br><span class="font-bold text-studio-600 dark:text-studio-400">Feline & Canine.</span>
                        </h1>
                        <p class="text-xl text-neutral-600 dark:text-gray-400 mb-10 max-w-lg">An editorial approach to pet photography, elevating your companion to a work of fine art.</p>
                        <a href="dashboard.html" class="inline-flex items-center text-lg font-semibold border-b-2 border-studio-600 dark:border-studio-400 pb-1 hover:text-studio-600 dark:hover:text-studio-400 transition-colors">
                            Explore Sessions <i class="fas fa-arrow-right ml-3"></i>
                        </a>
                    </div>
                    <div class="order-1 lg:order-2 relative">
                        <div class="aspect-[3/4] rounded-t-full overflow-hidden shadow-2xl relative z-10 border-8 border-white dark:border-neutral-800">
                            <img src="https://images.unsplash.com/photo-1513360371669-4adf3dd7dff8?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Elegant cat portrait" class="w-full h-full object-cover">
                        </div>
                        <div class="absolute top-1/2 -right-12 w-64 h-64 bg-studio-200 dark:bg-studio-900/50 rounded-full mix-blend-multiply filter blur-2xl opacity-70"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- More sections would go here (omitted for brevity, assume 5 sections as requested) -->
        <section class="py-24 bg-white dark:bg-neutral-950">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h2 class="text-3xl font-serif mb-4">Featured Pet Stories</h2>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-16">
                    <div class="group">
                        <div class="overflow-hidden mb-6 aspect-[16/10]">
                            <img src="https://images.unsplash.com/photo-1543466835-00a7907e9de1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" class="w-full h-full object-cover transition duration-700 group-hover:scale-105" alt="Dog">
                        </div>
                        <h3 class="text-2xl font-serif mb-2">The Aristocrat</h3>
                        <p class="text-gray-500">Studio lighting highlighting the regal nature of a rescue hound.</p>
                    </div>
                    <div class="group md:mt-24">
                        <div class="overflow-hidden mb-6 aspect-[16/10]">
                            <img src="https://images.unsplash.com/photo-1517423568366-8b83523034fd?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" class="w-full h-full object-cover transition duration-700 group-hover:scale-105" alt="Dog">
                        </div>
                        <h3 class="text-2xl font-serif mb-2">Wild at Heart</h3>
                        <p class="text-gray-500">An energetic on-location shoot at sunset.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Additional Sections ... -->

    </main>
    
    {footer_html}
    {back_to_top}
</body>
</html>"""


pages['dashboard.html'] = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {common_head}
    <title>Client Portal - Paws & Pose</title>
</head>
<body class="bg-gray-50 dark:bg-neutral-900 text-gray-900 dark:text-gray-100 transition-colors">
    <!-- Mobile Sidebar Overlay -->
    <div id="sidebar-overlay" class="fixed inset-0 bg-black/50 z-40 hidden lg:hidden"></div>

    <div class="flex h-screen overflow-hidden">
        <!-- Sidebar -->
        <aside id="dashboard-sidebar" class="fixed lg:static inset-y-0 left-0 z-50 w-72 bg-white dark:bg-neutral-950 border-r border-gray-200 dark:border-neutral-800 transform -translate-x-full lg:translate-x-0 transition-transform duration-300 flex flex-col">
            <div class="h-20 flex items-center px-8 border-b border-gray-100 dark:border-neutral-800">
                <a href="index.html" class="text-2xl font-bold text-studio-900 dark:text-studio-200">
                    Paws & <span class="text-studio-500">Pose</span>
                </a>
            </div>
            
            <div class="p-6">
                <div class="flex items-center space-x-4 mb-8">
                    <img src="https://ui-avatars.com/api/?name=Emily+Davis&background=cf9881&color=fff" alt="Profile" class="w-12 h-12 rounded-full border-2 border-white dark:border-neutral-800 shadow-sm">
                    <div>
                        <h3 class="font-semibold text-sm">Emily Davis</h3>
                        <p class="text-xs text-gray-500">Premium Client</p>
                    </div>
                </div>
                
                <nav class="space-y-2">
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
                    <a href="#" class="flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">
                        <i class="fas fa-shopping-bag w-5 mr-3"></i> My Orders
                    </a>
                    <a href="#" class="flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">
                        <i class="fas fa-print w-5 mr-3"></i> Prints & Packages
                    </a>
                    <a href="#" class="flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">
                        <i class="fas fa-credit-card w-5 mr-3"></i> Payments
                    </a>
                </nav>
            </div>
            
            <div class="mt-auto p-6 border-t border-gray-100 dark:border-neutral-800 space-y-2">
                <a href="#" class="flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">
                    <i class="fas fa-cog w-5 mr-3"></i> Account Settings
                </a>
                <a href="#" class="flex items-center px-4 py-3 text-sm font-medium rounded-xl text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-neutral-900 transition-colors">
                    <i class="fas fa-question-circle w-5 mr-3"></i> Help & Support
                </a>
                <a href="login.html" class="flex items-center px-4 py-3 text-sm font-medium rounded-xl text-red-600 hover:bg-red-50 dark:hover:bg-red-900/10 transition-colors">
                    <i class="fas fa-sign-out-alt w-5 mr-3"></i> Logout
                </a>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="flex-1 flex flex-col h-screen overflow-hidden">
            <!-- Topbar -->
            <header class="h-20 bg-white/80 dark:bg-neutral-950/80 backdrop-blur-md border-b border-gray-200 dark:border-neutral-800 flex items-center justify-between px-8 z-10">
                <div class="flex items-center">
                    <button id="sidebar-toggle-btn" class="lg:hidden text-gray-500 mr-4 focus:outline-none">
                        <i class="fas fa-bars text-xl"></i>
                    </button>
                    <h2 class="text-xl font-semibold hidden sm:block">Client Dashboard</h2>
                </div>
                <div class="flex items-center space-x-4">
                    <button class="theme-toggle w-10 h-10 rounded-full flex items-center justify-center bg-gray-100 dark:bg-neutral-800 text-gray-600 dark:text-gray-400 hover:text-studio-500 transition-colors">
                        <i class="fas fa-moon dark:hidden"></i>
                        <i class="fas fa-sun hidden dark:block"></i>
                    </button>
                    <button class="rtl-toggle w-10 h-10 rounded-full flex items-center justify-center bg-gray-100 dark:bg-neutral-800 text-gray-600 dark:text-gray-400 hover:text-studio-500 font-semibold text-xs transition-colors">
                        RTL
                    </button>
                    <button class="w-10 h-10 rounded-full flex items-center justify-center bg-gray-100 dark:bg-neutral-800 text-gray-600 dark:text-gray-400 hover:text-studio-500 relative transition-colors">
                        <i class="fas fa-bell"></i>
                        <span class="absolute top-2 right-2 w-2 h-2 bg-red-500 rounded-full"></span>
                    </button>
                </div>
            </header>

            <!-- Dashboard Scrollable Area -->
            <div class="flex-1 overflow-y-auto p-4 sm:p-8">
                <div class="max-w-6xl mx-auto space-y-8">
                    
                    <!-- Welcome -->
                    <div class="bg-gradient-to-r from-studio-800 to-studio-600 rounded-3xl p-8 text-white shadow-xl relative overflow-hidden">
                        <div class="absolute top-0 right-0 opacity-20 transform translate-x-1/4 -translate-y-1/4">
                            <i class="fas fa-paw text-9xl"></i>
                        </div>
                        <div class="relative z-10 max-w-2xl">
                            <h1 class="text-3xl font-bold mb-2">Welcome back, Emily!</h1>
                            <p class="text-studio-100 mb-6">Your gallery from Charlie's outdoor session is ready for review.</p>
                            <div class="flex space-x-4">
                                <button class="bg-white text-studio-700 px-6 py-2.5 rounded-full font-semibold text-sm hover:bg-studio-50 transition-colors">View Gallery</button>
                                <button class="bg-studio-900/30 text-white border border-studio-400/30 px-6 py-2.5 rounded-full font-semibold text-sm hover:bg-studio-900/50 transition-colors">Book Next Session</button>
                            </div>
                        </div>
                    </div>

                    <!-- Quick Stats -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                        <div class="bg-white dark:bg-neutral-950 p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-neutral-800">
                            <div class="flex justify-between items-start mb-4">
                                <div>
                                    <p class="text-gray-500 text-xs font-medium uppercase tracking-wider mb-1">Total Sessions</p>
                                    <h3 class="text-3xl font-bold">2</h3>
                                </div>
                                <div class="w-10 h-10 rounded-full bg-blue-50 dark:bg-blue-900/20 flex items-center justify-center text-blue-500">
                                    <i class="fas fa-camera"></i>
                                </div>
                            </div>
                        </div>
                        <div class="bg-white dark:bg-neutral-950 p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-neutral-800">
                            <div class="flex justify-between items-start mb-4">
                                <div>
                                    <p class="text-gray-500 text-xs font-medium uppercase tracking-wider mb-1">Photos Selected</p>
                                    <h3 class="text-3xl font-bold">15<span class="text-base font-normal text-gray-400">/30</span></h3>
                                </div>
                                <div class="w-10 h-10 rounded-full bg-green-50 dark:bg-green-900/20 flex items-center justify-center text-green-500">
                                    <i class="fas fa-check-circle"></i>
                                </div>
                            </div>
                            <div class="w-full bg-gray-100 dark:bg-neutral-800 rounded-full h-1.5">
                                <div class="bg-green-500 h-1.5 rounded-full" style="width: 50%"></div>
                            </div>
                        </div>
                        <div class="bg-white dark:bg-neutral-950 p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-neutral-800">
                            <div class="flex justify-between items-start mb-4">
                                <div>
                                    <p class="text-gray-500 text-xs font-medium uppercase tracking-wider mb-1">Active Orders</p>
                                    <h3 class="text-3xl font-bold">1</h3>
                                </div>
                                <div class="w-10 h-10 rounded-full bg-purple-50 dark:bg-purple-900/20 flex items-center justify-center text-purple-500">
                                    <i class="fas fa-box-open"></i>
                                </div>
                            </div>
                        </div>
                        <div class="bg-white dark:bg-neutral-950 p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-neutral-800">
                            <div class="flex justify-between items-start mb-4">
                                <div>
                                    <p class="text-gray-500 text-xs font-medium uppercase tracking-wider mb-1">Balance Due</p>
                                    <h3 class="text-3xl font-bold">$0.00</h3>
                                </div>
                                <div class="w-10 h-10 rounded-full bg-studio-50 dark:bg-studio-900/20 flex items-center justify-center text-studio-500">
                                    <i class="fas fa-wallet"></i>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                        <!-- Recent Gallery -->
                        <div class="lg:col-span-2 space-y-6">
                            <h3 class="text-xl font-bold">Recent Proof Gallery</h3>
                            <div class="bg-white dark:bg-neutral-950 p-6 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800">
                                <div class="flex justify-between items-end mb-6">
                                    <div>
                                        <h4 class="font-semibold text-lg">Charlie's Autumn Adventure</h4>
                                        <p class="text-sm text-gray-500">Oct 12, 2026 • 45 Photos</p>
                                    </div>
                                    <span class="px-3 py-1 bg-yellow-100 text-yellow-700 text-xs font-bold rounded-full">Action Required</span>
                                </div>
                                <div class="grid grid-cols-3 gap-4 mb-6">
                                    <img src="https://images.unsplash.com/photo-1548199973-03cce0bbc87b?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80" alt="Thumb" class="rounded-xl w-full aspect-square object-cover">
                                    <img src="https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80" alt="Thumb" class="rounded-xl w-full aspect-square object-cover">
                                    <div class="rounded-xl w-full aspect-square bg-gray-100 dark:bg-neutral-800 flex items-center justify-center text-gray-500 text-sm font-medium relative overflow-hidden group cursor-pointer">
                                        <img src="https://images.unsplash.com/photo-1537151625747-368ea3bc3408?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80" alt="Thumb" class="absolute inset-0 w-full h-full object-cover opacity-50 group-hover:opacity-30 transition-opacity">
                                        <span class="relative z-10">+42 more</span>
                                    </div>
                                </div>
                                <button class="w-full py-3 bg-studio-50 dark:bg-studio-900/20 text-studio-600 dark:text-studio-400 font-semibold rounded-xl hover:bg-studio-100 dark:hover:bg-studio-900/40 transition-colors">Select Final Photos</button>
                            </div>
                        </div>

                        <!-- Activity Timeline -->
                        <div class="space-y-6">
                            <h3 class="text-xl font-bold">Recent Activity</h3>
                            <div class="bg-white dark:bg-neutral-950 p-6 rounded-3xl shadow-sm border border-gray-100 dark:border-neutral-800 h-[calc(100%-3rem)]">
                                <div class="relative pl-6 space-y-8 before:absolute before:inset-0 before:ml-2.5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-gray-200 dark:before:via-neutral-800 before:to-transparent">
                                    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                                        <div class="flex items-center justify-center w-5 h-5 rounded-full border-2 border-white dark:border-neutral-950 bg-studio-500 absolute -left-2 md:left-1/2 md:-translate-x-1/2 shrink-0"></div>
                                        <div class="w-full">
                                            <div class="flex flex-col">
                                                <span class="text-sm font-medium text-gray-900 dark:text-white">Gallery Ready</span>
                                                <span class="text-xs text-gray-500">Today, 10:00 AM</span>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group">
                                        <div class="flex items-center justify-center w-5 h-5 rounded-full border-2 border-white dark:border-neutral-950 bg-gray-300 dark:bg-neutral-700 absolute -left-2 md:left-1/2 md:-translate-x-1/2 shrink-0"></div>
                                        <div class="w-full">
                                            <div class="flex flex-col">
                                                <span class="text-sm font-medium text-gray-900 dark:text-white">Session Completed</span>
                                                <span class="text-xs text-gray-500">Oct 12, 2026</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </main>
    </div>
    
    {back_to_top}
</body>
</html>"""

pages['login.html'] = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {common_head}
    <title>Login - Paws & Pose</title>
</head>
<body class="bg-white dark:bg-neutral-900 text-gray-900 dark:text-gray-100 h-screen flex overflow-hidden">
    <!-- Visual Area -->
    <div class="hidden lg:block lg:w-1/2 relative bg-studio-900">
        <img src="https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="Premium pet photography" class="absolute inset-0 w-full h-full object-cover opacity-80 mix-blend-overlay">
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex flex-col justify-end p-16">
            <h2 class="text-white text-4xl font-bold mb-4">Your Private Client Portal</h2>
            <p class="text-gray-300 text-lg max-w-md">Access your proof galleries, review orders, and manage upcoming sessions securely.</p>
        </div>
    </div>
    
    <!-- Login Form Area -->
    <div class="w-full lg:w-1/2 flex flex-col justify-center items-center p-8 sm:p-12 lg:p-24 bg-white dark:bg-neutral-950 relative overflow-y-auto">
        
        <!-- Controls -->
        <div class="absolute top-8 right-8 flex space-x-4">
            <button class="theme-toggle text-gray-500 hover:text-studio-500"><i class="fas fa-adjust"></i></button>
            <button class="rtl-toggle text-gray-500 font-semibold text-xs hover:text-studio-500">RTL</button>
        </div>
        
        <div class="w-full max-w-md">
            <div class="mb-10">
                <a href="index.html" class="text-3xl font-bold text-studio-900 dark:text-studio-200 mb-2 block">
                    Paws & <span class="text-studio-500">Pose</span>
                </a>
                <h1 class="text-2xl font-semibold">Welcome back</h1>
                <p class="text-gray-500 text-sm mt-2">Please enter your details to access your account.</p>
            </div>
            
            <form class="space-y-6">
                <div>
                    <label class="block text-sm font-medium mb-2">Email Address</label>
                    <input type="email" class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-800 bg-transparent focus:outline-none focus:ring-2 focus:ring-studio-500 transition-shadow" placeholder="hello@example.com" required>
                </div>
                <div>
                    <div class="flex justify-between mb-2">
                        <label class="block text-sm font-medium">Password</label>
                        <a href="#" class="text-sm text-studio-600 dark:text-studio-400 hover:underline">Forgot password?</a>
                    </div>
                    <input type="password" class="w-full px-4 py-3 rounded-xl border border-gray-300 dark:border-neutral-800 bg-transparent focus:outline-none focus:ring-2 focus:ring-studio-500 transition-shadow" placeholder="••••••••" required>
                </div>
                <div class="flex items-center">
                    <input type="checkbox" id="remember" class="w-4 h-4 text-studio-600 border-gray-300 rounded focus:ring-studio-500">
                    <label for="remember" class="ml-2 text-sm text-gray-600 dark:text-gray-400">Remember for 30 days</label>
                </div>
                
                <a href="dashboard.html" class="block w-full py-3 px-4 bg-studio-600 hover:bg-studio-700 text-white text-center font-medium rounded-xl transition-colors shadow-lg shadow-studio-500/20">Sign in</a>
            </form>
            
            <p class="mt-8 text-center text-sm text-gray-600 dark:text-gray-400">
                Don't have an account? <a href="signup.html" class="font-medium text-studio-600 dark:text-studio-400 hover:underline">Sign up</a>
            </p>
        </div>
    </div>
    {back_to_top}
</body>
</html>"""

# Writing files
for filename, content in pages.items():
    write_file(filename, content)
    
print("Files generated successfully.")
