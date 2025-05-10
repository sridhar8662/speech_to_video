import streamlit as st

# App config
st.set_page_config(page_title="🎥 Text to Video Generator", page_icon="🎬")
st.title("🎥 Text to Video Generator")
st.markdown("Enter a scene description and view a sample video result.")

# Prompt input
prompt = st.text_input("Enter a prompt (e.g., 'a person playing with a ball')")

# Button to generate video
if st.button("Generate Video"):
    if prompt.strip():
        st.success("✅ Video generated successfully!")

        # Display a public sample video (no file needed)
        video_url = "https://www.w3schools.com/html/mov_bbb.mp4"  # Public demo video
        st.video(video_url)

        st.info("This is a placeholder video. For real generation, integrate with an AI API like RunwayML or Pika.")
    else:
        st.warning("⚠️ Please enter a prompt to generate a video.")
    