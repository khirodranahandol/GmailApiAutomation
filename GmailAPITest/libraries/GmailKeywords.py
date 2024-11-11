from googleapiclient.discovery import build
from libraries.OAuthKeywords import OAuthKeywords

class GmailKeywords:
    def __init__(self):
        self.creds = OAuthKeywords().authenticate_gmail_api()
        self.service = build('gmail', 'v1', credentials=self.creds)

    def list_emails(self, max_results=10):
        """Lists the latest emails."""
        results = self.service.users().messages().list(userId='me', maxResults=max_results).execute()
        return results.get('messages', [])

    def get_email_content(self, message_id):
        """Retrieves the email content by message ID."""
        message = self.service.users().messages().get(userId='me', id=message_id).execute()
        return message

    def send_email(self, to, subject, body):
        """Sends an email."""
        message = {
            'raw': self._create_base64_email(to, subject, body)
        }
        return self.service.users().messages().send(userId='me', body=message).execute()

    def delete_email(self, message_id):
        """Deletes an email by message ID."""
        return self.service.users().messages().delete(userId='me', id=message_id).execute()

    def _create_base64_email(self, to, subject, body):
        """Helper to format email content as base64."""
        import base64
        from email.mime.text import MIMEText
        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject
        return base64.urlsafe_b64encode(message.as_bytes()).decode()
