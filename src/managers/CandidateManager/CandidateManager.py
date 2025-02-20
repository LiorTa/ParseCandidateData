from typing import List, Dict, Any
from datetime import datetime
from GeneralClasses import Candidate, WorkExperience
from ResumesManager import fetch_resumes


def calculate_days_gap(start_date: str, end_date: str) -> int:
    """
    Calculate the number of days between two dates.
    
    Args:
        start_date (str): Start date in format "Jan/01/1970"
        end_date (str): End date in format "Jan/01/1970"
        
    Returns:
        int: Number of days between the two dates
    """
    start = datetime.strptime(start_date, '%b/%d/%Y')
    end = datetime.strptime(end_date, '%b/%d/%Y')
    return (start - end).days


def process_experience(experience: List[Dict[str, Any]]) -> List[WorkExperience]:


    experience_list = []

    # Sort by start date (first job to last job)
    sorted_exp = sorted(experience, 
                       key=lambda x: datetime.strptime(x.get('start_date', 'Jan/01/1970'), '%b/%d/%Y'),
                       reverse=False)


    for i, exp in enumerate(sorted_exp):
        location = f"{exp.get('location', {}).get("short_display_address", "Unknown")}"
        company_name = exp.get("company_normalized_name", "Unknown")
        current_job = exp.get("current_job", False)
        work_experience = WorkExperience(exp.get("title", "Unknown Role"), company_name, exp.get("start_date", ""), exp.get("end_date", ""), location, current_job)

        if i > 0:
            # Calculate gap between current job and previous job
            prev_job = sorted_exp[i-1]
            gap_days = calculate_days_gap(exp['start_date'],prev_job['end_date'])
            if gap_days and gap_days > 0:
                experience_list[-1].gap_after = gap_days

        experience_list.append(work_experience)

    return experience_list


def get_all_candidates(resumes: list[dict]) -> list[Candidate]:
    """
    Process all resumes and return a list of Candidate objects.
    
    Args:
        resumes (list[dict]): List of dictionaries containing resume data
        
    """
    candidates = []
    for resume in resumes:
        experiences = process_experience(resume.get("experience", []))
        education = resume.get("education", [])
        if education:
            education = education[0]
        candidate = Candidate(resume.get("contact_info", {}).get("name", {}).get("formatted_name", "Unknown"), experiences, education.get("degree_type", "Unknown"), education.get("institute_type", "Unknown"), education.get("GPA", "Unknown"))
        candidates.append(candidate)
    return candidates


if __name__ == "__main__":
    url = "https://recruiting-test-resume-data.hiredscore.com/allcands-full-api_hub_b1f6-acde48001122.json"
    resumes = fetch_resumes(url)
    print(resumes)
    candidates = get_all_candidates(resumes)
    print(candidates)

    for candidate in candidates:
        print(candidate)
        print("--------------------------------")





