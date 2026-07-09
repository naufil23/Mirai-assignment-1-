import streamlit as st

# -----------------------------
# Task 1: The UI Shell
# -----------------------------
st.title("The Identity Echo Interface")

st.write(
    "Welcome! Please enter your name and message, then click the Transmit button."
)

# -----------------------------
# Task 2: Multi-Data Collection
# -----------------------------
user_name = st.text_input("Enter your Name")

user_message = st.text_input("Enter your Message")

# -----------------------------
# Task 3: The Action Gate
# -----------------------------
if st.button("Transmit"):

    # -----------------------------
    # Task 4: Conditional Routing
    # -----------------------------
    if user_name.strip() == "":
        st.error("Please provide your name.")

    elif user_message.strip() == "":
        st.warning("Please type a message to transmit.")

    # -----------------------------
    # Task 5: Formatted Output
    # -----------------------------
    else:
        st.success(
            f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}"
        )

        # -----------------------------
        # Advanced Challenge
        # -----------------------------
        total_characters = len(user_message)
        token_count = round(total_characters / 4, 2)

        st.info(
            f"System Check: Your message will consume approximately {token_count} tokens from our context window."
        )
        