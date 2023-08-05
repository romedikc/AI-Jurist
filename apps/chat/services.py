import os

import openai
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
loader = TextLoader("apps/chat/data/articles.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

# raw_documents = TextLoader("test.txt").load()
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separator="\n")
# documents = text_splitter.split_documents(raw_documents)
# db = Chroma.from_documents(documents, OpenAIEmbeddings())
#
# user_query = "Кто такой спанч боб?"
# docs = db.similarity_search(user_query)
# most_relevant_document = docs[0]
# prompt_with_data = most_relevant_document.page_content + "\n" + user_query
#
# response = openai.Completion.create(
#     engine="text-davinci-003",
#     prompt=prompt_with_data,
#     max_tokens=500,
#     stop=None
# )
# print(response['choices'][0]['text'].strip())
