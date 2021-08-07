import gdrive as gd
import argparse


def main():
    parser = argparse.ArgumentParser(description='Download file from Google drive')
    parser.add_argument('filename', metavar='<filename>', help='Name of file to download')
    parser.add_argument('--cred', default='credentials.json', help="Credential json file \n"
                                                                   "(default: credentials.json) "
                                                                   "Refer https://developers.google.com/workspace"
                                                                   "/guides/create-credentials")
    args = parser.parse_args()

    obj = gd.GdriveDownloader()
    obj.download_file(args.cred, args.filename)


if __name__ == '__main__':
    main()
    '''a = gd.gdrive_downloader()
    #a.download_file('Khomesh_resume_latest')
    a.download_file('My New Text Document')
    '''
