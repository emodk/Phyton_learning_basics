filepath = input().split(chr(92))
full_filename = filepath[-1]
file_details = full_filename.split(".")
file_name = file_details[0]
file_ext = file_details[1]
print(f"File name: {file_name}")
print(f"File extension: {file_ext}")
