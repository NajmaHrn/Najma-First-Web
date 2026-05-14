import streamlit as st
from datetime import datetime

# ============================================================================
# CONFIG & TEMA (Customize bagian ini!)
# ============================================================================

st.set_page_config(
    page_title="Game Showcase Najma",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CUSTOM CSS (Design Modern)
# ============================================================================

st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
        color: #e0e0e0;
    }
    
    .main {
        background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
        padding: 2rem;
    }
    
    /* Header */
    .header-container {
        text-align: center;
        margin-bottom: 3rem;
        animation: fadeIn 0.8s ease-in;
    }
    
    .header-title {
        font-size: 3.5em;
        font-weight: 900;
        background: linear-gradient(135deg, #ff6b6b, #ffd93d, #6bcf7f, #4d96ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        letter-spacing: 2px;
    }
    
    .header-subtitle {
        font-size: 1.3em;
        color: #b0b0b0;
        font-style: italic;
        margin-bottom: 1rem;
    }
    
    .header-divider {
        width: 100px;
        height: 3px;
        background: linear-gradient(90deg, #ff6b6b, #ffd93d, #6bcf7f, #4d96ff);
        margin: 1rem auto;
        border-radius: 2px;
    }
    
    /* Game Cards */
    .game-card {
        background: linear-gradient(135deg, #2d2d44 0%, #3a3a52 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        border: 2px solid #444;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .game-card:hover {
        transform: translateY(-10px);
        border-color: #ff6b6b;
        box-shadow: 0 15px 40px rgba(255, 107, 107, 0.3);
    }
    
    .game-title {
        font-size: 2em;
        font-weight: 800;
        color: #ff6b6b;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .game-genre {
        font-size: 0.9em;
        color: #ffd93d;
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .game-desc {
        color: #d0d0d0;
        line-height: 1.6;
        margin-bottom: 1rem;
        font-size: 1em;
    }
    
    .game-image {
        width: 100%;
        border-radius: 10px;
        margin-bottom: 1rem;
        max-height: 400px;
        object-fit: cover;
        border: 2px solid #444;
        transition: transform 0.4s;
    }
    
    .game-image:hover {
        transform: scale(1.02);
    }
    
    .game-stats {
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
    }
    
    .stat-item {
        background: rgba(255, 107, 107, 0.1);
        padding: 0.8rem 1.2rem;
        border-radius: 8px;
        border-left: 3px solid #ff6b6b;
        color: #e0e0e0;
        font-size: 0.9em;
    }
    
    .button-steam {
        background: linear-gradient(135deg, #1b1f3a, #2d5016);
        color: white !important;
        border: 2px solid #165dbb;
        padding: 0.8rem 2rem;
        border-radius: 8px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s;
        font-size: 1em;
    }
    
    .button-steam:hover {
        background: linear-gradient(135deg, #165dbb, #3d7bc5);
        transform: translateX(5px);
        box-shadow: 0 5px 15px rgba(22, 93, 187, 0.4);
    }
    
    /* About Section */
    .about-section {
        background: linear-gradient(135deg, #2d2d44 0%, #3a3a52 100%);
        padding: 2.5rem;
        border-radius: 15px;
        border: 2px solid #444;
        margin-bottom: 3rem;
    }
    
    .about-title {
        font-size: 2.5em;
        color: #6bcf7f;
        margin-bottom: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .about-text {
        color: #d0d0d0;
        line-height: 1.8;
        font-size: 1.1em;
    }
    
    /* Contact Section */
    .contact-section {
        background: linear-gradient(135deg, #2d2d44 0%, #3a3a52 100%);
        padding: 2.5rem;
        border-radius: 15px;
        border: 2px solid #444;
        text-align: center;
    }
    
    .contact-title {
        font-size: 2em;
        color: #4d96ff;
        margin-bottom: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .contact-item {
        display: inline-block;
        margin: 0.5rem 1rem;
        padding: 0.8rem 1.5rem;
        background: rgba(77, 150, 255, 0.1);
        border-radius: 8px;
        border: 1px solid #4d96ff;
        color: #4d96ff;
        text-decoration: none;
        transition: all 0.3s;
        font-weight: 600;
    }
    
    .contact-item:hover {
        background: rgba(77, 150, 255, 0.2);
        transform: translateY(-3px);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #808080;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid #444;
        font-size: 0.9em;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HEADER
# ============================================================================

col1, col2, col3 = st.columns(3)

with col2:
    st.markdown("""
    <div class="header-container">
        <div class="header-title">🎮 Najimi's Showcase</div>
        <div class="header-subtitle">mai favorit game gim aku my saya ku!!</div>
        <div class="header-divider"></div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# TENTANG SAYA (ABOUT SECTION)
# ============================================================================

st.markdown("""
<div class="about-section">
    <div class="about-title">👨‍💻 Tentang Aku</div>
    <div class="about-text">
        Haloo semuanyaa! aku najma, bisa dibilang aku tuu gamer yang passionate tentang berbagai genre game! hehe 
        Website ini adalah kumpulan game-game favorit aku yang menurut aku layak banget untuk dimainkan. 
        Setiap game di bawah memiliki story dan gameplay yang ok bangett!!! 
        Jika kalian tertarik dengan salah satu game, yuk support developernya dengan membeli di Steam!
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# DATA GAME (CUSTOMIZE BAGIAN INI!)
# ============================================================================

games = [
    {
        "title": "Dave The Diver",
        "genre": "Adventure RPG",
        "description": "menampilkan alur permainan hibrida yang unik, menggabungkan eksplorasi laut bawah air 2.5D di siang hari dengan pengelolaan restoran sushi di malam hari.",
        "image": "img/davethediver.jpg",  # Ganti dengan nama file gambar kamu
        "rating": "9.67/10",
        "playtime": "16+ jam",
        "release_year": "2023",
        "steam_link": "https://store.steampowered.com/app/1868140/DAVE_THE_DIVER/"
    },
    {
        "title": "Battlefield V",
        "genre": "FPS Multiplayer",
        "description": "perang dunia 2 ala battlefield, multiplayer chaos 64 player di map gede banget dengan destructible environment. squad based combatnya seru, fortification system bikin lo bisa bangun defense ala engineer.",
        "image": "img/battlev.jpg",
        "rating": "8,2/10",
        "playtime": "80+ jam",
        "release_year": "2018",
        "steam_link": "https://store.steampowered.com/app/1238810/Battlefield_V/"
    },
    {
        "title": "Grand Theft Auto V",
        "genre": "action-adventure",
        "description": "masterpiece open world los santos, switch antara 3 karakter criminal michael franklin trevor lakuin heist gila-gilaan. storynya epic, online nya endless grind, modding pc nya bikin replayable forever",
        "image": "img/gtav.jpg",
        "rating": "10/10",
        "playtime": "1000+ jam",
        "release_year": "2013",
        "steam_link": "https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/"
    },
    {
        "title": "Stardew Valley",
        "genre": "farming simulation",
        "description": "chill farming life simulator, warisin farm dari kakek, tanem panen ternak ayam sapi, befriend villager sampe nikah. mining dungeon quest romance, konten endless update",
        "image": "img/stadewvalley.jpg",
        "rating": "9.2/10",
        "playtime": "200+ jam",
        "release_year": "2016",
        "steam_link": "https://store.steampowered.com/app/413150/Stardew_Valley/"
    },
    {
        "title": "Tomodachi Life: Living the Dream",
        "genre": "Life Simulation",
        "description": "aku suka banget life sim absurd kocak versi switch yang baru rilis 2026 ini, aku populate island pake mii-miiku (temen celeb bahkan presiden), aku liat drama pacaran kerja ribut ngantor sampe event random gila. pure chaos entertainment yang bikin ketawa ngakak tiap hari!!.",
        "image": "img/tomoo.jpg",
        "rating": "9.7/10",
        "playtime": "12+ jam",
        "release_year": "2026",
        "steam_link": "https://www.nintendo.com/us/store/products/tomodachi-life-living-the-dream-switch/"
    }
]

# ============================================================================
# RENDER GAME CARDS
# ============================================================================

st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #ffd93d; font-size: 2.5em; margin-bottom: 2rem;'> Game Favorit Najma!!</h2>", unsafe_allow_html=True)

for game in games:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Try to load image, if not found show placeholder
        try:
            st.image(game["image"], use_container_width=True)
        except:
            st.info(f"📁 Letakkan file '{game['image']}' di folder project mu")
    
    with col2:
        st.markdown(f"""
        <div class="game-card">
            <div class="game-title">{game['title']}</div>
            <div class="game-genre">📌 {game['genre']}</div>
            
            <div class="game-stats">
                <div class="stat-item">⭐ Rating: {game['rating']}</div>
                <div class="stat-item">⏱️ Playtime: {game['playtime']}</div>
                <div class="stat-item">📅 Release: {game['release_year']}</div>
            </div>
            
            <div class="game-desc">{game['description']}</div>
            
            <a href="{game['steam_link']}" target="_blank" class="button-steam">
                🔗 View on Steam →
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")

# ============================================================================
# CONTACT SECTION
# ============================================================================

st.markdown("""
<div class="contact-section">
    <div class="contact-title">📬 Get in touch w najma!?</div>
    <p style='color: #d0d0d0; margin-bottom: 1.5rem;'>
        Punya rekomendasi game yang menarik? Atau ingin diskusi tentang gaming? 
        Hubungi aku melaluii:
    </p>
    <a href="mailto:hurinnajma25@gmail.com" class="contact-item">📧 Email</a>
    <a href="https://twitter.com/marieulvenson" target="_blank" class="contact-item">𝕏 Twitter</a>
    <a href="https://https://www.instagram.com/urn.naaj?igsh=MXA2dDAxa3VnNmQzeg==" target="_blank" class="contact-item">📷 Instagram</a>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown(f"""
<div class="footer">
    <p>Made with ❤️ using Streamlit | Last updated: {datetime.now().strftime('%B %d, %Y')}</p>
</div>
""", unsafe_allow_html=True)
