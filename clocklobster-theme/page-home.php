<?php
/**
 * Template Name: Homepage
 *
 * @package Clock Lobster
 */

get_header();
?>

<!-- Hero Section -->
<section class="hero">
    <div class="container">
        <div class="hero-grid">
            <div class="hero-content">
                <h1 class="hero-title">Reclaim Your Team's Most Valuable Asset: <span>Time</span>.</h1>
                <p class="hero-subtitle">We rescue wasted hours by deploying bespoke digital employees and sovereign AI infrastructure — so your people can focus on what actually drives growth.</p>
                <div class="hero-actions">
                    <a href="<?php echo esc_url( home_url( '/book-consultation/' ) ); ?>" class="btn btn-primary btn-lg">Book a Reclamation Consultation</a>
                    <a href="#lead-magnet" class="btn btn-secondary btn-lg">Get the Free Playbook</a>
                </div>
            </div>
            <div class="automation-visual">
                <div class="automation-flow">
                    <div class="flow-node person">👤</div>
                    <div class="flow-words">
                        <span>Emails</span>
                        <span>Reports</span>
                        <span>Data</span>
                    </div>
                    <div class="flow-particle p1"></div>
                    <div class="flow-particle p2"></div>
                    <div class="flow-label in">Input</div>

                    <div class="flow-node system">⚙️</div>

                    <div class="flow-particle p3"></div>
                    <div class="flow-particle p4"></div>
                    <div class="flow-label out">Output</div>

                    <div class="flow-node output">📋</div>
                    <div class="flow-reports">
                        <span>Drafted</span>
                        <span>Sorted</span>
                        <span>Done</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Problem / Agitation -->
<section class="section problem-section">
    <div class="container">
        <div class="text-center max-w-3xl mx-auto mb-8">
            <span class="section-label">The Problem</span>
            <h2 class="section-title">How many hours this week were lost to repetition?</h2>
            <p class="section-subtitle mx-auto">Your team is talented. But talent buried under inbox triage, data entry, and status reports is talent wasted. The cost isn't just time — it's missed opportunities, stifled creativity, and burnout.</p>
        </div>
        <div class="grid-3 text-center">
            <div class="glass-card">
                <div class="problem-stat">10+</div>
                <p class="problem-stat-label">Hours per employee lost weekly to repetitive tasks</p>
            </div>
            <div class="glass-card">
                <div class="problem-stat">40%</div>
                <p class="problem-stat-label">Of the work week spent on coordination, not creation</p>
            </div>
            <div class="glass-card">
                <div class="problem-stat">67%</div>
                <p class="problem-stat-label">Of workers report burnout from administrative overload</p>
            </div>
        </div>
    </div>
</section>

<!-- Solution (3-Column) -->
<section class="section">
    <div class="container">
        <div class="text-center max-w-3xl mx-auto mb-8">
            <span class="section-label">The Solution</span>
            <h2 class="section-title">The Clock Lobster Difference</h2>
            <p class="section-subtitle mx-auto">We don't sell software. We build digital employees that work inside your infrastructure, follow your rules, and free your humans to do what humans do best.</p>
        </div>
        <div class="grid-3">
            <div class="glass-card">
                <div class="service-icon">🎯</div>
                <h3>Bespoke Automation</h3>
                <p>Every workflow is unique. We custom-build solutions that match your exact processes — not force you into pre-built templates that almost fit.</p>
            </div>
            <div class="glass-card">
                <div class="service-icon">🤝</div>
                <h3>Human-Centric Design</h3>
                <p>AI should elevate your team, not erase them. We design automations that create windfall time for growth, innovation, and deeper human connection.</p>
            </div>
            <div class="glass-card">
                <div class="service-icon">🔒</div>
                <h3>Data Sovereignty</h3>
                <p>Your data never leaves your control. We deploy inside containerized, sovereign infrastructure with national compliance built in from day one.</p>
            </div>
        </div>
    </div>
</section>

<!-- How It Works -->
<section class="section" style="background: linear-gradient(180deg, var(--bg) 0%, rgba(30,41,59,0.2) 50%, var(--bg) 100%);">
    <div class="container">
        <div class="text-center max-w-3xl mx-auto mb-8">
            <span class="section-label">How It Works</span>
            <h2 class="section-title">From Chaos to Clarity in Three Steps</h2>
        </div>
        <div class="grid-3">
            <div class="glass-card">
                <div class="step-number">1</div>
                <h4 class="step-title">Discovery Call</h4>
                <p class="step-desc">We map your workflows, identify your biggest time drains, and build a prioritized automation roadmap tailored to your business.</p>
            </div>
            <div class="glass-card">
                <div class="step-number">2</div>
                <h4 class="step-title">Build & Deploy</h4>
                <p class="step-desc">We architect your solution using containerized agents, secure integrations, and sovereign infrastructure — with your team looped in at every step.</p>
            </div>
            <div class="glass-card">
                <div class="step-number">3</div>
                <h4 class="step-title">Reclaim & Scale</h4>
                <p class="step-desc">Your digital employees go live. Your humans get their time back. We monitor, optimize, and expand as your business grows.</p>
            </div>
        </div>
    </div>
