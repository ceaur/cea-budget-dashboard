import pandas as pd
from dataloader import load_data_pipeline
from config import NEEDED_COLUMNS
from utils import dedup_student

def calculate_costs():
    student_data, program_cost_data = load_data_pipeline()

    merged_df = pd.merge(student_data, program_cost_data, on='Program Name', how='left')
    deduplicated = dedup_student(merged_df=merged_df)



