import dropbox.files
from dropbox.exceptions import AuthError
import os
local_dir = os.path.dirname(__file__)

# set your dropbox token here
token = 'sl.BTUsafv_4w-1KXkajmka_ahWuWfsBMrN4vMcSe-V8qCLBSVm5g-KWwKs-iS18ZNNKX-xoh1DpjisZzEmHwgQ02P3gjaLy5TuSYFZ0_AfmD6VbXwX9YRnM41CRFuym4ettueboMJo'


class Dropbox:
    def __init__(self):
        try:
            self.dbx = dropbox.Dropbox(token)
        except AuthError as e:
            print('Error connecting to Dropbox with access token: ' + str(e))

    def download(self, file):
        #
        try:
            with open(local_dir + f'/{file}.txt', 'wb') as f:
                _, result = self.dbx.files_download(path=f'/Vinted/{file}.txt')
                f.write(result.content)
        except Exception as e:
            print('Error downloading file: ' + str(e))

    def upload(self, file):
        try:
            with open(local_dir + f'/{file}.txt', 'r') as f:
                self.dbx.files_upload(bytes(f.read(), 'UTF-8'), path=f'/Vinted/{file}.txt',
                                      mode=dropbox.files.WriteMode("overwrite"))
        except Exception as e:
            print('Error downloading file: ' + str(e))

