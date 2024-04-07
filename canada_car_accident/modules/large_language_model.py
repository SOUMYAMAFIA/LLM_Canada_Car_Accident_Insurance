from llama_index.llms import OpenAI
from llama_index import LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os



def llm_llama_index(file_path, question):

    base_path='./data/'
    full_path = os.path.join(base_path,file_path)

    print(full_path)
    documents=SimpleDirectoryReader(full_path).load_data()

    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo"))
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    custom_llm_index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    
    custom_llm_query_engine = custom_llm_index.as_query_engine()
    result = custom_llm_query_engine.query(question).response

    return result
