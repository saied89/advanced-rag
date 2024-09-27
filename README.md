# Mastering Large Language Models (LLM) with Retrieval Augmented Generation (RAG)

This repository includes a set of assets that are used in the above course, which dives
deeper into the various problems and solutions when building a RAG system in enterprise environments.


## Common Problems in RAG Systems and Their Solutions

1. **Long Documents**
   - Problem: Difficulty in processing and retrieving information from lengthy documents.
   - Solution: Chunking options
     - Sentence-based chunking
     - Paragraph-based chunking
     - Fixed-size chunking with overlap

2. **Mismatch Between Questions and Document Formats**
   - Problem: User queries may not align with the way information is structured in documents.
   - Solutions:
     - Hypothetical Document Embeddings (HyDE)
     - Reverse HyDE

3. **Domain-Specific Jargon**
   - Problem: General LLMs may struggle with specialized vocabulary.
   - Solutions:
     - Fine-tuning on domain-specific corpora
     - Incorporating domain-specific embeddings

4. **Contextual Relevance**
   - Problem: Retrieved passages may lack broader context.
   - Solutions:
     - Hierarchical retrieval (e.g., parent-child chunks)
     - Multi-vector retrieval

5. **Query Ambiguity**
   - Problem: Vague or broad user queries leading to irrelevant results.
   - Solutions:
     - Query expansion techniques
     - Interactive clarification prompts

6. **Handling Numerical Data and Tables**
   - Problem: Difficulty in retrieving and reasoning with structured data.
   - Solutions:
     - Table-specific embeddings
     - Hybrid retrieval combining text and structured data

7. **Temporal Relevance**
   - Problem: Outdated information in retrieved passages.
   - Solutions:
     - Time-aware retrieval mechanisms
     - Regular content updates and re-indexing

8. **Multi-lingual Support**
   - Problem: Dealing with documents and queries in multiple languages.
   - Solutions:
     - Cross-lingual embeddings
     - Language-specific fine-tuning

9. **Bias and Fairness**
   - Problem: Potential amplification of biases present in the corpus.
   - Solutions:
     - Diverse and representative document collections
     - Bias detection and mitigation techniques in retrieval

10. **Scalability and Performance**
    - Problem: Maintaining efficiency with large document collections.
    - Solutions:
      - Optimized vector databases
      - Approximate Nearest Neighbor (ANN) search algorithms

