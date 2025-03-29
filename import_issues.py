import csv
import requests

# Ask the user for necessary inputs
GITHUB_TOKEN = input("Enter your GitHub Personal Access Token: ")
REPO_OWNER = input("Enter your GitHub username or organization name: ")
REPO_NAME = input("Enter the repository name: ")
CSV_FILE = input("Enter the CSV filename (with path, e.g. github_issues_full.csv): ")

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def create_issue(title, body):
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues'
    data = {'title': title, 'body': body}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f'✅ Created: {title}')
    else:
        print(f'❌ Failed: {title} | {response.status_code} - {response.text}')

def import_issues(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            create_issue(row['title'], row['body'])

if __name__ == '__main__':
    import_issues(CSV_FILE)
