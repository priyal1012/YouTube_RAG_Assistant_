import streamlit as st
import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

# --- UI Setup ---
st.set_page_config(page_title="YouTube RAG Assistant", layout="centered")
st.title("📺 YouTube Video RAG Assistant")
st.write("Enter a YouTube Video ID and ask questions about its content.")

# Ensure API key is loaded from the environment (Colab sidebar removed)
if "GOOGLE_API_KEY" not in os.environ:
    st.error("Missing Google API Key. Please add it to your .env file.")

# --- Main Logic ---
video_id = st.text_input("Enter YouTube Video ID (e.g., Gfr50f6ZBvo):")

# Button to process the video
if st.button("Process Video"):
    if not video_id:
        st.error("Please enter a valid Video ID.")
    else:
        with st.spinner("Fetching transcript and indexing..."):
            try:
                ytt_api = YouTubeTranscriptApi()
                transcript_list = ytt_api.list(video_id).find_transcript(["en"]).fetch()
                transcript = " ".join(chunk.text for chunk in transcript_list)
                
                splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
                chunks = splitter.create_documents([transcript])
                
                embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
                vector_store = FAISS.from_documents(chunks, embeddings)
                
                st.session_state.vector_store = vector_store
                st.success("Video processed successfully! You can now ask questions.")
            
            except TranscriptsDisabled:
                st.error("No captions available for this video.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

# --- Chat Interface ---
st.divider()

if "vector_store" in st.session_state:
    question = st.text_input("Ask a question about the video:")
    
    if st.button("Ask") and question:
        with st.spinner("Generating answer..."):
            retriever = st.session_state.vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
            llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)
            prompt = PromptTemplate(
                template="""
                  You are a helpful assistant.
                  Answer ONLY from the provided transcript context.
                  If the context is insufficient, just say you don't know.

                  {context}
                  Question: {question}
                """,
                input_variables=['context', 'question']
            )
            
            def format_docs(retrieved_docs):
                return "\n\n".join(doc.page_content for doc in retrieved_docs)
            
            parallel_chain = RunnableParallel({
                'context': retriever | RunnableLambda(format_docs),
                'question': RunnablePassthrough()
            })
            main_chain = parallel_chain | prompt | llm | StrOutputParser()
            
            answer = main_chain.invoke(question)
            st.markdown("### Answer:")
            st.write(answer)