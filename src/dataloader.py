from pathlib import Path
import pandas as pd
from config import PROGRAM_COST_PATH, APPLICANT_DATA_PATH, STUDENTS_NEEDED_COLUMNS, COST_NEEDED_COLUMS

def get_latest_file(dir_path: str) -> Path | None:
    p = Path(dir_path)
    files = list(p.glob('*.csv'))
    if not files:
        return None
    
    return max(files, key=lambda f: f.stat.st_mtime)

def load_dataframe(file_path: Path | None) -> pd.DataFrame | None:
    if file_path is None: 
        print("No matching files found")
    return pd.read_csv(file_path)

def load_data_pipeline(dir_path: str) -> pd.DataFrame:
    applicant_file_path = get_latest_file(dir_path=APPLICANT_DATA_PATH)
    applicant_dataframe = load_dataframe(file_path=APPLICANT_DATA_PATH)

    program_cost_file_path = get_latest_file(dir_path=PROGRAM_COST_PATH)
    program_cost_dataframe = load_dataframe(file_path=PROGRAM_COST_PATH)
    

    return applicant_dataframe[STUDENTS_NEEDED_COLUMNS], program_cost_dataframe[COST_NEEDED_COLUMS]