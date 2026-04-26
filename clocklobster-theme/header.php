<?php
/**
 * The header for our theme.
 *
 * @package Clock Lobster
 */
?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Clock Lobster liberates human potential from repetitive drudgery with bespoke digital employees and sovereign AI infrastructure.">
    <?php wp_head(); ?>
</head>

<body <?php body_class( 'bg-charcoal text-white antialiased' ); ?>>
<?php wp_body_open(); ?>

<header class="site-header sticky top-0 z-50">
    <div class="header-glass">
        <div class="container nav-container">
            <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="site-logo" aria-label="Clock Lobster Home">
                <span class="logo-icon">🦞</span>
                <span class="logo-text">Clock Lobster</span>
            </a>

            <nav class="main-nav" aria-label="Primary Navigation">
                <?php
                wp_nav_menu(
                    array(
                        'theme_location' => 'primary',
                        'menu_class'     => 'nav-menu',
                        'container'      => false,
                        'fallback_cb'    => false,
                    )
                );
                ?>
            </nav>

            <div class="header-cta">
                <a href="<?php echo esc_url( home_url( '/book-consultation/' ) ); ?>" class="btn btn-primary">
                    Book a Consultation
                </a>
            </div>

            <button class="mobile-menu-toggle" aria-label="Toggle Menu" aria-expanded="false">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </div>
</header>

<div id="content" class="site-content">
