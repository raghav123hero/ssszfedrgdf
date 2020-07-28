import dropbox
import os

class TransferData:
    def __init__(self,accesstoken):
        self.accesstoken = accesstoken
    def uploadfile(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.accesstoken)
        for root ,dirs,files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root,filename)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))
def main():
    accesstoken = 'Yo8iFQHQsfAAAAAAAAAADKBvRZzBphI6q07JOVfUE8HripLfq4'
    transferData = TransferData(accesstoken)
    file_from = input("Enter the file to be transfered:\n")
    file_to = input("Enter the full to path to upload to dropbox:\n")
    transferData.uploadfile(file_from,file_to)
    print("file is moved")
main()
