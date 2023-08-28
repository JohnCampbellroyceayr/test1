import os

source = r'C:\Users\John Campbell\AppData\Roaming\IBM\Client Access\Emulator\private'
destination = r'Z:\Software\John Campbell\.mac files'



def copyFile(sourceFile, destinationFile):
    with open(sourceFile, 'r') as source_file, open(destinationFile, 'w') as destination_file:
        contents = source_file.read()

        destination_file.write(contents)

    source_file.close()
    destination_file.close()


for filename in os.listdir(source):
    file_path = os.path.join(source, filename)
    if filename.endswith('.mac') and filename[0].isnumeric() == False:
        if os.path.isfile(file_path):
            newFile = os.path.join(destination, filename)
            copyFile(file_path, newFile)
            # Perform desired action with the file
            # print(file_path)
            # print(filename)
    elif filename == "text files":
        folder = os.path.join(source, filename)
        for file_name in os.listdir(folder):
            sourceFile = os.path.join(source, filename, file_name)
            destinationFile = os.path.join(destination, filename, file_name)
            print(sourceFile)
            if os.path.isfile(sourceFile):
                copyFile(sourceFile, destinationFile)
                print('copied', file_name)