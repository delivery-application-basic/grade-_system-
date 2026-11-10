"""
Student Grade Management System
A simple, robust Python CLI application to record student marks,
validate input, calculate averages and letter grades, and display summary reports.
"""

def get_letter_grade(average: float) -> str:
    """Determine the letter grade based on the average score."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_grade_description(grade: str) -> str:
    """Return a descriptive remark for the grade."""
    remarks = {
        "A": "Excellent",
        "B": "Very Good",
        "C": "Good",
        "D": "Pass",
        "F": "Fail",
    }
    return remarks.get(grade, "Unknown")


def get_valid_string(prompt: str) -> str:
    """Prompt user for a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [!] Input cannot be empty. Please try again.")


def get_valid_mark(subject_name: str) -> float:
    """Prompt user for a valid mark between 0 and 100."""
    while True:
        val_str = input(f"  Enter mark for {subject_name} (0 - 100): ").strip()
        try:
            mark = float(val_str)
            if 0.0 <= mark <= 100.0:
                return mark
            print("  [!] Mark must be between 0 and 100.")
        except ValueError:
            print("  [!] Invalid number. Please enter a numerical value.")


def get_valid_positive_int(prompt: str) -> int:
    """Prompt user for a positive integer."""
    while True:
        val_str = input(prompt).strip()
        try:
            val = int(val_str)
            if val > 0:
                return val
            print("  [!] Please enter an integer greater than 0.")
        except ValueError:
            print("  [!] Invalid input. Please enter a valid whole number.")


def add_student_record(students: list) -> None:
    """Collect student info, subject marks, calculate metrics, and save to list."""
    print("\n" + "=" * 45)
    print("            ADD STUDENT RECORD")
    print("=" * 45)

    name = get_valid_string("Enter student name: ")
    num_subjects = get_valid_positive_int("Enter number of subjects: ")

    marks = {}
    for i in range(1, num_subjects + 1):
        subject_name = get_valid_string(f"Name of subject #{i}: ")
        mark = get_valid_mark(subject_name)
        marks[subject_name] = mark

    total_marks = sum(marks.values())
    average = total_marks / num_subjects
    letter_grade = get_letter_grade(average)
    remark = get_grade_description(letter_grade)

    student_data = {
        "name": name,
        "marks": marks,
        "total": total_marks,
        "average": average,
        "grade": letter_grade,
        "remark": remark,
    }
    students.append(student_data)

    print("-" * 45)
    print(f" Record successfully saved for {name}!")
    print(f" Total: {total_marks:.2f} | Average: {average:.2f}% | Grade: {letter_grade} ({remark})")
    print("-" * 45)


def display_individual_reports(students: list) -> None:
    """Display detailed report cards for all students."""
    if not students:
        print("\n[!] No student records available to display.")
        return

    print("\n" + "#" * 50)
    print("               DETAILED REPORT CARDS")
    print("#" * 50)

    for idx, student in enumerate(students, start=1):
        print(f"\nStudent #{idx}: {student['name']}")
        print("-" * 40)
        print(f"{'Subject':<25} {'Mark':>10}")
        print("-" * 40)
        for subject, mark in student["marks"].items():
            print(f"{subject:<25} {mark:>10.2f}")
        print("-" * 40)
        print(f"{'Total Marks:':<25} {student['total']:>10.2f}")
        print(f"{'Average:':<25} {student['average']:>9.2f}%")
        print(f"{'Grade:':<25} {student['grade']:>10}")
        print(f"{'Remark:':<25} {student['remark']:>10}")
        print("=" * 40)


def display_class_summary(students: list) -> None:
    """Display a tabular overview and summary statistics for the whole class."""
    if not students:
        print("\n[!] No student records available to summarize.")
        return

    print("\n" + "=" * 65)
    print(f"{'NAME':<20} {'TOTAL':<10} {'AVERAGE':<12} {'GRADE':<8} {'REMARK':<12}")
    print("=" * 65)

    for s in students:
        avg_str = f"{s['average']:.2f}%"
        print(
            f"{s['name']:<20} "
            f"{s['total']:<10.2f} "
            f"{avg_str:<12} "
            f"{s['grade']:<8} "
            f"{s['remark']:<12}"
        )
    print("=" * 65)

    # Class statistics
    averages = [s["average"] for s in students]
    class_avg = sum(averages) / len(averages)
    top_student = max(students, key=lambda s: s["average"])
    lowest_student = min(students, key=lambda s: s["average"])

    print("\n--- CLASS STATISTICS ---")
    print(f"Total Students  : {len(students)}")
    print(f"Class Average   : {class_avg:.2f}%")
    print(f"Top Performer   : {top_student['name']} ({top_student['average']:.2f}%, Grade {top_student['grade']})")
    print(f"Lowest Performer: {lowest_student['name']} ({lowest_student['average']:.2f}%, Grade {lowest_student['grade']})")
    print("------------------------\n")


def main() -> None:
    """Main menu loop for the grade management system."""
    students = []

    while True:
        print("\n=========================================")
        print("    STUDENT GRADE MANAGEMENT SYSTEM")
        print("=========================================")
        print("1. Add New Student Record")
        print("2. View All Student Report Cards")
        print("3. View Class Summary Table & Statistics")
        print("4. Exit")
        print("=========================================")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            add_student_record(students)
        elif choice == "2":
            display_individual_reports(students)
        elif choice == "3":
            display_class_summary(students)
        elif choice == "4":
            print("\nExiting Student Grade Management System. Goodbye!\n")
            break
        else:
            print("\n[!] Invalid choice! Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
