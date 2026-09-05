

import streamlit as st
import requests
import os

st.set_page_config(
    page_title="Jiya's Chatbot",
    page_icon="💜",
    layout="centered"
)

API_URL = "http://127.0.0.1:8000"


# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

/* =========================
   MAIN PURPLE + PINK BACKGROUND
   ========================= */

.stApp {
    background:
        radial-gradient(
            circle at 10% 15%,
            rgba(255, 105, 180, 0.35),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 85%,
            rgba(170, 80, 255, 0.35),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #16002b 0%,
            #310052 40%,
            #5a0875 70%,
            #240039 100%
        );

    min-height: 100vh;
}


/* =========================
   CUTE MOVING STARS
   ========================= */

.stApp::before {

    content:
        "✦     ⋆       ✧       ˚       ✦
         ⋆       ✧     ✦       ⋆
         ˚       ✦       ✧       ⋆
         ✧       ⋆       ˚       ✦";

    position: fixed;

    top: -100px;
    left: 0;

    width: 100%;
    height: 120%;

    color: rgba(
        255,
        220,
        250,
        0.75
    );

    font-size: 16px;

    line-height: 110px;

    letter-spacing: 35px;

    white-space: pre-wrap;

    pointer-events: none;

    z-index: 0;

    animation:
        fallingStars
        14s
        linear
        infinite;
}


@keyframes fallingStars {

    0% {
        transform: translateY(-80px);
        opacity: 0.2;
    }

    30% {
        opacity: 0.8;
    }

    60% {
        opacity: 1;
    }

    100% {
        transform: translateY(100vh);
        opacity: 0.2;
    }
}


/* =========================
   MAIN CONTENT
   ========================= */

.block-container {

    position: relative;

    z-index: 2;

    max-width: 700px;

    padding-top: 60px;

    padding-bottom: 80px;
}


/* =========================
   TITLE
   ========================= */

h1 {

    text-align: center !important;

    color: #ffffff !important;

    font-size: 46px !important;

    font-weight: 700 !important;

    text-shadow:
        0 0 10px
        rgba(
            255,
            105,
            180,
            0.9
        ),

        0 0 25px
        rgba(
            190,
            90,
            255,
            0.8
        ),

        0 0 45px
        rgba(
            255,
            105,
            180,
            0.4
        );
}


/* =========================
   SUBTITLE
   ========================= */

.stMarkdown p {
    color: #f8dfff;
}


/* =========================
   TABS
   ========================= */

button[data-baseweb="tab"] {

    color: #f7c8ff !important;

    font-weight: 600 !important;

    font-size: 16px !important;
}


button[data-baseweb="tab"][aria-selected="true"] {

    color: #ffffff !important;

    text-shadow:
        0 0 8px #ff69b4;
}


div[data-baseweb="tab-highlight"] {

    background:
        linear-gradient(
            90deg,
            #ff4fa3,
            #c56cff
        ) !important;
}


/* =========================
   LABELS
   ========================= */

label {

    color: #ffd9f5 !important;

    font-weight: 500 !important;
}


/* =========================
   INPUT FIELDS
   ========================= */

div[data-baseweb="input"] {

    background:
        rgba(
            255,
            180,
            230,
            0.18
        ) !important;

    border:
        1px solid
        rgba(
            255,
            160,
            225,
            0.65
        ) !important;

    border-radius: 15px !important;

    box-shadow:
        0 0 15px
        rgba(
            255,
            105,
            180,
            0.15
        );
}


div[data-baseweb="input"]:focus-within {

    border:
        1px solid
        #ff8ed8 !important;

    box-shadow:

        0 0 8px
        rgba(
            255,
            105,
            180,
            0.7
        ),

        0 0 25px
        rgba(
            190,
            90,
            255,
            0.35
        );
}


/* INPUT TEXT BLACK */

input {

    color:
        #160d1c !important;

    background:
        transparent !important;

    caret-color:
        #d6339a !important;

    font-weight:
        500 !important;
}


/* PLACEHOLDER */

input::placeholder {

    color:
        #8f557f !important;

    opacity:
        1 !important;
}


/* =========================
   BUTTONS
   ========================= */

