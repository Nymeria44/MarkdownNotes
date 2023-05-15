import os

def remove_metadata(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            with open(file_path, 'w') as file:
                writing = True
                for line in lines:
                    if line.strip() == '---':
                        writing = not writing
                        continue
                    elif not writing:
                        if line.strip() == '---':
                            writing = not writing
                        continue
                    file.write(line)
