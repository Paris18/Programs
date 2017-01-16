import sys,os

fp = open("text.txt","w+")

print fp.name
print fp.mode
print fp.closed
print fp.softspace


fp.write("hi how r u");
print fp.tell()
fp.seek(0,0)
stra = fp.read(9);
print stra
fp.close()
os.rename("text.txt","filepy.txt")
# os.remove("filename")
# os.mkdir("dirname")