class FileHaldler:
    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
       read_file = open(self.file_name, 'r')
       self.content = read_file.read()
       read_file.close()
       return self.content

    def file_fill(self, save_content):
        write_file = open(self.file_name, 'w')
        write_file.write(save_content)
        write_file.close()
