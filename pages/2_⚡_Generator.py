"""
LaunchPad AI - Generator Page
The actual AI tool that turns one sentence into a full landing page
Made with 💜 by Vivi
"""

import streamlit as st
import json
import random
from utils.styles import (
    apply_design_system, 
    render_footer, 
    render_spotlight_hero,
    render_section_header,
    render_sidebar,
)
from utils.ai_engine import LaunchPadAI

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="Generator · LaunchPad AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_design_system()
render_sidebar()


# ============================================
# INITIALIZE SESSION STATE
# ============================================
if "blueprint" not in st.session_state:
    st.session_state.blueprint = None
if "product_input" not in st.session_state:
    st.session_state.product_input = ""
if "gradient_variant" not in st.session_state:
    st.session_state.gradient_variant = "default"


# ============================================
# HERO
# ============================================
st.markdown("""
<div class="hero-container">
    <div class="hero-eyebrow">⚡ GENERATOR</div>
    <div class="hero-title">Describe your idea.</div>
    <div class="hero-subtitle">One sentence about your product. We'll generate the entire landing page blueprint — hero, features, FAQs, design system, and more.</div>
</div>
""", unsafe_allow_html=True)


# ============================================
# INPUT SECTION
# ============================================
st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    # Example prompts FIRST
    st.markdown("""
    <div style="margin-bottom: 12px;">
        <p style="font-size: 13px; color: var(--ink-muted); text-transform: uppercase; letter-spacing: 2px; font-weight: 600; margin-bottom: 12px;">
            💡 Try an example
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    ex_col1, ex_col2, ex_col3 = st.columns(3)
    with ex_col1:
        if st.button("🎨 Design tool", use_container_width=True, key="ex1"):
            st.session_state.product_input = "A collaborative design tool for remote startup teams to prototype and ship faster"
            st.rerun()
    with ex_col2:
        if st.button("📚 Learning app", use_container_width=True, key="ex2"):
            st.session_state.product_input = "An AI-powered learning platform that adapts to how each student thinks"
            st.rerun()
    with ex_col3:
        if st.button("💰 Fintech tool", use_container_width=True, key="ex3"):
            st.session_state.product_input = "A budgeting app for Gen-Z that makes saving feel like a game"
            st.rerun()
    
    st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)
    
    # Text area
    product_description = st.text_area(
        label="YOUR PRODUCT IDEA",
        placeholder="E.g., An AI tool that helps developers write better documentation from their code comments...",
        height=120,
        max_chars=300,
        key="product_input"
    )
    
    # Character counter
    char_count = len(product_description) if product_description else 0
    counter_class = "warning" if char_count > 250 else ""
    st.markdown(f"""
    <div class="char-counter {counter_class}">
        {char_count} / 300 characters
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)
    
    # Generate button
    gen_col1, gen_col2, gen_col3 = st.columns([1, 2, 1])
    with gen_col2:
        generate_clicked = st.button(
            "✨ Generate Landing Page",
            type="primary",
            use_container_width=True,
            disabled=not product_description or len(product_description.strip()) < 10,
            key="generate_btn"
        )


# ============================================
# GENERATION LOGIC
# ============================================
if generate_clicked and product_description:
    st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)
    
    # Randomize gradient variant for this generation
    st.session_state.gradient_variant = random.choice(["default", "lavender", "coral"])
    
    # Progress display
    progress_container = st.container()
    with progress_container:
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            progress_bar = st.progress(0)
            status_text = st.empty()
    
    def update_progress(current, total, message):
        progress = (current / total) if total > 0 else 0
        progress_bar.progress(progress)
        status_text.markdown(f"""
        <div style="text-align: center; padding: 16px; color: var(--accent-purple); font-family: 'Inter', sans-serif; font-weight: 500; font-size: 16px;">
            {message}
        </div>
        """, unsafe_allow_html=True)
    
    try:
        ai = LaunchPadAI()
        blueprint = ai.generate_full_landing_page(product_description, progress_callback=update_progress)
        st.session_state.blueprint = blueprint
        st.session_state.product_description = product_description
        st.balloons()  # 🎉 Celebration!
        st.rerun()
    except Exception as e:
        st.error(f"Oops! Something went wrong: {str(e)}")


