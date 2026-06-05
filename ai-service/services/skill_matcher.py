from typing import List, Dict
from difflib import SequenceMatcher
import logging

logger = logging.getLogger(__name__)

class SkillMatcher:
    def __init__(self):
        self.skill_synonyms = {
            'ml': ['machine learning', 'ai'],
            'nlp': ['natural language processing'],
            'cv': ['computer vision'],
            'js': ['javascript', 'node.js'],
            'py': ['python'],
        }
    
    def calculate_match_score(self, resume_skills: List[str], job_requirements: List[str]) -> float:
        """
        Calculate skill match score (0-1)
        """
        if not job_requirements:
            return 0.0
        
        matched = 0
        for req_skill in job_requirements:
            if self._is_skill_match(req_skill, resume_skills):
                matched += 1
        
        score = matched / len(job_requirements)
        return round(score, 2)
    
    def get_matched_skills(self, resume_skills: List[str], job_requirements: List[str]) -> List[str]:
        """
        Get list of matched skills
        """
        matched = []
        for req_skill in job_requirements:
            for res_skill in resume_skills:
                if self._skill_similarity(req_skill, res_skill) > 0.7:
                    matched.append(req_skill)
                    break
        return list(set(matched))
    
    def get_missing_skills(self, resume_skills: List[str], job_requirements: List[str]) -> List[str]:
        """
        Get list of missing skills
        """
        matched = self.get_matched_skills(resume_skills, job_requirements)
        missing = [skill for skill in job_requirements if skill not in matched]
        return missing
    
    def _is_skill_match(self, job_skill: str, resume_skills: List[str]) -> bool:
        """
        Check if job skill matches any resume skill
        """
        job_skill_lower = job_skill.lower()
        
        for res_skill in resume_skills:
            res_skill_lower = res_skill.lower()
            
            # Exact match
            if job_skill_lower == res_skill_lower:
                return True
            
            # Fuzzy match
            if self._skill_similarity(job_skill_lower, res_skill_lower) > 0.7:
                return True
            
            # Synonym match
            if self._check_synonyms(job_skill_lower, res_skill_lower):
                return True
        
        return False
    
    def _skill_similarity(self, skill1: str, skill2: str) -> float:
        """
        Calculate similarity between two skills
        """
        return SequenceMatcher(None, skill1.lower(), skill2.lower()).ratio()
    
    def _check_synonyms(self, skill1: str, skill2: str) -> bool:
        """
        Check if skills are synonyms
        """
        for key, synonyms in self.skill_synonyms.items():
            if (skill1 in synonyms or skill1 == key) and (skill2 in synonyms or skill2 == key):
                return True
        return False
