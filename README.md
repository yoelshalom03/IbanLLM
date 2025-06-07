# IbanLLM
This project aims to develop a lightweight language model for the Iban language, focused initially on chatbot applications in the education sector. The long-term goal is to create a fully fine-tuned local LLM capable of understanding and generating Iban text fluently.
# Project Structure
IbanLLM/
├── data/
│   ├── raw/                   # Unprocessed corpus (lyrics, essays, scraped files)
│   ├── cleaned/               # Cleaned corpus after filtering
│   └── tokenizer/             # Tokenizer model files (vocab, model)
├── notebooks/                 # Jupyter notebooks for exploration, testing
├── scripts/
│   ├── scrape.py              # Web scraper for Iban text sources
│   ├── clean_corpus.py        # Text cleaning logic
│   └── train_tokenizer.py     # SentencePiece training code
├── models/
│   ├── mistral_adapter/       # Fine-tuned adapters (e.g., QLoRA)
│   └── checkpoints/           # Model checkpoints
├── outputs/                   # Generated text results for evaluation
├── README.md
└── requirements.txt
# Objectives
Build a custom tokenizer using SentencePiece for Iban.
Scrape and clean Iban corpus data (lyrics, essays, Wikipedia, etc.).
Fine-tune Mistral 7B or smaller models with Iban tokenizer using QLoRA or similar.
Create a chatbot demo for educational pilot projects.
Prepare for institutional deployment and government grant proposals.
# Tech Stack
Python 3.10+                                                  
Hugging Face Transformers
SentencePiece
PyTorch (w/ ROCm or CUDA)
Ubuntu 24.04.2 LTS (for local fine-tuning)
Git + GitHub (for collaboration)
# Contributors
Yoel Anding – Project Lead,Data Management,Corpus Developer
Ismail Nuqman – Collaborator,Devops,Backend
# License
TBD — for now, Private Repository for internal development. Public release after stabilization and fine-tuning.
# Sample Prompt
Prompt: ngintu pengawa ti meri kitai semengat
Output: [repetitive output due to unfine-tuned base]
