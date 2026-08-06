# ==================================================
# PREPTRACK — BOILERPLATE CODE
# Complete every section marked TODO.
# ==================================================

print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------

# TODO: Validate that the student name is not empty.
student_name = input("Enter student name: ")

while not student_name.strip():
    print("Student name cannot be empty.")
    student_name = input("Enter student name: ")

registration_number = input("Enter registration number: ")

graduation_year = int(input("Enter graduation year: "))

graduation_eligible = ( graduation_year >= 2025 and graduation_year <= 2027)

# TODO: Validate attendance between 0 and 100.
attendance = float(input("Enter attendance percentage: "))
while not (0 <= attendance <= 100):
    print("Invalid attendance . Attendance must be between 0 and 100.")
    attendance = float(input("Enter attendance percentage: "))
print("Attendance accepted")

# TODO: Accept only yes or no.
project_input = input(
    "Has the student completed the required project? Enter yes or no: "
)


while not (project_input == "yes" or project_input == "no"):
    print("Invalid input. Enter yes or no.")
    project_input = input("Enter yes or no: ")
    

# TODO: Convert project_input into True or False.
if project_input == "yes":
    project_completed = True
else:
    project_completed = False

# TODO: Accept only yes or no.
profile_input = input(
    "Is the student profile verified? Enter yes or no: "
)

while not (profile_input == "yes" or profile_input == "no"):
    print("Invalid profile input. Please enter yes or no.")
    profile_input = input("Enter yes or no: ")
if profile_input == "yes":
    profile_verified=True
else:
    profile_verified=False
# TODO: Convert profile_input into True or False.profile_verified = False


# --------------------------------------------------
# 2. INITIALIZE COUNTERS AND VARIABLES
# --------------------------------------------------

total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0


# --------------------------------------------------
# 3. PROCESS SEVEN PRACTICE DAYS
# --------------------------------------------------

for day in range(1, 8):

    # TODO: Use a while loop to accept only:
    # -1 or a score between 0 and 100.
    while True:
        score = int(
            input(f"Enter Day {day} score from 0 to 100, "
               "or -1 for absent: "
            )
        )

        if score == -1 or (score >= 0 and score <= 100):
             break

        print("Invalid score. Enter -1 or a value between 0 and 100.")
    
    # TODO: Handle absence.
    # Increase absent_days and use continue.
    if score==-1:
        absent_days+=1
        print(f"Day {day} Result: Absent")
        continue

    # TODO: Increase attempted_days and total_score.
    attempted_days+=1
    total_score+=score

    # TODO: Initialize or update:
    # highest_score, highest_score_day,
    # lowest_score and lowest_score_day.
    if not first_attempt_found:
        highest_score=score
        highest_score_day=day
        lowest_score=score
        lowest_score_day=day
        first_attempt_found=True
    else:
        if score>highest_score:
            highest_score=score
            highest_score_day=day
        if score<lowest_score:
            lowest_score=score
            lowest_score_day=day

    # TODO: Classify the score:
    # 75–100  -> Strong
    # 60–74   -> Satisfactory
    # 40–59   -> Needs Improvement
    # 0–39    -> Critical
    if score >= 75:
        print(f"Day {day} Result: Strong")
        strong_days += 1
        passed_days += 1
    elif score >= 60:
        print(f"Day {day} Result: Satisfactory")
        satisfactory_days += 1
        passed_days += 1
    elif score >= 40:
        print(f"Day {day} Result: Needs Improvement")
        improvement_days += 1
        failed_days += 1
    else:
        print(f"Day {day} Result: Critical")
        critical_days += 1
        failed_days += 1

    # TODO: Store only the first critical day and score.
    if score <= 39 and not critical_score_found:
        first_critical_day = day
        first_critical_score = score
        critical_score_found = True


# --------------------------------------------------
# 4. CALCULATE THE AVERAGE
# --------------------------------------------------

# TODO: Prevent division by zero.
average_score = 0
if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0



# --------------------------------------------------
# 5. CREATE ELIGIBILITY CONDITIONS
# --------------------------------------------------

graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)

attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)


# --------------------------------------------------
# 6. DETERMINE FINAL STATUS
# --------------------------------------------------

