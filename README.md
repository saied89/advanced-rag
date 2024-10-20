# Mastering Large Language Models (LLM) with Retrieval Augmented Generation (RAG)

This repository includes a set of assets that are used in the above course, which dives
deeper into the various problems and solutions when building a RAG system in enterprise environments.

## Simple RAG Flow

![Naive RAG](images/Naiive_RAG.png)

## Jupyter Notebooks

1. [Simple RAG](01_simple_rag.ipynb): This notebook introduces the fundamental concepts and implementation of Retrieval Augmented Generation (RAG).
2. [Embedding Model](02_embedding_model.ipynb): This notebook examines the role of embedding models in RAG systems, including their applications and limitations.
3. [Semantic Chunking](03_semantic_chunking.ipynb): This notebook investigates the process of semantic chunking in RAG systems, focusing on its significance in information retrieval.
4. [Reverse Hyde](04_reverse_hyde.ipynb): This notebook explores the Reverse Hyde technique in RAG systems, highlighting its importance in addressing contextual relevance and query ambiguity.
5. [Contextual Retrieval](05_contextual_retrieval.ipynb): This notebook delves into the strategies for contextual retrieval in RAG systems, emphasizing the effective handling of numerical data and tables.
6. [Hybrid Search](06_hybrid_search.ipynb): This notebook discusses the integration of hybrid search capabilities in RAG systems, encompassing both temporal relevance and multi-lingual support.
7. [Multi Modal Retrieval](07_multimodal_pdf.ipynb): This notebook explore the possibilities of retrieval from images and not limited to text. 

## Common Problems in RAG Systems and Their Solutions

The problematic part of a RAG application is usually the retrieval part. The system might retrieve the wrong documents, or only part of them and lead to wrong replies. This is the classical problem in machine learning of the precision-recall-tradeoff.

![Recall Precision Tradeoff](images/Recall_Precision_in_RAG_Diagram.png)

The following list of complexity factors in real-life documents can lead to a decrease in overall retrieval accuracy, and the various techniques that can improve the retrieval performance. 

1. **Long Documents**
  - Problem: Difficulty in processing and retrieving information from lengthy documents.
  - Solutions: 
    - Chunking options
      - Sentence-based chunking
      - Paragraph-based chunking
      - Fixed-size chunking with overlap
      - Statistical chunking (see: [03_semantic_chunking.ipynb](03_semantic_chunking.ipynb))
    - Hierarchical retrieval (e.g., parent-child chunks)
    - Contextual retrieval (see: [05_contextual_retrieval.ipynb](05_contextual_retrieval.ipynb))

2. **Mismatch Between Questions and Document Formats**
   - Problem: User queries may not align with the way information is structured in documents.
   - Solutions:
     - Hypothetical Document Embeddings (HyDE)
     - Reverse HyDE (see: [04_reverse_hyde.ipynb](04_reverse_hyde.ipynb))

3. **Domain-Specific Jargon**
   - Problem: General LLMs may struggle with specialized vocabulary.
   - Solutions:
     - Incorporating domain-specific embeddings (see: [02_embedding_model.ipynb](02_embedding_model.ipynb))
     - Hybrid Search (see: [06_hybrid_search.ipynb](06_hybrid_search.ipynb))
     - Fine-tuning on domain-specific corpora

4. **Complex Documents**
   - Problem: Handling documents with complex structures, such as scanned documents, which can be challenging for traditional text-based retrieval methods.
   - Solutions:
     - Multi-modal retrieval (see: [07_multimodal_pdf.ipynb](07_multimodal_pdf.ipynb))
       - Utilizing computer vision techniques to extract information from images and other non-textual elements within documents.
       - Integrating this information with text-based retrieval methods for a more comprehensive search capability.

## Advanced RAG System

![Advanced RAG](images/Advanced_RAG.png)

## Set Up

   To set up the project, you have two options: using `uv` or traditional `pip`.

   **Using [`uv`](https://github.com/astral-sh/uv)**

  1. Install `uv` by running `pip install uv`.
  2. Create a virtual environment using `uv venv --python 3.12.0`.
  3. Activate the virtual environment.
  4. Compile the project dependencies using `uv pip compile requirements.in --output-file requirements.txt`.
  5. Sync the dependencies using `uv pip sync requirements.txt`.

   **Using traditional `pip`**

  1. Create a virtual environment using your preferred method (e.g., `python -m venv myenv`).
  2. Activate the virtual environment.
  3. Install the project dependencies using `pip install -r requirements.txt`.

   Note: The `uv` method is recommended for its speed, ease of use and management of project dependencies. However, the traditional `pip` method is also supported for those familiar with it.
