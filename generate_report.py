import subprocess
import os
import datetime

report_file = "client_report.txt"
modules = [f for f in os.listdir('.') if f.startswith('solution_')]

with open(report_file, "w") as f:
    f.write(f"System Audit Report - {datetime.datetime.now()}\n")
    f.write("="*40 + "\n")
    for module in modules:
        result = subprocess.run(["python3", module], capture_output=True, text=True)
        f.write(f"Module: {module}\n{result.stdout}\n")
        f.write("-" * 20 + "\n")

print(f"Report generated: {report_file}")
