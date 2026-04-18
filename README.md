# 🤖 n8n AI Personal Assistant

A fully automated, AI-powered personal assistant built with **n8n**, connected to your Google Workspace and powered by **Groq (LLaMA 3.3 70B)**. Interact via a **Streamlit** frontend — just type your request and the assistant handles the rest.

---

## ✨ Features

| Capability | Tools |
|---|---|
| 📧 Gmail | Read single/multiple emails, send emails |
| 📅 Google Calendar | Create events, get events, get single event |
| ✅ Google Tasks | Create, get single, get multiple, delete tasks |
| 📝 Google Docs (Notes) | Create notes file, update notes, get notes |
| 💰 Expense Tracking | Add expense, get expenses (Google Sheets) |
| 🔍 Web Search | SerpAPI live search when info not in memory |
| 🧠 Memory | Simple memory for context across conversation |

---

## 🏗️ Architecture

```
User (Streamlit UI)
        ↓
   Webhook (n8n)
        ↓
   Main AI Agent  ←→  Groq LLaMA 3.3 70B
        ↓
  ┌─────┬──────┬──────┬──────┬──────┬──────┐
Gmail  Calendar Tasks  Docs  Sheets Search
```

---

## 🛠️ Tech Stack

- **Workflow Engine** — [n8n](https://n8n.io) (self-hosted via Docker)
- **AI Model** — Groq `llama-3.3-70b-versatile`
- **Frontend** — Streamlit
- **APIs** — Gmail, Google Calendar, Google Tasks, Google Docs, Google Sheets, SerpAPI

---

## 🚀 Setup & Run

### 1. Prerequisites
- Docker installed
- n8n self-hosted running locally
- Google Cloud project with OAuth credentials
- Groq API key
- SerpAPI key

### 2. Start n8n with Docker

```bash
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```

Open → `http://localhost:5678`

### 3. Import Workflow

1. In n8n, go to **Workflows → Import**
2. Upload `Personal Assistant workflow.json`
3. Set up your credentials (Google OAuth, Groq, SerpAPI)
4. **Activate** the workflow

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment

Create a `.env` file:

```env
N8N_WEBHOOK_URL=http://localhost:5678/webhook/your-webhook-id
```

### 6. Run the Frontend

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
n8n-personal-assistant/
├── Personal Assistant workflow.json  # n8n workflow export
├── app.py                            # Streamlit frontend
├── main.py                           # Core logic
├── index.html                        # HTML frontend (alternative)
├── requirements.txt                  # Python dependencies
├── pyproject.toml                    # Project config
├── test_webhook.py                   # Webhook testing script
└── README.md
```

---

## 💡 How It Works

1. You type a message in the Streamlit UI
2. It hits the **n8n webhook**
3. The **AI Agent** (Groq LLaMA 3.3 70B) understands your intent
4. It calls the right tool — Gmail, Calendar, Tasks, Docs, Sheets, or Search
5. Response comes back to the UI

The agent uses **Simple Memory** to maintain context within a session.

---

## 📌 Example Prompts

```
"Send an email to john@example.com about tomorrow's meeting"
"What's on my calendar this week?"
"Create a task: Review project proposal by Friday"
"Add expense: Lunch $12"
"Search for latest AI news"
"Create a note titled 'Ideas' with my project thoughts"
```

---

## 🔐 Credentials Required

- Google OAuth 2.0 (Gmail, Calendar, Tasks, Docs, Sheets)
- [Groq API Key](https://console.groq.com)
- [SerpAPI Key](https://serpapi.com)

All credentials are stored securely inside n8n — never hardcoded.

---

## 👤 Author

**Abdul Moeez**  
BS Artificial Intelligence  
[GitHub](https://github.com/Abdulmoeez1010)

---

## 📄 License

MIT License — free to use and modify.
