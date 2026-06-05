# AI-Powered Student Placement Portal

An intelligent platform that leverages AI to analyze and shortlist student resumes based on quality metrics and job requirements.

## Features

- **Student Dashboard**: Upload and manage resumes
- **AI Resume Analysis**: Automatic quality scoring and skill extraction
- **Smart Shortlisting**: AI-powered candidate matching with job descriptions
- **Company Portal**: Browse and manage shortlisted candidates
- **Admin Panel**: System configuration and analytics
- **Resume Parsing**: Extract key information from PDF/DOCX resumes

## Tech Stack

### Frontend
- React.js / Next.js
- Tailwind CSS
- Redux/Context API

### Backend
- Node.js with Express.js
- Python FastAPI (for AI services)
- JWT Authentication

### AI/ML
- spaCy / NLTK (NLP)
- scikit-learn (ML)
- transformers (BERT-based models)
- PyPDF2 / python-docx (Resume parsing)

### Database
- MongoDB (NoSQL)
- Redis (Caching)

### Deployment
- Docker & Docker Compose
- AWS / Heroku / DigitalOcean

## Project Structure

```
student-placement-portal/
├── frontend/                 # React.js frontend
├── backend/                  # Node.js Express API
├── ai-service/              # Python FastAPI AI service
├── docker-compose.yml       # Docker orchestration
├── .env.example             # Environment variables template
└── README.md
```

## Getting Started

### Prerequisites
- Node.js 16+
- Python 3.9+
- MongoDB
- Docker (optional)

### Installation

See individual README files in `frontend/`, `backend/`, and `ai-service/` directories.

## License

MIT License
