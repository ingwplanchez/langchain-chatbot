# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

- Run the application: `streamlit run app.py`

## Architecture & Structure

- **Entry Point**: `streamlit_chatbot.py` contains the entire application (UI, logic, and LLM configuration).
- **LLM Orchestration**: Uses LangChain Expression Language (LCEL) to chain a `PromptTemplate` with `ChatGoogleGenerativeAI`.
- **State Management**: Conversation history is stored in `st.session_state.mensajes` as a list of LangChain message objects (`HumanMessage`, `AIMessage`).
- **Infrastructure**:
    - API Key: Loaded via `python-dotenv` from `.env` (`GOOGLE_API_KEY`).
    - Model: Google Gemini (Flash family).
    - UI: Streamlit with a sidebar for hyperparameter tuning (temperature, model selection).
