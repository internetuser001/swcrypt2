import subprocess
import sys

print("""
                                             __   
  ________  _  __ ___________ ___.__._______/  |_ 
 /  ___/\ \/ \/ // ___\_  __ <   |  |\____ \   __\\
 \___ \  \     /\  \___|  | \/\___  ||  |_> >  |  
/____  >  \/\_/  \___  >__|   / ____||   __/|__|  
     \/              \/       \/     |__|         
                                                             
                --- credit:@internetuser001 ---                       
""")

print("Choose an option:")
print("1 — Generate Key")
print("2 — Encrypt")
print("3 — Decrypt")

choice = input("Enter 1, 2, or 3: ").strip()

if choice == "1":
    subprocess.run([sys.executable, "tools/keygen.py"])
elif choice == "2":
    subprocess.run([sys.executable, "tools/encryptor2.py"])
elif choice == "3":
    subprocess.run([sys.executable, "tools/decryptor.py"])
else:
    print("Invalid choice.")
