FROM python:3.11-slim

WORKDIR /app

# Install system dependeencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install \
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ src/
COPY data_dir/ data_dir
COPY steps.txt ./
COPY start.sh ./start.sh

# Make start.sh executable
RUN chmod +x start.sh

# Expose backend and frontend variables
EXPOSE 8000 8501

# Set environemnt variables (can be overridden at runtime)
ENV DOCUMENTS_DIR="/app/data_dir"
ENV VECTOR_STORE_DIR="/app/doc_vector_store"
ENV COLLECTION_NAME="document_collection"
ENV MODEL_NAME="llama-3.3-70b-versatile"
ENV MODEL_TEMPERATURE=0.0
ENV CHAT_ENDPOINT_URL="http://localhost:8000/chat/answer"

# Run all services using start.sh
CMD ["/app/start.sh"]




