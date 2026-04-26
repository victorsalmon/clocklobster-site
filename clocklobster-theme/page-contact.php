<?php
/**
 * Template Name: Contact
 *
 * @package Clock Lobster
 */

get_header();
?>

<!-- Hero -->
<section class="hero" style="padding-bottom: 4rem;">
    <div class="container text-center">
        <span class="section-label">Contact</span>
        <h1 class="hero-title" style="max-width: 700px; margin-left: auto; margin-right: auto;">Let's Talk About Your Time.</h1>
        <p class="hero-subtitle mx-auto" style="max-width: 560px;">Tell us what's eating your team's hours. We'll respond within one business day — usually much sooner.</p>
    </div>
</section>

<!-- Contact Grid -->
<section class="section" style="padding-top: 0;">
    <div class="container">
        <div class="contact-grid">
            <div>
                <span class="section-label">Get in Touch</span>
                <h2 class="section-title" style="font-size: 1.5rem; margin-bottom: 1rem;">We read every message.</h2>
                <p style="margin-bottom: 2rem;">Whether you're ready to automate or just curious about what's possible, we're here. No sales scripts. No pressure. Just honest answers from people who build this stuff every day.</p>

                <div class="contact-info-item">
                    <div class="contact-info-icon">📧</div>
                    <div>
                        <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">Email</h4>
                        <p style="font-size: 0.9375rem;">hello@clocklobster.com</p>
                    </div>
                </div>

                <div class="contact-info-item">
                    <div class="contact-info-icon">⏱️</div>
                    <div>
                        <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">Response Time</h4>
                        <p style="font-size: 0.9375rem;">Within 24 hours, often same-day</p>
                    </div>
                </div>

                <div class="contact-info-item">
                    <div class="contact-info-icon">🌍</div>
                    <div>
                        <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">Availability</h4>
                        <p style="font-size: 0.9375rem;">Monday – Friday, 9am – 6pm ET<br>Consultations available worldwide via video</p>
                    </div>
                </div>

                <div class="glass-card" style="margin-top: 2rem;">
                    <h4 style="font-size: 1rem; margin-bottom: 0.5rem;">Prefer to book directly?</h4>
                    <p style="font-size: 0.9375rem; margin-bottom: 1rem;">Skip the form and schedule your free 30-minute Reclamation Consultation now.</p>
                    <a href="<?php echo esc_url( home_url( '/book-consultation/' ) ); ?>" class="btn btn-primary">Book a Consultation</a>
                </div>
            </div>

            <div>
                <div class="lead-magnet-form" style="padding: 2.5rem;">
                    <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem;">Send us a message</h3>
                    <p style="font-size: 0.9375rem; color: var(--text-muted); margin-bottom: 1.5rem;">Fill out the form below and we'll get back to you shortly.</p>

                    <!-- Fluent Form placeholder: Contact form -->
                    <div class="fluent-form-placeholder" style="margin-bottom: 1rem; text-align: left;">
                        <p style="text-align: left;"><strong>Fields needed in Fluent Forms:</strong></p>
                        <ul style="color: var(--text-muted); font-size: 0.875rem; line-height: 2; margin-left: 1rem; list-style: disc;">
                            <li>Full Name (required)</li>
                            <li>Email Address (required)</li>
                            <li>Company Name</li>
                            <li>What repetitive tasks are eating your team's time? (textarea)</li>
                            <li>Budget range (dropdown: Under $2k, $2k–$8k, $8k–$20k, $20k+, Not sure yet)</li>
                        </ul>
                        <p style="margin-top: 1rem; font-size: 0.875rem;"><em>On submission: redirect to /book-consultation/ and send webhook to Attio CRM via WP Webhooks.</em></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- FAQ Teaser -->
<section class="section" style="border-top: 1px solid var(--border);">
    <div class="container">
        <div class="text-center max-w-3xl mx-auto mb-8">
            <span class="section-label">FAQ</span>
            <h2 class="section-title">Common Questions</h2>
        </div>
        <div class="grid-2">
            <div class="glass-card">
                <h4 style="font-size: 1.125rem; margin-bottom: 0.5rem;">How long does a typical project take?</h4>
                <p style="font-size: 0.9375rem;">Starter integrations can go live in 3–5 days. Full digital employee deployments typically take 2–4 weeks, depending on the complexity of your workflows and how quickly we can access the required systems.</p>
            </div>
            <div class="glass-card">
                <h4 style="font-size: 1.125rem; margin-bottom: 0.5rem;">Do you work with our existing tools?</h4>
                <p style="font-size: 0.9375rem;">Absolutely. We integrate with Gmail, Outlook, Slack, Salesforce, HubSpot, Zapier, Pabbly Connect, and virtually any system with an API. If it has an interface, we can probably connect to it.</p>
            </div>
            <div class="glass-card">
                <h4 style="font-size: 1.125rem; margin-bottom: 0.5rem;">What if we're not technical?</h4>
                <p style="font-size: 0.9375rem;">You don't need to be. We handle all the technical architecture, deployment, and maintenance. You just tell us what you want to happen — we build the machine that makes it happen.</p>
            </div>
            <div class="glass-card">
                <h4 style="font-size: 1.125rem; margin-bottom: 0.5rem;">Is our data really private?</h4>
                <p style="font-size: 0.9375rem;">Yes. We deploy inside containerized environments you control. Your data never trains public AI models, never commingles with other clients, and is backed up only to regions compliant with your local laws. Read more on our <a href="<?php echo esc_url( home_url( '/privacy/' ) ); ?>" style="color: var(--accent); text-decoration: underline;">Data Sovereignty page</a>.</p>
            </div>
        </div>
    </div>
</section>

<?php get_footer(); ?>
