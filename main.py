# from gauth import authenticate_gmail
import gauth
import ollamaresponse
import fetchmail

import sys
print(sys.path)
sys.path.append('C:\code\ollama-auto') 
print("after: " + sys.path)


def main():
    auth = gauth.authenticate_gmail()
    emails = fetchmail.fetch_emails_from_last_30_days(auth)
    print(emails)



if __name__ == '__main__':
    main()