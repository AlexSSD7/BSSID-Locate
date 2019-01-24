import shutil
import os

print("Copying files...")
shutil.copyfile("bssid-locate", "/bin/bssid-locate")
print("Finishing...")
os.system("chmod +x /bin/bssid-locate")
print("Done.")