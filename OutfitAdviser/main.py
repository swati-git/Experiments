import gradio as gr
from src.utils import initialize_storage    
#from ..src.ui import ui
from src.ui import create_app

def main():
   
    initialize_storage()

    app = create_app()
    app.launch(theme=gr.themes.Soft())

if __name__ == "__main__":
    main()