from datetime import datetime


def get_current_time_for_db():
    # datetime object containing current date and time
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    