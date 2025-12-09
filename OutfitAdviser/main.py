import gradio as gr

with gr.Blocks(title="Fashion Outfit Recommender") as app:
    gr.Markdown("""
    # 👔 Fashion Outfit Recommender
    
    Your personal AI stylist that helps you create perfect outfits from your wardrobe!
    """)

if __name__ == "__main__":
    app.launch(theme=gr.themes.Monochrome())