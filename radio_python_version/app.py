import streamlit as st
import os
from PIL import Image

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")

# Load images using PIL for better compatibility with different environments
def load_image(image_name):
    path = os.path.join(IMAGE_DIR, image_name)
    if os.path.exists(path):
        return Image.open(path)
    return None

icon = load_image("g4.png")

# Page configuration
st.set_page_config(
    page_title="Boleros Online",
    page_icon=icon,
    layout="centered"
)

# Open Graph meta tags for WhatsApp preview
st.markdown("""
<meta property="og:title" content="Boleros Románticos" />
<meta property="og:description" content="Escucha las mejores radios de boleros románticos online, 20 estaciones disponibles." />
<meta property="og:image" content="https://boleros.streamlit.app/radio_python_version/images/miniatura.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:url" content="https://boleros.streamlit.app" />
<meta property="og:type" content="website" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Boleros Románticos - Radios Online" />
<meta name="twitter:description" content="Escucha las mejores radios de boleros románticos online." />
<meta name="twitter:image" content="https://boleros.streamlit.app/radio_python_version/images/miniatura.jpg" />
""", unsafe_allow_html=True)

# Custom CSS to match the original design
st.markdown("""
<style>
    .stApp {
        background-color: #c7cce6;
    }
    h1 {
        color: black;
        text-align: center;
        font-size: 30px;
        font-family: Arial, sans-serif;
    }
    .stButton > button {
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #0056b3;
        color: white;
    }
    .stButton > button:focus {
        background-color: #004080;
        color: white;
    }
    /* Hide Streamlit branding for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    .station-info {
        text-align: center;
        margin-top: 10px;
        font-size: 18px;
        font-weight: bold;
        color: #333;
    }
    .footer {
        text-align: center;
       
    }
    .footer a {
        color: #007bff;
        text-decoration: none;
    }
    /* Audio player styling */
    audio {
        width: 100% !important;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Station List
stations = [
    {"name": "1.- Radio Boleros", "url": " https://stream.zeno.fm/b10wvksv7mruv"},
    {"name": "2.- Su majestad el bolero", "url": "https://conectperu.com:7182/stream?icy=http"},
    {"name": "3.- Radio Viejitas", "url": "https://media.streamingradiomx.com/listen/viejitas/stream"},
    {"name": "4.- Besame Medellin", "url": "https://19213.live.streamtheworld.com/BESAME_MEDELLINAAC_SC?csegid=2000"},
    {"name": "5.- Cafe Romantico Radio", "url": "https://panel.retrolandigital.com/listen/cafe_romantico_radio/listen"},
    {"name": "6.- Baladas románticas en español", "url": "https://media.streamingradiomx.com/listen/romantica/on"},
    {"name": "7.- Fórmula Melódica", "url": "https://s2.yesstreaming.net:9085/stream"},
    {"name": "8.- Radio ritmo romantica", "url": "https://mdstrm.com/audio/6839e2376607bdf6b2fcde27/icecast.audio"},
    {"name": "9.- Romance 99.5", "url": "https://stream.zeno.fm/3avzkdt91rhvv"},
    {"name": "10.- Acerca de Amor", "url": "https://27163.live.streamtheworld.com/XHRHFMAAC_SC"},
    {"name": "11.- Boleros, Baladas y mas", "url": "https://stream.zeno.fm/vx4vcv5qyk8uv"},
    {"name": "12.- María Vargas Boleros por siempre", "url": "https://stream.zeno.fm/40f0h23f938uv"},
    {"name": "13.- 100 Boleros con aroma", "url": "https://stream.zeno.fm/lfonv1tnignuv"},
    {"name": "14.- Boleros de oro, plata y bronce", "url": "https://stream.zeno.fm/8mk5quawgs8uv"},
    {"name": "15.- Criollas y Boleros", "url": "https://stream.zeno.fm/qw3at85dqrhvv"},
    {"name": "16.- Boleros del alma", "url": "https://stream.zeno.fm/09wxqvzovf2vv"},
    {"name": "17.- Boleros de antaño", "url": "https://stream.zeno.fm/dllwo2vggqltv"},
    {"name": "18.- Soneros", "url": "https://stream.zeno.fm/7xw911mv2f8uv"},
    {"name": "19.- Buenisima radio boleros", "url": "https://stream.zeno.fm/fbpd99sqkchvv"},
    {"name": "20.- Radio felicidad tríos y boleros", "url": "https://17843.live.streamtheworld.com/ACIR17_S01.mp3"},
]

# Initialize Session State
if 'current_station_url' not in st.session_state:
    st.session_state['current_station_url'] = None
if 'current_station_name' not in st.session_state:
    st.session_state['current_station_name'] = "Selecciona una emisora"

# Header
st.markdown("<h1>BOLEROS ROMANTICOS<br>Radios Online</h1>", unsafe_allow_html=True)

# Main Container
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="radio-container">', unsafe_allow_html=True)
        st.markdown('<p style="color:black; margin-bottom: 10px; text-align: center;">Selecciona una radio para reproducir:</p>', unsafe_allow_html=True)
        
        for station in stations:
            if st.button(station["name"], key=station["name"], use_container_width=True):
                # Toggle: if clicking the same station, stop it
                if st.session_state['current_station_url'] == station["url"]:
                    st.session_state['current_station_url'] = None
                    st.session_state['current_station_name'] = "Selecciona una emisora"
                else:
                    # Play new station
                    st.session_state['current_station_url'] = station["url"]
                    st.session_state['current_station_name'] = station["name"]
        
        # Audio Player - Always visible with autoplay
        st.markdown('<div style="margin-top: 15px;">', unsafe_allow_html=True)
        if st.session_state['current_station_url']:
            # Custom HTML5 audio player with autoplay using components
            import streamlit.components.v1 as components
            
            audio_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    audio {{
                        width: 100%;
                        margin: 10px 0;
                    }}
                </style>
            </head>
            <body>
                <audio id="radioPlayer" controls autoplay>
                    <source src="{st.session_state['current_station_url']}" type="audio/mpeg">
                    Tu navegador no soporta la reproducción de audio.
                </audio>
                <script>
                    // Force play on load
                    window.onload = function() {{
                        var player = document.getElementById('radioPlayer');
                        player.play().catch(function(error) {{
                            console.log('Autoplay prevented:', error);
                        }});
                    }};
                </script>
            </body>
            </html>
            """
            components.html(audio_html, height=60)
        else:
            # Placeholder when no station is selected
            st.markdown('<div style="height: 54px; background-color: #e9ecef; border-radius: 5px; display: flex; align-items: center; justify-content: center; color: #6c757d;">Selecciona una estación</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Station Name Display
        st.markdown(f'<p style="text-align: center; margin-top: 10px; font-weight: bold; color: #333;">Reproduciendo: {st.session_state["current_station_name"]}</p>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# Footer & QR
#st.markdown("---")
col_footer1, col_footer2, col_footer3 = st.columns([1, 2, 1])
with col_footer2:
    st.markdown("""
    <div class="footer">
        <p style="color:black; text-align: center;">Estos proyectos web son mi aporte a la comunidad<br> 
        si te ha servido y deseas que éste proyecto continue\n, tu aporte al número Yape: \n <strong>904076033</strong> ó al QR</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display QR Code (centered)
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    yape_qr = load_image("yape.jpeg")
    if yape_qr:
        st.image(yape_qr)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="footer">
        <p style="color:black; text-align: center;">Creado por: Jenrry Soto Dextre <br>Web: <a href="https://dextre.xyz" target="_blank">dextre.xyz</a></p>
    </div>
    """, unsafe_allow_html=True)

