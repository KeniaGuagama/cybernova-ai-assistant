import streamlit as st
import chatbot
import time
import os
import base64


# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="CyberNova AI Assistant",
    page_icon="🛡️",
    layout="centered"
)


# =====================================================
# CARGAR AGENTE UNA VEZ
# =====================================================

@st.cache_resource(show_spinner=False)
def load_agent():
    return chatbot.ask_agent


ask_agent = load_agent()


# =====================================================
# ESTILOS PREMIUM
# =====================================================

st.markdown("""
<style>


/* Fondo */

.stApp{
    background:
    radial-gradient(circle at top,#1e1b4b,#060B1A 45%);
    font-family:'Segoe UI', sans-serif;
}


/* Ocultar elementos */

#MainMenu{
display:none;
}

footer{
display:none;
}

header{
display:none;
}

.logo-container{

text-align:center;

margin-top:20px;

margin-bottom:10px;

}


.logo-container img{

width:160px;

height:160px;

object-fit:contain;

            filter:
drop-shadow(0 0 25px #60A5FA)
drop-shadow(0 0 35px #A855F7);

animation:float 3s ease-in-out infinite;

}



@keyframes float{

0%{
transform:translateY(0px);
}

50%{
transform:translateY(-8px);
}

100%{
transform:translateY(0px);
}

}

 /* TITULO */

.title{

text-align:center;

font-size:48px;

font-weight:900;

letter-spacing:1px;


background:
linear-gradient(
90deg,
#38BDF8,
#818CF8,
#C084FC
);


-webkit-background-clip:text;
background-clip:text;

color:transparent;


text-shadow:
0 0 20px rgba(96,165,250,.35);


animation:
glow 3s ease-in-out infinite alternate,
floatTitle 4s ease-in-out infinite;


}


/* Brillo animado */

@keyframes glow{

from{

filter:
drop-shadow(0 0 8px #2563EB);

}


to{

filter:
drop-shadow(0 0 25px #C084FC);

}

}


/* Pequeño movimiento */

@keyframes floatTitle{

0%{

transform:translateY(0px);

}


50%{

transform:translateY(-3px);

}


100%{

transform:translateY(0px);

}

}           

.subtitle{

text-align:center;

color:#CBD5E1;

font-size:18px;

font-weight:500;

letter-spacing:2px;

text-transform:uppercase;

margin-bottom:35px;

opacity:.9;

animation:fadeIn 1.5s ease;

}


@keyframes fadeIn{

from{
opacity:0;
transform:translateY(10px);
}

to{
opacity:1;
transform:translateY(0);
}

}


/* TARJETAS */


.card{

background:
linear-gradient(
135deg,
rgba(37,99,235,.25),
rgba(124,58,237,.20)
);

border:1px solid rgba(255,255,255,.15);

padding:20px;

border-radius:18px;

text-align:center;

color:white;

height:120px;

transition:.3s;

}


.card:hover{

transform:translateY(-8px);

box-shadow:
0 0 25px rgba(124,58,237,.5);

}



.user{

background:#1E293B;

padding:15px;

border-radius:15px;

color:white;

margin-bottom:15px;

animation:slide .4s;

}



.bot{

background:
linear-gradient(
135deg,
#312E81,
#2563EB
);

padding:15px;

border-radius:15px;

color:white;

margin-bottom:20px;

animation:slide .5s;

}



@keyframes slide{

from{

opacity:0;

transform:translateY(15px);

}


to{

opacity:1;

transform:translateY(0);

}

}



/* INPUT */

.stTextInput input{


background:#111827;

color:white;

border-radius:15px;

border:1px solid #475569;

font-size:16px;

}



.stTextInput input:focus{

border:1px solid #A855F7;

}


/* BOTONES */


.stButton button{


width:100%;

height:50px;

border-radius:15px;

border:none;

background:

linear-gradient(
90deg,
#2563EB,
#9333EA
);


color:white;

font-weight:bold;

font-size:17px;


transition:.3s;


}



.stButton button:hover{

transform:scale(1.03);

box-shadow:
0 0 20px #8B5CF6;

}



</style>

""", unsafe_allow_html=True)



# =====================================================
# HEADER
# =====================================================

# LOGO

st.markdown(
"""

<div class="logo-container">
<img src="data:image/png;base64,{}">
</div>
""".format(
    base64.b64encode(
        open("assets/cybernova_logo.png","rb").read()
    ).decode()
),
unsafe_allow_html=True
)

st.markdown(
'<div class="title">CyberNova AI Assistant</div>',
unsafe_allow_html=True
)

st.markdown(
"""
<div class="subtitle">
 Intelligent Cybersecurity Knowledge Assistant
</div>
""",
unsafe_allow_html=True
)



# =====================================================
# TARJETAS
# =====================================================


c1,c2,c3 = st.columns(3)


with c1:

    st.markdown(
    """
    <div class="card">
    🔐<br>
    <b>Protección Inteligente</b>
    <br>
    Seguridad empresarial
    </div>
    """,
    unsafe_allow_html=True
    )


with c2:

    st.markdown(
    """
    <div class="card">
    📚<br>
    <b>Base RAG</b>
    <br>
    Documentación segura
    </div>
    """,
    unsafe_allow_html=True
    )


with c3:

    st.markdown(
    """
    <div class="card">
    ⚡<br>
    <b>Respuesta IA</b>
    <br>
    Consulta rápida
    </div>
    """,
    unsafe_allow_html=True
    )



st.write("")



# =====================================================
# MEMORIA
# =====================================================


if "messages" not in st.session_state:

    st.session_state.messages=[]



# =====================================================
# BORRAR
# =====================================================


if st.button("🗑️  Borrar conversación"):

    st.session_state.messages=[]

    st.rerun()



# =====================================================
# CHAT
# =====================================================


st.markdown(
'<div class="chat-box">',
unsafe_allow_html=True
)



for role,text in st.session_state.messages:


    if role=="user":

        st.markdown(
        f"""
        <div class="user">
        👤 <b>Tú</b>
        <br><br>
        {text}
        </div>
        """,
        unsafe_allow_html=True
        )


    else:

        st.markdown(
        f"""
        <div class="bot">
        🛡️ <b>CyberNova</b>
        <br><br>
        {text}
        </div>
        """,
        unsafe_allow_html=True
        )



st.markdown(
"</div>",
unsafe_allow_html=True
)

# =====================================================
# INPUT + CONSULTAR
# =====================================================


with st.form("chat_form", clear_on_submit=True):


    question = st.text_input(
        "",
        placeholder="💬 Pregunta algo sobre ciberseguridad..."
    )


    submit = st.form_submit_button(
        "🚀 Consultar con IA"
    )



if submit:


    if question.strip():


        st.session_state.messages.append(
            ("user", question)
        )


        with st.spinner("🧠 Analizando conocimiento de CyberNova..."):


            answer = ask_agent(question)



        st.session_state.messages.append(
            ("assistant", answer)
        )


        st.rerun()