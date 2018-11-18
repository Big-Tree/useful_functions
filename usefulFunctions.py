# A function that takes a directory and a string and returns all the 
# matching files
import os
import fnmatch
import matplotlib.pyplot as plt

def get_files(directory, search):
    file_list = []
    for path, sub_dirs, files in os.walk(directory):
        for name in files:
            if fnmatch.fnmatch(name, search):
                file_list.append(os.path.join(path, name))
    return file_list


# Directory should NOT have a '/' at the end
# If the supplied directory does not exist, it will be created
def save_matplotlib_figure(directory, figure, file_format, name):
    if os.path.exists(directory) == False:
        os.makedirs(directory)
    # Set current figure
    plt.figure(figure.number)
    plt.savefig(directory + '/' + name + '.' + file_format)
    return
