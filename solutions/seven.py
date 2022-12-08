from collections import defaultdict
with open('input7.txt') as f:
    lines = f.readlines()
    
directory = ['']
files = defaultdict(int)

for command in lines:
        command = command.strip().split()
        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "..":
                    directory.pop()
                elif command[2] == "/":
                    directory = ['']
                else:
                   directory.append(command[2])
        elif command[0] != "dir":
            dir_str = ''
            for dir in directory:
                dir_str += dir
                files[dir_str] += int(command[0])

total_size = 0
unused_space = 70000000 - files['']

space_to_free_up = 30000000 - unused_space
space_to_delete= files['']

for dir, size in files.items():
    if size <= 100000:
        total_size += size
    if size >= space_to_free_up and size < space_to_delete:
        space_to_delete = size

print(total_size)
print(space_to_delete)
#%%
