import json
from pathlib import Path
from datetime import datetime
import shutil

WARDROBE_DIR = Path("digital_wardrobe")
IMAGES_DIR = WARDROBE_DIR / "images"
METADATA_FILE = WARDROBE_DIR / "wardrobe_metadata.json"

def initialize_storage():
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

def load_wardrobe():
    """Load wardrobe metadata from JSON file"""
    if METADATA_FILE.exists():
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    return {"items": [], "user_preferences": {}}

def update_body_type(body_type):
    if not body_type:
        return
    
    wardrobe = load_wardrobe()
    wardrobe["user_preferences"]["body_type"] = body_type
    save_wardrobe(wardrobe)

def save_wardrobe(wardrobe_data):
    """Save wardrobe metadata to JSON file"""
    with open(METADATA_FILE, 'w') as f:
        json.dump(wardrobe_data, f, indent=2)


def save_image(image_file):
    """
    Save an uploaded image to the wardrobe directory.
    Returns the path to the saved image.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    img_filename = f"item_{timestamp}.jpg"
    img_path = IMAGES_DIR / img_filename
    
    if hasattr(image_file, 'name'):
        shutil.copy(image_file.name, img_path)
    else:
        shutil.copy(image_file, img_path)
    
    return str(img_path), timestamp

def add_item_to_wardrobe(image_path, item_id, analysis):
    """Add a new clothing item to the wardrobe metadata"""
    wardrobe = load_wardrobe()
    
    item = {
        "id": item_id,
        "image_path": image_path,
        "analysis": analysis,
        "added_date": datetime.now().isoformat()
    }
    
    wardrobe["items"].append(item)
    save_wardrobe(wardrobe)

def get_all_items():
    """Get all wardrobe items"""
    wardrobe = load_wardrobe()
    return wardrobe["items"]

def get_body_type():
    """Get user's body type preference"""
    wardrobe = load_wardrobe()
    return wardrobe["user_preferences"].get("body_type", "not specified")
