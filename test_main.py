import unittest
from gdrive import GdriveDownloader

credentialFile = 'credentials.json'
filename = 'abc.txt'
outputFile = 'xyz.txt'


class test_Gdrive(unittest.TestCase):
    def test_upload(self):
        obj = GdriveDownloader()
        fileID = obj.upload_file(credentialFile, filename)
        self.assertIsNotNone(fileID)

    def test_success(self):
        obj = GdriveDownloader()
        self.assertEqual(obj.download_file(credentialFile, outputFile, filename), 0)

    def test_failed_file_not_found(self):
        obj = GdriveDownloader()
        self.assertEqual(obj.download_file(credentialFile, "", "file_doesnt_exit"),
                         'Error: File file_doesnt_exit not found')
