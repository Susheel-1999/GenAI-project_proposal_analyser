from langchain_openai import OpenAIEmbeddings, ChatOpenAI

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

llm = ChatOpenAI(model="gpt-4o", temperature=0, max_tokens=None, timeout=None, max_retries=2)
