# Chat Widget Options

## Current Implementation

The site includes a **static CSS/JS mockup chat widget** in `template-parts/chat-widget.php`. It features:
- Floating bubble in bottom-right corner
- Modal chat window with glassmorphism styling
- Pre-loaded static welcome message
- 5 mock bot responses that cycle randomly
- Fully responsive (mobile-friendly)

**To modify mock responses:** Edit the `botResponses` array in `js/main.js`.

---

## Future Implementation Paths

When you're ready to replace the mockup with a real AI chatbot, here are the recommended options:

### Option 1: Chatbase (Fastest Deployment)
**Best for:** Getting a working RAG chatbot live in under 30 minutes

**How it works:**
1. Sign up at chatbase.co
2. Upload your documents (PDFs, website content, FAQs)
3. Train the bot on your knowledge base
4. Customize appearance (colors, avatar, welcome message)
5. Copy embed script
6. Replace `template-parts/chat-widget.php` with Chatbase embed code

**Pros:**
- No-code setup
- Built-in analytics
- Human handoff to live chat
- Automatic retraining when documents update
- Embeddable widget matches our design system

**Cons:**
- Monthly SaaS cost ($19–$399/mo)
- Data processes through Chatbase servers (less sovereign)
- Limited customization of underlying model

**Pricing:** Starts at ~$19/mo for basic plan

---

### Option 2: Custom OpenAI Assistants API
**Best for:** Full data sovereignty and custom behavior

**How it works:**
1. Create an OpenAI Assistant in platform.openai.com
2. Upload documents to Assistant's vector store (RAG)
3. Build custom chat UI (or modify our existing widget)
4. Call OpenAI API from your server or edge function
5. Stream responses to the frontend

**Pros:**
- Full control over model, prompts, and behavior
- No third-party SaaS lock-in
- Data goes directly to OpenAI (one hop, not two)
- Can self-host if using open-source models later

**Cons:**
- Requires backend development (PHP or Node.js endpoint)
- Need to handle API keys securely
- Must implement rate limiting and abuse prevention
- Ongoing maintenance of prompts and retrieval logic

**Pricing:** Pay-per-use (~$0.20–$0.40 per 1K tokens) + API infrastructure costs

**Technical Approach:**
```
User message → WordPress AJAX endpoint → PHP proxy → OpenAI Assistants API
     ↓
Response streamed back → Displayed in chat widget
```

**Security considerations:**
- Never expose OpenAI API key in frontend JavaScript
- Use WordPress AJAX or REST API as proxy
- Validate and sanitize all user inputs
- Implement session-based rate limiting

---

### Option 3: SiteGPT
**Best for:** Automatic website content syncing

**How it works:**
1. Sign up at sitegpt.ai
2. Enter your website URL — it auto-scrapes and trains
3. Upload additional documents if needed
4. Customize widget and embed

**Pros:**
- Auto-syncs when website content changes
- WordPress plugin available
- Simple setup

**Cons:**
- Less mature than Chatbase
- Similar SaaS dependency
- Weaker enterprise features

---

### Option 4: Botpress (Self-Hosted)
**Best for:** Maximum control and data sovereignty

**How it works:**
1. Deploy Botpress on your own server (or use their cloud)
2. Build conversation flows visually
3. Add Knowledge Base with vector search (RAG)
4. Deploy widget to site

**Pros:**
- Open-source core
- Can self-host for full data control
- Visual flow builder
- Highly customizable

**Cons:**
- Steeper learning curve
- Self-hosting requires server management
- More setup time than SaaS options

---

### Option 5: Tidio / Crisp + AI Layer
**Best for:** Hybrid human + AI support

**How it works:**
1. Install Tidio or Crisp chat widget
2. Enable AI knowledge base feature
3. Train on your documents
4. Configure human handoff rules

**Pros:**
- Live chat + AI in one platform
- Good for businesses that want human backup
- Established customer support tools

**Cons:**
- RAG capabilities are weaker than dedicated solutions
- More expensive for AI features
- Less control over AI behavior

---

## Recommendation for Clock Lobster

**Phase 1 (Now):** Keep the static mockup. It qualifies leads, provides instant engagement, and looks professional.

**Phase 2 (Short-term):** Implement **Chatbase** for fastest time-to-value. Upload your services documentation, pricing FAQ, and process explanations. This handles 80% of common questions automatically.

**Phase 3 (Long-term):** If data sovereignty becomes a client concern, migrate to **Custom OpenAI Assistants API** or **Botpress self-hosted**. By then you'll know exactly what questions users ask most and can optimize the system.

---

## Implementation Notes

### Replacing the Mockup

To swap in a real chat widget:

1. **Backup** `template-parts/chat-widget.php`
2. Replace contents with embed code from your chosen provider
3. Remove chat-related CSS from `css/main.css` (or let provider styles override)
4. Remove chat JS from `js/main.js`
5. Test on mobile and desktop

### Keeping the Mockup Design

If you want to keep our custom glassmorphism design but add real AI:
- Use **Chatbase** or **SiteGPT** with custom CSS overrides
- Or build custom frontend that calls your backend API (Option 2 or 4)
- Our `.chat-widget`, `.chat-window`, `.chat-header` classes can be reused

### RAG Document Preparation

For any RAG-based solution, prepare these documents:
1. Services overview (from Services page)
2. Pricing and packages
3. FAQ (common questions about security, process, timeline)
4. Data Sovereignty practices
5. Case studies / success stories (when available)
6. Contact and booking information

Upload as PDF or plain text. The more comprehensive the documents, the better the chatbot responses.

---

## Resources

- Chatbase: https://chatbase.co
- OpenAI Assistants API: https://platform.openai.com/docs/assistants
- SiteGPT: https://sitegpt.ai
- Botpress: https://botpress.com
- Tidio: https://tidio.com
- Crisp: https://crisp.chat
