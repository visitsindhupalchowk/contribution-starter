# Contribution Starter

Contribution Starter is an open source project created to facilitate the journey of newcomers in the field of computer science and open source contribution. This project aims to provide a welcoming environment where beginners can learn about GitHub issues, pull requests, and the process of contributing to open source projects.

## Purpose

The purpose of Contribution Starter is to guide individuals who are just starting their journey in computer science and want to learn about GitHub issues, pull requests, and contributions to open source projects. By providing step-by-step guidance and resources, Contribution Starter aims to empower beginners to become confident contributors to the open source community.

## How It Helps?

Contribution Starter helps beginners by:

- Providing clear instructions on how to get started with Git and GitHub.
- Offering guidance on adding their [CV](docs/CV_GUIDLINE.md) as a README file to personalize their contributions.
- Encouraging contributions to documentation, issue resolution, and pull requests to build practical skills.
- Offering opportunities for beginners to progress to more complex projects and gain confidence in their abilities.

## Who Is This For?

Contribution Starter is for individuals who are:

- New to computer science and looking to learn about GitHub and open source contribution.
- Interested in building their skills through practical experience in a supportive community.
- Seeking guidance and mentorship as they begin their journey in open source development.

Whether you're a student, self-learner, or career changer, Contribution Starter is designed to help you take your first steps into the world of open source contribution.

## How To Contribute?

For contribution, please refer to our [Contribution Guidelines](docs/CONTRIBUTING.md)

## Project Structure and Purpose

The structure of the project is as follows:
```
contribution-starter/
    ├── .github
    |    ├── ISSUE_TEMPLATE/
    |    |       ├── bug-report.yaml
    |    |       ├── config.yaml
    |    |       ├── custom-issue.yaml
    |    |       ├── docs.yaml
    |    |       └── feature-request.yaml
    |    ├── workflows/
    |    |       ├── properties/
    |    |       ├── greetings.yaml
    |    |       ├── lint.yaml
    |    |       └── test_cv_on_pr.yml
    |    └── PULL_REQUEST_TEMPLATE.md
    ├── cv/
    |    ├── YourGitHubUsername1.md
    |    └── YourGitHubUsername2.md
    ├── docs/
    |    ├── CONTRIBUTING.md
    │    └── CV_GUIDELINE.md
    ├── tests/
    │    └── test_cv.py
    ├── .editorconfig
    ├── .gitignore
    ├── .pre-commit-config.yaml
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    └── ruff.toml     
```
The purpose of the files is as follows:
- **contribution-starter/**
  - **.github/**
    - **ISSUE_TEMPLATE/**
      - `bug-report.yaml`: Template for reporting bugs.
      - `config.yaml`: Configuration for issue templates.
      - `custom-issue.yaml`: Template for custom issues.
      - `docs.yaml`: Template for documentation-related issues.
      - `feature-request.yaml`: Template for requesting new features.
    - **workflows/**
      - **properties/**: (Assumed) Directory for storing workflow property files.
      - `greetings.yaml`: GitHub Actions workflow for greeting new contributors.
      - `lint.yaml`: GitHub Actions workflow for linting code.
      - `test_cv_on_pr.yml`: GitHub Actions workflow for testing CV submissions on pull requests.
    - `PULL_REQUEST_TEMPLATE.md`: Template for pull requests.
  - **cv/**
    - `YourGitHubUsername1.md`: Example CV file for the first user.
    - `YourGitHubUsername2.md`: Example CV file for the second user.
  - **docs/**
    - `CONTRIBUTING.md`: Guidelines for contributing to the project.
    - `CV_GUIDELINE.md`: Guidelines for creating and submitting CVs.
  - **tests/**
    - `test_cv.py`: Tests for the CV submission functionality.
  - `.editorconfig`: Configuration for consistent coding styles between different editors.
  - `.gitignore`: Specifies files and directories to ignore in the repository.
  - `.pre-commit-config.yaml`: Configuration for pre-commit hooks.
  - `LICENSE`: License for the project.
  - `README.md`: Overview and instructions for the project.
  - `requirements.txt`: List of dependencies for the project.
  - `ruff.toml`: Configuration for the Ruff linter.

Ready to start your journey? Fork this repository and let's get started!
