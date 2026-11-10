# Student Grade Management System

A Python console application that accepts student marks, validates inputs, computes total & average scores, assigns letter grades, and presents individual report cards and class summaries.

---

## Features

1. **Input Validation**:
   - Ensures student and subject names are not left blank.
   - Restricts number of subjects to positive integers.
   - Enforces marks to be numerical values between `0` and `100`.

2. **Calculations**:
   - Calculates total score and percentage average.
   - Maps average scores to standard letter grades:
     - **A**: 90% – 100% (Excellent)
     - **B**: 80% – 89.9% (Very Good)
     - **C**: 70% – 79.9% (Good)
     - **D**: 60% – 69.9% (Pass)
     - **F**: Below 60% (Fail)

3. **Reporting & Statistics**:
   - Individual student report cards showing each subject's mark.
   - Class summary table with total, average, grade, and remarks.
   - Overall class statistics (class average, highest and lowest performers).

---

## How to Run

Run the script using Python:

```bash
python student_grade_system.py
```

