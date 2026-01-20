---

🚀 Study Planner AI Agent

A Full-Stack Generative AI Application using Pydantic AI

> An intelligent AI agent that generates personalized, structured study plans based on user goals, time availability, and duration — built with Pydantic AI, FastAPI, and a free OpenRouter model.




---

✨ Key Highlights

🤖 Generative AI Agent built using Pydantic AI

📐 Strongly typed & validated outputs using Pydantic schemas

⚡ FastAPI backend with clean, production-ready APIs

🌐 Live public deployment (Cloudflare Tunnel for demo)

🎯 Clear real-world use case with practical value

🔐 Secure API key handling using environment variables

🧩 Modular, clean, and readable codebase



---

🧠 Problem Statement

Students often struggle to create realistic and balanced study plans that fit their daily schedules and goals.

This project solves that by:

Understanding a user’s goal

Considering hours per day and total duration

Generating a structured day-wise plan with actionable tasks



---

🛠️ Tech Stack

Layer	Technology

Backend	FastAPI
AI Agent	Pydantic AI
LLM Provider	OpenRouter (Free Model)
Model	Mistral 7B Instruct
Validation	Pydantic
Deployment (Demo)	Google Colab + Cloudflare Tunnel



---

🧩 Architecture Overview

Client / Swagger UI
        |
        v
FastAPI Backend
        |
        v
Pydantic AI Agent
        |
        v
OpenRouter (Mistral 7B)

The agent enforces strict JSON output

Responses are validated before returning to the client

Errors are handled gracefully at the API layer



---

📥 API Usage

Endpoint

POST /generate-plan

Request Body

{
  "goal": "Prepare for ML internship interviews",
  "hours_per_day": 4,
  "duration_days": 7
}

Sample Response

{
  "summary": "A focused 7-day plan to strengthen ML fundamentals and interview readiness.",
  "daily_plan": [
    {
      "day": 1,
      "tasks": [
        "Revise Python basics",
        "Review linear algebra essentials"
      ]
    }
  ]
}


---

🔒 Security & Best Practices

❌ No API keys hardcoded

✅ Keys managed via environment variables

✅ OpenAI-compatible routing via OPENAI_API_BASE

✅ Strict schema validation to prevent malformed AI outputs



---

🧪 Validation & Reliability

Structured outputs enforced at the agent level

Backend only returns validated JSON

Prevents hallucinated or malformed responses

Clear separation of concerns (agent, API, schemas)



---

🚀 Deployment Notes

The backend was developed and tested in Google Colab

Exposed publicly using Cloudflare Tunnel for live evaluation

Easily deployable to:

Render

Railway

Fly.io

Any FastAPI-compatible hosting platform




---

📌 Assignment Alignment

✔ Live deployed application
✔ Full stack implementation
✔ Pydantic AI–based agent system
✔ Clean APIs & backend design
✔ Structured validation & orchestration
✔ Real-world problem solving


---

🔮 Future Enhancements

🔁 Retry & fallback model support

📊 User history and progress tracking

🖥️ Frontend UI (React / Next.js)

🧠 Multi-agent planning (planner + reviewer)

☁️ Production deployment with CI/CD



---

👨‍💻 Author

Yasaswini Machineni
SRM Institute of Science and Technology

> Built as part of a Full Stack Generative AI assignment using Pydantic AI.




---
