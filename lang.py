from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain.tools import tool
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder



openai_api_key = "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"

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You can ask me to generate a random data in the same syntax of the input query. Input is a filename. Output will be a randomly ganarated data with the same syntax as the input query. for example a /data.md will generate a randomly generate data in mark syntx",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

class SearchInput(BaseModel):
    query: str = Field(description="should be a search query")


@tool("search-tool", args_schema=SearchInput, return_direct=True)
def multiply(query: str) -> str:
    """multiply two numbers"""
    return "Response of the tool"

tools = [multiply]


agent = create_openai_functions_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke({"input": "Hi."})
