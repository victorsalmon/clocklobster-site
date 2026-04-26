(function() {
    'use strict';

    // Mobile menu toggle
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const siteHeader = document.querySelector('.site-header');

    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            const isOpen = siteHeader.classList.toggle('mobile-menu-open');
            this.setAttribute('aria-expanded', isOpen);
        });
    }

    // Close mobile menu when clicking a nav link
    document.querySelectorAll('.nav-menu a').forEach(function(link) {
        link.addEventListener('click', function() {
            siteHeader.classList.remove('mobile-menu-open');
            if (menuToggle) menuToggle.setAttribute('aria-expanded', 'false');
        });
    });

    // Chat Widget
    const chatBubble = document.querySelector('.chat-bubble');
    const chatWindow = document.querySelector('.chat-window');
    const chatInput = document.querySelector('.chat-input input');
    const chatSend = document.querySelector('.chat-input button');
    const chatMessages = document.querySelector('.chat-messages');

    if (chatBubble && chatWindow) {
        chatBubble.addEventListener('click', function() {
            chatWindow.classList.toggle('open');
            const isOpen = chatWindow.classList.contains('open');
            chatBubble.setAttribute('aria-expanded', isOpen);
            if (isOpen && chatInput) chatInput.focus();
        });
    }

    // Mock chat responses
    const botResponses = [
        "Clock Lobster builds bespoke digital employees and automation machines that handle repetitive tasks 24/7. Would you like to know which service fits your business best?",
        "We specialize in business time reclamation — automating menial work so your team can focus on growth. Our solutions start at $800.",
        "Data sovereignty is core to everything we build. Your data stays in containers you control, backed up to cloud regions compliant with your local laws.",
        "The best way to get started is a free 30-minute Reclamation Consultation. We'll map your biggest time drains and show you what's possible.",
        "We carry liability insurance and consult legal experts to ensure every deployment meets your compliance requirements."
    ];

    function addMessage(text, sender) {
        if (!chatMessages) return;
        const msg = document.createElement('div');
        msg.className = 'chat-message ' + sender;
        msg.textContent = text;
        chatMessages.appendChild(msg);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function handleChatSend() {
        if (!chatInput) return;
        const text = chatInput.value.trim();
        if (!text) return;

        addMessage(text, 'user');
        chatInput.value = '';

        // Simulate typing delay
        setTimeout(function() {
            const response = botResponses[Math.floor(Math.random() * botResponses.length)];
            addMessage(response, 'bot');
        }, 800 + Math.random() * 600);
    }

    if (chatSend) {
        chatSend.addEventListener('click', handleChatSend);
    }
    if (chatInput) {
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') handleChatSend();
        });
    }

    // Scroll-triggered fade-in
    const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    document.querySelectorAll('.glass-card, .step-number, .security-card, .service-card').forEach(function(el) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 500ms ease, transform 500ms ease';
        observer.observe(el);
    });
})();
