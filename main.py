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
    result = obj.download_file(args.cred, args.filename)
    if result == 0:
        print("Successfully downloaded {0}".format(args.filename))
        exit(0)
    else:
        print(result)
        exit(1)


if __name__ == '__main__':
    main()  
