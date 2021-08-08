import os.path
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload


class GdriveDownloader:
    def __init__(self):
        self.scope = ['https://www.googleapis.com/auth/drive']

    def get_token(self, cred_file):
        """
            Validate the token and refresh of required
        """
        creds = None
        # token.json store the temporary token, We are loading the token and refreshing it if expired.
        # If file is missing we are using the cred_file to create new token.
        if os.path.exists('token.json'):
            try:
                creds = Credentials.from_authorized_user_file('token.json', self.scope)
            except ConnectionError:
                print("Not able to connect to Google Apis")
                exit(1)

        if not creds or not creds.valid:
            try:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        cred_file, self.scope)
                    creds = flow.run_local_server(port=0)
            except ConnectionError as err:
                print(err)
                exit(1)

            # Save the credentials in token.json for next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        return creds

    def get_fileID(self, service, filename):
        """
            Get the fileID from filename
        """

        # Use service to fetch the list file from drive
        results = service.files().list(
            pageSize=1000, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        # Get the fileid from name and if file not found it will through an error
        file_id = ''
        for file in items:
            if filename == file['name']:
                file_id = file['id']
        return file_id

    def download_file(self, cred_file, output_file, filename):
        """
            Download the file using fileID and store file the output file
        """
        creds = self.get_token(cred_file)

        # Using Creds objects to create service request
        service = build('drive', 'v3', credentials=creds)

        file_id = self.get_fileID(service, filename)
        if file_id == '':
            return "Error: File " + filename + " not found"

        # Use service to download file from drive
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print('Download progress {0}'.format(status.progress() * 100))
        fh.seek(0)

        # Save the file in output file
        with open(output_file, 'wb') as f:
            f.write(fh.read())
            f.close()
        return 0

    def upload_file(self, cred_file, filename):
        """
            Upload file on drive
        """
        if os.path.exists(filename):
            creds = self.get_token(cred_file)

            # Using Creds objects to create service request
            service = build('drive', 'v3', credentials=creds)

            file_meta = {
                'name': filename
            }

            media = MediaFileUpload(filename, resumable=True)

            file = service.files().create(media_body=media,
                                          body=file_meta,
                                          fields='id').execute()

            print("File " + filename + " uploaded successfully")
            return file.get('id')
        else:
            print("File" + filename + " not found")
            return 1
