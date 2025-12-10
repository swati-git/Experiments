import gradio as gr
from src.utils import process_new_items

def create_add_items_tab():
    """Create the 'Add to Wardrobe' tab"""
    with gr.Tab("📤 Add to Wardrobe"):
        gr.Markdown("### Upload clothing items to build your digital wardrobe")
        
        with gr.Row():
            with gr.Column():
                image_input = gr.File(
                    label="Upload Clothing Images",
                    file_count="multiple",
                    file_types=["image"]
                )
                body_type_input = gr.Dropdown(
                    choices=["Pear Shape", "Hourglass", "Apple Shape"],
                    label="Your Body Type (optional - helps with recommendations)",
                    value=None
                )
                add_button = gr.Button("Add to Wardrobe", variant="primary")
            
            with gr.Column():
                add_output = gr.Textbox(
                    label="Analysis Results",
                    lines=15,
                    max_lines=20
                )

            
    add_button.click(
    fn=process_new_items,
    inputs=[image_input, body_type_input],
    outputs=add_output
)