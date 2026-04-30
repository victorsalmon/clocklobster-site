(function() {
    'use strict';

    var menuToggle = document.querySelector('.mobile-menu-toggle');
    var siteHeader = document.querySelector('.site-header');

    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            var isOpen = siteHeader.classList.toggle('mobile-menu-open');
            this.setAttribute('aria-expanded', isOpen);
        });
    }

    document.querySelectorAll('.nav-menu a').forEach(function(link) {
        link.addEventListener('click', function() {
            siteHeader.classList.remove('mobile-menu-open');
            if (menuToggle) menuToggle.setAttribute('aria-expanded', 'false');
        });
    });

    var chatBubble = document.querySelector('.chat-bubble');
    var chatWindow = document.querySelector('.chat-window');
    var chatInput = document.querySelector('.chat-input input');
    var chatSend = document.querySelector('.chat-input button');
    var chatMessages = document.querySelector('.chat-messages');

    if (chatBubble && chatWindow) {
        chatBubble.addEventListener('click', function() {
            chatWindow.classList.toggle('open');
            var isOpen = chatWindow.classList.contains('open');
            chatBubble.setAttribute('aria-expanded', isOpen);
            if (isOpen && chatInput) chatInput.focus();
        });
    }

    var botResponses = [
        "Clock Lobster builds bespoke digital employees and automation machines that handle repetitive tasks 24/7. Would you like to know which service fits your business best?",
        "We specialize in business time reclamation — automating menial work so your team can focus on growth. Our solutions start at $800.",
        "Data sovereignty is core to everything we build. Your data stays in containers you control, backed up to cloud regions compliant with your local laws.",
        "The best way to get started is a free 30-minute Reclamation Consultation. We'll map your biggest time drains and show you what's possible.",
        "We carry liability insurance and consult legal experts to ensure every deployment meets your compliance requirements."
    ];

    function addMessage(text, sender) {
        if (!chatMessages) return;
        var msg = document.createElement('div');
        msg.className = 'chat-message ' + sender;
        msg.textContent = text;
        chatMessages.appendChild(msg);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function handleChatSend() {
        if (!chatInput) return;
        var text = chatInput.value.trim();
        if (!text) return;

        addMessage(text, 'user');
        chatInput.value = '';

        setTimeout(function() {
            var response = botResponses[Math.floor(Math.random() * botResponses.length)];
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

    var FORM_API_URL = 'https://o5vk8qguvg.execute-api.ca-west-1.amazonaws.com/submit';

    function getFormSource(form) {
        if (form.closest('.footer-form')) return 'footer';
        if (form.closest('.lead-magnet-section')) return 'lead-magnet';
        if (window.location.pathname.includes('contact')) return 'contact';
        return 'unknown';
    }

    function showFormSuccess(form) {
        var successEl = form.parentElement.querySelector('.form-success');
        if (successEl) {
            form.style.display = 'none';
            successEl.style.display = 'block';
        }
        var redirect = form.getAttribute('data-redirect');
        if (redirect) {
            setTimeout(function() {
                window.location.href = redirect;
            }, 2000);
        }
    }

    document.querySelectorAll('.static-form').forEach(function(form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            var submitBtn = form.querySelector('button[type="submit"]');
            var originalText = submitBtn ? submitBtn.textContent : '';

            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = 'Sending...';
            }

            var formData = new FormData(form);
            var data = {
                name: (formData.get('name') || '').trim(),
                email: (formData.get('email') || '').trim(),
                company: (formData.get('company') || '').trim(),
                message: (formData.get('message') || '').trim(),
                budget: (formData.get('budget') || '').trim(),
                source: getFormSource(form)
            };

            if (FORM_API_URL && FORM_API_URL !== 'FORM_API_URL_PLACEHOLDER') {
                fetch(FORM_API_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                }).then(function(response) {
                    if (response.ok) {
                        showFormSuccess(form);
                    } else {
                        console.error('Form submission failed:', response.status);
                        if (submitBtn) {
                            submitBtn.disabled = false;
                            submitBtn.textContent = originalText || 'Send Message';
                        }
                        alert('Something went wrong. Please try again or email us directly at hello@clocklobster.com');
                    }
                }).catch(function(err) {
                    console.error('Form submission error:', err);
                    if (submitBtn) {
                        submitBtn.disabled = false;
                        submitBtn.textContent = originalText || 'Send Message';
                    }
                    alert('Something went wrong. Please try again or email us directly at hello@clocklobster.com');
                });
            } else {
                showFormSuccess(form);
            }
        });
    });

    var observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
    var observer = new IntersectionObserver(function(entries) {
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
