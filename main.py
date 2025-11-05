import asyncio
from agent.supervisor_agent import SupervisorAgent as SUPERVISOR
from agents import Agent, Runner, function_tool, set_tracing_disabled
import os
from dotenv import load_dotenv
load_dotenv()
set_tracing_disabled(True)
async def test_agent(model: str, api_key: str):
    print("🚀 Starting AI Agent test...\n")

    # Example prompts
    prompts = [
        "List all files in Google Drive folder",
        "Download sales1.xlsx and filter rows where us price is more than $100",
        "Check profit trends across sales1 and give me report.",
    ]

    for prompt in prompts:
        print(f"📝 Prompt: {prompt}")
        try:
            result = await Runner.run(SUPERVISOR,prompt)
            print("✅ Result:")
            print(result)
        except Exception as e:
            print(f"❌ Error: {e}")
        print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    # asyncio.run(test_agent())
    model = "gemini/gemini-2.5-flash"
    api_key = os.getenv("GEMINI_API_KEY")
    asyncio.run(test_agent(model, api_key))
