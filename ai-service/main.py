from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from typing import List
import logging

from services.resume_parser import ResumeParser
from services.resume_analyzer import ResumeAnalyzer
from services.skill_matcher import SkillMatcher

load_dotenv()

app = FastAPI(title="AI Resume Analysis Service")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize services
resume_parser = ResumeParser()
resume_analyzer = ResumeAnalyzer()
skill_matcher = SkillMatcher()

# Models
class ResumeAnalysisRequest(BaseModel):
    resume_text: str
    job_description: str = None

class ResumeAnalysisResponse(BaseModel):
    quality_score: float
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]
    extracted_skills: List[str]

# Routes
@app.get("/health")
async def health_check():
    return {"status": "AI service is running", "service": "resume-analyzer"}

@app.post("/analyze-resume", response_model=ResumeAnalysisResponse)
async def analyze_resume(request: ResumeAnalysisRequest):
    try:
        logger.info("Analyzing resume...")
        
        # Extract data from resume
        extracted_data = resume_parser.parse_text(request.resume_text)
        
        # Analyze quality
        quality_score = resume_analyzer.calculate_quality_score(extracted_data)
        strengths = resume_analyzer.identify_strengths(extracted_data)
        weaknesses = resume_analyzer.identify_weaknesses(extracted_data)
        suggestions = resume_analyzer.get_suggestions(extracted_data, weaknesses)
        
        # Extract skills
        skills = extracted_data.get('skills', [])
        
        return ResumeAnalysisResponse(
            quality_score=quality_score,
            strengths=strengths,
            weaknesses=weaknesses,
            suggestions=suggestions,
            extracted_skills=skills
        )
    except Exception as e:
        logger.error(f"Error analyzing resume: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/match-skills")
async def match_skills(resume_skills: List[str], job_requirements: List[str]):
    try:
        logger.info("Matching skills...")
        match_score = skill_matcher.calculate_match_score(resume_skills, job_requirements)
        matched_skills = skill_matcher.get_matched_skills(resume_skills, job_requirements)
        missing_skills = skill_matcher.get_missing_skills(resume_skills, job_requirements)
        
        return {
            "match_score": match_score,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        }
    except Exception as e:
        logger.error(f"Error matching skills: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload-and-analyze")
async def upload_and_analyze(file: UploadFile = File(...), job_description: str = None):
    try:
        logger.info(f"Processing file: {file.filename}")
        
        # Read file content
        content = await file.read()
        
        # Parse resume
        resume_text = resume_parser.parse_file(content, file.filename)
        
        # Analyze
        extracted_data = resume_parser.parse_text(resume_text)
        quality_score = resume_analyzer.calculate_quality_score(extracted_data)
        strengths = resume_analyzer.identify_strengths(extracted_data)
        weaknesses = resume_analyzer.identify_weaknesses(extracted_data)
        suggestions = resume_analyzer.get_suggestions(extracted_data, weaknesses)
        skills = extracted_data.get('skills', [])
        
        return {
            "quality_score": quality_score,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "suggestions": suggestions,
            "extracted_skills": skills,
            "extracted_data": extracted_data
        }
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
