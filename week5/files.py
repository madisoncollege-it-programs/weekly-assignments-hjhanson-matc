#Hunter Hanson
#This script copys the passwd file to a new file.

hFile = open("/etc/passwd","r")

indata = hFile.read()

print (f"The passwd file is {len(indata)} bytes long")
print ("This length includes all unicode characters, including line breaks.")


to_file = ("passwd_str.txt")

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
hFile.close()
