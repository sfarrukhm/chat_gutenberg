import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
import requests
# Function to fetch the book content from a URL
def fetch_book_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            st.error(f"Failed to fetch the book. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error fetching the book: {e}")
        return None

def text_splitter(text):
    text_splitter=RecursiveCharacterTextSplitter(separators="\n",chunk_size=1000,\
                                                 chunk_overlap=300,
                                                 length_function=len)
    chunks=text_splitter.split_text(text)
    return chunks

def main():
    st.set_page_config(page_title="BookLens – A lens into books, answering your queries",page_icon=":books:")
    st.header("Chat with your books :books:")
    st.text_input("Ask any question from the book")

    with st.sidebar:
        st.subheader("Book Text Reader")
        book_url=st.text_input("Enter the book URL")
        if st.button("Read"):
            with st.spinner("Reading..."):
                # get book text
                book_text=fetch_book_content(book_url)
                text_chunks=text_splitter(book_text)
                st.write(text_chunks)

                # get text chunks

                # create vector store





if __name__=="__main__":
    main()