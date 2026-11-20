def totals(records):
    result = {}
    for reg, date, status in records:
        result.setdefault(reg, {"P": 0, "A": 0})
        if status in ("P", "A"):
            result[reg][status] += 1
    return result

def percentage(present, working_days):
    return present / working_days * 100 if working_days else 0.0

def absent_three_consecutive(records):
    by_student = {}
    for reg, date, status in records:
        by_student.setdefault(reg, []).append((date, status))
    # Input dates are expected in YYYY-MM-DD order and one row per day.
    result = []
    for reg, rows in by_student.items():
        rows.sort()
        run = 0
        previous_date = None
        for date, status in rows:
            if status == "A":
                run = run + 1 if previous_date is not None else 1
                if run >= 3:
                    result.append(reg)
                    break
            else:
                run = 0
            previous_date = date
    return result