.stButton > button {

    width: 100%;

    border: none !important;

    border-radius: 15px !important;

    padding: 13px 20px !important;

    background:
        linear-gradient(
            90deg,
            #ff4fa3,
            #c052ff,
            #8f5cff
        ) !important;

    color:
        white !important;

    font-weight:
        600 !important;

    font-size:
        16px !important;

    box-shadow:
        0 5px 20px
        rgba(
            255,
            79,
            163,
            0.4
        );

    transition:
        all 0.3s ease;
}


.stButton > button:hover {

    transform:
        translateY(-3px)
        scale(1.01);

    box-shadow:
        0 8px 30px
        rgba(
            255,
            105,
            180,
            0.65
        );
}


/* =========================
   FILE UPLOADER
   ========================= */

[data-testid="stFileUploader"] {

    background:
        rgba(
            255,
            105,
            180,
            0.10
        );

    border:
        1px solid
        rgba(
            255,
            160,
            225,
            0.55
        );

    border-radius:
        16px;

    padding:
        10px;

    box-shadow:
        0 0 18px
        rgba(
            255,
            105,
            180,
            0.12
        );
}


/* =========================
   CHAT INPUT
   ========================= */

[data-testid="stChatInput"] {

    border:
        1px solid
        rgba(
            255,
            160,
            225,
            0.65
        ) !important;

    border-radius:
        18px !important;

    background:
        rgba(
            255,
            180,
            230,
            0.15
        ) !important;
}


/* =========================
   ALERTS
   ========================= */

div[data-testid="stAlert"] {

    border-radius:
        14px !important;

    background:
        rgba(
            255,
            255,
            255,
            0.10
        ) !important;

    color:
        white !important;
}


/* =========================
   DIVIDER
   ========================= */

hr {

    border-color:
        rgba(
            255,
            180,
            230,
            0.25
        ) !important;
}


/* =========================
   GLOWING PINK ORB
   ========================= */

.stApp::after {

    content: "";

    position: fixed;

    width: 200px;

    height: 200px;

    border-radius: 50%;

    background:
        rgba(
            255,
            80,
            180,
            0.14
        );

    filter:
        blur(45px);

    top: 8%;

    right: 4%;

    animation:
        glowingOrb
        5s
        ease-in-out
        infinite
        alternate;

    pointer-events:
        none;

    z-index:
        0;
}


@keyframes glowingOrb {

    from {

        transform:
            scale(0.8);

        opacity:
            0.3;
    }

    to {

        transform:
            scale(1.4);

        opacity:
            0.8;
    }
}


