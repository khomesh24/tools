# Download files from Google drive

#### Prerequisite

- Enable to [Google drive API](https://developers.google.com/drive/api/v3/enable-drive-api)

- Generate [OAuth token](https://developers.google.com/workspace/guides/create-credentials)

- Reference of [Google drive API](https://developers.google.com/drive/api/v3/about-sdk)

#### Setup

- Create a virtual environment

~~~
# python3.6 -m venv venv
# source venv/bin/activate
~~~

- Install dependencies

~~~
# pip install -r requirements.txt
~~~

- [Create a credentials.json file](https://developers.google.com/workspace/guides/create-credentials)

- Running the command

~~~
# python main.py --cred <Credential json file> --output <Save output to a file> <filename to be downloaded>
~~~