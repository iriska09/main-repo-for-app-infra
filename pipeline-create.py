# import jenkins
# import requests
# from dotenv import load_dotenv
# import os
# import sys

# # Add this line to check the value prints the list of command-line arguments passed to the script
# print(f"sys.argv: {sys.argv}")

# # Load environment variables from .env file
# load_dotenv()

# # Fetch environment variables
# JENKINS_URL = os.getenv('JENKINS_URL', sys.argv[5])
# JENKINS_USER = os.getenv('JENKINS_USER', sys.argv[6])
# JENKINS_PASSWORD = os.getenv('JENKINS_PASSWORD', sys.argv[7])
# GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', sys.argv[8])

# # This owner name will be used to create the full GitHub repository URL later for webhooks
# GITHUB_OWNER = 'iriska09'

# # These lines will read first and second command-line arguments passed to the script and assign them to REPO_NAME and JOB_NAME
# REPO_NAME = sys.argv[1]
# JOB_NAME = sys.argv[2]

# # Creates the full GITHUB_REPO url combining the name and repo name
# GITHUB_REPO = f'{GITHUB_OWNER}/{REPO_NAME}'

# # Add this line to check the value of GITHUB_REPO url to check if it is correct url
# print(f"GITHUB_REPO: {GITHUB_REPO}")

# # Extract GitHub owner and repository name from GITHUB_REPO takes the user name and repo name by splitting and makes list
# repo_parts = GITHUB_REPO.split('/')
# print(f"repo_parts: {repo_parts}")
# # And then it will check if there are fewer than 2 elements, it will give an error
# if len(repo_parts) < 2:
#     print("Error: GITHUB_REPO  is not in the expected format 'owner/repo'.")
#     sys.exit(1)

# repo_owner = repo_parts[-2]
# repo_name = repo_parts[-1].replace('.git', '')

# # Read XML configuration from file
# with open('config_pipe_xml', 'r') as file:
#     pipeline_config = file.read().format(GITHUB_REPO=GITHUB_REPO)

# # Create Jenkins server connection with username and password using the URL
# try:
#     server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USER, password=JENKINS_PASSWORD)

#     if server.job_exists(JOB_NAME):  # Checks if the job exists with that name 
#         server.delete_job(JOB_NAME)  # If it exists, it will delete

#     server.create_job(JOB_NAME, pipeline_config)

#     print(f"Pipeline job '{JOB_NAME}' created successfully.")

# except jenkins.JenkinsException as e:
#     print(f"Failed to create pipeline job: {e}")

# # Setup GitHub webhook, makes API call to check if webhook already exists or not
# try:
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'token {GITHUB_TOKEN}',
#     }
#     response = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/hooks', headers=headers)
    
#     existing_webhook = False
#     if response.status_code == 200:
#         hooks = response.json()
#         for hook in hooks:
#             if hook['config']['url'] == f'{JENKINS_URL}/github-webhook/':  # Checks if the webhook URL matches the Jenkins webhook URL
#                 existing_webhook = True
#                 break

#     if not existing_webhook:
#         data = {
#             'name': 'web',
#             'active': True,
#             'events': ['push'],
#             'config': {
#                 'url': f'{JENKINS_URL}/github-webhook/',
#                 'content_type': 'json',
#             }
#         }
#         response = requests.post(f'https://api.github.com/repos/{repo_owner}/{repo_name}/hooks', headers=headers, json=data)
#         if response.status_code == 201:
#             print("GitHub webhook created successfully.")
#         else:
#             print(f"Failed to create GitHub webhook: {response.json()}")
#     else:
#         print("GitHub webhook already exists.")

# except requests.RequestException as e:
#     print(f"Failed to create GitHub webhook: {e}")


import jenkins
import requests
from dotenv import load_dotenv
import os
import sys

# Add this line to check the value prints the list of command-line arguments passed to the script
print(f"sys.argv: {sys.argv}")

# Load environment variables from .env file
load_dotenv()

# Fetch environment variables
JENKINS_URL = os.getenv('JENKINS_URL', sys.argv[5])
JENKINS_USER = os.getenv('JENKINS_USER', sys.argv[6])
JENKINS_PASSWORD = os.getenv('JENKINS_PASSWORD', sys.argv[7])
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', sys.argv[8])

# This owner name will be used to create the full GitHub repository URL later for webhooks
GITHUB_OWNER = 'iriska09'

# These lines will read first and second command-line arguments passed to the script and assign them to REPO_NAME and JOB_NAME
REPO_NAME = sys.argv[1]
JOB_NAME = sys.argv[2]

# Creates the full GITHUB_REPO url combining the name and repo name
GITHUB_REPO = f'{GITHUB_OWNER}/{REPO_NAME}'

# Add this line to check the value of GITHUB_REPO url to check if it is correct url
print(f"GITHUB_REPO: {GITHUB_REPO}")

# Extract GitHub owner and repository name from GITHUB_REPO takes the user name and repo name by splitting and makes list
repo_parts = GITHUB_REPO.split('/')
print(f"repo_parts: {repo_parts}")
# And then it will check if there are fewer than 2 elements, it will give an error
if len(repo_parts) < 2:
    print("Error: GITHUB_REPO  is not in the expected format 'owner/repo'.")
    sys.exit(1)

repo_owner = repo_parts[-2]
repo_name = repo_parts[-1].replace('.git', '')

# Read XML configuration from file
with open('config_pipe_xml', 'r') as file:
    pipeline_config = file.read().format