from abc import ABC, abstractmethod

class BaseAIProvider(ABC):
    """Abstract interface for AI providers"""
    
    @abstractmethod
    def analyze_clothing_image(self, image_path: str) -> str:
        """
        Analyze a clothing item from an image.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Detailed analysis of the clothing item as a formatted string
        """
        pass
    
    @abstractmethod
    def generate_outfit_recommendation(
        self, 
        wardrobe_items: list, 
        occasion: str, 
        body_type: str, 
        specific_requirements: str
    ) -> str:
        """
        Generate outfit recommendation based on wardrobe and requirements.
        
        Args:
            wardrobe_items: List of wardrobe items with their analyses
            occasion: The occasion for the outfit
            body_type: User's body type
            specific_requirements: Additional user requirements
            
        Returns:
            Detailed outfit recommendation as a formatted string
        """
        pass