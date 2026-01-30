from config import STATUS_PRIORITY

def status_rank(s: str) -> int:
    return STATUS_PRIORITY.get(str(s), 0)

def dedup_student(merged_df, status_col = "Application Status", program_col = "Program Name"):
    