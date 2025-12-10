import google.generativeai as genai
from pathlib import Path
from PIL import Image
from .base_provider import BaseAIProvider
import config

class GeminiProvider(BaseAIProvider):
    
    def __init__(self):
        genai.configure(api_key=config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(config.GEMINI_MODEL)
    
    def analyze_clothing_image(self, image_path: str) -> str:
        """Analyze clothing item using Gemini's vision API"""
        
        img = Image.open(image_path)
        
        prompt = """Analyze this clothing item and provide details in the following format:

Category: (e.g., top, bottom, dress, jacket, accessory)
Color: (primary color)
Fabric: (inferred from visual cues like sheen, texture, drape - e.g., cotton, silk, denim, wool)
Formality: (casual, semi-formal, formal)
Style: (e.g., bohemian, classic, modern, sporty)
Pattern: (solid, striped, floral, etc.)
Embellishments: (buttons, embroidery, sequins, plain)
Season: (summer, winter, all-season)
Description: (brief 1-2 sentence description)

Be specific and concise. Base fabric inference on visual characteristics like shine, texture, and drape."""
        
        response = self.model.generate_content([prompt, img])
        return response.text
    
    
    def generate_outfit_recommendation(
        self, 
        wardrobe_items: list, 
        occasion: str, 
        body_type: str, 
        specific_requirements: str
    ) -> str:
        """Generate outfit recommendation using Gemini"""
        items_text = "\n\n".join([
            f"Item {i+1}:\n{item['analysis']}" 
            for i, item in enumerate(wardrobe_items)
        ])
        
        prompt = f"""You are a professional fashion stylist. Based on the following wardrobe and requirements, suggest the best outfit combination.

WARDROBE ITEMS:
{items_text}

OCCASION: {occasion}
BODY TYPE: {body_type}
ADDITIONAL REQUIREMENTS: {specific_requirements if specific_requirements else "None"}

BODY TYPE STYLING GUIDELINES:
- Pear shape: Balance proportions by drawing attention to the upper body. A-line skirts, boat necklines, and structured shoulders work well.
- Hourglass: Emphasize the waist. Fitted clothes, wrap dresses, and belted items are flattering.
- Apple shape: Create definition at the waist. V-necks, empire waists, and A-line silhouettes are ideal.
- Rectangle: Create curves. Peplum tops, ruffles, and clothes with horizontal details add dimension.
- Inverted triangle: Balance broad shoulders. A-line skirts, wide-leg pants, and details at the hip work well.

IMPORTANT: Respond with ONLY a JSON object (no markdown, no extra text) in this exact format:
{{
  "recommended_items": [1, 3, 5],
  "styling_sequence": [
    {{"item_number": 1, "styling_note": "Wear this as the base layer"}},
    {{"item_number": 3, "styling_note": "Layer this on top"}},
    {{"item_number": 5, "styling_note": "Complete the look with this accessory"}}
  ],
  "why_works_for_occasion": "Detailed explanation of why this combination is perfect for the occasion",
  "why_flatters_body_type": "Explanation of how this flatters the specific body type",
  "overall_styling_tips": "Additional tips for pulling the look together"
}}

Use actual item numbers from the wardrobe. Include 2-5 items in your recommendation."""

        response = self.model.generate_content(prompt)
        return response.text
    
    
#     def generate_outfit_recommendation(
#         self, 
#         wardrobe_items: list, 
#         occasion: str, 
#         body_type: str, 
#         specific_requirements: str
#     ) -> str:
#         """Generate outfit recommendation using Gemini"""
#         items_text = "\n\n".join([
#             f"Item {i+1}:\n{item['analysis']}" 
#             for i, item in enumerate(wardrobe_items)
#         ])
        
#         prompt = f"""You are a professional fashion stylist. Based on the following wardrobe and requirements, suggest the best outfit combination.

# WARDROBE ITEMS:
# {items_text}

# OCCASION: {occasion}
# BODY TYPE: {body_type}
# ADDITIONAL REQUIREMENTS: {specific_requirements if specific_requirements else "None"}

# BODY TYPE STYLING GUIDELINES:
# - Pear shape: Balance proportions by drawing attention to the upper body. A-line skirts, boat necklines, and structured shoulders work well.
# - Hourglass: Emphasize the waist. Fitted clothes, wrap dresses, and belted items are flattering.
# - Apple shape: Create definition at the waist. V-necks, empire waists, and A-line silhouettes are ideal.
# - Rectangle: Create curves. Peplum tops, ruffles, and clothes with horizontal details add dimension.
# - Inverted triangle: Balance broad shoulders. A-line skirts, wide-leg pants, and details at the hip work well.

# Please provide:
# 1. Recommended outfit combination (specify which items by their numbers)
# 2. Why these pieces work together for this occasion
# 3. Why this combination flatters the specified body type
# 4. Any styling tips (accessories, layering, etc.)

# Be specific about which items to wear and explain your reasoning."""

#         response = self.model.generate_content(prompt)
#         return response.text