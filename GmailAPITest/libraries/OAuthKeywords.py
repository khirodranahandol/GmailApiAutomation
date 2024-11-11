import json
import os
import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

class OAuthKeywords:
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
              'https://www.googleapis.com/auth/gmail.send']

    def authenticate_gmail_api(self):
        """Authenticates Gmail API and returns credentials."""
        creds = None
        token_file = 'config/token.json'
        credentials_file = 'config/credentials.json'

        # Check if token.json exists for cached credentials
        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, self.SCOPES)
        
        # If no valid credentials, go through OAuth flow
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(google.auth.transport.requests.Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_file, self.SCOPES)
                creds = flow.run_local_server(port=8080)

            # Save the credentials for future use
            with open(token_file, 'w') as token:
                token.write(creds.to_json())

        return creds
