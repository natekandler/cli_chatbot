import getpass
import os
import uuid
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph


if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")


class Chatbot():
    def __init__(self):
        thread_id = str(uuid.uuid4())
        memory = MemorySaver()
        workflow = StateGraph(state_schema=MessagesState)
        workflow.add_edge(START, "model")

        self.model = ChatOpenAI(model="gpt-4o-mini")
        workflow.add_node("model", self.call_model)

        self.app = workflow.compile(checkpointer=memory)
        self.config = {"configurable": {"thread_id": thread_id}}

    def call_model(self, state: MessagesState):
        response = self.model.invoke(state["messages"])
        return {"messages": response}

    def query_chat(self, query):
        input_messages = [HumanMessage(query)]
        output = self.app.invoke({"messages": input_messages}, self.config)
        output["messages"][-1].pretty_print()  
