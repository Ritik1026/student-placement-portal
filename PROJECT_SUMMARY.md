# AI-Powered Student Placement Portal - Project Summary

## 🎯 Overview

A comprehensive web platform that leverages artificial intelligence to analyze student resumes and intelligently shortlist candidates based on quality metrics and job requirements. The platform serves three key user types: **Students**, **Companies**, and **Administrators**.

---

## ✨ Key Features

### For Students
- ✅ Create and manage profiles
- ✅ Upload resumes (PDF/DOCX)
- ✅ Get AI-powered resume quality analysis
- ✅ Receive actionable improvement suggestions
- ✅ View matched job opportunities
- ✅ Track application history

### For Companies
- ✅ Create company profiles
- ✅ Post job openings with detailed requirements
- ✅ Browse AI-shortlisted candidates
- ✅ View candidate profiles and resumes
- ✅ Manage job postings and applications
- ✅ Track hiring pipeline

### For Admins
- ✅ System configuration and monitoring
- ��� User management (students, companies)
- ✅ Analytics and reporting
- ✅ Content moderation
- ✅ AI model management

---

## 🏗️ Architecture

### Frontend (React.js)
- **Location**: `/frontend`
- **Port**: 3000
- **Technologies**: React 18, React Router v6, Tailwind CSS, Redux/Context API, Axios
- **Components**:
  - Navbar (Navigation)
  - Home (Landing page)
  - Login (Authentication)
  - Register (User signup)
  - StudentDashboard (Resume upload & analysis)
  - CompanyDashboard (Job posting & candidate browsing)

### Backend (Node.js + Express)
- **Location**: `/backend`
- **Port**: 5000
- **Technologies**: Express.js, MongoDB, Redis, JWT, Multer
- **Key Features**:
  - RESTful API architecture
  - JWT-based authentication
  - File upload handling
  - Database operations
  - Cache management
  - Integration with AI service

### AI Service (Python + FastAPI)
- **Location**: `/ai-service`
- **Port**: 8000
- **Technologies**: FastAPI, spaCy, scikit-learn, PyPDF2, python-docx
- **Key Services**:
  - **ResumeParser**: Extracts text from PDF/DOCX files and parses content
  - **ResumeAnalyzer**: Calculates quality scores and provides feedback
  - **SkillMatcher**: Matches resume skills with job requirements

### Database (MongoDB)
- **Purpose**: Store users, resumes, jobs, applications, shortlists
- **Port**: 27017
- **Collections**:
  - `users` - Student/Company/Admin accounts
  - `resumes` - Uploaded resumes with extracted data
  - `jobs` - Job postings
  - `applications` - Student job applications
  - `shortlists` - AI-shortlisted candidates

### Cache Layer (Redis)
- **Purpose**: Session management, caching, job queues
- **Port**: 6379

---

## 📁 Project Structure

```
student-placement-portal/
├── frontend/                          # React.js Frontend
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Home.js
│   │   │   ├── Login.js
│   │   │   ├── Register.js
│   │   │   ├── StudentDashboard.js
│   │   │   └── CompanyDashboard.js
│   │   ├── components/
│   │   │   └── Navbar.js
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   ├── Dockerfile.dev
│   ├── tailwind.config.js
│   ├── .gitignore
│   └── README.md
│
├── backend/                           # Express.js Backend
│   ├── src/
│   │   ├── models/
│   │   │   ├── User.js
│   │   │   ├── Resume.js
│   │   │   └── Job.js
│   │   ├── routes/
│   │   │   ├── auth.js
│   │   │   ├── students.js
│   │   │   ├── companies.js
│   │   │   ├── jobs.js
│   │   │   ├── resumes.js
│   │   │   └── shortlist.js
│   │   └── index.js
│   ├── package.json
│   ├── Dockerfile
│   ├── .gitignore
│   └── README.md
│
├── ai-service/                        # FastAPI AI Service
│   ├── main.py
│   ├── services/
│   │   ├── resume_parser.py
│   │   ├── resume_analyzer.py
│   │   └── skill_matcher.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .gitignore
│   └── README.md
│
├── docker-compose.yml                 # Docker orchestration
├── .env.example                       # Environment variables template
├── .gitignore                         # Git ignore rules
├── SETUP.md                           # Installation & setup guide
├── PROJECT_SUMMARY.md                 # This file
└── README.md                          # Main project documentation
```

