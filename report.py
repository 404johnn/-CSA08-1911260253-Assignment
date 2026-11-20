from pathlib import Path
import csv

def write_summary(totals, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["register_number", "present", "absent"])
        for reg, count in sorted(totals.items()):
            writer.writerow([reg, count["P"], count["A"]])

def write_three_absent(register_numbers, output_path):
    Path(output_path).write_text("\n".join(register_numbers) + ("\n" if register_numbers else ""),
                                 encoding="utf-8")
