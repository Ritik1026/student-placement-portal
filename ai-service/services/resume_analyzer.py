from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class ResumeAnalyzer:
    def __init__(self):
        self.min_quality_score = 0.6
    
    def calculate_quality_score(self, extracted_data: Dict) -> float:
        """
        Calculate resume quality score (0-1)
        """
        score = 0.0
        max_score = 5.0
        
        # Check for essential information
        if extracted_data.get('name'):
            score += 1.0
        if extracted_data.get('email'):
            score += 0.5
        if extracted_data.get('phone'):
            score += 0.5
        if extracted_data.get('skills') and len(extracted_data.get('skills', [])) >= 3:
            score += 1.5
        if extracted_data.get('education'):
            score += 1.0
        if extracted_data.get('experience'):
            score += 0.5
        
        # Normalize to 0-1
        final_score = min(score / max_score, 1.0)
        return round(final_score, 2)
    
    def identify_strengths(self, extracted_data: Dict) -> List[str]:
        """
        Identify resume strengths
        """
        strengths = []
        
        if extracted_data.get('name') and extracted_data.get('email') and extracted_data.get('phone'):
            strengths.append("Contact information is complete")
        
        if extracted_data.get('skills'):
            if len(extracted_data.get('skills', [])) >= 5:
                strengths.append("Good variety of technical skills")
            else:
                strengths.append("Has technical skills mentioned")
        
        if extracted_data.get('education'):
            strengths.append("Education section is present")
        
        if extracted_data.get('experience'):
            strengths.append("Professional experience is documented")
        
        if len(strengths) == 0:
            strengths.append("Resume has basic structure")
        
        return strengths
    
    def identify_weaknesses(self, extracted_data: Dict) -> List[str]:
        """
        Identify resume weaknesses
        """
        weaknesses = []
        
        if not extracted_data.get('name'):
            weaknesses.append("Name/Contact header is missing or unclear")
        
        if not extracted_data.get('phone'):
            weaknesses.append("Phone number is missing")
        
        if not extracted_data.get('skills') or len(extracted_data.get('skills', [])) < 3:
            weaknesses.append("Limited technical skills mentioned")
        
        if not extracted_data.get('education'):
            weaknesses.append("Education section is missing")
        
        if not extracted_data.get('experience'):
            weaknesses.append("Professional experience is not highlighted")
        
        if len(weaknesses) == 0:
            weaknesses.append("Consider adding more details and achievements")
        
        return weaknesses
    
    def get_suggestions(self, extracted_data: Dict, weaknesses: List[str]) -> List[str]:
        """
        Get improvement suggestions
        """
        suggestions = [
            "Use action verbs (led, developed, implemented) to describe achievements",
            "Quantify accomplishments with metrics and numbers",
            "Keep resume to 1-2 pages maximum",
            "Use clear section headings and consistent formatting",
            "Tailor resume to match job description requirements"
        ]
        
        if not extracted_data.get('skills') or len(extracted_data.get('skills', [])) < 5:
            suggestions.append("Add more technical skills relevant to your target roles")
        
        if not extracted_data.get('phone'):
            suggestions.append("Include your phone number for easy contact")
        
        if not extracted_data.get('experience'):
            suggestions.append("Detail your professional experience with company names and dates")
        
        return suggestions[:5]  # Return top 5 suggestions
