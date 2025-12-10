import gradio as gr
import src.utils.outfit_recommender as recommender

def create_recommendation_tab():
    """Create the 'Get Outfit Suggestion' tab"""
    with gr.Tab("✨ Get Outfit Suggestion"):
        gr.Markdown("### Get AI-powered outfit recommendations for any occasion")
        
        with gr.Row():
            with gr.Column():
                occasion_input = gr.Dropdown(
                    choices=[
                        "Casual Brunch",
                        "Formal Wedding",
                        "Business Meeting",
                        "Date Night",
                        "Job Interview",
                        "Beach Outing",
                        "Cocktail Party",
                        "Gym/Workout",
                        "Casual Office",
                        "Family Gathering"
                    ],
                    label="Occasion",
                    value="Casual Brunch"
                )
                requirements_input = gr.Textbox(
                    label="Specific Requirements (optional)",
                    placeholder="e.g., 'I want to wear something blue' or 'I prefer modest outfits'",
                    lines=3
                )
                recommend_button = gr.Button("Get Recommendation", variant="primary")
            
            with gr.Column():
                recommendation_output = gr.Markdown(label="Your Outfit Recommendation")
        
        # Gallery to display outfit images
        gr.Markdown("### 👔 Your Complete Outfit")
        outfit_gallery = gr.Gallery(
            label="Recommended Clothing Items (in styling sequence)",
            show_label=True,
            columns=5,
            rows=1,
            height="auto",
            object_fit="contain"
        )
        
        recommend_button.click(
            fn=recommender.get_outfit_recommendation,
            inputs=[occasion_input, requirements_input],
            outputs=[outfit_gallery, recommendation_output]
        )
