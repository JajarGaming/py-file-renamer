import os

# specify the folder_path containing the files
folder_path = "changme"

# specify the base file name
base_name = "changme"

# specify the starting index for the new file names
start_index = 1

# specify the extension to target (optional)
target_extension = ''

for filename in os.listdir(folder_path) :

    extension = os.path.splitext(filename)[1]

    if target_extension == '' or extension == target_extension:

        new_name = f"{base_name}_{start_index}{extension}"

        start_index += 1

        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
print('Successfully renamed TODO files')