'''
Namex: a command line-based program that allows a user to rename all files in a directory.
by Dean Orenstein, Edited 6/3/19, 11/12/19
'''


# Import libraries
from os import *

#~~~ Useful methods ~~~#
# listdir(path): os, returns a list of the items in that directory
# remove(path, dir_fd=None): os, delete the file path (not directory path)
# rename(src, dst, src_dir_fd=None, dst_dir_fd=None): os, rename the file from src path to dst path


# User inputs the directory path and common name for all files, name is assumed to be a regular expression
# example of path: /Users/Deano/Documents/ENGR 216
path = '/'
location, not_complete = input('Enter base location for path for target directory (e.g. Users): '), True
while not_complete:
    if location.lower() == 'done':
        not_complete = False
    else:
        path += location + '/'
        location = input('Enter next location (type done to quit): ')

# Each item is distinguished by a number following this name, e.g. name2, by default
common_name = input('What would you like to name the items in this directory? ')


# The files in the directory are targeted and manipulated
items = listdir(path)
# There are DS_store files (on mac) which must get removed from the list so numbering isnt screwed up
items = [item for item in items] #if item.split('.')[1] != 'DS_Store']

num = 1
for item in items:  # Extract name and extension (if there is one)
    l = item.split('.')
    if len(l) == 2:
        name, extension = l[0], l[1]
        rename(path+'/'+name+'.'+extension, path+'/'+common_name+str(num)+'.'+extension, src_dir_fd=None, dst_dir_fd=None)
    elif len(l) == 1:
        name = l[0]
        rename(path+'/'+name, path+'/'+common_name+str(num), src_dir_fd=None, dst_dir_fd=None)
    num += 1


# Console outputs a message saying that the task is complete
print('Task complete! Check your finder application to see your new names :D')

