import streamlit as st

def intro():
    st.write("🚀 Welcome, space explorer! I have a mission for you — and you're the hero!")
    name = st.text_input("What's your name, cadet?")
    if st.button("That's me, ready for launch!"):
        if name:
            st.session_state.character_name = name
            st.session_state.scene = "crash_landing"
            st.rerun()
        else:
            st.warning("Please enter your name first!")

def crash_landing():
    char = st.session_state.character_name
    st.write(f"""
        One quiet evening, {char} was stargazing from the backyard when a streak of light 
        blazed across the sky and crashed into the woods nearby with a BOOM!

        {char} crept through the trees and found a small silver spaceship, no bigger than a car, 
        sitting in a smouldering crater. A hatch popped open with a hiss of steam.

        Do you look inside?
        """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, peek inside!"):
            st.session_state.scene = "airlock_puzzle"
            st.rerun()
    with col2:
        if st.button("No, run home!"):
            st.session_state.scene = "went_home"
            st.rerun()

def went_home():
    char = st.session_state.character_name
    st.write(f"""
        {char} backed away slowly and ran all the way home.

        The next morning, {char} went back to the woods but the crater was gone, the trees were 
        unscorched, and there was no trace of the spaceship.

        Had it all been a dream?

        Do you want to tell your mum and go back to search more carefully?
        """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Tell mum and go search!"):
            st.session_state.scene = "airlock_puzzle"
            st.rerun()
    with col2:
        if st.button("Decide it was a dream and watch TV"):
            st.session_state.scene = "watched_tv"
            st.rerun()

def watched_tv():
    st.write("""
        You watched TV until dinner, had a bath, and went to bed.

        THE END
        """)

def airlock_puzzle():
    char = st.session_state.character_name
    st.write(f"""
        {char} peered into the hatch. Inside was a tiny cockpit covered in blinking lights 
        and star maps. A small robot with big round eyes looked up at {char}.

        "GREETINGS EARTHLING. I AM BEEP-7. MY SHIP IS DAMAGED. I NEED A MATH-CAPABLE HUMAN
        TO HELP ME RECALIBRATE THE HYPERDRIVE."

        "To open the inner airlock," Beep-7 said, "solve this:"
        """)
    st.latex(r"5 \times 6 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="airlock")
    if st.button("Confirm"):
        if answer == 30:
            st.session_state.scene = "meet_crew"
            st.rerun()
        else:
            st.error("The airlock buzzes. INCORRECT CALCULATION. Try again.")

def meet_crew():
    char = st.session_state.character_name
    st.write(f"""
        The inner airlock slid open and {char} climbed in.

        Inside, two more robots were sparking and whirring.

        "This is ZORP-3 and NOVA-9," said Beep-7. "We crashed because a space pirate named 
        Captain Grox stole our Navigation Crystal. Without it we can never fly home."

        "We tracked Captain Grox to this planet," ZORP-3 beeped. "He is hiding in an old 
        lighthouse on the cliffs."

        "But first," said NOVA-9, "we need to repair the thrusters. {char}, can you help?"

        Which job do you tackle first?
        """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Fix the left thruster"):
            st.session_state.scene = "left_thruster"
            st.rerun()
    with col2:
        if st.button("Fix the right thruster"):
            st.session_state.scene = "right_thruster"
            st.rerun()

def left_thruster():
    char = st.session_state.character_name
    st.write(f"""
        {char} crawled into the left thruster compartment. It was full of tangled wires 
        and a cracked fuel cell.

        ZORP-3 handed {char} a glowing wrench. "To seal the fuel cell you need to enter 
        the correct pressure code:"
        """)
    st.latex(r"5 \times 8 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="left_thrust")
    if st.button("Confirm"):
        if answer == 40:
            st.session_state.scene = "left_thruster_2"
            st.rerun()
        else:
            st.session_state.scene = "loss_1"
            st.rerun()

def left_thruster_2():
    char = st.session_state.character_name
    st.write(f"""
        The fuel cell sealed with a satisfying CLUNK.

        "THRUSTER REPAIRED," ZORP-3 beeped happily. "You are a true math engineer, {char}!"

        Have you fixed the right thruster yet?
        """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Not yet — go fix the right thruster"):
            st.session_state.scene = "right_thruster"
            st.rerun()
    with col2:
        if st.button("Yes, both done — head to the lighthouse!"):
            st.session_state.scene = "lighthouse_gate"
            st.rerun()

def right_thruster():
    char = st.session_state.character_name
    st.write(f"""
        The right thruster had a loose plasma coil. Beep-7 explained that to re-magnetise 
        it, {char} needed to dial in the exact frequency:
        """)
    st.latex(r"5 \times 3 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="right_thrust")
    if st.button("Confirm"):
        if answer == 15:
            st.session_state.scene = "right_thruster_2"
            st.rerun()
        else:
            st.session_state.scene = "loss_2"
            st.rerun()

def right_thruster_2():
    char = st.session_state.character_name
    st.write(f"""
        The coil hummed back to life with a blue glow.

        "PLASMA COIL STABILISED," NOVA-9 chimed. "Excellent work, {char}!"

        Have you fixed the left thruster yet?
        """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Not yet — fix the left thruster"):
            st.session_state.scene = "left_thruster"
            st.rerun()
    with col2:
        if st.button("Yes, both done — head to the lighthouse!"):
            st.session_state.scene = "lighthouse_gate"
            st.rerun()

def loss_1():
    st.write("""
        The fuel cell exploded with a pop of purple smoke, knocking {char} out of the ship.
        
        By the time {char} recovered, the spaceship had sealed itself shut for emergency repairs 
        and the robots were nowhere to be seen.

        THE END
        """)

def loss_2():
    st.write("""
        The plasma coil overloaded and flung {char} across the woods with a spectacular ZAP.
        
        {char} landed in a bush, unharmed but very confused, and the spaceship door 
        slammed shut.

        THE END
        """)

def lighthouse_gate():
    char = st.session_state.character_name
    st.write(f"""
        With the ship repaired, {char} and the three robots set off across the cliffs toward 
        the old lighthouse. 

        At the lighthouse gate, a rusty automated security system creaked to life.

        "INTRUDER ALERT. SOLVE TO ENTER:"
        """)
    st.latex(r"5 \times 11 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="gate")
    if st.button("Confirm"):
        if answer == 55:
            st.session_state.scene = "lighthouse_inside"
            st.rerun()
        else:
            st.error("WRONG. ALARM SOUNDING. Try again!")

def lighthouse_inside():
    char = st.session_state.character_name
    st.write(f"""
        The gate groaned open and they slipped inside the lighthouse.

        At the top of the spiral staircase they found Captain Grox — a squat alien with 
        three eyes and a very pointy hat — sitting on a pile of stolen gadgets.

        He spotted them and leapt to his feet. "How did you get past my gate?!"

        "We're here for the Navigation Crystal," Beep-7 said firmly.

        Captain Grox laughed. "You'll never have it back unless someone here can answer—"
        """)
    st.latex(r"5 \times 9 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="grox1")
    if st.button("Confirm"):
        if answer == 45:
            st.session_state.scene = "grox_battle"
            st.rerun()
        else:
            st.session_state.scene = "loss_3"
            st.rerun()

def loss_3():
    st.write("""f
        Captain Grox cackled and pressed a trapdoor button. {char} and all three robots 
        tumbled down a chute and landed in a heap on the cliffs outside.

        By the time they climbed back up, the lighthouse was empty. Captain Grox had escaped.

        THE END
        """)

def grox_battle():
    char = st.session_state.character_name
    st.write(f"""
        Captain Grox looked furious. "Impossible! Fine — one more question. If you fail, 
        I keep the Crystal AND your robot friends!"

        NOVA-9 whispered to {char}: "Remember — math is our only weapon against him!"
        """)
    st.latex(r"5 \times 7 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="grox2")
    if st.button("Confirm"):
        if answer == 35:
            st.session_state.scene = "grox_final"
            st.rerun()
        else:
            st.session_state.scene = "loss_4"
            st.rerun()

def loss_4():
    char = st.session_state.character_name
    st.write(f"""
        Captain Grox snatched the robots' power packs and dumped {char} outside in the fog.
        
        {char} trudged home alone. The night sky seemed emptier than before.

        THE END
        """)

def grox_final():
    char = st.session_state.character_name
    st.write(f"""
        Each correct answer zapped Captain Grox with a beam of pure math energy!
        
        He backed against the window. "Ow! Stop! I— I give up!"
        
        "Then give us the Crystal," {char} said.
        
        Captain Grox reached into his pointy hat and pulled out a glowing purple crystal.
        
        "Last chance," ZORP-3 said to {char}. "Finish him off with the final calculation!"
        """)
    st.latex(r"5 \times 12 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="grox_final")
    if st.button("Confirm"):
        if answer == 60:
            st.session_state.scene = "victory"
            st.rerun()
        else:
            st.session_state.scene = "loss_4"
            st.rerun()

def victory():
    char = st.session_state.character_name
    st.balloons()
    st.write(f"""
        ✨ BOOM! ✨

        A blinding flash filled the lighthouse. When it cleared, Captain Grox was gone —
        teleported to the Intergalactic Prison for Space Pirates.
        
        Beep-7 held up the Navigation Crystal. "WE ARE GOING HOME, THANKS TO {char.upper()}!"
        
        The robots cheered (in beeps and whirrs) and Beep-7 gave {char} a small silver badge 
        shaped like a star.
        
        "Honorary Crew Member of the Starship Beep-7," NOVA-9 announced proudly.
        
        That night, {char} watched the little silver spaceship streak back up into the stars,
        brighter than any comet.
        
        THE END 🌟
        """)
