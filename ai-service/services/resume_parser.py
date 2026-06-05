import spacy
import re
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class ResumeParser:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            logger.error("spaCy model not found. Please run: python -m spacy download en_core_web_sm")
            self.nlp = None
    
    def parse_text(self, resume_text: str) -> Dict:
        """
        Parse resume text and extract key information
        """
        extracted_data = {
            'name': None,
            'email': None,
            'phone': None,
            'skills': [],
            'experience': [],
            'education': [],
            'certifications': []
        }
        
        try:
            # Email extraction
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            emails = re.findall(email_pattern, resume_text)
            if emails:
                extracted_data['email'] = emails[0]
            
            # Phone extraction
            phone_pattern = r'\b(?:\+?1[-.]?)?\(?([0-9]{3})\)?[-.]?([0-9]{3})[-.]?([0-9]{4})\b'
            phones = re.findall(phone_pattern, resume_text)
            if phones:
                extracted_data['phone'] = f"{phones[0][0]}-{phones[0][1]}-{phones[0][2]}"
            
            # NLP processing
            if self.nlp:
                doc = self.nlp(resume_text[:1000000])  # Limit to 1M chars for performance
                
                # Extract PERSON entities (potential names)
                for ent in doc.ents:
                    if ent.label_ == "PERSON" and not extracted_data['name']:
                        extracted_data['name'] = ent.text
                        break
            
            # Skill extraction (basic)
            common_skills = [
                'python', 'java', 'javascript', 'c++', 'c#', 'php', 'ruby', 'go', 'rust',
                'html', 'css', 'react', 'angular', 'vue', 'nodejs', 'express', 'django',
                'flask', 'sql', 'mongodb', 'postgresql', 'mysql', 'git', 'docker',
                'kubernetes', 'aws', 'azure', 'gcp', 'ci/cd', 'jenkins', 'agile'
            ]
            resume_lower = resume_text.lower()
            for skill in common_skills:
                if skill in resume_lower and skill not in extracted_data['skills']:
                    extracted_data['skills'].append(skill)
            
        except Exception as e:
            logger.error(f"Error parsing resume: {str(e)}")
        
        return extracted_data
    
    def parse_file(self, file_content: bytes, filename: str) -> str:
        """
        Parse resume file (PDF or DOCX) and return text
        """
        try:
            if filename.lower().endswith('.pdf'):
                return self._parse_pdf(file_content)
            elif filename.lower().endswith(('.docx', '.doc')):
                return self._parse_docx(file_content)
            else:
                raise ValueError(f"Unsupported file format: {filename}")
        except Exception as e:
            logger.error(f"Error parsing file: {str(e)}")
            raise
    
    def _parse_pdf(self, file_content: bytes) -> str:
        from PyPDF2 import PdfReader
        from io import BytesIO
        
        try:
            pdf_reader = PdfReader(BytesIO(file_content))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            logger.error(f"Error parsing PDF: {str(e)}")
            raise
    
    def _parse_docx(self, file_content: bytes) -> str:
        from docx import Document
        from io import BytesIO
        
        try:
            doc = Document(BytesIO(file_content))
            text = ""
            for para in doc.paragraphs:
                text += para.text + "\n"
            return text
        except Exception as e:
            logger.error(f"Error parsing DOCX: {str(e)}")
            raise
