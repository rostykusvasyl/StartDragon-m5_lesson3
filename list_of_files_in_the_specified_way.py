from pathlib import Path

directory = Path('/usr/local/share')
for currentFile in directory.iterdir():
   print(str(currentFile))
