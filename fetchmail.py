import gauth
import imaplib
from datetime import datetime, timedelta

import os.path
import base64
from email import policy
from email.parser import BytesParser
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import imaplib


def fetch_emails_from_last_30_days():
    # Fetch emails from the last 30 days and store them in an array.
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