import os
file_size = os.path.getsize("my_file.txt")
# Open the file in write mode.
with open("my_file.txt", "w") as f:
    # Write some data to the file.
    f.write("This is some data in the file.Hello There")
    print(file_size)
    # Truncate the file to 10 bytes.
    f.truncate(10)

# Close the file.
f.close()

# Check the file size.

print(file_size)