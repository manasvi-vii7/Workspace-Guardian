import csv
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

def log_activity(
        objects,
        risk,
        score,
        state,
        verdict
):

    with open("logs/activity.csv", "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([

            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

             ", ".join(objects),

            risk,

            score,

            state,

            verdict

        ])