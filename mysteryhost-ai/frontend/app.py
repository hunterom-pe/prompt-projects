import streamlit as st
import subprocess
import os

# ─── Session State Initialization ───
if "history" not in st.session_state:
    st.session_state.history = []
if "clues" not in st.session_state:
    st.session_state.clues = []

# ─── Page Configuration ───
st.set_page_config(page_title="Mystery Host AI", page_icon="🕵️", layout="centered")

# ─── Sidebar: Clue Tracker ───
with st.sidebar:
    st.header("🕵️ Clue Tracker")
    if st.session_state.clues:
        for i, c in enumerate(st.session_state.clues, start=1):
            st.markdown(f"**{i}.** {c}")
    else:
        st.markdown("_No clues yet…_")

# ─── Custom Header ───
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 2rem;">
      <h1 style="font-size: 3rem; color: #d4af37; font-family: Georgia, serif; text-shadow: 2px 2px #111;">
        Mystery Host AI
      </h1>
      <p style="color: #e0d8b0; font-style: italic;">
        A Chat‑powered noir detective adventure.
      </p>
    </div>
    """, unsafe_allow_html=True
)

# ─── Persona Loader & Ollama Runner ───
def load_persona():
    path = os.path.join(os.path.dirname(__file__), "../prompts/host_persona.txt")
    with open(path, "r") as f:
        return f.read()

def call_ollama(prompt, model="llama3"):
    proc = subprocess.run(
        ["ollama", "run", model, prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return proc.stdout.strip() if proc.returncode == 0 else f"Error: {proc.stderr}"

# ─── User Interaction & Story Loop ───
user_text = st.text_input("Your input:", placeholder="Ask a question or choose an option…")

if st.button("Submit") and user_text:
    persona = load_persona()
    conversation = "\n".join(st.session_state.history)
    full = f"{persona}\n\nStory so far:\n{conversation}\n\nUser: {user_text}"
    response = call_ollama(full)

    # Append history
    st.session_state.history.append(f"Detective: {user_text}")
    st.session_state.history.append(f"Mystery Host: {response}")

# ─── Clue Input Form ───
st.markdown("---")
with st.form(key="clue_form"):
    clue_val = st.text_input("Add a clue (optional):", key="clue_input")
    submitted = st.form_submit_button("Save Clue")

if submitted and clue_val.strip():
    st.session_state.clues.append(clue_val.strip())

# ─── Display Conversation ───
for line in st.session_state.history:
    st.markdown(f"> {line}")