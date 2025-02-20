# Define the WorkExperience class to store individual job details
class WorkExperience:
    def __init__(self, role: str, company_name: str, start_date: str, end_date: str, location: str, current_job: bool, gap_after: int = None):
        """
        Initialize a WorkExperience object.
        
        Args:
            role (str): Job title/role
            start_date (str): Start date in MM/DD/YYYY format
            end_date (str): End date in MM/DD/YYYY format
            location (str): Job location (city, state, country)
            gap_after (int, optional): Days gap after this job
        """
        self.role = role
        self.company_name = company_name
        self.current_job = current_job
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.gap_after = gap_after        

    def __str__(self):
        """String representation of work experience"""
        base_str = f"Worked as: {self.role}, From {self.start_date} To {self.end_date} in {self.location}, currently working: {self.current_job}"
        if self.gap_after:
            return f"{base_str}\nGap in CV from previous job: {self.gap_after} days"
        return base_str

# Define the Candidate class to store candidate details
class Candidate:
    def __init__(self, name: str, experiences: list[WorkExperience], education_degree: str, education_school: str, education_grade: str):
        """
        Initialize a Candidate object.
        
        Args:
            name (str): Candidate's name
            experiences (list): List of WorkExperience objects
        """
        self.name = name
        self.experiences = experiences
        self.education_degree = education_degree
        self.education_school = education_school
        self.education_grade = education_grade

    def __str__(self):
        """String representation of candidate with all experiences"""
        exp_str = "\n".join(str(exp) for exp in self.experiences)
        return f"Hello {self.name},\n{exp_str}\n\nEducation: {self.education_degree} at {self.education_school} with grade {self.education_grade}"