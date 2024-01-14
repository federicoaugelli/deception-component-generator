from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.tools import tool
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.tools.tavily_search import TavilySearchResults

openai_api_key = "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"

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=1, openai_api_key=openai_api_key)

'''
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

agent_executor.invoke({"input": "Can you generate a random data for me based on the syntax of .json?"})
'''



def generate_random_data(input_file: str):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Generate realistic data based on the content of the provided file. The file may contain information of multiple users (like 10 or 15) such as api keys, passwords or any other relevant data. Data has to look really, without any lorem ipsum or john doe. Ensure that the output is coherent and resembles authentic information. Output only the generated data, without any additional context or filler."),
        ("user", "{input}")
    ])

    chain = prompt | llm

    return chain.invoke({"input": input_file})



print(generate_random_data("data.json"))
