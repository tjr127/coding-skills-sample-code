
import os

#change working directory as VS Code musses with it
os.chdir("/home/tjr127/projects/coding-skills-sample-code/coding205-writing-file-ga")
print ("Writing to file..")

# You can open the file using 'with'.
# 'with' provides better exception handling and closes the file
with open("my-new-file2.txt", "w") as file:
    file.write("Cisco Developers are 1337!\n")
    file.write("DevNet Developers rock!")

print ("Do some stuff outside of the block")

# open the file again and append some additional text
with open("my-new-file2.txt", "w") as file:
    file.write("Level up!\n")
    file.write("Go to developer.cisco.com and do more learning labs!")