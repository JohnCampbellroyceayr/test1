sourceFile = r'C:\Users\User\OneDrive\Documents\John ProgramingProjects\python\test1\testfile.mac'
destinationFile = r'C:\Users\User\OneDrive\Documents\John ProgramingProjects\python\test1\copy.mac'

def copyFile():
    with open(sourceFile, 'r') as source_file, open(destinationFile, 'w') as destination_file:
        contents = source_file.read()

        destination_file.write(contents)

    source_file.close()
    destination_file.close()
    
copyFile()