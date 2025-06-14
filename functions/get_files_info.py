import os


def formatter(file_name, file_size, is_dir):
    return f"- {file_name}: file_size={file_size}, is_dir={is_dir}\n"

def get_files_info(working_directory, directory=None):
    try:
        # Handle the case where directory is a relative path
        # If it's a relative path, join it with the working directory
        if not os.path.isabs(directory):
            full_directory = os.path.join(working_directory, directory)
        else:
            full_directory = directory

        # Convert both paths to absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        abs_directory = os.path.abspath(full_directory)

        # Check if the directory is outside the working directory
        # A directory is outside if it doesn't start with the working directory path
        # We need to add a path separator to ensure we're checking for the directory itself
        # and not just a prefix match
        if not abs_directory.startswith(abs_working_dir + os.path.sep) and abs_directory != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if the directory exists and is a directory
        if not os.path.isdir(abs_directory):
            return f'Error: "{directory}" is not a directory'

        # Use the absolute directory path for listing files
        files = os.listdir(abs_directory)
        contents = []
        for file_name in files:
            # Create the full path for the file
            file_path = os.path.join(abs_directory, file_name)

            # Check if it's a directory
            is_dir = os.path.isdir(file_path)

            # Get the file size
            file_size = os.path.getsize(file_path)

            # Add the formatted information to contents
            contents.append(formatter(file_name, file_size, is_dir))

        # Join all the formatted strings and return
        return ''.join(contents)
    except Exception as e:
        return f"Error: {e}"

#- README.md: file_size=1032 bytes, is_dir=False
#- src: file_size=128 bytes, is_dir=True
#- package.json: file_size=1234 bytes, is_dir=False