---

## 🚀 Getting Started

### Quick Start (Docker Recommended)

```bash
# Clone repository
git clone https://github.com/Ritik1026/student-placement-portal.git
cd student-placement-portal

# Copy environment template
cp .env.example .env

# Start all services
docker-compose up -d

# Services will be available at:
# - Frontend: http://localhost:3000
# - Backend: http://localhost:5000/api
# - AI Service: http://localhost:8000
# - MongoDB: localhost:27017
# - Redis: localhost:6379
```

### Manual Setup (See SETUP.md for detailed instructions)

```bash
# Backend
cd backend && npm install && npm run dev

# AI Service (in new terminal)
cd ai-service && pip install -r requirements.txt && uvicorn main:app --reload

# Frontend (in new terminal)
cd frontend && npm install && npm start
```

---

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user

### Students
- `GET /api/students/:id` - Get student profile
- `PUT /api/students/:id` - Update student profile
- `POST /api/resumes/upload` - Upload resume
- `GET /api/resumes/student/:studentId` - Get student resumes

### Companies
- `GET /api/companies/:id` - Get company profile
- `POST /api/companies/:id/jobs` - Post job

### Jobs
- `GET /api/jobs` - Get all active jobs
- `GET /api/jobs/:id` - Get job details

### AI Analysis
- `GET /ai-service/health` - Health check
- `POST /ai-service/analyze-resume` - Analyze resume text
- `POST /ai-service/match-skills` - Match skills with job requirements
- `POST /ai-service/upload-and-analyze` - Upload and analyze resume file

---

## 🤖 AI/ML Features

### Resume Quality Scoring (0-1 scale)

**Scoring Factors:**
- Contact information completeness (1.0 pt)
- Email presence (0.5 pt)
- Phone number presence (0.5 pt)
- Technical skills (>=3) (1.5 pts)
- Education section (1.0 pt)
- Professional experience (0.5 pt)

**Total: 5.0 points → Normalized to 0-1 scale**

### Resume Analysis
1. **Strength Identification** - Highlights what's good
2. **Weakness Detection** - Identifies what's missing
3. **Improvement Suggestions** - Actionable recommendations
4. **Skill Extraction** - Identifies technical skills
5. **Job Matching** - Matches with job requirements

### Supported Skills (Extensible)
- **Languages**: Python, Java, JavaScript, C++, C#, PHP, Ruby, Go, Rust
- **Frontend**: HTML, CSS, React, Angular, Vue
- **Backend**: Node.js, Express, Django, Flask
- **Databases**: SQL, MongoDB, PostgreSQL, MySQL
- **DevOps**: Git, Docker, Kubernetes, AWS, Azure, GCP
- **Other**: CI/CD, Jenkins, Agile

---

## 🔐 Security Features

- ✅ JWT-based authentication
- ✅ Password hashing with bcryptjs
- ✅ CORS protection
- ✅ Environment variable management
- ✅ File upload validation
- ✅ Input validation and sanitization
- ✅ Role-based access control (RBAC)

---

## 📊 Database Schema

