import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun

openai_api_key = st.secrets["OPENAI"]["api_key"]

######################################################
########################################## Page config
######################################################

st.title("MVP - Positive psychology")

# Seletor de idioma
if "language" not in st.session_state:
    st.session_state["language"] = "Português"

language = st.selectbox(
    "Escolha seu idioma:", 
    ["Português", "English", "Español", "Deutsch", "Lëtzebuergesch"], 
    index=["Português", "English", "Español", "Deutsch", "Lëtzebuergesch"].index(st.session_state["language"])
)

# Atualiza o idioma selecionado
st.session_state["language"] = language

# Mensagens iniciais em diferentes idiomas
welcome_messages = {
    "Português": "Oi, eu sou Lulu. Gostaria de brincar com você. Vamos conversar?",
    "English": "Hi, I'm Lulu. I'd like to play with you. Shall we chat?",
    "Español": "Hola, soy Lulu. Me gustaría jugar contigo. ¿Vamos a charlar?",
    "Deutsch": "Hallo, ich bin Lulu. Ich würde gerne mit dir spielen. Sollen wir reden?",
    "Lëtzebuergesch": "Moien, ech sinn Lulu. Ech géif gär mat dir spillen. Wëlls de schwätzen?"
}

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": welcome_messages[language]}
    ]
else:
    # Atualiza a saudação se o idioma mudar
    if st.session_state["messages"][0]["content"] != welcome_messages[language]:
        st.session_state["messages"] = [
            {"role": "assistant", "content": welcome_messages[language]}
        ]
        

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="How are you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
    search = DuckDuckGoSearchRun(name="Search")
    search_agent = initialize_agent(
        [search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True
    )
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)