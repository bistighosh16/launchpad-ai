"""
LaunchPad AI - Landing Page
One sentence to a full landing page ✨
Made with 💜 by Vivi
"""

import streamlit as st
from utils.styles import (
    apply_design_system,
    render_footer,
    render_hero,
    render_feature_card,
    render_spotlight_card,
    render_cream_section,
    render_step_card,
    render_stat_card,
    render_sidebar,
)

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="LaunchPad AI · One sentence to a landing page",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_design_system()
render_sidebar()


# ============================================
# HERO SECTION
# ============================================
render_hero(
    eyebrow="✨ AI-POWERED LANDING PAGE GENERATOR",
    title="One sentence.<br>A full landing page.",
    subtitle="Describe your product in a sentence. Get a complete landing page blueprint with copy, structure, and a design system — in seconds."
)

# CTA Buttons - centered and equal width
btn_col1, btn_col2, btn_col3, btn_col4 = st.columns([2, 1.2, 1.2, 2])
with btn_col2:
    if st.button("Launch Generator →", type="primary", use_container_width=True, key="cta_hero_primary"):
        st.switch_page("pages/2_⚡_Generator.py")
with btn_col3:
    if st.button("See How It Works", type="secondary", use_container_width=True, key="cta_hero_secondary"):
        st.markdown("<script>window.scrollTo({top: 800, behavior: 'smooth'});</script>", unsafe_allow_html=True)


st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)


# ============================================
# FEATURES SECTION
# ============================================
st.markdown("""
<div style="text-align: center; padding: 32px 0;">
    <span class="badge-pill badge-purple">FEATURES</span>
    <h2 style="margin-top: 24px;">Everything you need to launch</h2>
    <p style="font-size: 18px; color: var(--ink-muted); max-width: 600px; margin: 16px auto 0 auto;">
        Not just headlines. A complete blueprint for your product's story.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    render_feature_card("✍️", "Hero Section", "Benefit-driven headlines and CTAs that convert. Written like a top SaaS copywriter would.")
with col2:
    render_feature_card("🎯", "Feature Highlights", "4 killer features positioned around user benefits, not technical specs.")
with col3:
    render_feature_card("🚀", "How It Works", "3-step process breakdown that reduces friction and builds confidence.")

st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)
with col4:
    render_feature_card("💬", "Social Proof", "Authentic-feeling testimonials and trust signals your audience will believe.")
with col5:
    render_feature_card("❓", "Smart FAQs", "Answers to real objections that convert hesitant visitors into customers.")
with col6:
    render_feature_card("🎨", "Design System", "Color palette, typography, and visual principles tailored to your brand.")


st.markdown("<div style='height: 96px;'></div>", unsafe_allow_html=True)


# ============================================
# HOW IT WORKS - CREAM SECTION
# ============================================
render_cream_section(
    badge="HOW IT WORKS",
    title="Three steps. That's it.",
    subtitle="From blank page to launch-ready blueprint in under a minute."
)

# Steps
step_col1, step_col2, step_col3 = st.columns(3)
with step_col1:
    render_step_card("01", "Describe your idea", "One sentence about your product or startup idea. That's all we need.")
with step_col2:
    render_step_card("02", "AI does the work", "Our AI generates every section — copy, structure, and design system.")
with step_col3:
    render_step_card("03", "Download & launch", "Export your complete landing page blueprint as a beautiful Markdown file.")


st.markdown("<div style='height: 96px;'></div>", unsafe_allow_html=True)


# ============================================
# GRADIENT SPOTLIGHT CTA
# ============================================
render_spotlight_card(
    title="Ready to launch?",
    subtitle="Turn your idea into a complete landing page blueprint in under a minute."
)

st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    if st.button("Try LaunchPad AI Now →", type="primary", use_container_width=True, key="cta_bottom"):
        st.switch_page("pages/2_⚡_Generator.py")


# ============================================
# WHY LAUNCHPAD SECTION
# ============================================
st.markdown("<div style='height: 96px;'></div>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 32px 0;">
    <span class="badge-pill badge-purple">WHY LAUNCHPAD</span>
    <h2 style="margin-top: 24px;">Built by a builder, for builders</h2>
    <p style="font-size: 18px; color: var(--ink-muted); max-width: 700px; margin: 16px auto 0 auto;">
        Landing pages take forever. Copywriting is hard. Design systems are overwhelming. 
        LaunchPad AI removes the friction — so you can focus on shipping.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 48px;'></div>", unsafe_allow_html=True)

stat_col1, stat_col2, stat_col3 = st.columns(3)
with stat_col1:
    render_stat_card("6", "Sections Generated")
with stat_col2:
    render_stat_card("<60s", "Time to Blueprint")
with stat_col3:
    render_stat_card("100%", "Free Forever")


# ============================================
# FOOTER
# ============================================
render_footer()