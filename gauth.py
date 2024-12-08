import os.path
import base64
from email import policy
from email.parser import BytesParser
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import imaplib

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    # Authenticate and return credentials
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def fetch_emails_from_last_30_days():
    # Fetch emails from the last 30 days and store them in an array.
    creds = authenticate_gmail()
    service_account_file = 'credentials.json'

    # Connect to Gmail IMAP server
    imap_server = 'imap.gmail.com'
    mail = imaplib.IMAP4_SSL(imap_server)

    # Use OAuth2 for authentication
    auth_string = f'user={creds.client_id}\1auth=Bearer {creds.token}\1\1'
    mail.authenticate('XOAUTH2', lambda x: auth_string)
    mail.select('inbox')

    # Define the date range for the last 30 days
    today = datetime.now()
    thirty_days_ago = today - timedelta(days=30)

    search_criteria = f'(SINCE {thirty_days_ago.strftime("%d-%b-%Y")})'

    # Search for all emails in the selected mailbox that match the criteria
    result, data = mail.search(None, search_criteria)
    email_ids = data[0].split()

    # Initialize an array to store email details
    emails_array = []

    # Fetch the email details and append them to the array
    for e_id in email_ids:
        result, msg_data = mail.fetch(e_id, '(RFC822)')
        raw_email = msg_data[0][1]
        email_message = BytesParser(policy=policy.default).parsebytes(raw_email)

        # Extract subject and sender for simplicity
        email_subject = email_message['Subject']
        email_from = email_message['From']

        # Append the extracted details to the array
        emails_array.append({'subject': email_subject, 'from': email_from})

    # Logout from the server
    mail.logout()

    return emails_array