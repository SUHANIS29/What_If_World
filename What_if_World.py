# # import streamlit as st
# # import google.generativeai as genai
# # import os

# # # --- API Setup ---
# # api_key = "AIzaSyCqDJS29W7Eb-gasWpnCSBg2_xS9p76a0g"

# # if not api_key:
# #     st.error("❌ GEMINI_API_KEY not found. Please add it in Streamlit Secrets or environment variables.")
# # else:
# #     genai.configure(api_key=api_key)

# # st.set_page_config(page_title="What-If World 🌍", page_icon="✨", layout="wide")

# # st.title("✨ What-If World 🌍")
# # st.markdown("Ask fun *what if* scenarios and explore creative answers powered by **Google Gemini AI**! 🚀")

# # # --- Input box ---
# # question = st.text_input("🤔 Ask a 'What if...' question", placeholder="e.g., What if humans could breathe underwater?")

# # # --- Button ---
# # if st.button("Generate Answer"):
# #     if not question.strip():
# #         st.warning("⚠️ Please enter a question first!")
# #     else:
# #         with st.spinner("Thinking with Gemini..."):
# #             try:
# #                 # ✅ Correct Model
# #                 model = genai.GenerativeModel("gemini-1.5-flash")

# #                 # Generate response
# #                 response = model.generate_content(question)

# #                 if response and response.text:
# #                     st.success("✨ Here's your What-If answer:")
# #                     st.write(response.text)
# #                 else:
# #                     st.error("⚠️ No response received. Try again!")

# #             except Exception as e:
# #                 st.error(f"❌ Error: {e}")
# import streamlit as st
# import google.generativeai as genai
# import random

# # --- API Setup ---
# api_key = "AIzaSyCqDJS29W7Eb-gasWpnCSBg2_xS9p76a0g"
# genai.configure(api_key=api_key)

# st.set_page_config(page_title="What-If World 🌍", page_icon="✨", layout="wide")

# st.title("✨ What-If World 🌍")
# st.markdown("Not just answers — experience **alternate realities** 🚀")

# # --- Input box ---
# question = st.text_input("🤔 Ask a 'What if...' question", placeholder="e.g., What if humans could breathe underwater?")

# # --- Button ---
# if st.button("Generate Alternate Reality"):
#     if not question.strip():
#         st.warning("⚠️ Please enter a question first!")
#     else:
#         with st.spinner("🌌 Building your What-If World..."):
#             try:
#                 model = genai.GenerativeModel("gemini-1.5-flash")

#                 # 1️⃣ Multi-Lens Thinking
#                 prompt_multi = f"""
#                 User asked: {question}
#                 Answer in 3 short sections:
#                 1. 🌍 Scientific Lens (logical, factual)
#                 2. 😂 Funny/Pop-culture Lens
#                 3. 💭 Philosophical/Deep Meaning Lens
#                 """
#                 resp_multi = model.generate_content(prompt_multi).text

#                 # 2️⃣ Timeline Simulator
#                 prompt_timeline = f"""
#                 Imagine {question}.
#                 Create a timeline of changes in 3 stages:
#                 - Year 1
#                 - Year 10
#                 - Year 50
#                 Short bullet points only.
#                 """
#                 resp_timeline = model.generate_content(prompt_timeline).text

#                 # 3️⃣ Reality Score
#                 reality_score = random.randint(10, 95)

#                 # 4️⃣ Story Mode
#                 prompt_story = f"""
#                 Write a short creative story (100-150 words) based on:
#                 {question}
#                 Make it engaging like a mini alternate universe.
#                 """
#                 resp_story = model.generate_content(prompt_story).text

#                 # --- Display ---
#                 st.subheader("🔮 Multi-Lens Perspectives")
#                 st.write(resp_multi)

#                 st.subheader("⏳ Timeline of Change")
#                 st.write(resp_timeline)

#                 st.subheader("📊 Reality Score")
#                 st.progress(reality_score / 100)
#                 st.write(f"**{reality_score}% chance this could be real someday!**")

#                 st.subheader("📖 Story Mode")
#                 st.write(resp_story)

#             except Exception as e:
#                 st.error(f"❌ Error: {e}")

import streamlit as st
import google.generativeai as genai
import random

# --- API Setup ---
api_key = "AIzaSyB4pK9CWTUprXalUbE37-9KxJERMmypewU"
genai.configure(api_key=api_key)

# --- Page Config ---
st.set_page_config(page_title="What-If World 🌍", page_icon="✨", layout="wide")

# # --- Dark Mode Toggle ---
# if "dark_mode" not in st.session_state:
#     st.session_state.dark_mode = False

# dark_mode = st.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)
# st.session_state.dark_mode = dark_mode

