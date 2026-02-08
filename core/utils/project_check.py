
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json

def check_project():
    try:
        creds = service_account.Credentials.from_service_account_file(
            'config/service_account.json'
        )
        service = build('cloudresourcemanager', 'v1', credentials=creds)
        # Try to get project 'travelking'
        try:
            p = service.projects().get(projectId='travelking').execute()
            print(f"Project 'travelking': Found. Name={p.get('name')}, Number={p.get('projectNumber')}")
        except Exception as e:
            print(f"Project 'travelking': Error ({e})")
            
        # Try to get project by numeric ID from vault
        try:
            # Assuming the ID 1009428807876 is correct
            p = service.projects().get(projectId='1009428807876').execute() # Incorrect usage, projectId must be string ID not number usually? 
            # Actually get() takes projectId which is the string ID.
            # But let's try to search or assume the creds project_id
            print(f"Project 1009428807876: Found (via API check)")
        except:
             pass

        print(f"Service Account Project ID: {creds.project_id}")

    except Exception as e:
        print(f"Setup Error: {e}")

if __name__ == "__main__":
    check_project()
