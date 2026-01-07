import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="Radios Online - Solo Rock",
    page_icon="images/g4.png",
    layout="centered"
)

# Custom CSS to match the original design
st.markdown("""
<style>
    .stApp {
        background-color: #c7cce6;
    }
    h1 {
        color: black !important;
        text-align: center;
        font-size: 40px;
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
    {"name": "1.- GotRadio 80s", "url": "https://pureplay.cdnstream1.com/6009_64.aac"},
    {"name": "2.- Radio Zlote Przeboje", "url": "https://radiostream.pl/tuba9-1.mp3"},
    {"name": "3.- Curtin Radio", "url": "https://usa7.fastcast4u.com/proxy/curtinfm?mp=%2F1"},
    {"name": "4.- Mix 106.5", "url": "https://playerservices.streamtheworld.com/api/livestream-redirect/XHDFMFMAAC.aac?dist=onlineradiobox"},
    {"name": "5.- Radio Music80s Stereo", "url": "https://stream-156.zeno.fm/qa29r0es1f8uv"},
    {"name": "6.- Stereorey", "url": "https://playerservices.streamtheworld.com/api/livestream-redirect/XHCAA.mp3?dist=onlineradiobox"},
    {"name": "7.- 181.fm - The Eagle", "url": "https://listen.181fm.com/181-eagle_128k.mp3"},
    {"name": "8.- Easy Hits Florida", "url": "https://streaming.live365.com/a80304"},
    {"name": "9.- 181.fm Awesoma 80's", "url": "https://tinyurl.com/181fmAwesome"},
    {"name": "10.- 80s80s", "url": "https://tinyurl.com/80s80s"},
    {"name": "11.- fmhits80s", "url": "https://cast.fmhits80s.net.pe/listen/fm_hits_80s/stream128"},
    {"name": "12.- BeatlesRadio", "url": "https://strw3.openstream.co/981?aw_0_1st.collectionid%3D6906%26stationId%3D6906"},
    {"name": "13.- Aardvark", "url": "https://ais-edge90-dal03.cdnstream.com/b77280_128mp3"},
    {"name": "14.- Rock Antenne Live", "url": "https://stream.rockantenne.de/rockantenne/stream/mp3"},
    {"name": "15.- Ochentas Radio - rock and pop", "url": "https://stream.zeno.fm/b751gt2uweruv"},
    {"name": "16.- Flashback Radio 80's Music", "url": "https://das-edge16-live365-dal02.cdnstream.com/a14920"},
    {"name": "17.- Classic Rock", "url": "https://hdradioclassicrock-rfritschka.radioca.st/stream.m3u"},
    {"name": "18.- The Blues Radio", "url": "https://i4.streams.ovh/sc/bluesrad/stream"},
    {"name": "19.- Beatles Radio stream", "url": "https://stream-150.zeno.fm/6tmx3ddb86duv"},
    {"name": "20.- Houston Blues Radio", "url": "https://ais-edge89-dal02.cdnstream.com/b76353_128mp3?listenerId=735eabef088f5b63e3d62297494ec615&aw_0_1st.playerid=esPlayer&aw_0_1st.skey=1696730860"},
]

# Initialize Session State
if 'current_station_url' not in st.session_state:
    st.session_state['current_station_url'] = None
if 'current_station_name' not in st.session_state:
    st.session_state['current_station_name'] = "Selecciona una emisora"

# Header
st.markdown("<h1>SOLO ROCK <br>Radios Online</h1>", unsafe_allow_html=True)

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
st.markdown("---")
col_footer1, col_footer2, col_footer3 = st.columns([1, 2, 1])
with col_footer2:
    st.markdown("""
    <div class="footer">
        <p style="color:black; text-align: center;">Estos proyectos web son mi aporte a la comunidad<br> 
        si te ha servido y deseas que éste proyecto continue\n, tu aporte al número Yape: \n <strong>904076033</strong> ó al QR</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display QR Code
    if os.path.exists("images/yape.jpeg"):
        st.image("images/yape.jpeg", width=300)
    
    st.markdown("""
    <div class="footer">
        <p style="color:black; text-align: center;">Creado por: Jenrry Soto Dextre <br>Web: <a href="https://dextre.xyz" target="_blank">dextre.xyz</a></p>
    </div>
    """, unsafe_allow_html=True)

