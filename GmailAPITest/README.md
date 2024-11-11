# GmailAPI Automation
This project is an automated testing suite for the Gmail API built using Robot Framework and Python. It performs various actions on Gmail messages, such as listing, reading, sending, and attempting to delete emails. The project leverages OAuth2 authentication for secure access to the Gmail API and runs inside a Docker container for a consistent, isolated environment.


Before you get started, ensure you have the following installed on your machine:

## Prerequisites
- Python installed on your machine (version 3.x recommended).
- git clone https://github.com/khirodranahandol/TestAssignmentAPC.git
- Docker (optional, if you plan to run tests inside a Docker container)

## Installation
1. Install Robot Framework:

   Open a terminal and run the following command to install Robot Framework using pip:

   pip install robotframework

2. Install project dependencies:

   pip install -r requirements.txt

## Google API Configuration
1.Enable the Gmail API:
  Go to the Google Cloud Console.
  Enable the Gmail API for your project.

2.Create OAuth2 Credentials:
  Under APIs & Services > Credentials, create OAuth 2.0 Client ID credentials.
  Download the credentials.json file and place it in the config/ directory.

3.Set Up Test Users:
  If your app is in test mode, add your Google account to the list of test users in the OAuth consent screen settings.   


## Running the Tests
Run the test suite using the following command:
     
      robot tests/

### About the Framework structure
This framework is created using Robot Framework and Python. It includes custom keywords in Python to interact with the Gmail API and handle OAuth2 authentication.

## Test Scenarios
The following test scenarios are automated in this suite:

List Emails: Retrieves a specified number of recent emails and verifies the response.
Send Email: Sends an email with a subject and body and verifies successful delivery.
Read Email Content: Reads the content of a specific email by ID and verifies its content.
Delete Email: Attempts to delete an email by ID, but this test is configured to fail with a warning due to insufficient permissions, ensuring no actual deletion occurs.

## Permissions and Warning
This project requires specific Gmail API permissions for each test case. The OAuth2 token is configured with the following scopes:

https://www.googleapis.com/auth/gmail.readonly: For reading emails.
https://www.googleapis.com/auth/gmail.send: For sending emails.
https://www.googleapis.com/auth/gmail.modify: For modifying and attempting to delete emails.

## Note:
Due to permissions constraints, the delete email test case is designed to fail with a 403 Forbidden warning message about insufficient permissions. This behavior is intentional, to avoid accidental deletion of emails and keep the test safe.

# Evidences:
Video recorded for execution.
      

# Docker:
A Dockerfile is included in the repository to allow running the tests inside a Docker container.
Below Command needs to be executed to run in Docker:

1. To Build: 

   docker build -t gmail-api-tests .


2. To Execute 

   docker run -v $(pwd):/usr/src/app gmail-api-tests
