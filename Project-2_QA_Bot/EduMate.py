import google.generativeai as genai
import streamlit as st

api_key = "GEMINI-API-KEY" #Paste your api key here
genai.configure(api_key=api_key)

def answer(query):
    try:
        prompt = query
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"College Admission related question: {prompt}")
        return response.text
    except Exception as e:
        st.write(f"An error occurred while processing: {e}")
        return "Sorry, we couldn't fetch information this time."

def main():
    st.set_page_config(page_title="EduMate", page_icon="https://th.bing.com/th/id/OIP.ithaQT5RG-mhITAaet7g-gHaHX?pid=ImgDet&w=474&h=471&rs=1")
    st.markdown("<h2 class='title'>Welcome to EduMate🎓! Ask your admission related questions here.</h2>", unsafe_allow_html=True)

    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    query = st.text_input("Ask your question here:", key="query", help="Type your question and click Search")
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    
    search = st.button("Search", key="search", help="Search for the answer to your question")
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    
    new_chat = st.button("New Chat", key="new_chat", help="Start a new chat session")
    st.markdown("---")

    if new_chat:
        st.session_state.chat_history = []

    if search:
        if query:
            ans = answer(query)
            st.session_state.chat_history.insert(0, (query, ans))  # Insert at the beginning to keep the latest on top

    # Display chat history
    if st.session_state.chat_history:
        for i, (q, a) in enumerate(st.session_state.chat_history):
            st.write(f"**Q{i+1}:** {q}")
            st.write(f"**A{i+1}:** {a}")
            st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.write("Powered by Generative AI")

if __name__ == "__main__":
    main()
