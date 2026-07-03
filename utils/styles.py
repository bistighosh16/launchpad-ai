"""
LaunchPad AI - Design System
Warm Midnight Theme (Framer × Claude Fusion)
Made with 💜 by Vivi
"""

import streamlit as st


def load_fonts():
    """Load Google Fonts: Fraunces (serif) + Inter (sans) + JetBrains Mono"""
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)


def apply_design_system():
    """Apply LaunchPad AI's Warm Midnight design system"""
    load_fonts()
    
    st.markdown("""
    <style>
    
    /* ============================================
       DESIGN TOKENS - Warm Midnight Palette
    ============================================ */
    :root {
        --canvas: #0F0B1A;
        --surface-1: #1A1526;
        --surface-2: #241D33;
        --cream: #F5F0E8;
        --cream-card: #EFE9DE;
        --hairline: #2A2438;
        --hairline-cream: #E6DFD8;
        --ink: #FAF7F2;
        --ink-muted: #9E96B0;
        --ink-cream: #141413;
        --ink-cream-muted: #6C6A64;
        --accent-purple: #B57BFF;
        --accent-purple-active: #9B5FE8;
        --gradient-violet: #8B5CF6;
        --gradient-pink: #EC4899;
        --gradient-lavender: #C084FC;
        --gradient-coral: #FB7185;
    }
    
    /* ============================================
       BASE - Hide Streamlit defaults (but keep toggle!)
    ============================================ */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Keep header visible but make it transparent for the sidebar toggle */
    header[data-testid="stHeader"] {
        background: transparent !important;
        height: 3rem;
    }
    
    /* Style the sidebar toggle button */
    button[data-testid="stBaseButton-headerNoPadding"] {
        color: var(--ink) !important;
    }
    
    /* Body base */
    .stApp {
        background: var(--canvas);
        color: var(--ink);
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    /* Main container width */
    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* ============================================
       TYPOGRAPHY - Editorial Bold
    ============================================ */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Fraunces', Georgia, serif !important;
        font-weight: 400 !important;
        color: var(--ink) !important;
        letter-spacing: -0.02em;
        line-height: 1.1 !important;
    }
    
    h1 {
        font-size: 4.5rem !important;
        letter-spacing: -0.04em !important;
        margin-bottom: 1.5rem !important;
    }
    
    h2 {
        font-size: 3rem !important;
        letter-spacing: -0.03em !important;
        margin-bottom: 1rem !important;
    }
    
    h3 {
        font-size: 2rem !important;
        letter-spacing: -0.02em !important;
    }
    
    p, div, span, li {
        font-family: 'Inter', sans-serif;
        color: var(--ink);
        line-height: 1.6;
    }
    
    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
        background: var(--surface-1) !important;
        color: var(--accent-purple) !important;
        border-radius: 6px;
        padding: 2px 8px;
    }
    
    /* ============================================
       BUTTONS - Purple Primary
    ============================================ */
       .stButton > button {
        background: var(--accent-purple);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 14px 24px;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        font-size: 14px;
        letter-spacing: -0.01em;
        transition: all 0.2s ease;
        height: 48px;
        white-space: nowrap;
        min-width: 180px;
    }
    
    .stButton > button:hover {
        background: var(--accent-purple-active);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(181, 123, 255, 0.3);
        color: white;
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    .stButton > button[kind="secondary"] {
        background: var(--surface-1);
        color: var(--ink);
        border: 1px solid var(--hairline);
    }
    
    .stButton > button[kind="secondary"]:hover {
        background: var(--surface-2);
        border-color: var(--accent-purple);
    }
    
    /* ============================================
       INPUTS - Warm Dark
    ============================================ */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: var(--surface-1) !important;
        color: var(--ink) !important;
        border: 1px solid var(--hairline) !important;
        border-radius: 8px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 15px !important;
        padding: 12px 16px !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--accent-purple) !important;
        box-shadow: 0 0 0 3px rgba(181, 123, 255, 0.15) !important;
    }
    
    .stTextInput label,
    .stTextArea label,
    .stSelectbox label {
        color: var(--ink-muted) !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* ============================================
       SIDEBAR
    ============================================ */
    section[data-testid="stSidebar"] {
        background: var(--surface-1);
        border-right: 1px solid var(--hairline);
    }
    
    section[data-testid="stSidebar"] .stMarkdown {
        color: var(--ink);
    }
    
    /* ============================================
       CUSTOM COMPONENTS
    ============================================ */
    
    /* Hero container */
    .hero-container {
        padding: 64px 0 48px 0;
        text-align: center;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
     .hero-eyebrow {
        display: inline-block;
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: var(--accent-purple);
        background: rgba(181, 123, 255, 0.1);
        padding: 8px 16px;
        border-radius: 9999px;
        margin-bottom: 24px;
        border: 1px solid rgba(181, 123, 255, 0.2);
    }
    
    .hero-title {
        font-family: 'Fraunces', serif !important;
        font-size: 5rem !important;
        font-weight: 400 !important;
        line-height: 1.05 !important;
        letter-spacing: -0.04em !important;
        color: var(--ink) !important;
        margin-bottom: 24px !important;
        margin-top: 0 !important;
        text-align: center !important;
        width: 100%;
    }
    
        .hero-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 20px;
        line-height: 1.5;
        color: var(--ink-muted);
        max-width: 640px;
        margin-left: auto !important;
        margin-right: auto !important;
        margin-bottom: 40px !important;
        text-align: center !important;
        display: block;
    }
    
    /* Hide the auto-generated anchor link icons on headers */
    .stMarkdown h1 a,
    .stMarkdown h2 a,
    .stMarkdown h3 a,
    .stMarkdown h4 a,
    h1 a, h2 a, h3 a, h4 a,
    a.anchor-link,
    [data-testid="stHeaderActionElements"] {
        display: none !important;
    }            
    /* Feature card - dark */
    .feature-card {
        background: var(--surface-1);
        border: 1px solid var(--hairline);
        border-radius: 16px;
        padding: 32px;
        transition: all 0.3s ease;
        height: 100%;
        min-height: 240px;
    }
    
    .feature-card:hover {
        border-color: var(--accent-purple);
        transform: translateY(-4px);
    }
    
    .feature-icon {
        font-size: 32px;
        margin-bottom: 16px;
        display: block;
    }
    
    .feature-title {
        font-family: 'Fraunces', serif;
        font-size: 24px;
        font-weight: 500;
        color: var(--ink);
        margin-bottom: 12px;
        letter-spacing: -0.02em;
    }
    
    .feature-description {
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        color: var(--ink-muted);
        line-height: 1.6;
    }
    
    /* Cream section (Claude-inspired rhythm break) */
    .cream-section {
        background: var(--cream);
        border-radius: 24px;
        padding: 64px 48px;
        margin: 48px 0;
        text-align: center;
    }
    
    .cream-section .cream-badge {
        display: inline-block;
        background: rgba(20, 20, 19, 0.05);
        color: #6C6A64;
        border: 1px solid #E6DFD8;
        padding: 8px 16px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 24px;
    }
    
    .cream-section .cream-title {
        font-family: 'Fraunces', serif;
        font-size: 3rem;
        font-weight: 400;
        color: #141413;
        letter-spacing: -0.03em;
        line-height: 1.1;
        margin-bottom: 16px;
    }
    
    .cream-section .cream-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        color: #6C6A64;
        line-height: 1.5;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* Gradient spotlight card (Framer-inspired atmosphere) */
    .spotlight-card {
        background: linear-gradient(135deg, var(--gradient-violet) 0%, var(--gradient-pink) 100%);
        border-radius: 32px;
        padding: 64px 48px;
        color: white;
        margin: 48px 0;
        text-align: center;
    }
    
    .spotlight-card-lavender {
        background: linear-gradient(135deg, var(--gradient-lavender) 0%, var(--accent-purple) 100%);
    }
    
    .spotlight-card-coral {
        background: linear-gradient(135deg, var(--gradient-coral) 0%, var(--gradient-pink) 100%);
    }
    
    .spotlight-card .spotlight-title {
        font-family: 'Fraunces', serif;
        font-size: 3.5rem;
        font-weight: 400;
        color: white;
        letter-spacing: -0.03em;
        line-height: 1.1;
        margin-bottom: 16px;
    }
    
    .spotlight-card .spotlight-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 20px;
        color: rgba(255, 255, 255, 0.9);
        line-height: 1.5;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* Section divider */
    .section-divider {
        height: 1px;
        background: var(--hairline);
        margin: 96px 0;
        border: none;
    }
    
    /* Footer signature */
    .made-with-purple {
        text-align: center;
        padding: 48px 0 32px 0;
        color: var(--ink-muted);
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        border-top: 1px solid var(--hairline);
        margin-top: 96px;
    }
    
    .made-with-purple .heart {
        color: var(--accent-purple);
        font-size: 16px;
    }
    
    /* Badge/pill */
    .badge-pill {
        display: inline-block;
        padding: 6px 14px;
        background: var(--surface-1);
        border: 1px solid var(--hairline);
        border-radius: 9999px;
        font-size: 12px;
        font-weight: 600;
        color: var(--ink-muted);
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    .badge-purple {
        background: rgba(181, 123, 255, 0.1);
        border-color: rgba(181, 123, 255, 0.3);
        color: var(--accent-purple);
    }
    
    /* Step number card */
    .step-card {
        text-align: center;
        padding: 24px;
    }
    
    .step-number {
        font-family: 'Fraunces', serif;
        font-size: 64px;
        color: var(--accent-purple);
        font-weight: 400;
        line-height: 1;
        margin-bottom: 16px;
    }
    
    .step-title {
        font-family: 'Fraunces', serif;
        font-size: 24px;
        font-weight: 500;
        color: var(--ink);
        margin: 16px 0 12px 0;
        letter-spacing: -0.02em;
    }
    
    .step-description {
        color: var(--ink-muted);
        font-size: 15px;
        line-height: 1.6;
    }
    
    /* Stat card */
    .stat-card {
        text-align: center;
        padding: 32px 24px;
        border: 1px solid var(--hairline);
        border-radius: 16px;
        background: var(--surface-1);
    }
    
    .stat-number {
        font-family: 'Fraunces', serif;
        font-size: 56px;
        color: var(--accent-purple);
        font-weight: 400;
        line-height: 1;
        margin-bottom: 8px;
    }
    
    .stat-label {
        color: var(--ink-muted);
        text-transform: uppercase;
        font-size: 12px;
        letter-spacing: 2px;
        font-weight: 600;
    }
    
    /* Alerts */
    .stAlert {
        background: var(--surface-1) !important;
        border: 1px solid var(--hairline) !important;
        border-radius: 12px !important;
        color: var(--ink) !important;
    }
    
        /* Divider */
    hr {
        border-color: var(--hairline) !important;
        margin: 48px 0 !important;
    }
    
    /* ============================================
       ANIMATIONS - Smooth entry
    ============================================ */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    @keyframes pulse-purple {
        0%, 100% { box-shadow: 0 0 0 0 rgba(181, 123, 255, 0.4); }
        50% { box-shadow: 0 0 0 12px rgba(181, 123, 255, 0); }
    }
    
    .fade-in {
        animation: fadeInUp 0.6s ease-out forwards;
    }
    
    .fade-in-delay-1 {
        animation: fadeInUp 0.6s ease-out 0.1s forwards;
        opacity: 0;
    }
    
    .fade-in-delay-2 {
        animation: fadeInUp 0.6s ease-out 0.2s forwards;
        opacity: 0;
    }
    
    .fade-in-delay-3 {
        animation: fadeInUp 0.6s ease-out 0.3s forwards;
        opacity: 0;
    }
    
    /* Progress bar custom style */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--gradient-violet), var(--gradient-pink)) !important;
    }
    
    /* Character counter */
    .char-counter {
        text-align: right;
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        color: var(--ink-muted);
        margin-top: 4px;
    }
    
    .char-counter.warning {
        color: var(--gradient-coral);
    }
    
    /* Section fade-in helper */
    .blueprint-section {
        animation: fadeInUp 0.5s ease-out forwards;
    }
    
    /* Copy button hint */
    .copy-hint {
        display: inline-block;
        font-size: 11px;
        color: var(--ink-muted);
        margin-left: 8px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    </style>
    """, unsafe_allow_html=True)


