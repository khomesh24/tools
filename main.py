from gdrive import GdriveDownloader
import argparse


def main():
    parser = argparse.ArgumentParser(description='Download file from Google drive')
    parser.add_argument('filename', metavar='<filename>', help='Name of file to download')
    parser.add_argument('--output', default='', help='Save output to a file')
    parser.add_argument('--cred', default='credentials.json',
                        help='''Credential json file (default: credentials.json) Refer
                        https://developers.google.com/workspace/guides/create-credentials''')
    args = parser.parse_args()

    if args.output == "":
        args.output = args.filename

    obj = GdriveDownloader()
    result = obj.download_file(args.cred, args.output, args.filename)
    if result == 0:
        print("Successfully downloaded {0}".format(args.output))
        exit(0)
    else:
        print(result)
        exit(1)


if __name__ == '__main__':
    main()
