from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.tools import tool
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=1, openai_api_key=openai_api_key)





def retreive_random_data(input_file: str):
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"Generate realistic data based on the content of the provided file. The file may contain information of multiple users (like 10 or 15) such as api keys, passwords or any other relevant data. Data has to look really, without any lorem ipsum or john doe. Ensure that the output is coherent and resembles authentic information. Output only the generated data, without any additional context or filler, nor Generated data placeholder. The output has to be in the same syntax of {input_file}"),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    class SearchInput(BaseModel):
        query: str = Field(description=f"Useful to retreive information. Input will be a filename, and the output syntax has to be the same of {input_file}")


    @tool("search-tool", args_schema=SearchInput, return_direct=False)
    def retreive(query: str) -> str:
        """Useful to retreive random data. Input will be a filename"""

        #hardcoded
        return {"data": {"username": "federico", "password": "1234"}, "api_key": "asdfasdf", "location": {"home": "via Zagnoli 108", "work": "via Ercolani 1"}, "phones": {"home": "123456789", "work": "987654321"}}

    tools = [retreive]

    agent = create_openai_functions_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    response = agent_executor.invoke({"input": input_file})

    return response["output"]





def generate_random_data(input_file: str):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Generate realistic data based on the content of the provided file. The file may contain information of multiple users (like 10 or 15) such as api keys, passwords or any other relevant data. Data has to look really, without any lorem ipsum or john doe. Ensure that the output is coherent and resembles authentic information. Output only the generated data, without any additional context or filler."),
        ("user", "{input}")
    ])

    chain = prompt | llm

    return chain.invoke({"input": input_file})



#print(generate_random_data("data.json"))

#print(retreive_random_data("data.json"))
