
import streamlit as st
import base64
from pathlib import Path
from PIL import Image
import io

st.set_page_config(page_title="Sharing the beauty of Traditional Chinese gardens.", layout="wide")

# This is the final version webpage for COMP5415 Multimedia Design and Authoring


# Image loading helper
def load_image(image_path: str, max_width: int = 400, max_height: int = 200):
    """Load and resize image for display"""
    try:
        if not Path(image_path).exists():
            return None
        
        image = Image.open(image_path)
        
        # Calculate new size while maintaining aspect ratio
        original_width, original_height = image.size
        aspect_ratio = original_width / original_height
        
        if aspect_ratio > max_width / max_height:
            # Image is wider, fit to width
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:
            # Image is taller, fit to height
            new_height = max_height
            new_width = int(max_height * aspect_ratio)
        
        # Resize image
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Convert to base64 for HTML display
        buffer = io.BytesIO()
        resized_image.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        return f"data:image/png;base64,{img_str}"
    except Exception as e:
        st.error(f"Error loading image {image_path}: {str(e)}")
        return None

# Helpers 
def set_background(local_image_path: str, add_dark_overlay: bool = True, overlay_opacity: float = 0.45):
    """Injects CSS to set a full-screen background from a local image path.
    Optionally adds a dark overlay for readability of foreground text."""
    p = Path(local_image_path)
    if not p.exists():
        st.warning(f"Background image not found: {p}")
        return

    # Read file and base64-encode so it works in Streamlit CSS
    p = Path("bg.jpg")
    img_bytes = p.read_bytes()
    b64 = base64.b64encode(img_bytes).decode()

    # (Optional) adjust dark overlay 
    bg_css = f"""
        <style>
        /* App background */
        .stApp {{
            background: {'linear-gradient(rgba(0,0,0,' + str(overlay_opacity) + '), rgba(0,0,0,' + str(overlay_opacity) + ')), ' if add_dark_overlay else ''}
                        url("data:image/{p.suffix[1:]};base64,{b64}") center/cover no-repeat fixed;
        }}

        /* Make main block transparent so the background shows through */
        .stMainBlockContainer, .stApp > main {{
            background: transparent;
        }}

        /* Hide default Streamlit header/footer padding for a clean hero look */
        header, footer {{ visibility: hidden; height: 0; }}
        </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

# Apply background with fixed settings
set_background("bg.jpg", add_dark_overlay=True, overlay_opacity=0.45)



st.markdown("<div style='height: 30vh'></div>", unsafe_allow_html=True)  # top spacing - increased to move title down

# title block
fadein_css = """
<style>
@keyframes fadeInDown {
  0% {
    opacity: 0;
    transform: translateY(-40px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.hero-text {
  animation: fadeInDown 1.2s ease-out forwards;
}
</style>
"""
st.markdown(fadein_css, unsafe_allow_html=True)
hero_html = """
<div class="hero-text" style="text-align:center;">
    <h1 style="font-size: 4rem; line-height:1.1; margin: 0; color: #ffffff; font-weight:300;">
        Sharing the <span style="font-family: 'Georgia', serif; font-style: italic; font-weight:400;">beauty</span> of Chinese gardens.
    </h1>
    <h1 style="font-size: 4rem; line-height:1.1; margin: 0.1em 0 0; color: #ffffff; font-weight:300;">
        By   
        <span style="background-color: rgba(255,255,255,0.95); color: #2d5a27; padding: 0.1em 0.4em; border-radius: 0.3em; font-weight:800;">Multimedia</span> 
    </h1>
    <p style="color:#E9E9F5; max-width: 720px; margin: 1rem auto 0; font-size: 1.15rem;">
       COMP5415 Multimedia Design and Authorising
    </p>
</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)



# Five sections layout
st.markdown("<div style='height: 8vh'></div>", unsafe_allow_html=True)

# CSS for the new sections
section_css = """
<style>
.section-card {
    background: rgba(255,255,255,0.95);
    border-radius: 20px;
    padding: 24px;
    margin: 16px 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    height: 400px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-sizing: border-box;
}

.section-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.15);
}

.section-image {
    width: 100%;
    height: 150px;
    object-fit: contain;
    border-radius: 12px;
    margin-bottom: 16px;
    background-color: rgba(255,255,255,0.1);
    flex-shrink: 0;
}

.section-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #2d5a27;
    margin-bottom: 8px;
}

.section-description {
    font-size: 1rem;
    color: #4a7c59;
    line-height: 1.5;
}
</style>
"""
st.markdown(section_css, unsafe_allow_html=True)

# First row - 2 sections
col1, col2 = st.columns(2, gap="large")
with col1:
    DS_path = "design_idea.png"  
    DS_img = load_image(DS_path)
    st.markdown(f"""
    <div class="section-card">
        <img src="{DS_img}" class="section-image" alt="Idea">
        <h3 class="section-title">design Idea</h3>
        <p class="section-description">The project aims to express the aesthetic and philosophical essence of traditional Chinese culture through the design of a classical Chinese garden. By combining natural elements such as water, rocks, trees, lotus and architecture in a harmonious composition, the project seeks to recreate the peaceful and poetic atmosphere that characterizes Chinese gardens.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Load logo image
    logo_path = "logo.jpg"  
    logo_img = load_image(logo_path)
    
    if logo_img:
        st.markdown(f"""
        <div class="section-card">
            <img src="{logo_img}" class="section-image" alt="Logo">
            <h3 class="section-title">Logo</h3>
            <p class="section-description">The logo uses a silhouette to represent the structure of the pavilion, does not show specific materials or detailed construction, leaving space for imagination. The overall design remains simple and elegant.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="section-card">
            <h3 class="section-title">Logo</h3>
            <p class="section-description">The logo uses a silhouette to represent the structure of the pavilion, does not show specific materials or detailed construction, leaving space for imagination. The overall design remains simple and elegant.</p>
        </div>
        """, unsafe_allow_html=True)

# Second row - 2 sections  
col3, col4 = st.columns(2, gap="large")
with col3:
    # Load poster image
    poster_path = "poster.png"  
    poster_img = load_image(poster_path)
    
    if poster_img:
        st.markdown(f"""
        <div class="section-card">
            <img src="{poster_img}" class="section-image" alt="Poster">
            <h3 class="section-title">Poster</h3>
            <p class="section-description">Showing the main conponent in the traditional Chinese garden. Use vintage fonts to convey a sense of long-standing history.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="section-card">
            <h3 class="section-title">Poster</h3>
            <p class="section-description">Showing the main conponent in the traditional Chinese garden. Use vintage fonts to convey a sense of long-standing history.</p>
        </div>
        """, unsafe_allow_html=True)

with col4:
    # Load video
    video_path = "0001-1200.mp4"  
    video_exists = Path(video_path).exists() if video_path else False
    
    if video_exists:
        st.markdown(f"""
        <div class="section-card">
            <video width="100%" height="150px" controls preload="metadata" style="border-radius: 12px; margin-bottom: 16px; flex-shrink: 0;">
                <source src="{video_path}" type="video/mp4">
            </video>
            <h3 class="section-title">3D model and animation video</h3>
            <p class="section-description">Present the main outcomes through multimedia approaches in a video: 3D models, animation, and audio.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="section-card">
            <h3 class="section-title">3D model and animation video</h3>
            <p class="section-description">Present the main outcomes through multimedia approaches in a video: 3D models, animation, and audio.</p>
        </div>
        """, unsafe_allow_html=True)

# Third row - 1 section (centered)
col5, col6, col7 = st.columns([1, 2, 1])
with col6:
    st.markdown("""
    <div class="section-card">
        <h3 class="section-title">Dependencies</h3>
        <p class="section-description">Make sure you got the project folder and do not modify the file structure.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 10vh'></div>", unsafe_allow_html=True)


st.markdown(
    """
    <div style="position: fixed; bottom: 5px; right: 10px; font-size: 12px; color: white; opacity: 0.7;">
        Webpage developed by Yuqi Dong.
        
        Background image source: wallpaperaccess
    </div>
    """,
    unsafe_allow_html=True
)