# ============================================
# DISPLAY GENERATED BLUEPRINT
# ============================================
if st.session_state.blueprint:
    blueprint = st.session_state.blueprint
    gradient = st.session_state.gradient_variant
    
    st.markdown("<div style='height: 48px;'></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Success header
    st.markdown("""
    <div style="text-align: center; padding: 48px 0 32px 0;" class="fade-in">
        <span class="badge-pill badge-purple">✨ YOUR BLUEPRINT</span>
        <div style="font-family: 'Fraunces', serif; font-size: 3rem; font-weight: 400; color: var(--ink); letter-spacing: -0.03em; margin-top: 24px; line-height: 1.1;">
            Here's your landing page.
        </div>
        <p style="color: var(--ink-muted); font-size: 18px; margin-top: 16px;">
            Every section, tailored to your product. Copy, structure, and design.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================
    # SECTION 1: HERO
    # ============================================
    if "hero" in blueprint and "error" not in blueprint["hero"]:
        hero = blueprint["hero"]
        render_spotlight_hero(
            section_label="HERO SECTION",
            headline=hero.get('headline', ''),
            subheadline=hero.get('subheadline', ''),
            cta_primary=hero.get('cta_primary', 'Get Started'),
            cta_secondary=hero.get('cta_secondary', 'Learn More'),
            variant=gradient
        )
    
    # ============================================
    # SECTION 2: FEATURES
    # ============================================
    if "features" in blueprint and "error" not in blueprint["features"]:
        st.markdown("<div style='height: 48px;'></div>", unsafe_allow_html=True)
        render_section_header("FEATURES", "Key Features")
        
        features = blueprint["features"].get("features", [])
        if features:
            cols = st.columns(2)
            for i, feature in enumerate(features):
                with cols[i % 2]:
                    st.markdown(f"""
                    <div class="feature-card blueprint-section" style="margin-bottom: 24px;">
                        <span class="feature-icon">{feature.get('icon', '✨')}</span>
                        <h3 class="feature-title">{feature.get('title', '')}</h3>
                        <p class="feature-description">{feature.get('description', '')}</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    # ============================================
    # SECTION 3: HOW IT WORKS
    # ============================================
    if "how_it_works" in blueprint and "error" not in blueprint["how_it_works"]:
        st.markdown("<div style='height: 48px;'></div>", unsafe_allow_html=True)
        st.markdown("""
        <div class="cream-section blueprint-section">
            <div class="cream-badge">HOW IT WORKS</div>
            <div class="cream-title">Simple process</div>
            <p class="cream-subtitle">Three steps to get started</p>
        </div>
        """, unsafe_allow_html=True)
        
        steps = blueprint["how_it_works"].get("steps", [])
        if steps:
            cols = st.columns(len(steps))
            for i, step in enumerate(steps):
                with cols[i]:
                    st.markdown(f"""
                    <div class="step-card blueprint-section">
                        <div class="step-number">{step.get('number', f'0{i+1}')}</div>
                        <div class="step-title">{step.get('title', '')}</div>
                        <p class="step-description">{step.get('description', '')}</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    # ============================================
    # SECTION 4: SOCIAL PROOF
    # ============================================
    if "social_proof" in blueprint and "error" not in blueprint["social_proof"]:
        st.markdown("<div style='height: 48px;'></div>", unsafe_allow_html=True)
        render_section_header("SOCIAL PROOF", "Loved by users")
        
        testimonials = blueprint["social_proof"].get("testimonials", [])
        if testimonials:
            cols = st.columns(len(testimonials))
            for i, testimonial in enumerate(testimonials):
                with cols[i]:
                    st.markdown(f"""
                    <div class="feature-card blueprint-section">
                        <div style="font-size: 40px; color: var(--accent-purple); font-family: 'Fraunces', serif; line-height: 1;">"</div>
                        <p style="font-family: 'Fraunces', serif; font-size: 18px; color: var(--ink); line-height: 1.5; margin: 8px 0 24px 0; font-style: italic;">
                            {testimonial.get('quote', '')}
                        </p>
                        <div style="border-top: 1px solid var(--hairline); padding-top: 16px;">
                            <div style="color: var(--ink); font-weight: 600; font-size: 14px;">{testimonial.get('author', '')}</div>
                            <div style="color: var(--ink-muted); font-size: 13px; margin-top: 4px;">{testimonial.get('role', '')}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Trust signals
        trust_signals = blueprint["social_proof"].get("trust_signals", [])
        if trust_signals:
            st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)
            trust_cols = st.columns(len(trust_signals))
            for i, signal in enumerate(trust_signals):
                with trust_cols[i]:
                    st.markdown(f"""
                    <div style="text-align: center; padding: 20px; border: 1px solid var(--hairline); border-radius: 12px; background: var(--surface-1);" class="blueprint-section">
                        <div style="font-family: 'Fraunces', serif; font-size: 24px; color: var(--accent-purple); font-weight: 500;">
                            {signal}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
    
    # ============================================
    # SECTION 5: FAQ
    # ============================================
    if "faq" in blueprint and "error" not in blueprint["faq"]:
        st.markdown("<div style='height: 48px;'></div>", unsafe_allow_html=True)
        render_section_header("FAQ", "Common questions")
        
        faqs = blueprint["faq"].get("faqs", [])
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            for faq in faqs:
                with st.expander(f"**{faq.get('question', '')}**"):
                    st.markdown(f"<p style='color: var(--ink-muted); line-height: 1.6;'>{faq.get('answer', '')}</p>", unsafe_allow_html=True)
    
    # ============================================
    # SECTION 6: DESIGN SYSTEM
    # ============================================
    if "design_system" in blueprint and "error" not in blueprint["design_system"]:
        design = blueprint["design_system"]
        st.markdown("<div style='height: 48px;'></div>", unsafe_allow_html=True)
        render_section_header(
            "DESIGN SYSTEM", 
            "Recommended visual identity",
            f"Vibe: <strong style='color: var(--accent-purple);'>{design.get('vibe', 'Modern & clean')}</strong>"
        )
        
        # Color palette
        palette = design.get("color_palette", {})
        if palette:
            st.markdown("""
            <p style="color: var(--ink-muted); text-transform: uppercase; letter-spacing: 2px; font-size: 12px; font-weight: 600; margin-bottom: 16px;">
                🎨 Color Palette
            </p>
            """, unsafe_allow_html=True)
            
            color_cols = st.columns(4)
            color_items = [
                ("Primary", palette.get("primary", "#000")),
                ("Accent", palette.get("accent", "#000")),
                ("Background", palette.get("background", "#000")),
                ("Text", palette.get("text", "#000")),
            ]
            
            for i, (name, hex_code) in enumerate(color_items):
                with color_cols[i]:
                    st.markdown(f"""
                    <div style="text-align: center; padding: 16px; border: 1px solid var(--hairline); border-radius: 12px;" class="blueprint-section">
                        <div style="width: 100%; height: 80px; background: {hex_code}; border-radius: 8px; margin-bottom: 12px; border: 1px solid var(--hairline);"></div>
                        <div style="color: var(--ink); font-weight: 600; font-size: 13px;">{name}</div>
                        <div style="color: var(--ink-muted); font-family: 'JetBrains Mono', monospace; font-size: 12px; margin-top: 4px;">{hex_code}</div>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Typography
        typography = design.get("typography", {})
        if typography:
            st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)
            st.markdown("""
            <p style="color: var(--ink-muted); text-transform: uppercase; letter-spacing: 2px; font-size: 12px; font-weight: 600; margin-bottom: 16px;">
                🔤 Typography
            </p>
            """, unsafe_allow_html=True)
            
            typo_col1, typo_col2 = st.columns(2)
            with typo_col1:
                st.markdown(f"""
                <div class="feature-card blueprint-section">
                    <div style="color: var(--ink-muted); font-size: 12px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px;">HEADLINE FONT</div>
                    <div style="font-family: 'Fraunces', serif; font-size: 32px; color: var(--accent-purple);">{typography.get('heading_font', 'Inter')}</div>
                </div>
                """, unsafe_allow_html=True)
            with typo_col2:
                st.markdown(f"""
                <div class="feature-card blueprint-section">
                    <div style="color: var(--ink-muted); font-size: 12px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px;">BODY FONT</div>
                    <div style="font-family: 'Fraunces', serif; font-size: 32px; color: var(--accent-purple);">{typography.get('body_font', 'Inter')}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="margin-top: 16px; padding: 20px; background: var(--surface-1); border-radius: 12px; border-left: 3px solid var(--accent-purple);">
                <p style="color: var(--ink-muted); margin: 0; font-style: italic;">
                    💡 {typography.get('pairing_reason', '')}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Design principles
        principles = design.get("design_principles", [])
        if principles:
            st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)
            st.markdown("""
            <p style="color: var(--ink-muted); text-transform: uppercase; letter-spacing: 2px; font-size: 12px; font-weight: 600; margin-bottom: 16px;">
                📐 Design Principles
            </p>
            """, unsafe_allow_html=True)
            
            for i, principle in enumerate(principles):
                st.markdown(f"""
                <div style="padding: 16px 20px; background: var(--surface-1); border-radius: 12px; margin-bottom: 8px; border: 1px solid var(--hairline);" class="blueprint-section">
                    <span style="color: var(--accent-purple); font-family: 'Fraunces', serif; font-size: 20px; margin-right: 12px;">0{i+1}</span>
                    <span style="color: var(--ink);">{principle}</span>
                </div>
                """, unsafe_allow_html=True)
    
    # ============================================
    # DOWNLOAD SECTION
    # ============================================
    st.markdown("<div style='height: 64px;'></div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 32px;">
        <div style="font-family: 'Fraunces', serif; font-size: 2rem; color: var(--ink); letter-spacing: -0.03em;">
            Take your blueprint anywhere
        </div>
        <p style="color: var(--ink-muted); margin-top: 8px;">Download your complete landing page as Markdown or JSON.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate downloadable markdown
    def generate_markdown(bp, description):
        md = f"# Landing Page Blueprint\n\n"
        md += f"**Product:** {description}\n\n"
        md += "---\n\n"
        
        if "hero" in bp and "error" not in bp["hero"]:
            h = bp["hero"]
            md += f"## 🎯 Hero Section\n\n"
            md += f"**Headline:** {h.get('headline', '')}\n\n"
            md += f"**Subheadline:** {h.get('subheadline', '')}\n\n"
            md += f"**Primary CTA:** {h.get('cta_primary', '')}\n\n"
            md += f"**Secondary CTA:** {h.get('cta_secondary', '')}\n\n---\n\n"
        
        if "features" in bp and "error" not in bp["features"]:
            md += f"## ✨ Features\n\n"
            for f in bp["features"].get("features", []):
                md += f"### {f.get('icon', '')} {f.get('title', '')}\n{f.get('description', '')}\n\n"
            md += "---\n\n"
        
        if "how_it_works" in bp and "error" not in bp["how_it_works"]:
            md += f"## 🚀 How It Works\n\n"
            for s in bp["how_it_works"].get("steps", []):
                md += f"### {s.get('number', '')} — {s.get('title', '')}\n{s.get('description', '')}\n\n"
            md += "---\n\n"
        
        if "social_proof" in bp and "error" not in bp["social_proof"]:
            md += f"## 💬 Social Proof\n\n### Testimonials\n\n"
            for t in bp["social_proof"].get("testimonials", []):
                md += f"> \"{t.get('quote', '')}\"\n> — **{t.get('author', '')}**, {t.get('role', '')}\n\n"
            md += "### Trust Signals\n"
            for ts in bp["social_proof"].get("trust_signals", []):
                md += f"- {ts}\n"
            md += "\n---\n\n"
        
        if "faq" in bp and "error" not in bp["faq"]:
            md += f"## ❓ FAQs\n\n"
            for q in bp["faq"].get("faqs", []):
                md += f"**Q: {q.get('question', '')}**\n\n{q.get('answer', '')}\n\n"
            md += "---\n\n"
        
        if "design_system" in bp and "error" not in bp["design_system"]:
            d = bp["design_system"]
            md += f"## 🎨 Design System\n\n**Vibe:** {d.get('vibe', '')}\n\n"
            p = d.get("color_palette", {})
            md += f"### Color Palette\n- Primary: `{p.get('primary', '')}`\n- Accent: `{p.get('accent', '')}`\n- Background: `{p.get('background', '')}`\n- Text: `{p.get('text', '')}`\n\n"
            t = d.get("typography", {})
            md += f"### Typography\n- Headings: **{t.get('heading_font', '')}**\n- Body: **{t.get('body_font', '')}**\n- Why: _{t.get('pairing_reason', '')}_\n\n"
            md += f"### Design Principles\n"
            for pr in d.get("design_principles", []):
                md += f"- {pr}\n"
            md += "\n"
        
        md += "\n---\n\n_Made with 💜 by LaunchPad AI_\n"
        return md
    
    markdown_content = generate_markdown(blueprint, st.session_state.get("product_description", ""))
    json_content = json.dumps(blueprint, indent=2)
    
    dl_col1, dl_col2, dl_col3, dl_col4 = st.columns([1, 1.2, 1.2, 1])
    with dl_col2:
        st.download_button(
            label="📄 Download as Markdown",
            data=markdown_content,
            file_name="landing-page-blueprint.md",
            mime="text/markdown",
            use_container_width=True,
            key="dl_md"
        )
    with dl_col3:
        st.download_button(
            label="📦 Download as JSON",
            data=json_content,
            file_name="landing-page-blueprint.json",
            mime="application/json",
            use_container_width=True,
            key="dl_json"
        )
    
    # Regenerate button
    st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)
    regen_col1, regen_col2, regen_col3 = st.columns([2, 1, 2])
    with regen_col2:
        if st.button("↻ Generate New", type="secondary", use_container_width=True, key="regen"):
            st.session_state.blueprint = None
            st.rerun()


# ============================================
# FOOTER
# ============================================
render_footer()