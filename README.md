A Python script to fetch and process candidate resume data from a remote url, extracting work experience and calculating gaps between jobs. Outputs are formatted as readable strings with dates displayed in "Jan/DD/YYYY" format.

## Features
- Fetches candidate data from a JSON API.
- Processes work experience into `Candidate` and `WorkExperience` objects.
- Calculates gaps between consecutive jobs in days.
- Displays dates in "Jan/DD/YYYY" format (e.g., "Jan/01/2008").

## Prerequisites
- `requests` library

## Usage
set the relevant url in the `CandidateManager.py` file at main, and run the script.

