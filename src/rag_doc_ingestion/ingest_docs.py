import logging
import chromadb

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

from src.rag_doc_ingestion.config.doc_ingestion_settings import DocIngestionSettings


# ---------------- logging ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ---------------- settings ----------------
settings = DocIngestionSettings()

# ---------------- embedding model ----------------
logger.info("Loading HuggingFace embedding model...")
embed_model = HuggingFaceEmbedding()


def build_vector_store_from_documents():
    logger.info("Starting vector store ingestion process...")

    try:
        docs_dir_path = settings.DOCUMENTS_DIR
        vector_store_path = settings.VECTOR_STORE_DIR
        collection_name = settings.COLLECTION_NAME

        # ---------------- load documents ----------------
        logger.info(f"Loading documents from: {docs_dir_path}")
        documents = SimpleDirectoryReader(input_dir=docs_dir_path).load_data()

        # ---------------- chunking ----------------
        logger.info("Chunking documents...")
        parser = SentenceSplitter(chunk_size=1024, chunk_overlap=50)
        nodes = parser.get_nodes_from_documents(documents)

        logger.info(f"Created {len(nodes)} nodes")

        # ---------------- chroma DB ----------------
        logger.info(f"Initializing ChromaDB at: {vector_store_path}")
        db = chromadb.PersistentClient(path=vector_store_path)

        chroma_collection = db.get_or_create_collection(collection_name)

        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

        storage_context = StorageContext.from_defaults(
            vector_store=vector_store
        )

        # ---------------- build index ----------------
        logger.info("Building vector index...")

        index = VectorStoreIndex(
            nodes,
            storage_context=storage_context,
            embed_model=embed_model
        )

        logger.info("Vector store built successfully.")

        return 0

    except Exception as e:
        logger.exception(f"Error during vector store build: {e}")
        return 1


if __name__ == "__main__":
    build_vector_store_from_documents()





