from pathlib import Path

currentDirectory = Path('/usr/local/share')
for currentFile in currentDirectory.iterdir():  
   print(str(currentFile))
