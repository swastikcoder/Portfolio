import streamlit as st

# --- Page config ---
st.set_page_config(
    page_title="Swastik Ranjan | Portfolio",
    layout="wide",
    page_icon="💼"
)

# --- Custom CSS for styling ---
st.markdown("""
<style>
    body {
        font-family: 'Inter', sans-serif;
        color: #262730;
    }
    h1, h2, h3 {
        color: #1f77b4;
    }
    .info-card, .project-card, .contact-card {
        background-color: #f9f9f9;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }
    .info-card:hover, .project-card:hover, .contact-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }
    a {
        text-decoration: none;
        color: #0073e6;
        font-weight: 500;
    }
    a:hover {
        text-decoration: underline;
    }
    .contact-btn {
        display: inline-block;
        background-color: #1f77b4;
        color: white !important;
        padding: 10px 18px;
        margin: 8px;
        border-radius: 8px;
        font-weight: 500;
        transition: background-color 0.2s ease-in-out, transform 0.2s ease-in-out;
    }
    .contact-btn:hover {
        background-color: #155d8b;
        transform: scale(1.05);
    }
    .profile-card {
        background: linear-gradient(135deg, #e3f2fd, #bbdefb);
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    .profile-card h2 {
        color: #0d47a1;
        margin-bottom: 5px;
    }
    .profile-card p {
        color: #1a237e;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🧾 Employment History", "💻 Projects", "📞 Contact"])

# --- Home Page ---
if page == "🏠 Home":
    # Profile Snapshot Card
    st.markdown("""
    <div class="profile-card">
        <h2>Swastik Ranjan</h2>
        <p>Full Stack & GenAI Developer | BITS Pilani Alumnus</p>
        <p>💻 Python • JavaScript • Django • React • Docker</p>
    </div>
    """, unsafe_allow_html=True)

    st.title("👋 Hi, I'm Swastik Ranjan")
    st.write("""
    I'm a **Full Stack Developer** with exposure to **GenAI**, building clean, scalable, and functional applications using 
    **Python** and **JavaScript** frameworks such as **Django**, **React**, and **Flask**.  
    I also have hands-on experience with **Docker** and related backend technologies.

    """)
    st.info("💡 Tip: Explore the sidebar to see my projects and contact details!")

    # --- About Me Section ---
    st.markdown("## 🧑‍💻 About Me")
    st.markdown("""
    Hello! I’m **Swastik Ranjan**, an alumnus of **BITS Pilani**.  
    I have a keen interest in **Software Development**, **Data Science**, and **everything Tech**.  

    I’m passionate about **Tech for Good**, leveraging technology to create meaningful impact rather than being just another developer.  
    My goal is to contribute to innovation that helps shape a better future 🌍.

    Outside of coding, I’m a **huge cricket fanatic** 🏏, and I love discussing **Tech, Engineering life, Sports**, and **eSports** (especially **cloud gaming** 🎮).  

    ### 🎓 Positions of Responsibility
    - **President**, Baithak (North Indian Association), BITS Pilani  
    - **Batch Representative**, BITS Pilani  
    - **Vice-Captain**, Athletics Team, BITS Pilani  
    - **Prefect**, School Council Member  
    """)

    # --- Skills Section ---
    st.markdown("## 🧠 Skills Overview")
    st.markdown("""
    ### 🖥️ Frontend
    React, Vue.js, HTML, CSS, JavaScript, HTMX, Svelte, TypeScript

    ### ⚙️ Backend
    Django, Python, Flask, Java, C++, C

    ### 🗃️ Databases
    SQL, MySQL

    ### 🧩 Frameworks / Tools
    Wagtail, Reflex, Nuxt, Docker

    ### 💡 Core Concepts
    Data Structures & Algorithms, Object-Oriented Programming, Operating Systems
    """)

# --- Employment History Page ---
elif page == "🧾 Employment History":
    st.header("🧾 Employment History")
    st.write("A concise summary of my professional experience and key contributions 👇")

    # PalTech
    st.markdown("""
    <div class="info-card">
        <h3>PalTech | Associate Software Engineer</h3>
        <p><em>Hyderabad — July 2024 – Present</em></p>
        <ul>
            <li>Architected and deployed scalable backend microservices using <b>Django</b> and <b>Wagtail CMS</b> for a real estate client, implementing rate limiting, Redis caching, and role-based access control for 5+ user types.</li>
            <li>Reduced API response time from <b>2000ms → 200ms</b> with async processing and query optimizations, improving listing performance by 40%.</li>
            <li>Developed a secure <b>Insurance Adjustment Portal</b> (Django REST + React + JWT + WebSockets), cutting claims processing time by 30% and improving data accuracy by 20%.</li>
            <li>Resolved 15+ ORM and migration conflicts ensuring 99.9% uptime and zero-downtime releases across 3 environments.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Rivigo
    st.markdown("""
    <div class="info-card">
        <h3>Rivigo | Intern</h3>
        <p><em>Gurugram — July 2023 – Dec 2023</em></p>
        <ul>
            <li>Automated logistics reporting pipelines using <b>Python</b> & <b>Pandas</b>, processing 500+ daily reports and reducing manual effort by 60% across 50+ cities.</li>
            <li>Built a <b>Captain Distance Tracker</b> that compared real OpenStreetMap route data with captain-quoted distances — revealed a <b>25% variance</b> after adjustments, improving transparency and accuracy.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Projects Page ---
elif page == "💻 Projects":
    st.header("💻 My Projects")
    st.write("A few handpicked projects that combine frontend, backend, and Generative AI applications")

    st.markdown("""
    <div class="project-card">
        <h3>🛍️ E-commerce Platform (Vue + Django)</h3>
        <p>Full-stack store with JWT authentication, product listing, and analytics dashboard.</p>
        <p><a href="https://github.com/swastikcoder/Ecommerce_Vue_Django" target="_blank">📂 View Code</a></p>
    </div>

    <div class="project-card">
        <h3>🗣️ Voice Agent (Streamlit + Gemini + LangChain)</h3>
        <p>Interactive voice chatbot powered by speech recognition, TTS, and Gemini API.</p>
        <p><a href="https://github.com/swastikcoder/Voice-agents" target="_blank">📂 View Code</a></p>
    </div>

    <div class="project-card">
        <h3>📝 Blog Application (Django)</h3>
        <p>A simple, elegant blogging platform built with Django featuring CRUD, authentication, and admin tools.</p>
        <p><a href="https://github.com/swastikcoder/Django_app" target="_blank">📂 View Code</a></p>
    </div>
    """, unsafe_allow_html=True)

# --- Contact Page ---
elif page == "📞 Contact":
    st.header("📬 Get in Touch")
    st.write("If you'd like to collaborate, discuss ideas, or just connect — here are a few ways you can reach me 👇")

    st.markdown("""
    <div class="contact-card">
        <h3>💌 Email</h3>
        <p><a href="mailto:swastikr787@gmail.com" class="contact-btn">Send Email</a></p>
    </div>

    <div class="contact-card">
        <h3>🐙 GitHub</h3>
        <p><a href="https://github.com/swastikcoder" target="_blank" class="contact-btn">Visit GitHub</a></p>
    </div>

    <div class="contact-card">
        <h3>💼 LinkedIn</h3>
        <p><a href="https://www.linkedin.com/in/swastik-ranjan-978610203/" target="_blank" class="contact-btn">View Profile</a></p>
    </div>

    <div class="contact-card">
        <h3>🗂️ Resume</h3>
        <p><a href="https://drive.google.com/file/d/1M3_T_8ZD_PcX5FVymG9KJEcOd2c2Lmw8/view?usp=sharing" target="_blank" class="contact-btn">Download Resume</a></p>
    </div>
    """, unsafe_allow_html=True)
