import os
print "UPGRADING.."
os.system('apt-get update && apt-get upgrade && apt update && apt upgrade && echo "[SUCESS!]:"')
os.system('apt-get autoclean && apt-get autoremove')

print("Bye, bro ;)")