from services.prompts import Prompt
from utils.llms import get_llm

# Local
def llm(query: str, chat_history: list[dict], context: str = "No Context Found Do not response") -> tuple[str, str]:
    prompt = Prompt.response_prompt(context=context)
    promptm={"role":"human","content":prompt}
    chat_history.insert(0,promptm)
    querym={"role":"human","content":query}
    chat_history.append(querym)
    messages = chat_history
    generation = get_llm().invoke(messages)
    response = generation.content
    tokens=generation.usage_metadata["total_tokens"]
    return response,tokens