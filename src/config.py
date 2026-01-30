# define where our data will be stored
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # project root

APPLICANT_DATA_PATH = BASE_DIR / "data" / "Applicants"
PROGRAM_COST_PATH = BASE_DIR / "data" / "ProgramCosts"

STUDENTS_NEEDED_COLUMNS = [
    'User ID', 'Name', 'User Last Name', 'User First Name', 
    'Program Name', 'Program Type', 'Program Group',
    'Program Year', 'Program Term', 'Application Status', 'Phase'
]

COST_NEEDED_COLUMS = [
    'Program Name', 'Cost'
]

# statuses we consider "approved" for the dashboard
APPROVED_STATUSES = [
    "Committed",
    "Accepted",
    "Permission to Study Abroad: Granted",
    "Provisional Permission",
]

# and their priority for de-dup
STATUS_PRIORITY = {
    "Committed": 4,
    "Accepted": 3,
    "Permission to Study Abroad: Granted": 2,
    "Provisional Permission": 1,
}