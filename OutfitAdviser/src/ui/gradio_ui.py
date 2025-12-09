import gradio as gr
from .add_items_tab import create_add_items_tab

def create_app():
    """Create the complete Gradio application"""
    with gr.Blocks(title="Fashion Outfit Recommender") as app:
        gr.Markdown("""
        # 👔 Fashion Outfit Recommender
        
        Your personal AI stylist that helps you create perfect outfits from your wardrobe!
        """)
        
        with gr.Tabs():
            create_add_items_tab()
    
    return app