### Users Collection
```javascript
{
  _id: ObjectId,
  name: String,
  email: String (unique),
  password: String (hashed),
  role: String (student/company/admin),
  phone: String,
  profilePicture: String,
  isVerified: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

### Resumes Collection
```javascript
{
  _id: ObjectId,
  studentId: ObjectId (ref: User),
  filename: String,
  fileUrl: String,
  extractedData: {
    name: String,
    email: String,
    phone: String,
    skills: [String],
    experience: String,
    education: [String]
  },
  qualityScore: Number (0-1),
  aiAnalysis: {
    strengths: [String],
    weaknesses: [String],
    suggestions: [String],
    analyzedAt: Date
  },
  uploadedAt: Date
}
```

### Jobs Collection
```javascript
{
  _id: ObjectId,
  companyId: ObjectId (ref: User),
  jobTitle: String,
  description: String,
  requiredSkills: [String],
  experienceLevel: String,
  salary: String,
  location: String,
  jobType: String (Full-time/Part-time/Internship),
  deadline: Date,
  status: String (active/closed),
  createdAt: Date
}
```

---

## 🧪 Testing

### Frontend Testing
```bash
cd frontend
npm test
```

### Backend Testing
```bash
cd backend
npm test
```

### AI Service Testing
```bash
cd ai-service
pytest
```

---

## 📦 Technologies Used

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | React 18, React Router, Tailwind CSS | User Interface |
| Backend | Express.js, Node.js | API Server |
| Database | MongoDB | Data Storage |
| Cache | Redis | Session & Cache |
| AI/ML | FastAPI, spaCy, scikit-learn | Resume Analysis |
| Auth | JWT, bcryptjs | Authentication |
| File Upload | Multer | Resume Upload |
| Containerization | Docker, Docker Compose | Deployment |

---

## 🔄 Workflow

### Student Workflow
1. **Register** → Create student account
2. **Upload Resume** → Submit resume file
3. **AI Analysis** → Get quality score & feedback
4. **Improve Resume** → Use suggestions to enhance
5. **Browse Jobs** → View available positions
6. **Apply** → Submit applications
7. **Track Status** → Monitor applications

### Company Workflow
1. **Register** → Create company account
2. **Post Job** → Create job opening with requirements
3. **Browse Candidates** → View AI-shortlisted students
4. **Review Profiles** → Examine resume quality scores
5. **Select Candidates** → Choose suitable candidates
6. **Manage Pipeline** → Track hiring progress

---

## 🚀 Deployment

### Docker Deployment
```bash
docker-compose -f docker-compose.yml up -d
```

### Cloud Deployment Options
- **Heroku** - Frontend + Backend
- **AWS** - EC2, RDS (MongoDB Atlas), ElastiCache (Redis)
- **DigitalOcean** - App Platform, Managed Databases
- **Google Cloud** - Cloud Run, Cloud SQL, Firestore
- **Azure** - App Service, Cosmos DB, Azure Cache

### Environment Configuration
Create `.env` file with required variables (see `.env.example`)

---

## 📈 Future Enhancements

### Phase 2
- [ ] Email notifications
- [ ] Resume ATS scoring
- [ ] Advanced analytics dashboard
- [ ] Video interview integration
- [ ] LinkedIn profile integration

### Phase 3
- [ ] Mobile app (React Native)
- [ ] Real-time notifications
- [ ] Advanced AI for candidate recommendation
- [ ] Blockchain certificates
- [ ] Multi-language support

### Phase 4
- [ ] Machine learning for predictive hiring
- [ ] Chatbot support
- [ ] Virtual recruitment events
- [ ] Skills marketplace
- [ ] Career path recommendations

---

## 📖 Documentation Files

- **README.md** - Main project documentation
- **SETUP.md** - Detailed installation and setup guide
- **backend/README.md** - Backend API documentation
- **frontend/README.md** - Frontend setup guide
- **ai-service/README.md** - AI service documentation
- **PROJECT_SUMMARY.md** - This file

---

## 👥 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤝 Support

For issues, questions, or suggestions:
1. Check the SETUP.md troubleshooting section
2. Review individual README files
3. Open a GitHub Issue
4. Contact the development team

---

## 📞 Contact

- **GitHub**: [@Ritik1026](https://github.com/Ritik1026)
- **Email**: ritikchaudhary5282@gmail.com

---

**Last Updated**: June 5, 2026
**Version**: 1.0.0
