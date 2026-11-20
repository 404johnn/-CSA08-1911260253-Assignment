"""Attendance processing package."""
from .reader import read_records
from .stats import totals, percentage, absent_three_consecutive
from .report import write_summary, write_three_absent
