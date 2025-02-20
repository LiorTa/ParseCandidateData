import unittest
from GeneralClasses import WorkExperience, Candidate
from CandidateManager import calculate_days_gap, process_experience

class TestParseCandidates(unittest.TestCase):
    def test_work_experience_str_no_gap(self):
        """Test WorkExperience string representation without a gap"""
        exp = WorkExperience(
            role="HR",
            company_name="Workday",
            start_date="Jan/01/2008",
            end_date="Dec/31/2008",
            location="New York, NY, US",
            current_job=False
        )
        expected = "Worked as: HR in Workday, From Jan/01/2008 To Dec/31/2008 in New York, NY, US, currently working: False"
        self.assertEqual(str(exp), expected)

    def test_work_experience_str_with_gap(self):
        """Test WorkExperience string representation with a gap"""
        exp = WorkExperience(
            role="Programmer",
            start_date="Jan/01/2008",
            end_date="Dec/31/2008",
            location="Israel, TL, Rot",
            company_name="Workday",
            current_job=False,
            gap_after=20
        )
        expected = "Worked as: Programmer in Workday, From Jan/01/2008 To Dec/31/2008 in Israel, TL, Rot, currently working: False\nGap in CV from previous job: 20 days"
        self.assertEqual(str(exp), expected)

    def test_candidate_str(self):
        """Test Candidate string representation"""
        exp = WorkExperience("Programmer", "Workday", "Jan/01/2008", "Dec/31/2008", "New York, NY, US", False)
        candidate = Candidate("Shimon Peres", [exp], "Bachelor", "BGU", "4.5")
        expected = "Hello Shimon Peres,\nWorked as: Programmer in Workday, From Jan/01/2008 To Dec/31/2008 in New York, NY, US, currently working: False\n\nEducation: Bachelor at BGU with grade 4.5"
        self.assertEqual(str(candidate), expected)

    def test_calculate_days_gap_positive(self):
        """Test gap calculation with a positive gap"""
        gap = calculate_days_gap("Dec/31/2008", "Jan/20/2008")
        self.assertEqual(gap, 346)

    def test_calculate_days_gap_zero(self):
        """Test gap calculation with no gap (adjacent dates)"""
        gap = calculate_days_gap("Dec/31/2008", "Dec/30/2008")
        self.assertEqual(gap, 1)  # 1 day gap due to consecutive days

    def test_calculate_days_gap_negative(self):
        """Test gap calculation with overlapping dates (returns 0)"""
        gap = calculate_days_gap("Jan/20/2009", "Jan/01/2009")
        self.assertEqual(gap, 19)

    def test_calculate_days_gap_invalid_date(self):
        """Test gap calculation with invalid date format"""
        gap = calculate_days_gap("", "01/01/2009")
        self.assertEqual(gap, 0)

    def test_process_experiences_with_gap(self):
        """Test processing experiences with a gap"""
        exp_list = [
      {
        "company_normalized_name": "Valley Wastements",
        "last_job": True,
        "company_name": "Valley Wastements Inc",
        "position_type": "directHire",
        "duration_in_month": 11,
        "current_job": False,
        "title": "Staff Accountant",
        "start_date": "Jan/01/2008",
        "same_company": False,
        "description_short": "1. Forget Purchase requisitions', Purchase orders and order materials;\n2. Physical count Spiderwebs;\n3. Adjust Spiderwebs balances and prices;\n4. Forget voucher package;\n5. Other administrative duties;",
        "company_details": {
          "company_type": "Privately Held",
          "company": "Valley Wastements",
          "_id": "54aef31217252229a56a86a4",
          "company_url": "/company/Valley-Wastements?trk=ppro_cprof",
          "number_of_time_seen": 13,
          "industry": "Real Estate industry",
          "size": " 11-50 employees"
        },
        "end_date": "Dec/31/2008",
        "employer_org_name": "Valley Wastements Inc",
        "location": {
          "region": "GM",
          "country_code": "US",
          "municipality": "Agrabah",
          "short_display_address": "Agrabah, GM, US"
        },
        "description": "2008 Valley Wastements Inc.\t\tAgrabah, GM.\nStaff Accountant:\n1. Forget Purchase requisitions', Purchase orders and order materials;\n2. Physical count Spiderwebs;\n3. Adjust Spiderwebs balances and prices;\n4. Forget voucher package;\n5. Other administrative duties;"
      },
      {
        "company_normalized_name": "Lion's King",
        "company_name": "Lion's King",
        "position_type": "directHire",
        "duration_in_month": 11,
        "current_job": False,
        "title": "C.O.A.'s",
        "start_date": "Jan/01/2007",
        "same_company": False,
        "description_short": "Staff Accountant:\n1. Enter checks and invoice into smashing system;\n2. Forget Dig Statements;\n3. Forget newspaper entries;\n4. Forget Outcome Statement, Balance Sheet and Statement of pickles\n5. Forget Wax returns;\n6. Perform other administrative duties;",
        "company_details": None,
        "end_date": "Dec/31/2007",
        "employer_org_name": "Lion's King",
        "location": {
          "region": "GM",
          "country_code": "US",
          "municipality": "Agrabah",
          "short_display_address": "Agrabah, GM, US"
        },
        "description": "2007 Lion's King service, C.O.A.'s\t\tAgrabah, GM.\nStaff Accountant:\n1. Enter checks and invoice into smashing system;\n2. Forget Dig Statements;\n3. Forget newspaper entries;\n4. Forget Outcome Statement, Balance Sheet and Statement of pickles\n5. Forget Wax returns;\n6. Perform other administrative duties;"
      }]
        experiences = process_experience(exp_list)
        self.assertEqual(len(experiences), 2)
        self.assertEqual(experiences[1].gap_after, None)  
        self.assertEqual(experiences[0].gap_after, 1)

    def test_process_experiences_empty(self):
        """Test processing an empty experience list"""
        experiences = process_experience([])
        self.assertEqual(experiences, [])

if __name__ == '__main__':
    unittest.main()