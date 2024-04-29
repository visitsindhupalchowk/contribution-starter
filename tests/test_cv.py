import unittest
import os
import re


class TestCV(unittest.TestCase):
    def test_cv_requirements(self):
        required_sections = [
            "Personal Details",
            "Objective",
            "Education",
            "Work Experience",
            "Skills",
            "Interests and Hobbies",
            "References",
        ]
        cv_directory = "cv/"
        cv_files = [f for f in os.listdir(cv_directory) if f.endswith(".md")]

        for cv_file in cv_files:
            cv_path = os.path.join(cv_directory, cv_file)
            with self.subTest(cv_file=cv_file):
                self.assertTrue(
                    os.path.exists(cv_path), f"CV file '{cv_file}' not found"
                )

                with open(cv_path, "r") as file:
                    # Convert content to lowercase for case-insensitive matching
                    content = file.read().lower()
                    # Check each required section separately
                    missing_sections = []
                    for section in required_sections:
                        # Use regex to search for the section ignoring case
                        pattern = re.compile(
                            rf"^#\s*{re.escape(section)}\s*$",
                            re.IGNORECASE | re.MULTILINE,
                        )
                        if not pattern.search(content):
                            missing_sections.append(section)
                    # If any required section is missing, fail the test
                    self.assertFalse(
                        missing_sections,
                        f"Required section(s) '{', '.join(missing_sections)}' missing in CV '{cv_file}'",
                    )


if __name__ == "__main__":
    unittest.main()
