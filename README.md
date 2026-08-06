# PrepTrack — Placement Preparation Performance Analyzer

---

# Project Title

**PrepTrack — Placement Preparation Performance Analyzer**

---

# Project Overview

PrepTrack is a Python-based console application designed to monitor and evaluate a student's placement preparation progress. The system captures student profile information, validates user inputs, records seven daily coding practice scores, and analyzes overall performance based on attendance and coding consistency.

The application generates a detailed performance report that includes attendance percentage, average coding score, highest and lowest scores, placement eligibility status, key improvement areas, and personalized recommendations to help students prepare effectively for placement interviews.
---

# Features Implemented

### Student Details Processing

- Student name validation using a `while` loop.
- Registration number input.
- Graduation year input.
- Attendance percentage validation (0–100).
- Project completion validation (`yes` / `no`).
- Profile verification validation (`yes` / `no`).

### Practice Score Processing

- Seven-day coding practice processing using a single `for` loop.
- Score validation (`0–100` or `-1` for absent).
- Absent day handling using `continue`.
- Score classification:
  - Strong (75–100)
  - Satisfactory (60–74)
  - Needs Improvement (40–59)
  - Critical (0–39)

### Performance Analysis

- Counts attempted, absent, passed, and failed days.
- Counts Strong, Satisfactory, Needs Improvement, and Critical days.
- Calculates total score and average score.
- Identifies highest and lowest attempted scores.
- Detects the first critical score.
- Prevents division-by-zero while calculating the average.

### Placement Readiness Evaluation

- Graduation year eligibility check.
- Attendance eligibility check.
- Practice attempt verification.
- Average score verification.
- Critical score verification.
- Passed practices verification.
- Project completion verification.
- Profile verification.
- Final placement readiness evaluation.

### Final Report

Displays:

- Student Profile
- Practice Summary
- Performance Analysis
- Critical Score Information
- Final Decision

---

# Python Concepts Used

| Category | Concepts |
|----------|----------|
| Input / Output | `input()`, `print()` |
| Type Casting | `int()`, `float()` |
| Data Types | String, Integer, Float, Boolean |
| Operators | Arithmetic, Relational, Logical |
| Conditional Statements | `if`, `elif`, `else` |
| Loops | `while`, `for`, `range()` |
| Loop Control | `break`, `continue` |
| Variables | Counters & Accumulators |
| Formatting | f-Strings |

---

# Project Structure

```text
preptrack-pavitra/
│
├── main.py
└── README.md
```

---

# Instructions to Run

```bash
python main.py
```

or

```bash
python3 main.py
```

---

# Test Result Summary

| Test ID | Scenario | Expected Result | Actual Result | Status |
|---------|----------|-----------------|---------------|--------|
| TC-01 | All eligibility conditions satisfied | Ready for Mock Interview | Ready for Mock Interview | ✅ Pass |
| TC-02 | Critical score detected | Critical Support Required | Critical Support Required | ✅ Pass |
| TC-03 | Fewer than six attempts | Practice Incomplete | Practice Incomplete | ✅ Pass |
| TC-04 | Fewer than four passed days | Insufficient Passed Practices | Insufficient Passed Practices | ✅ Pass |
| TC-05 | Average below 70 | Practice Improvement Required | Practice Improvement Required | ✅ Pass |
| TC-06 | Attendance below 75 | Attendance Improvement Required | Attendance Improvement Required | ✅ Pass |
| TC-07 | Graduation year outside eligible range | Graduation Criteria Not Met | Graduation Criteria Not Met | ✅ Pass |
| TC-08 | Project not completed | Application On Hold | Application On Hold | ✅ Pass |
| TC-09 | Profile not verified | Application On Hold | Application On Hold | ✅ Pass |
| TC-10 | All practice days absent | Practice Not Evaluated | Practice Not Evaluated | ✅ Pass |
| TC-11 | Invalid score below -1 | Input Rejected | Input Rejected | ✅ Pass |
| TC-12 | Invalid score above 100 | Input Rejected | Input Rejected | ✅ Pass |
| TC-13 | Boundary value testing | Correct Classification | Correct Classification | ✅ Pass |
| TC-14 | Multiple blockers | First Major Blocker Displayed | First Major Blocker Displayed | ✅ Pass |

---

# Individual Contribution

**Name:** Jayadithya Kuppam

**Repository URL:**

https://github.com/jayadithyakuppam/preptrack-jayadithya

### My Main Contribution

Built the complete PrepTrack application using Python, featuring student data management, input validation, coding score analysis, placement eligibility evaluation, and automated performance report generation with actionable recommendations.

### Features I Implemented

- Student profile validation
- Attendance validation
- Graduation year eligibility
- Project completion validation
- Profile verification validation
- Seven-day coding practice processing
- Absent day handling
- Score classification
- Passed and failed day counting
- Highest and lowest score detection
- First critical score detection
- Average score calculation
- Placement readiness evaluation
- Final report generation

### Python Concepts Used

Variables, Strings, Integers, Floats, Boolean Expressions, if-elif-else, while loops, for loops, break, continue, range(), Counters, Accumulators, Relational Operators, Logical Operators, and f-Strings.

### Most Difficult Logic

Implementing the placement readiness evaluation while maintaining the correct priority order for displaying the first major blocker when multiple eligibility conditions failed.

### Problem I Faced

Handling absent practice days without affecting the total score, average score, highest score, and lowest score calculations.

### How I Solved It

Used the `continue` statement to skip absent practice days and initialized highest and lowest score tracking only after the first valid practice score.

---

# Code Review Completed

| Reviewed Member | Repository Link | What Was Done Well | Issue Identified | Suggested Improvement |
|-----------------|-----------------|--------------------|------------------|-----------------------|
| Tarun | https://github.com/tarunbs16/preptrack-Tarun | The input validation and placement readiness logic were implemented clearly. The report formatting was well organized and easy to understand. | The invalid score message could provide clearer guidance to the user. | Updated the validation message to display **"Invalid score. Enter -1 or a value between 0 and 100."** |

---

# Feedback Received

**Reviewed By**

Tarun

**Feedback Received**

Improve the validation message for invalid practice scores by clearly mentioning the accepted input range.

**Was the Feedback Valid?**

Yes

**Change Made**

Updated the score validation message to:

`Invalid score. Enter -1 or a value between 0 and 100.`

**Commit Message Used**

```
Apply peer review feedback: improve score validation message
```

---

# Future Enhancements

- Store multiple student records.
- Generate PDF reports.
- Connect the application to a database.
- Develop a graphical user interface.
- Display graphical performance analysis.

---

# Author

**Jayadithya Kuppam**

B.Tech – Computer Science and Engineering (Data Science)

GitHub: https://github.com/jayadithyakuppam/preptrack-jayadithya
