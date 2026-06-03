# Models in LangChain

Models are one of the core components of LangChain, enabling applications to interact with **Language Models** and **Embedding Models**.

## Types of Models

### 1. Language Models

Language Models are used to generate, understand, and process natural language.

They are further divided into:

* **LLMs (Large Language Models)**
* **Chat Models**

Both LLMs and Chat Models can be:

* **Closed Source Models** (OpenAI, Claude, Gemini, etc.)
* **Open Source Models** (Llama, Mistral, GPT-J, BLOOM, etc.)

### 2. Embedding Models

Embedding Models convert text into numerical vector representations for tasks such as semantic search, retrieval, clustering, and recommendation systems.

Embedding Models can also be:

* **Closed Source Models** (OpenAI Embeddings, Gemini Embeddings, etc.)
* **Open Source Models** (Sentence Transformers, BGE, E5, Instructor Embeddings, etc.)

---

## Closed Source Models

These models are accessed through APIs provided by vendors.

**Examples:** OpenAI, Anthropic Claude, Google Gemini

These providers offer language models, chat models, and embedding models that can be integrated into LangChain applications.

---

## Open Source Models

Open source models are commonly available through **Hugging Face** and can be run locally or accessed through the Hugging Face Inference API.

**Popular Models:** Llama, Mistral, GPT-J, BLOOM

### Advantages

* Free to use with no API costs
* Supports model customization and fine-tuning
* Greater control over deployment and infrastructure
* Better data privacy through local execution
* Can be deployed on-premises or in the cloud

### Disadvantages

* High hardware requirements, especially GPUs
* More complex setup involving PyTorch, CUDA, and Transformers
* Generally less RLHF optimization compared to leading proprietary models
* Limited multimodal capabilities in many models

---

# LLMs vs Chat Models

## LLMs (Large Language Models)

LLMs are designed for raw or free-form text generation based on a given prompt.

**Common Use Cases:** Text generation, summarization, translation, question answering, content creation

**Examples:** GPT-3, Llama 2 7B, Mistral 7B

### Characteristics

* Accept plain text as input and generate plain text as output
* No built-in conversation memory
* Do not inherently understand roles such as *system*, *user*, or *assistant*

---

## Chat Models

Chat Models are specialized language models optimized for conversational interactions.

**Common Use Cases:** Chatbots, virtual assistants, AI tutors, customer support systems

**Examples:** GPT-4, Claude, Gemini, Llama 2 Chat

### Characteristics

* Support structured conversations and message history
* Understand roles such as *system*, *user*, and *assistant*
* Optimized for multi-turn conversations and dialogue-based applications

---

This folder contains my notes, experiments, and code examples related to Language Models, Chat Models, and Embedding Models in LangChain.
