from shutil import copy2
from os import listdir, mkdir
from os.path import exists, isdir, join, isfile

src: str = r''
destinations: str = r''
Folders: list = []


def init(source: str, dest: str) -> None:
    global src
    global destinations

    src = source
    destinations = dest

    append_folders(src)
    while len(Folders) != 0:
        for i in Folders:
            try:
                Folders.remove(i)
                print('Removed {i} from Folders'.format(i=i))

                src = i[1]
                print("From {files} in {src}".format(files=i[0], src=src))
                append_folders(src)
            except:
                pass


def append_folders(directory: str) -> None:
    if not exists(directory):
        print('Directory does not exist')
        return

    for files in listdir(directory):
        if isdir(join(directory, files)):
            Folders.append([files, join(directory, files)])

    # * Iterating over the files in the given directory after appending the folders
    iteratingOverFiles(directory)


def iteratingOverFiles(directory: str) -> None:
    for files in listdir(directory):
        if isfile(join(directory, files)):
            print('{files} found in {directory}'.format(
                files=files, directory=directory))
            typeOfFile = files.split('.')[-1]

            if typeOfFile == files:
                print('No file extension found')
                if not exists(join(destinations, 'No Extension')):
                    mkdir(join(destinations, 'No Extension'))

                moveFiles(join(destinations, 'No Extension'),
                          join(directory, files))
                continue

            if checkFolderExistence(typeOfFile):
                print('Folder exists')
                moveFiles(typeOfFile, join(directory, files))
            else:
                mkdir(join(destinations, typeOfFile))
                moveFiles(typeOfFile, join(directory, files))


def checkFolderExistence(file_extension: str) -> bool:
    return isdir(join(destinations, file_extension))


def moveFiles(destination_folder: str, current_location: str) -> None:
    copy2(current_location, join(destinations, destination_folder))
