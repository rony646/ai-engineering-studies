# AI Engineering Studies

Notes and small programs from my AI engineering studies. The work moves from a local transformer, through the OpenAI API, to local apps with Ollama. The code lives in `source/`.

## What I practiced

**Local generation.** `source/intro_transformers.py` and `source/intro_transfomer_enhanced.py` load `distilgpt2` with Hugging Face `transformers` and generate text on the machine. That is where tokenization, weights, and sampling show up.

**The OpenAI API.** `source/openai-simple.py` sends a chat completion to `gpt-4o-mini`. `source/prompts.py` compares prompting styles: few-shot, direct, chain of thought, instructional, and role-play. The role-play example turns the model's text into a real PDF.

**Memory and logs.** `source/context_memory/no_memory.py` sends each turn alone. `source/context_memory/ctx_memory.py` keeps the message list and can talk to OpenAI or to a local Ollama server. `source/logging/chatbot_logging.py` writes each session to a JSON log.

**Local models with Ollama.** The `source/ollama/` folder runs `llama3.2` on this computer:

- `start-1.py` and `start-2.py` call the local API and stream a reply
- `Modelfile` defines a custom assistant
- `categorizer.py` sorts a grocery list
- `function-calling.py` lets the model call Python functions
- `pdf-rag.py`, `pdf-rag-clean.py`, and `pdf-rag-streamlit.py` chunk a PDF, embed it, and answer from those chunks
- `final-rag-voice.py` adds a spoken interface on top of that retrieval flow

## Setup

```bash
cd source
python3 -m venv venv
source venv/bin/activate
pip install transformers torch openai python-dotenv fpdf2 ollama langchain langchain-community langchain-ollama langchain-text-splitters chromadb streamlit
```

API scripts read `OPENAI_API_KEY` from a `.env` file in `source/`. Do not commit that file.

Ollama scripts need the [Ollama](https://ollama.com) app and the models they name, for example:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

Run a script from `source/`, with the virtual environment active:

```bash
python intro_transformers.py
python prompts.py
python ollama/start-2.py
```
