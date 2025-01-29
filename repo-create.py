# import requests
# import json
# import sys
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Get GitHub token from environment variables
# GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# if not GITHUB_TOKEN:
#     print("Error: GITHUB_TOKEN is not set in env file")
#     sys.exit(1)

# # Read repository names from command-line arguments
# app_repo_name = sys.argv[1]
# infra_repo_name = sys.argv[2]

# # Define the template repository names (Update these variables)
# app_template_repo = 'iriska09/template-app-repo'
# infra_template_repo = 'iriska09/template-infra-repo'

# # Function to create a GitHub repository from a template
# def create_repo_from_template(template_repo, repo_name):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {GITHUB_TOKEN}',
#     }

#     data = {
#         "name": repo_name,
#         "include_all_branches": False,
#         "private": True
#     }

#     response = requests.post(
#         f'https://api.github.com/repos/{template_repo}/generate',
#         headers=headers,
#         data=json.dumps(data)
#     )

#     if response.status_code == 201:
#         print(f"Repository '{repo_name}' created successfully from template '{template_repo}'.")
#     else:
#         print(f"Failed to create repository from template '{template_repo}': {response.json()}")

# # Create the App repo from the app template
# create_repo_from_template(app_template_repo, app_repo_name)

# # Create the Infra repo from the infra template
# create_repo_from_template(infra_template_repo, infra_repo_name)

#//////
import requests
import json
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get GitHub token from environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN is not set in env file")
    sys.exit(1)

# Read repository names from command-line arguments
app_repo_name = sys.argv[1]
infra_repo_name = sys.argv[2]

# Define the template repository names (Update these variables)
app_template_repo = 'iriska09/template-app-repo'
infra_template_repo = 'iriska09/template-infra-repo'

# Function to create a GitHub repository from a template
def create_repo_from_template(template_repo, repo_name):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {GITHUB_TOKEN}',
    }

    data = {
        "name": repo_name,
        "include_all_branches": False,
        "private": True
    }

    response = requests.post(
        f'https://api.github.com/repos/{template_repo}/generate',
        headers=headers,
        data=json.dumps(data)
    )

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully from template '{template_repo}'.")
    else:
        print(f"Failed to create repository from template '{template_repo}': {response.json()}")

# Create the App repo from the app template
create_repo_from_template(app_template_repo, app_repo_name)

# Create the Infra repo from the infra template
create_repo_from_template(infra_template_repo, infra_repo_name)