/* =========================
   HIDE STREAMLIT UI
   ========================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background:
        transparent !important;
}

</style>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.title("🤖 Jiya's Chatbot")

st.markdown(
    """
    <p style="
        text-align:center;
        font-size:17px;
        color:#ffd6f5;
    ">
        ✨ Your cute little AI knowledge assistant ✨
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")


# =========================
# LOGIN / REGISTER TABS
# =========================

login_tab, register_tab = st.tabs(
    [
        "🔐 Login",
        "💗 Register"
    ]
)


# =========================
# LOGIN
# =========================

with login_tab:

    st.subheader(
        "Welcome Back 💜"
    )

    email = st.text_input(
        "Email",
        placeholder="Enter your email",
        key="login_email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password",
        key="login_password"
    )

    st.write("")

    if st.button(
        "✨ Login",
        key="login_button"
    ):

        if not email or not password:

            st.warning(
                "💗 Please enter your email and password."
            )

        else:

            try:

                response = requests.post(
                    f"{API_URL}/login",

                    json={
                        "email": email,
                        "password": password
                    }
                )

                data = response.json()

                if data["success"]:

                    st.session_state[
                        "logged_in"
                    ] = True

                    st.session_state[
                        "email"
                    ] = email

                    st.rerun()

                else:

                    st.error(
                        "💔 " +
                        data["message"]
                    )

            except Exception as e:

                st.error(
                    f"🌸 Could not connect to backend: {e}"
                )


# =========================
# REGISTER
# =========================

with register_tab:

    st.subheader(
        "Create Your Account 💕"
    )

    name = st.text_input(
        "Name",
        placeholder="Enter your name",
        key="register_name"
    )

    register_email = st.text_input(
        "Email",
        placeholder="Enter your email",
        key="register_email"
    )

    register_password = st.text_input(
        "Password",
        type="password",
        placeholder="Create a password",
        key="register_password"
    )

    st.write("")

    if st.button(
        "💗 Create Account",
        key="register_button"
    ):

        if (
            not name
            or not register_email
            or not register_password
        ):

            st.warning(
                "🌷 Please fill in all the fields."
            )

        else:

            try:

                response = requests.post(
                    f"{API_URL}/register",

                    json={
                        "name": name,
                        "email": register_email,
                        "password": register_password
                    }
                )

                data = response.json()

                if data["success"]:

                    st.success(
                        "🎀 " +
                        data["message"]
                    )

                else:

                    st.error(
                        "💔 " +
                        data["message"]
                    )

            except Exception as e:

                st.error(
                    f"🌸 Could not connect to backend: {e}"
                )


# =========================
# CHATBOT DASHBOARD
# =========================

if st.session_state.get(
    "logged_in",
    False
):

    st.divider()

    st.markdown(
        """
        <h2 style="
            text-align:center;
            color:white;
            text-shadow:
                0 0 10px #ff69b4;
        ">
            💬 Welcome to Your AI Assistant
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <p style="
            text-align:center;
            color:#ffd6f5;
        ">
            Logged in as 💗
            {st.session_state["email"]}
        </p>
        """,
        unsafe_allow_html=True
    )


    # =========================
    # DOCUMENT UPLOAD
    # =========================

    st.markdown(
        """
        <h3 style="
            color:white;
            text-align:center;
            margin-top:25px;
            margin-bottom:5px;
            text-shadow:
                0 0 10px #ff69b4;
        ">
            📚 Upload Your Knowledge
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="
            text-align:center;
            color:#ffd6f5;
            font-size:14px;
        ">
            Upload a PDF or TXT file and I'll learn from it ✨
        </p>
        """,
        unsafe_allow_html=True
    )


    uploaded_file = st.file_uploader(
        "Choose your document",
        type=[
            "pdf",
            "txt"
        ],
        key="document_uploader"
    )


    if uploaded_file is not None:

        os.makedirs(
            "documents",
            exist_ok=True
        )

        file_path = os.path.join(
            "documents",
            uploaded_file.name
        )

        with open(
            file_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        st.success(
            f"💗 {uploaded_file.name} uploaded successfully!"
        )


    st.write("")


    # =========================
    # CHAT HISTORY
    # =========================

    if "messages" not in st.session_state:

        st.session_state[
            "messages"
        ] = []


    # =========================
    # DISPLAY MESSAGES
    # =========================

    for message in st.session_state[
        "messages"
    ]:

        if message["role"] == "user":

            st.markdown(
                f"""
                <div style="
                    background:
                        linear-gradient(
                            90deg,
                            #ff4fa3,
                            #b85cff
                        );

                    padding:
                        13px 18px;

                    border-radius:
                        18px;

                    margin:
                        10px 0;

                    color:
                        white;

                    text-align:
                        right;

                    box-shadow:
                        0 4px 15px
                        rgba(
                            255,
                            79,
                            163,
                            0.3
                        );
                ">
                    🧑‍💻 {message["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div style="
                    background:
                        rgba(
                            255,
                            255,
                            255,
                            0.10
                        );

                    border:
                        1px solid
                        rgba(
                            255,
                            180,
                            230,
                            0.3
                        );

                    padding:
                        13px 18px;

                    border-radius:
                        18px;

                    margin:
                        10px 0;

                    color:
                        white;
                ">
                    🤖 {message["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )


    # =========================
    # CHAT INPUT
    # =========================

    user_question = st.chat_input(
        "Ask something about your documents... 💭"
    )


    if user_question:

        st.session_state[
            "messages"
        ].append(
            {
                "role": "user",
                "content": user_question
            }
        )

        st.session_state[
            "messages"
        ].append(
            {
                "role": "assistant",
                "content":
                    "✨ I'm ready! Soon I'll answer using your documents."
            }
        )

        st.rerun()


    st.write("")


    # =========================
    # LOGOUT
    # =========================

    if st.button(
        "🚪 Logout",
        key="logout_button"
    ):

        st.session_state[
            "logged_in"
        ] = False

        st.session_state[
            "email"
        ] = ""

        st.session_state[
            "messages"
        ] = []

        st.rerun()

