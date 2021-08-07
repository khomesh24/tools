import os.path
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaIoBaseDownload


class GdriveDownloader:
    def __init__(self):
        self.scope = ['https://www.googleapis.com/auth/drive']

    def download_file(self, cred_file, file_name):
        creds = None

        '''
        token.json store the temporary token, We are loading the token and refreshing it if expired.
        If file is missing we are using the cred_file to create new token.
        '''
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.scope)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    cred_file, self.scope)
                creds = flow.run_local_server(port=0)

            '''
            Save the credentials in token.json for next run
            '''
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        '''
        Using Creds objects to create service request
        '''
        service = build('drive', 'v3', credentials=creds)

        '''
        Use service to fetch the list file from drive
        '''
        results = service.files().list(
            pageSize=1000, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        '''
        Get the fileid from name and if file not found it will through an error
        '''
        file_id = ''
        for file in items:
            if file_name == file['name']:
                file_id = file['id']
        if file_id == '':
            return "Error: File " + file_name + " not found"

        '''
        Use service to download file from drive
        '''
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print('Download progress {0}'.format(status.progress() * 100))
        fh.seek(0)
        with open(file_name, 'wb') as f:
            f.write(fh.read())
            f.close()
        return 0
