import json
from pathlib import Path
from datetime import datetime
import shutil

WARDROBE_DIR = Path("digital_wardrobe")
IMAGES_DIR = WARDROBE_DIR / "images"
METADATA_FILE = WARDROBE_DIR / "wardrobe_metadata.json"

def initialize_storage():
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
