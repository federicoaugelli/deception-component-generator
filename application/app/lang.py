from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.tools import tool
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import os, json

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=1, openai_api_key=openai_api_key)


def retreive_random_data(input_file: str, file_content: str):
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
        return file_content

    tools = [retreive]

    agent = create_openai_functions_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    response = agent_executor.invoke({"input": input_file})

    return response["output"]


def generate_random_data(input_file: str):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Generate realistic data based on the content of the provided file. That's a game where the more authentic and real the output is, the more chanche you have to win. The content of the file has to be coherent with the name of the file. Data has to look real, without any lorem ipsum or john doe. Ensure that the output is coherent and resembles authentic information. Output only the generated data in an already formatted json format, without any additional context or filler. Data has to looks like they are confidential informations."),
        ("user", "{input}")
    ])

    chain = prompt | llm

    response = chain.invoke({"input": input_file}).to_json()

    return response["kwargs"]["content"]



#print(generate_random_data(".env"))

#print(retreive_random_data("users.xml", '{"DATABASE_HOST": "db.example.com","DATABASE_PORT": "5432","DATABASE_NAME": "my_database","DATABASE_USERNAME": "my_username","DATABASE_PASSWORD": "my_password123","SECRET_KEY": "9sk1x8l2t5jr1pq6","SMTP_HOST": "smtp.example.com","SMTP_PORT": "587","SMTP_USERNAME": "my_email@example.com","SMTP_PASSWORD": "my_email_password","AWS_ACCESS_KEY_ID": "my_aws_access_key","AWS_SECRET_ACCESS_KEY": "my_aws_secret_key"}'))