# TODO: Check conditions in this priority:
# 1. No practice attempted
# 2. Critical score found
# 3. Fewer than six attempts
# 4. Fewer than four passed days
# 5. Average below 70
# 6. Attendance below 75
# 7. Graduation year not eligible
# 8. Project incomplete
# 9. Profile not verified
# 10. Ready for Mock Interview
final_status = ""
primary_blocker = ""
next_action = ""

if attempted_days == 0:
    final_status = "No practice attempted"
    primary_blocker = "No practice attempted"
    next_action = "Attend practice sessions"
elif not critical_score_clear:
    final_status = "Critical score found"
    primary_blocker = "Critical score found"
    next_action = "Improve critical scores"
elif not practice_count_eligible:
    final_status = "Fewer than six attempts"
    primary_blocker = "Fewer than six attempts"
    next_action = "Attend more practice sessions"
elif not passed_days_eligible:
    final_status = "Fewer than four passed days"
    primary_blocker = "Fewer than four passed days"
    next_action = "Pass more days"
elif not average_eligible:
    final_status = "Average score below 70"
    primary_blocker = "Average score below 70"
    next_action = "Improve average score"
elif not attendance_eligible:
    final_status = "Attendance below 75"
    primary_blocker = "Attendance below 75"
    next_action = "Improve attendance"
elif not graduation_eligible:
    final_status = "Graduation year not eligible"
    primary_blocker = "Graduation year not eligible"
    next_action = "Check eligibility"
elif not project_completed:
    final_status = "Project incomplete"
    primary_blocker = "Project incomplete"
    next_action = "Complete project"
elif not profile_verified:
    final_status = "Profile not verified"
    primary_blocker = "Profile not verified"
    next_action = "Verify profile"
else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Attend mock interview"



# --------------------------------------------------
# 7. DISPLAY FINAL REPORT
# --------------------------------------------------

print()
print("=" * 50)
print("              PREPTRACK REPORT")
print("=" * 50)
print()
print("STUDENT PROFILE")
print()
print(f"Student Name           : {student_name}")
print(f"Registration Number    : {registration_number}")
print(f"Graduation Year        : {graduation_year}")
print(f"Attendance             : {attendance}%")
print(f"Project Completed      : {'Yes' if project_completed else 'No'}")
print(f"Profile Verified       : {'Yes' if profile_verified else 'No'}")
print()

print("PRACTICE SUMMARY")
print()
print(f"Attempted Days         : {attempted_days}")
print(f"Absent Days            : {absent_days}")
print(f"Passed Days            : {passed_days}")
print(f"Failed Days            : {failed_days}")

print()
print(f"Strong Days            : {strong_days}")
print(f"Satisfactory Days      : {satisfactory_days}")
print(f"Needs Improvement Days : {improvement_days}")
print(f"Critical Days          : {critical_days}")
print()
print("PERFORMANCE ANALYSIS")
print()
print(f"Total Score            : {total_score}")
print(f"Average Score          : {average_score:.2f}")
if attempted_days > 0:
    print(f"Highest Score          : {highest_score}")
    print(f"Highest Score Day      : Day {highest_score_day}")
    print(f"Lowest Score           : {lowest_score}")
    print(f"Lowest Score Day       : Day {lowest_score_day}")
else:
    print("Highest Score          : Not Available")
    print("Highest Score Day      : Not Available")
    print("Lowest Score           : Not Available")
    print("Lowest Score Day       : Not Available")

# TODO: Display first critical details only when
# a critical score exists.

print()
print("CRITICAL SCORE INFORMATION")
print()
print(f"Critical Score Found   : {'Yes' if critical_score_found else 'No'}")
if critical_score_found:
    print(f"First Critical Day     : Day {first_critical_day}")
    print(f"First Critical Score   : {first_critical_score}")
else:
    print("First Critical Day     : Not Applicable")
    print("First Critical Score   : Not Applicable")
print()
print("FINAL DECISION")
print()
print(f"Final Status           : {final_status}")
print(f"Primary Blocker        : {primary_blocker}")
print(f"Next Action            : {next_action}")

print("=" * 50)