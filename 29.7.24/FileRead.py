def write_read_file(file_path):
    with open(file_path, 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")

    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

write_read_file('test_file.txt')
