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

    // Active Navigation State
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    
    // Desktop Nav
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath) {
            link.classList.remove('text-gray-600', 'dark:text-gray-300', 'hover:text-studio-500', 'dark:hover:text-studio-400', 'font-medium');
            link.classList.add('text-studio-600', 'dark:text-studio-400', 'font-bold');
        }
    });

    // Mobile Nav
    if (mobileMenu) {
        const mobileNavLinks = mobileMenu.querySelectorAll('a');
        mobileNavLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (href === currentPath) {
                // Remove inactive classes
                link.classList.remove('text-gray-700', 'dark:text-gray-200', 'hover:bg-studio-50', 'hover:text-studio-600', 'dark:hover:bg-neutral-800');
                // Add active classes
                link.classList.add('bg-studio-50', 'text-studio-600', 'dark:bg-neutral-800', 'dark:text-studio-400');
            }
        });
    }
});
