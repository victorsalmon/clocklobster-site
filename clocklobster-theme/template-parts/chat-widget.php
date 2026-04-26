<?php
/**
 * Chat Widget Template Part
 *
 * @package Clock Lobster
 */
?>
<div class="chat-widget" role="complementary" aria-label="AI Support Chat">
    <button class="chat-bubble" aria-label="Open chat" aria-expanded="false">
        💬
    </button>

    <div class="chat-window">
        <div class="chat-header">
            <div class="chat-header-icon">🦞</div>
            <div class="chat-header-text">
                <h4>Clock Lobster AI</h4>
                <p>Ask us anything about automation</p>
            </div>
        </div>

        <div class="chat-messages">
            <div class="chat-message bot">
                Hi there! I'm the Clock Lobster assistant. I can tell you about our digital employees, automation services, or data sovereignty practices. What would you like to know?
            </div>
        </div>

        <div class="chat-input">
            <input type="text" placeholder="Type your question..." aria-label="Chat message">
            <button aria-label="Send message">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="22" y1="2" x2="11" y2="13"></line>
                    <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                </svg>
            </button>
        </div>
    </div>
</div>
