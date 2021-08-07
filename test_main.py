import unittest
import gdrive as gd


class Test_Gdrive(unittest.TestCase):
    def test_success(self):
        obj = gd.GdriveDownloader()
        self.assertEqual(obj.download_file("credentials.json", "My New Text Document"), 0)

    def test_failed_file_not_found(self):
        obj = gd.GdriveDownloader()
        self.assertEqual(obj.download_file("credentials.json", "file_doesnt_exit"),
                         'Error: File file_doesnt_exit not found')
