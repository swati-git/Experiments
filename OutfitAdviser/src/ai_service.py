import config
from src.ai_providers import GeminiProvider

def get_ai_provider():
    """
    Factory function that returns the configured AI provider.
    
    Returns:
        An instance of BaseAIProvider (either ClaudeProvider or GeminiProvider)
    
    Raises:
        ValueError: If an invalid AI provider is configured
    """
    if config.AI_PROVIDER == "gemini":
        return GeminiProvider()
    # elif config.G == "gemini":
    #     return GeminiProvider()
    else:
        raise ValueError(f"Unknown AI provider: {config.AI_PROVIDER}")

