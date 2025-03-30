# Python GitHub Issue Importer

A simple and efficient Python tool to **automatically import GitHub issues** from a CSV file into your GitHub repository using the GitHub API. This tool is ideal for project management, task tracking, and automation in your development workflow.

## Features

- **Mass Import Issues**: Import multiple GitHub issues in one go from a CSV file.  
- **Customizable**: Easily configure the project by changing a few parameters (e.g., repository name, token, CSV file path).  
- **Authentication**: Uses personal access tokens for secure and easy authentication with GitHub.  
- **Error Handling**: Handles error responses gracefully and provides detailed error messages.  

## Requirements

- Python 3.6 or higher  
- `requests` library for API calls  

## Installation

### Clone the Repository

```bash
git clone https://github.com/FaraiB/csv-to-github.git
cd github-issue-importer
```

### Install Dependencies


If you don't have `requests` installed:

```bash
pip install requests
```

## Setup

### 1. GitHub Token

Generate a [Personal Access Token](https://github.com/settings/tokens) with the following scopes:
- `repo` (for public or private repositories)

### 2. CSV File

Prepare a `.csv` file with the following columns:

```csv
title,body,labels
"Fix login bug","User can't login due to cookie error","bug,frontend"
"Add dark mode","Implement dark mode toggle","feature,UI"
```

## Usage

Run the script and follow the onscreen instructions:

```bash
python import_issues.py
```

It will loop through the CSV and create an issue for each row.

## Error Handling

If any issue fails to create, the script will show the HTTP status and error message returned by the GitHub API (e.g., `401 Bad Credentials`, `404 Repository Not Found`).

## Contributing

Pull requests are welcome! If you have:
- Feature ideas  
- Bug reports  
- Suggestions to improve this tool  

Feel free to open an issue or a PR.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
