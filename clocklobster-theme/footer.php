<?php
/**
 * The footer for our theme.
 *
 * @package Clock Lobster
 */
?>
</div><!-- #content -->

<footer class="site-footer">
    <div class="footer-main">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="site-logo">
                        <span class="logo-icon">🦞</span>
                        <span class="logo-text">Clock Lobster</span>
                    </a>
                    <p class="footer-tagline">Liberating human potential from the drudgery of repetition.</p>
                    <p class="footer-email">hello@clocklobster.com</p>
                </div>

                <div class="footer-nav-group">
                    <h4 class="footer-heading">Company</h4>
                    <nav aria-label="Footer Navigation">
                        <?php
                        wp_nav_menu(
                            array(
                                'theme_location' => 'footer',
                                'menu_class'     => 'footer-menu',
                                'container'      => false,
                                'fallback_cb'    => false,
                            )
                        );
                        ?>
                    </nav>
                </div>

                <div class="footer-nav-group">
                    <h4 class="footer-heading">Resources</h4>
                    <ul class="footer-menu">
                        <li><a href="<?php echo esc_url( home_url( '/privacy/' ) ); ?>">Data Sovereignty</a></li>
                        <li><a href="<?php echo esc_url( home_url( '/services/' ) ); ?>">Services</a></li>
                        <li><a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>">Contact</a></li>
                    </ul>
                </div>

                <div class="footer-form">
                    <h4 class="footer-heading">Ready to reclaim your time?</h4>
                    <p class="footer-form-text">Send us a message and we'll get back to you within one business day.</p>
                    <!-- Fluent Form placeholder: Form ID to be inserted here -->
                    <div class="fluent-form-placeholder">
                        <p><em>[Fluent Form ID="1" will go here — contact form with Name, Email, Company, Message fields. On submission, redirect to /book-consultation/]</em></p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="footer-bottom">
        <div class="container">
            <p class="copyright">&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?> Clock Lobster. All rights reserved.</p>
            <p class="footer-legal">
                <a href="<?php echo esc_url( home_url( '/privacy/' ) ); ?>">Data Sovereignty &amp; Security</a>
            </p>
        </div>
    </div>
</footer>

<?php get_template_part( 'template-parts/chat-widget' ); ?>

<?php wp_footer(); ?>
</body>
</html>