</section>

<!-- Services Preview -->
<section class="section">
    <div class="container">
        <div class="text-center max-w-3xl mx-auto mb-8">
            <span class="section-label">What We Build</span>
            <h2 class="section-title">Three Ways to Reclaim Time</h2>
            <p class="section-subtitle mx-auto">From intelligent agents that reason like humans to simple integrations that just work — we match the right automation to the right problem.</p>
        </div>
        <div class="grid-3">
            <div class="glass-card service-card">
                <div class="service-icon">🤖</div>
                <h3>Digital Employees</h3>
                <p>AI-powered containers like Nemo Claw and Open Claw that manage inboxes, draft correspondence, schedule meetings, and make decisions within guardrails you set.</p>
                <a href="<?php echo esc_url( home_url( '/services/' ) ); ?>" class="btn btn-secondary mt-4" style="width:100%;">Learn More</a>
            </div>
            <div class="glass-card service-card">
                <div class="service-icon">⚙️</div>
                <h3>Automation Machines</h3>
                <p>Smart containers running process-specific software, connected to LLMs for lightweight reasoning. Ideal for data processing, reporting, and operational routines.</p>
                <a href="<?php echo esc_url( home_url( '/services/' ) ); ?>" class="btn btn-secondary mt-4" style="width:100%;">Learn More</a>
            </div>
            <div class="glass-card service-card">
                <div class="service-icon">🔗</div>
                <h3>Simple Integrations</h3>
                <p>Clean, reliable if-this-then-that automations via Zapier, Pabbly Connect, or direct webhooks. Perfect for straightforward tasks that shouldn't need a human.</p>
                <a href="<?php echo esc_url( home_url( '/services/' ) ); ?>" class="btn btn-secondary mt-4" style="width:100%;">Learn More</a>
            </div>
        </div>
    </div>
</section>

<!-- Trust / Social Proof -->
<section class="section-sm" style="border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
    <div class="container">
        <div class="trust-grid">
            <div class="trust-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                <span>Liability Insurance Coverage</span>
            </div>
            <div class="trust-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                <span>Legal Consults on Every Deployment</span>
            </div>
            <div class="trust-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                <span>Data Sovereignty by Design</span>
            </div>
            <div class="trust-item">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
                <span>24/7 Agent Runtime Available</span>
            </div>
        </div>
    </div>
</section>

<!-- Lead Magnet -->
<section id="lead-magnet" class="section lead-magnet-section">
    <div class="container">
        <div class="lead-magnet-grid">
            <div>
                <span class="section-label">Free Resource</span>
                <h2 class="section-title">The Time Reclamation Playbook</h2>
                <p class="mb-4">A practical guide for business owners who are tired of watching talent drown in admin. Inside, you'll discover:</p>
                <ul style="color: var(--text-secondary); line-height: 2;">
                    <li>The 5 most expensive hidden time drains in every business</li>
                    <li>A simple audit framework to spot automatable tasks</li>
                    <li>How to evaluate AI tools without compromising security</li>
                    <li>A free email-drafting tool guaranteed to save you hours every week</li>
                </ul>
                <p class="mt-4" style="font-size: 0.9375rem; color: var(--text-muted);">Plus: our recommended email productivity tool with an exclusive setup guide.</p>
            </div>
            <div class="lead-magnet-form">
                <h3 class="mb-4" style="font-size: 1.25rem;">Get instant access</h3>
                <p style="font-size: 0.9375rem; margin-bottom: 1.5rem;">Enter your email and we'll send the Playbook to your inbox immediately.</p>
                <!-- Fluent Form placeholder -->
                <div class="fluent-form-placeholder" style="margin-bottom: 1rem;">
                    <p><em>[Fluent Form: Email capture — Name, Email, Company. On submit: send PDF + Mailbutler affiliate link via email.]</em></p>
                </div>
                <p style="font-size: 0.75rem; color: var(--text-muted); text-align: center;">No spam. Unsubscribe anytime. Your email is never shared.</p>
            </div>
        </div>
    </div>
</section>

<?php get_footer(); ?>
