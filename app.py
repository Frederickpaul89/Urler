import os
import joblib
import langchain
import streamlit as st
import pickle as pkl
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.document_loaders import UnstructuredURLLoader,WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma, FAISS
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import time


load_dotenv("ping.env")
api_key=os.getenv("OPENAI_API_KEY")
api_base=os.getenv("OPENAI_API_BASE")

llm=ChatOpenAI(model_name="google/gemma-3n-e2b-it:free",temperature=0)
try:
    with open("embedmo.pkl", "rb") as f:
        m1 = pkl.load(f)
    # Quick sanity check
    if not isinstance(m1, SentenceTransformerEmbeddings):
        raise ValueError("Loaded object is not a SentenceTransformerEmbeddings instance.")
except Exception as e:
    st.error(f"Failed to load embedding model: {str(e)}")
    st.stop()

m2=joblib.load("m1.joblib")
st.title("URL ANALYSER🔗")
st.sidebar.title("Give your URls🔗?")
mp=st.empty()

urs=[]
for i in range(3):
  url=st.sidebar.text_input(f"URL {i+1}🔗")
  urs.append(url)



purs=st.button("gotcha", disabled=not any(url.strip() for url in urs))
if purs:
    
    urs = [url.strip() for url in urs if url.strip()]
    
    mp.text("Loading..URl..Loader....☑️☑️☑️")
    valid_urls = [url for url in urs if url.strip()]
    if not valid_urls:
        st.warning("⚠️ No valid URLs entered.")
        st.stop()
    try:
        sic = WebBaseLoader(valid_urls)
        docs = sic.load()
    except Exception as e:
        st.error(f"❌ Failed to load URLs: {e}")
        st.stop()
    if not docs:
        st.warning("⚠️ No content loaded from URLs. This might be due to network restrictions or invalid URLs.")
        st.stop()
    st.write(len(docs))

    mp.text("Loading..txt..splitter....☑️☑️☑️")
    tot=RecursiveCharacterTextSplitter.from_tiktoken_encoder(encoding_name="cl100k_base",chunk_size=512,chunk_overlap=16)
    doccs=tot.split_documents(docs)
    
    mp.text("Loading..VB...☑️☑️☑️")
    vv=Chroma.from_documents(doccs,m1)
    r2=vv.as_retriever(search_type="similarity",search_kwargs={"k":4})
    mp.text("Loading..Retri....☑️☑️☑️")
    ra1=RetrievalQAWithSourcesChain.from_chain_type(llm=llm,retriever=r2,chain_type="map_reduce")
    st.session_state.ra1=ra1
    mp.text("DB & Retri Done ✅✅✅")
    time.sleep(3)
query=mp.text_input("UR Question??")
if query:
    if "ra1" not in st.session_state:
        st.warning("pls give ur urls")
    else:
        with st.spinner("Wait for it..."):
            result=st.session_state.ra1({"question":query},return_only_outputs=True)
        st.header("Answer")
        st.subheader(result["answer"])

  

