import os
import requests
import base64
import json
from datetime import datetime

# Configuration
CODEFORCES_HANDLE = os.environ.get('CODEFORCES_HANDLE')
GITHUB_TOKEN = os.environ.get('PERSONAL_ACCESS_TOKEN')
GITHUB_REPO = os.environ.get('GITHUB_REPO')
GITHUB_API_URL = f'https://api.github.com/repos/{GITHUB_REPO}/contents/'

def get_accepted_submissions(handle):
    url = f'https://codeforces.com/api/user.status?handle={handle}&from=1&count=50'
    response = requests.get(url)
    accepted_submissions = []
    
    if response.status_code == 200:
        submissions = response.json().get('result', [])
        for submission in submissions:
            if submission['verdict'] == 'OK':
                submission_id = submission['id']
                problem_id = f"{submission['problem']['contestId']}{submission['problem']['index']}"
                programming_language = submission['programmingLanguage']
                accepted_submissions.append((submission_id, problem_id, programming_language))
    return accepted_submissions

def get_solution_code(submission_id):
    url = f'https://codeforces.com/contest/{submission_id//1000000}/submission/{submission_id}'
    response = requests.get(url)
    
    if response.status_code == 200:
        # Extract code from the HTML response (this is a simplified approach and might need adjustment)
        code_start = response.text.find('<pre id="program-source-text" class="prettyprint lang-cpp linenums program-source" style="padding: 0.5em;">')
        code_end = response.text.find('</pre>', code_start)
        if code_start != -1 and code_end != -1:
            code = response.text[code_start:code_end]
            return code.strip()
    return None

def commit_solution(problem_id, content, language):
    file_extension = '.cpp' if 'C++' in language else '.py' if 'Python' in language else '.txt'
    file_name = f'{problem_id}{file_extension}'
    url = GITHUB_API_URL + file_name
    
    commit_message = f'Auto-commit solution for {problem_id}'
    
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Check if file already exists
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # File exists, update it
        data = {
            'message': commit_message,
            'content': base64.b64encode(content.encode()).decode(),
            'sha': response.json()['sha']
        }
    else:
        # File doesn't exist, create it
        data = {
            'message': commit_message,
            'content': base64.b64encode(content.encode()).decode()
        }
    
    response = requests.put(url, headers=headers, json=data)
    return response.status_code in (201, 200)

def main():
    if not all([CODEFORCES_HANDLE, GITHUB_TOKEN, GITHUB_REPO]):
        print("Error: Missing environment variables. Please set CODEFORCES_HANDLE, GITHUB_TOKEN, and GITHUB_REPO.")
        return

    accepted_submissions = get_accepted_submissions(CODEFORCES_HANDLE)
    
    for submission_id, problem_id, language in accepted_submissions:
        solution_code = get_solution_code(submission_id)
        if solution_code:
            if commit_solution(problem_id, solution_code, language):
                print(f"Successfully committed solution for problem {problem_id}")
            else:
                print(f"Failed to commit solution for problem {problem_id}")
        else:
            print(f"Failed to retrieve solution code for problem {problem_id}")

if __name__ == '__main__':
    main()
