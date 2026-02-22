from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(model="openai/gpt-oss-20b",temperature=0.8)

print("Hello I am the maths tutor, Ask any question from me.")

message=[
    SystemMessage(content="""You are a Mathematics Tutor.
                            Solve the question step-by-step in maximum 5 lines only.
                            Use clear mathematical steps.
                            Write only the solution and final answer.
                            No extra explanation.""")
]

while(True):
    query=input("")
    if query=='exit':
        break
    message.append(HumanMessage(content=query))
    result=llm.invoke(message)
    print(result.content)
    message.append(AIMessage(content=result.content))

print("!!!!!Thanks!!!!!")