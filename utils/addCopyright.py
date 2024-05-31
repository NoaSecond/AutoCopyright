import os
import re

# Configurations des commentaires pour chaque type de fichier
copyright_comment = "Développé avec ❤️ par : www.noasecond.com."

comments = {
    '.php': "<!-- {} -->".format(copyright_comment),
    '.js': "// {}".format(copyright_comment),
    '.html': "<!-- {} -->".format(copyright_comment),
    '.yml': "# {}".format(copyright_comment),
    '.css': "/* {} */".format(copyright_comment),
    '.sql': "-- {}".format(copyright_comment),
    '.py': "# {}".format(copyright_comment)
}

extensions = tuple(comments.keys())
exclude_dirs = ['logs', '.git', '.github']
exclude_files = ['.gitattributes', '.gitignore']

def should_exclude(file_path):
    """
    Determines whether a file should be excluded based on its path.

    Args:
        file_path (str): The path of the file to check.

    Returns:
        bool: True if the file should be excluded, False otherwise.
    """
    for excl_dir in exclude_dirs:
        if excl_dir in file_path:
            return True
    for excl_file in exclude_files:
        if file_path.endswith(excl_file):
            return True
    return False

def add_comment_to_file(file_path, comment):
    """
    Adds a comment to the specified file.

    Args:
        file_path (str): The path to the file.
        comment (str): The comment to be added.

    Returns:
        None
    """
    with open(file_path, 'r+') as file:
        content = file.read()
        # Remove old comment if present
        content = re.sub(r'(\n\n{}|\n\n{}|\n\n{}|\n\n{}|\n\n{})'.format(
            comments['.js'],
            comments['.html'],
            comments['.yml'],
            comments['.css'],
            comments['.sql']
        ), '', content)

        # Remove trailing empty lines
        content = content.rstrip()
        
        if comment.strip() not in content:
            # Add a newline if the last line is not empty
            if not content.endswith(('\n', '\r')):
                content += "\n"
            file.seek(0)
            file.write(content + comment)
            file.truncate()

def main():
    """
    Recursively walks through the current directory and adds a specified comment to files with specific extensions.
    Excludes specified directories and files based on exclusion criteria.
    """
    for root, dirs, files in os.walk('.'):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(extensions) and not should_exclude(file_path):
                ext = os.path.splitext(file)[1]
                comment = comments[ext]
                add_comment_to_file(file_path, comment)

if __name__ == "__main__":
    main()
# Développé avec ❤️ par : www.noasecond.com.