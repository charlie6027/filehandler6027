from filehandler import FileHandler, FileHandleMode

print("Trying out FileHandler on windows platform...")

data = {
    'username': 'charliesky',
    'mission': 'celebrate first successful package install!',
    'status': '★ working perfectly!'
}

output_file = '~/Documents/celebration_output.txt'
handler = FileHandler(FileHandleMode.Modern)

handler.write(output_file, data)
content = handler.read(output_file)

print("✔ File content successfully read back:")
print(content)
