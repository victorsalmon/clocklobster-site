<?php
/**
 * Clock Lobster functions and definitions.
 *
 * @package Clock Lobster
 */

if ( ! defined( 'CLOCKLOBSTER_VERSION' ) ) {
    define( 'CLOCKLOBSTER_VERSION', '1.0.0' );
}

/**
 * Theme setup.
 */
function clocklobster_setup() {
    add_theme_support( 'title-tag' );
    add_theme_support( 'post-thumbnails' );
    add_theme_support( 'html5', array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption' ) );
    add_theme_support( 'responsive-embeds' );
    add_theme_support( 'customize-selective-refresh-widgets' );

    register_nav_menus(
        array(
            'primary' => __( 'Primary Menu', 'clocklobster' ),
            'footer'  => __( 'Footer Menu', 'clocklobster' ),
        )
    );
}
add_action( 'after_setup_theme', 'clocklobster_setup' );

/**
 * Enqueue scripts and styles.
 */
function clocklobster_scripts() {
    wp_enqueue_style(
        'clocklobster-google-fonts',
        'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap',
        array(),
        null
    );

    wp_enqueue_style(
        'clocklobster-style',
        get_stylesheet_directory_uri() . '/css/main.css',
        array(),
        CLOCKLOBSTER_VERSION
    );

    wp_enqueue_script(
        'clocklobster-main',
        get_template_directory_uri() . '/js/main.js',
        array(),
        CLOCKLOBSTER_VERSION,
        true
    );
}
add_action( 'wp_enqueue_scripts', 'clocklobster_scripts' );

/**
 * Disable WordPress default gallery styles to keep our theme clean.
 */
add_filter( 'use_default_gallery_style', '__return_false' );