# --- Custom CSS ---
# if dark_mode:
bg_color = "#0e1117"
text_color = "#fafafa"
card_bg = "#1e222a"
# else:
# bg_color = "#f8f9fa"
# text_color = "#000000"
# card_bg = "#ffffff"

st.markdown(f"""
    <style>
    body {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .big-title {{
        font-size: 2.5rem;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 0.5em;
    }}
    .subtitle {{
        font-size: 1.2rem;
        text-align: center;
        color: #888;
        margin-bottom: 1.5em;
    }}
    .response-box {{
        background: {card_bg};
        padding: 1em;
        border-radius: 12px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 1em;
    }}
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<div class='big-title'>✨ What-If World 🌍</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Not just answers - experience <b>alternate realities</b> 🚀</div>", unsafe_allow_html=True)
# --- Why Different Section ---
with st.expander("🆚 Why This App is Different from ChatGPT/Gemini?"):
    st.markdown("""
    Unlike normal AI chatbots, **What-If World** doesn’t just answer your questions.
    
    ✅ **Multi-Lens Thinking** → Science, Funny, Philosophy in one go.  
    ✅ **Timeline Simulator** → See the future in Year 1, Year 10, Year 50.  
    ✅ **Reality Score** → A metric showing how plausible your idea is.  
    ✅ **Story Mode** → Mini alternate universe stories.  
    ✅ **Random Qs** → Interactive, gamified experience.  
    
    👉 It's not Q&A, it's **Imagination as a Service** ✨
    """)
# --- Input Box with Random Feature ---
random_qs = [
    "What if humans had wings?",
    "What if robots ruled the world?",
    "What if the ocean was made of chocolate?",
    "What if time could be paused?",
    "What if animals could speak?"
]

col1, col2 = st.columns([3,1])
with col1:
    question = st.text_input("🤔 Ask a 'What if...' question", 
                             value=st.session_state.get("question", ""), 
                             placeholder="e.g., What if humans could breathe underwater?")
with col2:
    if st.button("🎲 Random Question"):
        st.session_state["question"] = random.choice(random_qs)
        question = st.session_state["question"]

# --- Generate Button ---
if st.button("🚀 Generate Alternate Reality"):
    if not question.strip():
        st.warning("⚠️ Please enter a question first!")
    else:
        with st.spinner("🌌 Building your What-If World..."):
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")

                # Multi-Lens
                prompt_multi = f"""
                User asked: {question}
                Answer in 3 short sections:
                1. 🌍 Scientific Lens
                2. 😂 Funny Lens
                3. 💭 Philosophical Lens
                """
                resp_multi = model.generate_content(prompt_multi).text

                # Timeline
                prompt_timeline = f"""
                Imagine {question}.
                Create a timeline of changes:
                - Year 1
                - Year 10
                - Year 50
                """
                resp_timeline = model.generate_content(prompt_timeline).text

                # Reality Score


                # Story
                prompt_story = f"""
                Write a short, engaging, imaginative story based on this What-If scenario:
                "{question}"

                Guidelines:
                - 3-5 sentences max
                - Include a clear character or entity affected
                - Add a fun twist or unexpected consequence
                - Keep tone: playful and futuristic
                - Make it unique and memorable
                """


                # --- Display Results ---
                st.markdown("<div class='response-box'><h4>🔮 Multi-Lens Perspectives</h4></div>", unsafe_allow_html=True)
                st.write(resp_multi)

                st.markdown("<div class='response-box'><h4>⏳ Timeline of Change</h4></div>", unsafe_allow_html=True)
                st.write(resp_timeline)

                

                                                # --- Reality Score using AI ---
                prompt_reality = f"""
                User asked: {question}.
                For this scenario, give a reality score between 1-100, based on scientific, historical and social plausibility.
                Respond with just a number only.
                """
                resp_score = model.generate_content(prompt_reality).text.strip()

                # Try to convert AI response to integer
                try:
                    reality_score = int(''.join(filter(str.isdigit, resp_score)))
                    reality_score = max(0, min(reality_score, 100))  # clamp 0-100
                except:
                    reality_score = 50  # fallback in case AI fails

                # --- Display Reality Score ---
                st.markdown("<div class='response-box'><h4>📊 Reality Score</h4></div>", unsafe_allow_html=True)
                st.progress(reality_score / 100)
                st.write(f"**{reality_score}% chance this could be real someday!**")
                # st.markdown("<div class='response-box'><h4>📊 Reality Score</h4></div>", unsafe_allow_html=True)
                # st.progress(reality_score / 100)
                # st.write(f"**{reality_score}% chance this could be real someday!**")

                # st.markdown("<div class='response-box'><h4>📖 Story Mode</h4></div>", unsafe_allow_html=True)
                # st.write(resp_story)

            except Exception as e:
                st.error(f"❌ Error: {e}")


