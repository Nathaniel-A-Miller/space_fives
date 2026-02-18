import streamlit as st
import scenes

st.title("🚀 The Robots of Destiny")

# Initialize state
if "scene" not in st.session_state:
    st.session_state.scene = "intro"
if "character_name" not in st.session_state:
    st.session_state.character_name = ""

# Map scene names to functions
SCENES = {
    "intro": scenes.intro,
    "crash_landing": scenes.crash_landing,
    "went_home": scenes.went_home,
    "watched_tv": scenes.watched_tv,
    "airlock_puzzle": scenes.airlock_puzzle,
    "meet_crew": scenes.meet_crew,
    "left_thruster": scenes.left_thruster,
    "left_thruster_2": scenes.left_thruster_2,
    "right_thruster": scenes.right_thruster,
    "right_thruster_2": scenes.right_thruster_2,
    "loss_1": scenes.loss_1,
    "loss_2": scenes.loss_2,
    "lighthouse_gate": scenes.lighthouse_gate,
    "lighthouse_inside": scenes.lighthouse_inside,
    "loss_3": scenes.loss_3,
    "grox_battle": scenes.grox_battle,
    "loss_4": scenes.loss_4,
    "grox_final": scenes.grox_final,
    "victory": scenes.victory,
}

# Run the current scene
current_scene_name = st.session_state.scene
SCENES[current_scene_name]()
