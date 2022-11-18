from src.parser import dbx


class FileManager:
    def __init__(self, file):
        self.dropbox = dbx.Dropbox()
        self.file = file
        # local project directory is set by default
        self.dir = dbx.local_dir + f'/{self.file}.txt'
        if self.file == 'sellers':
            self.sellers = []

    def save(self, file_value=''):
        # write cookie file/seller list to a file and upload to dropbox cloud
        try:
            with open(self.dir, 'wb') as f:
                if self.file == 'sellers':
                    for k in self.sellers:
                        f.write(bytes(str(k) + '\n', 'UTF-8'))
                else:
                    f.write(bytes(file_value, 'UTF-8'))
            self.dropbox.upload(f'{self.file}')
        except Exception as e:
            print(f'Error saving {self.file}: ' + str(e))

    def load(self):
        # download cookie/seller list from dropbox cloud and return value
        try:
            self.dropbox.download(f'{self.file}')
            with open(self.dir, 'r') as f:
                if self.file == 'sellers':
                    for i in str(f.read()).split('\n'):
                        if i == '': continue
                        self.sellers.append(i)
                else:
                    return f.read()
        except Exception as e:
            print(f'Error loading {self.file}: ' + str(e))



