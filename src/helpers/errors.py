class FileExistsError2(FileExistsError):
    def __init__(self, message, directory, file_name):
        super(FileExistsError2, self).__init__(message)
        self.message = message
        self.directory = directory
        self.file_name = file_name

