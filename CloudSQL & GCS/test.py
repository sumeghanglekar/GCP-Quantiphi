from google.cloud import storage
import os

BUCKET_NAME = 'sumegh2'
DOWNLOAD_FOLDER = 'folder1'
DESTINATION_FOLDER = 'final/'

# make destination folder in local machine
try:
    os.mkdir(DESTINATION_FOLDER)
except Exception as e:
    print('Folder already exists.')

def main():
    client = storage.Client()

    bucket = client.get_bucket(BUCKET_NAME)

    blobs = bucket.list_blobs()

    for b in blobs:
        
        fold = DESTINATION_FOLDER + ''
        
        if b.name.startswith(DOWNLOAD_FOLDER) and b.name[-1] != '/':
            
            folder_struct = b.name.split('/')
            
            for folder in folder_struct[:-1]:
                fold += folder + '/'
                try:
                    os.mkdir(fold)
                except Exception as e:
                    pass
            
            b.download_to_filename(fold + folder_struct[-1])

    print('Replicated')

if __name__ == '__main__':
    main()