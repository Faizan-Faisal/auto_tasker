import litellm
from openai import AsyncOpenAI
from openai.agents import AssistantRuntime
import os   # For environment variables

# Configure LiteLLM globally
litellm.api_key = os.getenv("GEMINI_API_KEY")
litellm.model = os.getenv("GEMINI_MODEL")   # or any default model you want

# Now integrate with Agent SDK
runtime = AssistantRuntime(
    client=AsyncOpenAI()  # this will route through litellm defaults
)
