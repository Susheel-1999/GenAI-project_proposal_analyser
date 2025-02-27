from crewai.tools import tool
from crewai_tools import WebsiteSearchTool, SerperDevTool, TXTSearchTool
from langchain.chains import RetrievalQA
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from utils import llm, embeddings
from read_document import read_document

# default tools
web_search_tool = WebsiteSearchTool()
serper_search_tool = SerperDevTool()
file_read_tool = TXTSearchTool()

# custom tools using the decorator
vector_store = Chroma(
    collection_name="job_description",
    embedding_function=embeddings,
    persist_directory='chroma_data',
)

jd_documents = read_document('data/job_description.pdf')
jd_documents = [Document(page_content=jd_documents)]
jd_chunks = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=100).split_documents(jd_documents)
vector_store.add_documents(documents=jd_chunks)

jd_retriever = RetrievalQA.from_chain_type(
    return_source_documents=True,
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
    verbose=True
)

@tool("jd_reader_tool")
def jd_reader_tool() -> str:
    """
    Understand the job description.
    """
    query = "Summarize"
    result = jd_retriever.invoke(query)
    return result.get("result", "No relevant information found.")

# custom tools using the class
resume_analyzer_tool = TXTSearchTool(txt="data/candidate_resume.txt")