"""
LaunchPad AI - AI Engine
Powered by Groq (Llama 3.3 70B)
Made with 💜 by Vivi
"""

import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class LaunchPadAI:
    """The brain of LaunchPad AI - generates landing page blueprints"""
    
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env file!")
        
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"
    
    def _call_ai(self, system_prompt: str, user_prompt: str, temperature: float = 0.7) -> str:
        """Internal method to call Groq API"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature,
            max_tokens=2000,
        )
        return response.choices[0].message.content.strip()
    
    def _parse_json_response(self, response: str) -> dict:
        """Extract JSON from AI response (handles markdown code blocks)"""
        # Remove markdown code fences if present
        cleaned = response.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        elif cleaned.startswith("```"):
            cleaned = cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()
        
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError as e:
            # Fallback: return raw text wrapped
            return {"error": f"Could not parse JSON: {str(e)}", "raw": response}
    
    # ============================================
    # GENERATOR METHODS
    # ============================================
    
    def generate_hero(self, product_description: str) -> dict:
        """Generate the hero section (headline + subheadline + CTA)"""
        system = """You are a world-class landing page copywriter who has written for 
        top SaaS companies like Linear, Vercel, Stripe, and Notion. You understand 
        that great headlines are benefit-driven, specific, and emotionally compelling.
        
        You MUST respond with ONLY valid JSON, no other text."""
        
        user = f"""Generate a hero section for this product:
        
        PRODUCT: {product_description}
        
        Respond with ONLY this JSON structure (no markdown, no explanation):
        {{
            "headline": "A powerful, benefit-driven headline (max 8 words)",
            "subheadline": "A clear explanation of the value proposition (max 20 words)",
            "cta_primary": "Primary button text (2-4 words, action-oriented)",
            "cta_secondary": "Secondary button text (2-4 words, low commitment)"
        }}"""
        
        response = self._call_ai(system, user, temperature=0.8)
        return self._parse_json_response(response)
    
    def generate_features(self, product_description: str) -> dict:
        """Generate 4 key features"""
        system = """You are a product marketer who specializes in feature positioning.
        You know how to translate technical capabilities into user benefits.
        
        You MUST respond with ONLY valid JSON, no other text."""
        
        user = f"""Generate 4 key features for this product:
        
        PRODUCT: {product_description}
        
        Respond with ONLY this JSON (no markdown):
        {{
            "features": [
                {{
                    "icon": "single relevant emoji",
                    "title": "Short feature name (3-5 words)",
                    "description": "Benefit-focused description (max 15 words)"
                }}
            ]
        }}
        
        Generate exactly 4 features. Each icon should be a single emoji."""
        
        response = self._call_ai(system, user, temperature=0.7)
        return self._parse_json_response(response)
    
    def generate_how_it_works(self, product_description: str) -> dict:
        """Generate 3-step how it works"""
        system = """You are a UX writer who excels at breaking complex processes into 
        simple, digestible steps that reduce friction.
        
        You MUST respond with ONLY valid JSON, no other text."""
        
        user = f"""Generate a 3-step "How It Works" section for:
        
        PRODUCT: {product_description}
        
        Respond with ONLY this JSON (no markdown):
        {{
            "steps": [
                {{
                    "number": "01",
                    "title": "Short action title (3-5 words)",
                    "description": "What the user does (max 15 words)"
                }}
            ]
        }}
        
        Generate exactly 3 steps."""
        
        response = self._call_ai(system, user, temperature=0.6)
        return self._parse_json_response(response)
    
    def generate_social_proof(self, product_description: str) -> dict:
        """Generate testimonial templates + trust signals"""
        system = """You are a conversion copywriter who understands social proof psychology.
        Create realistic-feeling testimonials that sound authentic, not sales-y.
        
        You MUST respond with ONLY valid JSON, no other text."""
        
        user = f"""Generate social proof for:
        
        PRODUCT: {product_description}
        
        Respond with ONLY this JSON (no markdown):
        {{
            "testimonials": [
                {{
                    "quote": "Realistic user testimonial (max 25 words)",
                    "author": "Persona name",
                    "role": "Job title, Company type"
                }}
            ],
            "trust_signals": [
                "Trust signal 1 (e.g., '10,000+ users')",
                "Trust signal 2",
                "Trust signal 3"
            ]
        }}
        
        Generate exactly 3 testimonials and 3 trust signals."""
        
        response = self._call_ai(system, user, temperature=0.7)
        return self._parse_json_response(response)
    
    def generate_faq(self, product_description: str) -> dict:
        """Generate FAQ section"""
        system = """You are a customer success expert who understands the top objections 
        and questions people have before purchasing a product.
        
        You MUST respond with ONLY valid JSON, no other text."""
        
        user = f"""Generate 4 FAQs for:
        
        PRODUCT: {product_description}
        
        Respond with ONLY this JSON (no markdown):
        {{
            "faqs": [
                {{
                    "question": "Common user question",
                    "answer": "Clear, helpful answer (max 30 words)"
                }}
            ]
        }}
        
        Generate exactly 4 FAQs that address real objections/concerns."""
        
        response = self._call_ai(system, user, temperature=0.6)
        return self._parse_json_response(response)
    
    def generate_design_system(self, product_description: str) -> dict:
        """Generate design recommendations (colors, fonts, vibe)"""
        system = """You are a senior brand designer who understands how visual identity 
        communicates product positioning. You know color psychology and typography pairing.
        
        You MUST respond with ONLY valid JSON, no other text."""
        
        user = f"""Recommend a design system for:
        
        PRODUCT: {product_description}
        
        Respond with ONLY this JSON (no markdown):
        {{
            "vibe": "3-4 mood keywords (e.g., 'Modern, playful, trustworthy')",
            "color_palette": {{
                "primary": "#HEX (main brand color)",
                "accent": "#HEX (secondary accent)",
                "background": "#HEX (page background)",
                "text": "#HEX (primary text color)"
            }},
            "typography": {{
                "heading_font": "Google Font name for headlines",
                "body_font": "Google Font name for body text",
                "pairing_reason": "Why this pairing works (max 20 words)"
            }},
            "design_principles": [
                "Principle 1",
                "Principle 2",
                "Principle 3"
            ]
        }}"""
        
        response = self._call_ai(system, user, temperature=0.8)
        return self._parse_json_response(response)
    
    # ============================================
    # THE MAIN METHOD
    # ============================================
    
    def generate_full_landing_page(self, product_description: str, progress_callback=None) -> dict:
        """Generate ALL sections in sequence with progress updates"""
        result = {}
        
        steps = [
            ("hero", "✨ Crafting your hero section...", self.generate_hero),
            ("features", "🎯 Designing feature highlights...", self.generate_features),
            ("how_it_works", "🚀 Building your process flow...", self.generate_how_it_works),
            ("social_proof", "💬 Creating social proof...", self.generate_social_proof),
            ("faq", "❓ Generating FAQs...", self.generate_faq),
            ("design_system", "🎨 Recommending design system...", self.generate_design_system),
        ]
        
        for i, (key, message, method) in enumerate(steps):
            if progress_callback:
                progress_callback(i, len(steps), message)
            
            try:
                result[key] = method(product_description)
            except Exception as e:
                result[key] = {"error": str(e)}
        
        if progress_callback:
            progress_callback(len(steps), len(steps), "✅ Complete!")
        
        return result