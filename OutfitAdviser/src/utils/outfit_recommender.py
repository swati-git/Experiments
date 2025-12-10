from . import wardrobe_storage as storage
#import claude_api
import src.ai_service as ai_service


def process_new_items(images, body_type):
    """
    Process newly uploaded clothing items.
    Analyzes each image and adds to wardrobe.
    """
    if not images:
        return "Please upload at least one image!", ""
    
    ai_provider = ai_service.get_ai_provider()
    
    storage.update_body_type(body_type)
    
    results = []
    
    for img in images:
        try:
            img_path, item_id = storage.save_image(img)
            
            # Analyze using configured AI provider
            analysis = ai_provider.analyze_clothing_image(img_path)
            
            # Add to wardrobe
            storage.add_item_to_wardrobe(img_path, item_id, analysis)
            
            results.append(f"✅ Item added successfully!\n{analysis}\n")
            
        except Exception as e:
            results.append(f"❌ Error analyzing image: {str(e)}\n")
    
    summary = f"Added {len(images)} item(s) to your wardrobe!\n\n" + "\n".join(results)
    return summary


