import streamlit as st
import wikipedia
from llama_index import VectorStoreIndex, SimpleDirectoryReader

def main():
    
    # Give your Streamlit app a title
    st.title("Custom Chatbot using GPT 3.5 and lLamaIndex")

    # Create a text box
    user_input = st.text_input("Enter the Title of the topic want to grab from wikipedia for the Custom ChatBot:", "Enter text here...", key="text_input1")

    if user_input != "Enter text here...":
    
        data= wikipedia.page(user_input).content
        # Display the entered text
        st.write("You entered:", user_input)
        
        #open text file
        text_file = open("./data/data.txt", "w", encoding="utf-8")
         
        #write string to file
        text_file.write(data)
         
        #close file
        text_file.close()
        
        documents = SimpleDirectoryReader('data').load_data()
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()

        def query(user_input):    
            return query_engine.query(user_input).response
               
        user_input = st.text_input("Enter your question:", key="text_input2")
        if user_input!='':
            response = query(user_input)    
            st.write("Bot response:", response)

if __name__ == "__main__":
    main()
