import requests
import streamlit as st

from api_client import ask_question


st.set_page_config(
    page_title="Smart RAG Document Assistant",
    page_icon="📚",
    layout="centered",
)

st.title("📚 Smart RAG Document Assistant")
st.caption(
    "Ask questions about the provided documents and get grounded answers "
    "with their sources."
)

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
question = st.chat_input(
    "Ask a question about the documents..."
)


if question:
    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Call backend
    with st.chat_message("assistant"):
        with st.spinner("Searching documents and generating answer..."):
            try:
                result = ask_question(question)

                answer = result.get(
                    "answer",
                    "No answer returned.",
                )

                sources = result.get("sources", [])

                st.markdown(answer)

                if sources:
                    st.markdown("### 📖 Sources")

                    for i, source in enumerate(sources, 1):
                        st.markdown(f"{i}. {source}")

                # Save assistant response
                assistant_content = answer

                if sources:
                    assistant_content += "\n\n### 📖 Sources\n"
                    assistant_content += "\n".join(
                        f"{i}. {source}"
                        for i, source in enumerate(sources, 1)
                    )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": assistant_content,
                    }
                )

            except requests.exceptions.ConnectionError:
                error_message = (
                    "❌ Cannot connect to the backend. "
                    "Make sure FastAPI is running on port 8000."
                )

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                    }
                )

            except requests.exceptions.Timeout:
                error_message = (
                    "⏳ The request took too long. "
                    "Please try again."
                )

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                    }
                )

            except requests.exceptions.HTTPError as e:
                error_message = (
                    f"❌ Backend returned an error: {e}"
                )

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                    }
                )

            except Exception as e:
                error_message = f"❌ Unexpected error: {e}"

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                    }
                )
