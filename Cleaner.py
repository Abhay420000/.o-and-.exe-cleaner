import os

#Getting files names to delete
eolist = []
with os.scandir('./') as entries:
    print('Following Files are going to delete:')
    for entry in entries:
        if ('.exe' in entry.name) or ('.o' in entry.name):
            eolist.append(entry)
            print(entry.name)
    print('Number of files: ',len(eolist))

#Deleting files
op = input('Continue:')
if op == 'y' or op == 'Y':
    for i in eolist:
        try:
            os.unlink(i)
        except:
            print('Files can not be deleted!')
