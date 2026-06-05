# AI Resume Analysis Service

Python-based FastAPI service for resume parsing, quality analysis, and skill matching.

## Features

- Resume text extraction (PDF, DOCX)
- Resume quality scoring using NLP
- Skill extraction and recognition
- Job requirement matching
- Resume strength and weakness analysis
- Improvement suggestions

## Technology Stack

- **Framework**: FastAPI
- **NLP**: spaCy, NLTK
- **ML**: scikit-learn, transformers
- **File Processing**: PyPDF2, python-docx
- **Server**: Uvicorn

## Installation

```bash
cd ai-service
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

## Environment Variables

Create a `.env` file in the ai-service directory:

```
AI_SERVICE_PORT=8000
AI_SERVICE_HOST=0.0.0.0
PYTHONUNBUFFERED=1
MIN_RESUME_QUALITY_SCORE=0.6
SKILL_EXTRACTION_THRESHOLD=0.5
```

## Running the Service

### Development

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## API Endpoints

### Health Check

```
GET /health
```

Response:
```json
{
  "status": "AI service is running",
  "service": "resume-analyzer"
}
```

### Analyze Resume (Text)

```
POST /analyze-resume
```

Request body:
```json
{
  "resume_text": "John Doe...",
  "job_description": "We are looking for..."
}
```

Response:
```json
{
  "quality_score": 0.85,
  "strengths": ["Contact information is complete", "Good variety of technical skills"],
  "weaknesses": ["Limited professional experience"],
  "suggestions": ["Use action verbs", "Quantify accomplishments"],
  "extracted_skills": ["python", "javascript", "react"]
}
```

### Match Skills

```
POST /match-skills
```

Request body:
```json
{
  "resume_skills": ["python", "javascript"],
  "job_requirements": ["python", "nodejs", "docker"]
}
```

Response:
```json
{
  "match_score": 0.67,
  "matched_skills": ["python"],
  "missing_skills": ["nodejs", "docker"]
}
```

### Upload and Analyze

```
POST /upload-and-analyze
Content-Type: multipart/form-data
```

Parameters:
- `file`: Resume file (PDF or DOCX)
- `job_description` (optional): Job description for matching

Response:
```json
{
  "quality_score": 0.85,
  "strengths": [...],
  "weaknesses": [...],
  "suggestions": [...],
  "extracted_skills": [...],
  "extracted_data": {...}
}
```

## Services

### ResumeParser
Extracts text from PDF/DOCX files and parses resume content using NLP.

**Methods:**
- `parse_text(resume_text)` - Parse resume text
- `parse_file(file_content, filename)` - Parse resume file

### ResumeAnalyzer
Analyzes resume quality and provides improvement suggestions.

**Methods:**
- `calculate_quality_score(extracted_data)` - Get quality score (0-1)
- `identify_strengths(extracted_data)` - List resume strengths
- `identify_weaknesses(extracted_data)` - List resume weaknesses
- `get_suggestions(extracted_data, weaknesses)` - Get improvement suggestions

### SkillMatcher
Matches resume skills with job requirements.

**Methods:**
- `calculate_match_score(resume_skills, job_requirements)` - Get match score (0-1)
- `get_matched_skills(resume_skills, job_requirements)` - List matched skills
- `get_missing_skills(resume_skills, job_requirements)` - List missing skills

## Quality Score Calculation

The quality score is calculated based on:
- Presence of name/contact header (1.0 point)
- Email address (0.5 points)
- Phone number (0.5 points)
- Technical skills count >= 3 (1.5 points)
- Education section (1.0 point)
- Professional experience (0.5 points)

**Total: 5.0 points → Normalized to 0-1 scale**

## Skill Extraction

Currently supports common technical skills:
- Programming Languages: Python, Java, JavaScript, C++, C#, PHP, Ruby, Go, Rust
- Frontend: HTML, CSS, React, Angular, Vue
- Backend: Node.js, Express, Django, Flask
- Databases: SQL, MongoDB, PostgreSQL, MySQL
- DevOps: Git, Docker, Kubernetes, AWS, Azure, GCP
- Other: CI/CD, Jenkins, Agile

## Extending Skill List

Edit the `common_skills` list in `services/resume_parser.py` to add more skills:

```python
common_skills = [
    'python', 'java', 'javascript', 'c++', 'c#', 'php', 'ruby', 'go', 'rust',
    # Add your custom skills here
    'custom_skill_1', 'custom_skill_2'
]
```

## Testing

### Manual Testing with curl

```bash
# Health check
curl http://localhost:8000/health

# Analyze resume
curl -X POST http://localhost:8000/analyze-resume \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "John Doe\nEmail: john@example.com\nPhone: 123-456-7890\nSkills: Python, JavaScript, React",
    "job_description": "Looking for Python developer"
  }'
```

### Docker

```bash
docker build -t placement-ai-service .
docker run -p 8000:8000 placement-ai-service
```

## Performance Optimization

- Resume text is limited to 1M characters to prevent memory issues
- Consider using caching for repeated analyses
- Use async processing for large batch operations
- Deploy with multiple workers for production

## Future Enhancements

- [ ] Resume ATS scoring
- [ ] Certification validation
- [ ] Experience level classification
- [ ] Custom skill taxonomy
- [ ] Resume formatting analysis
- [ ] Deep learning-based quality scoring
