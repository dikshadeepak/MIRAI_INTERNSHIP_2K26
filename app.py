import streamlit as st


# Task 1: The UI Shell

st.title("Diksha's Signal Station")
st.write("Enter your name and message below, then click Transmit to send your message.")

# Task 2: Multi-Data Collection
user_name = st.text_input("Name")
user_message = st.text_input("Message")

# Task 3: The Action Gate
if st.button("Transmit"):

    # Task 4: Conditional Routing
    if user_name.strip() == "":
        st.error("Please provide your name.")

    elif user_message.strip() == "":
        st.warning("Please type a message to transmit.")

    # Task 5: Formatted Output
    else:
        st.success(
            f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}"
        )

        # Advanced Challenge
        total_characters = len(user_message)
        token_count = total_characters / 4

        st.info(
            f"System Check: Your message will consume approximately {token_count:.2f} tokens from our context window."
        )

        st.divider()
st.caption("Built with ❤️ using Streamlit")

