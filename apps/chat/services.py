import os

import openai
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
loader = TextLoader("apps/chat/chat_data/articles.txt")
index = VectorstoreIndexCreator().from_loaders([loader])
