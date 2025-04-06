# SaathiAI – A Compassionate GenAI Companion for the Elderly

**SaathiAI** is a voice-first, multi-agent AI system designed to help elderly individuals fight **loneliness**, manage their **daily routines**, and stay **connected to their loved ones**.  
Built with empathy, simplicity, and accessibility in mind, SaathiAI uses Generative AI to provide **conversational companionship**, **health and safety monitoring**, and **caregiver updates** — all through an intuitive interface.

---

## 🌟 Problem Statement

Loneliness is one of the biggest epidemics among the elderly. With the rise of nuclear families, many seniors feel isolated and struggle with complex technologies meant to support them.

**SaathiAI** aims to:
- Provide emotional companionship using AI-powered conversations
- Simplify daily tasks like reminders and health tracking
- Keep families connected through updates and summaries
- Make technology less intimidating, with voice-first and multilingual support (future scope)

---

## 🧠 Multi-Agent System Design

| Agent              | Role                                                                 |
|--------------------|----------------------------------------------------------------------|
| Companion Agent    | Friendly conversations, memory prompts, emotional check-ins         |
| Reminder Agent     | Voice-based reminders for medication, appointments, and routines    |
| Health Monitor     | Monitors sensor data (e.g., heart rate) and detects anomalies       |
| Safety Agent       | Detects inactivity or falls and triggers emergency alerts           |
| Caregiver Agent    | Shares summaries and alerts with family or healthcare providers     |
| Language Agent     | (Future) Translates interactions to Indian regional languages       |

---

## 🔧 Technologies Used

- Ollama + Local LLMs (e.g., Mistral, Phi-2)
- LangChain / AutoGen for agent coordination
- Vosk for offline speech-to-text
- Coqui TTS / pyttsx3 for voice responses
- SQLite for local memory and reminders
- Streamlit / Flask for caregiver dashboard
- Python, FastAPI

---

## 📂 Project Structure

SaathiAI-genai-elderly-care/ ├── agents/ ├── services/ ├── ui/ ├── utils/ ├── main.py ├── requirements.txt └── README.md

yaml
Copy
Edit

---

## 🚀 How to Run

```bash
git clone https://github.com/Smritiprem22/SaathiAI-genai-elderly-care.git
cd SaathiAI-genai-elderly-care
pip install -r requirements.txt
python main.py
