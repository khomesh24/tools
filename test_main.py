import unittest
import gdrive


class Test_Gdrive(unittest.TestCase):
    def test_success(self):
        obj = gdrive.GdriveDownloader()
        self.assertEqual(obj.download_file("credentials.json", "abc.txt", "My New Text Document"), 0)

    def test_failed_file_not_found(self):
        obj = gdrive.GdriveDownloader()
        self.assertEqual(obj.download_file("credentials.json", "", "file_doesnt_exit"),
                         'Error: File file_doesnt_exit not found')