def render_footer():
    """Render the signature 'Made with 💜' footer"""
    st.markdown("""
    <div class="made-with-purple">
        Made with <span class="heart">💜</span> by <strong>Vivi</strong> · LaunchPad AI
    </div>
    """, unsafe_allow_html=True)


def render_hero(eyebrow: str, title: str, subtitle: str):
    """Render a hero section with our signature style"""
    st.markdown(f"""
    <div class="hero-container">
        <div class="hero-eyebrow">{eyebrow}</div>
        <div class="hero-title">{title}</div>
        <div class="hero-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)


def render_feature_card(icon: str, title: str, description: str):
    """Render a dark feature card"""
    st.markdown(f"""
    <div class="feature-card">
        <span class="feature-icon">{icon}</span>
        <h3 class="feature-title">{title}</h3>
        <p class="feature-description">{description}</p>
    </div>
    """, unsafe_allow_html=True)


def render_spotlight_card(title: str, subtitle: str, variant: str = "default"):
    """Render a gradient spotlight card
    Variants: 'default' (violet-pink), 'lavender', 'coral'
    """
    variant_class = f"spotlight-card-{variant}" if variant != "default" else ""
    st.markdown(f"""
    <div class="spotlight-card {variant_class}">
        <div class="spotlight-title">{title}</div>
        <p class="spotlight-subtitle">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def render_cream_section(badge: str, title: str, subtitle: str):
    """Render a cream editorial section"""
    st.markdown(f"""
    <div class="cream-section">
        <div class="cream-badge">{badge}</div>
        <div class="cream-title">{title}</div>
        <p class="cream-subtitle">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def render_step_card(number: str, title: str, description: str):
    """Render a numbered step card"""
    st.markdown(f"""
    <div class="step-card">
        <div class="step-number">{number}</div>
        <div class="step-title">{title}</div>
        <p class="step-description">{description}</p>
    </div>
    """, unsafe_allow_html=True)


def render_stat_card(number: str, label: str):
    """Render a stat/metric card"""
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{number}</div>
        <div class="stat-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)

def render_spotlight_hero(section_label: str, headline: str, subheadline: str, 
                          cta_primary: str, cta_secondary: str, variant: str = "default"):
    """Render the hero preview as a spotlight card with rotating gradient variants"""
    variant_class = f"spotlight-card-{variant}" if variant != "default" else ""
    st.markdown(f"""
    <div class="spotlight-card {variant_class} blueprint-section">
        <div style="text-align: left;">
            <span style="font-size: 12px; letter-spacing: 2px; text-transform: uppercase; font-weight: 600; color: rgba(255,255,255,0.75);">
                {section_label}
            </span>
            <div style="font-family: 'Fraunces', serif; color: white; font-size: 3rem; font-weight: 400; margin-top: 16px; margin-bottom: 16px; letter-spacing: -0.03em; line-height: 1.1;">
                {headline}
            </div>
            <p style="color: rgba(255,255,255,0.9); font-size: 20px; margin-bottom: 32px; line-height: 1.5;">
                {subheadline}
            </p>
            <div style="display: flex; gap: 12px; flex-wrap: wrap;">
                <span style="background: white; color: #241D33; padding: 12px 24px; border-radius: 8px; font-weight: 500; font-size: 14px;">
                    {cta_primary}
                </span>
                <span style="background: rgba(255,255,255,0.15); color: white; padding: 12px 24px; border-radius: 8px; font-weight: 500; font-size: 14px; border: 1px solid rgba(255,255,255,0.3);">
                    {cta_secondary}
                </span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_section_header(badge: str, title: str, subtitle: str = ""):
    """Render a consistent section header"""
    subtitle_html = f'<p style="color: var(--ink-muted); font-size: 18px; margin-top: 16px;">{subtitle}</p>' if subtitle else ''
    st.markdown(f"""
    <div style="text-align: center; padding: 32px 0;" class="blueprint-section">
        <span class="badge-pill badge-purple">{badge}</span>
        <div style="font-family: 'Fraunces', serif; font-size: 2.5rem; color: var(--ink); margin-top: 20px; letter-spacing: -0.03em; line-height: 1.1;">
            {title}
        </div>
        {subtitle_html}
    </div>
    """, unsafe_allow_html=True)

def render_sidebar():
    """Render a beautiful, informative sidebar"""
    with st.sidebar:
        # Brand
        st.markdown("""
        <div style="text-align: center; padding: 24px 0 16px 0;">
            <div style="font-family: 'Fraunces', serif; font-size: 32px; font-weight: 500; color: var(--ink); letter-spacing: -0.02em; line-height: 1;">
                🚀 LaunchPad
            </div>
            <div style="font-family: 'Fraunces', serif; font-size: 20px; font-weight: 400; color: var(--accent-purple); letter-spacing: -0.02em; margin-top: 4px;">
                AI
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; padding: 0 16px 24px 16px;">
            <p style="color: var(--ink-muted); font-size: 13px; line-height: 1.5; margin: 0;">
                One sentence to a full landing page blueprint.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<hr style='margin: 8px 0 16px 0;'>", unsafe_allow_html=True)
        
        # Section label
        st.markdown("""
        <div style="padding: 8px 16px;">
            <p style="color: var(--ink-muted); font-size: 11px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; margin: 0;">
                ✨ What You Get
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Features list
        features_list = [
            ("✍️", "Hero Section", "Copy that converts"),
            ("🎯", "4 Key Features", "Benefit-driven"),
            ("🚀", "How It Works", "3-step process"),
            ("💬", "Social Proof", "Testimonials + trust"),
            ("❓", "Smart FAQs", "Real objections"),
            ("🎨", "Design System", "Colors + typography"),
        ]
        
        for icon, title, desc in features_list:
            st.markdown(f"""
            <div style="padding: 10px 16px; margin: 2px 0;">
                <div style="display: flex; align-items: flex-start; gap: 10px;">
                    <div style="font-size: 16px; line-height: 1.2;">{icon}</div>
                    <div style="flex: 1;">
                        <div style="color: var(--ink); font-size: 13px; font-weight: 500; line-height: 1.3;">{title}</div>
                        <div style="color: var(--ink-muted); font-size: 11px; line-height: 1.4; margin-top: 2px;">{desc}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<hr style='margin: 16px 0;'>", unsafe_allow_html=True)
        
        # Pro tips
        st.markdown("""
        <div style="padding: 8px 16px;">
            <p style="color: var(--ink-muted); font-size: 11px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; margin: 0 0 12px 0;">
                💡 Pro Tips
            </p>
            <div style="padding: 12px; background: var(--surface-2); border-radius: 8px; border-left: 3px solid var(--accent-purple); margin-bottom: 8px;">
                <p style="color: var(--ink); font-size: 12px; line-height: 1.5; margin: 0;">
                    Be <strong>specific</strong> about who your product serves.
                </p>
            </div>
            <div style="padding: 12px; background: var(--surface-2); border-radius: 8px; border-left: 3px solid var(--accent-purple); margin-bottom: 8px;">
                <p style="color: var(--ink); font-size: 12px; line-height: 1.5; margin: 0;">
                    Include the <strong>main benefit</strong>, not just features.
                </p>
            </div>
            <div style="padding: 12px; background: var(--surface-2); border-radius: 8px; border-left: 3px solid var(--accent-purple);">
                <p style="color: var(--ink); font-size: 12px; line-height: 1.5; margin: 0;">
                    Try <strong>3-5 variations</strong> to find the best one.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<hr style='margin: 16px 0;'>", unsafe_allow_html=True)
        
        # Tech badge
        st.markdown("""
        <div style="padding: 8px 16px;">
            <p style="color: var(--ink-muted); font-size: 11px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; margin: 0 0 12px 0;">
                ⚡ Powered By
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                <span style="background: var(--surface-2); color: var(--ink-muted); padding: 4px 10px; border-radius: 6px; font-size: 11px; font-family: 'JetBrains Mono', monospace;">Groq</span>
                <span style="background: var(--surface-2); color: var(--ink-muted); padding: 4px 10px; border-radius: 6px; font-size: 11px; font-family: 'JetBrains Mono', monospace;">Llama 3.3</span>
                <span style="background: var(--surface-2); color: var(--ink-muted); padding: 4px 10px; border-radius: 6px; font-size: 11px; font-family: 'JetBrains Mono', monospace;">Streamlit</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Made with love
        st.markdown("""
        <div style="text-align: center; padding: 32px 16px 16px 16px; margin-top: 16px;">
            <p style="color: var(--ink-muted); font-size: 12px; margin: 0;">
                Made with <span style="color: var(--accent-purple); font-size: 14px;">💜</span> by
            </p>
            <p style="color: var(--ink); font-size: 14px; font-weight: 600; margin: 4px 0 0 0; font-family: 'Fraunces', serif;">
                Vivi
            </p>
        </div>
        """, unsafe_allow_html=True)