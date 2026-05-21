# Simple RAG retrieval service

# Example knowledge base for RAG retrieval
DOCUMENTS = [
    # Product documentation
    "FastAPI allows you to build APIs quickly with automatic OpenAPI documentation and async support.",
    "Groq's LLM API enables developers to generate text, answer questions, and build chatbots with high speed and reliability.",
    # Company FAQ
    "Our support team is available 24/7 via email and chat for all enterprise customers.",
    "To reset your password, click 'Forgot Password' on the login page and follow the instructions sent to your email.",
    # Technical knowledge
    "To connect FastAPI to a PostgreSQL database, use SQLAlchemy and configure the DATABASE_URL with your credentials.",
    "Groq supports models like llama3-8b-8192 and llama-3.1-8b-instant for various NLP tasks.",
    # Policies
    "Refunds are processed within 5-7 business days after approval.",
    "User data is encrypted at rest and in transit to ensure privacy and security.",
]


# Simple keyword-based retrieval: returns the first document containing any keyword from the question.
# For production, replace with a vector database or semantic search for better results.
def retrieve_context(question: str) -> str:
    """
    Retrieve relevant context from DOCUMENTS for the given question.
    Returns the first matching document or an empty string if none found.
    """
    for doc in DOCUMENTS:
        if any(word.lower() in doc.lower() for word in question.split()):
            return doc
    return ""
