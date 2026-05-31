import hashlib
import sys
import os
 
def detect_hash(hash_value):
    length = len(hash_value)
    if length == 32 :
        print("hash type : MD5")
        return [hashlib.md5]
    elif length == 40:  
     print("hash type : SHA1")
     return[hashlib.sha1]

    elif length == 64:   
        print("hash type : SHA256")
        return [hashlib.sha256]
 
    elif length ==  128:   
        print("hash type : SHA512")
        return [hashlib.sha512]
     
    else :
        print("Unknown hash length! Entering Brute-Force Mode...")
        return [hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha512]



def covert(text,hash_algorithm):
    get = hash_algorithm(text.encode()).hexdigest()
    return get
 
def main():
    os.system("cls" if os.name == "nt" else "clear") 

    user_sha = sys.argv[1]
    user_clean = user_sha.strip().lower()
    hash_type = detect_hash(user_clean)

    if hash_type is None:
        print("type of hash is not definfd ")
        return 
    
    print("hash is : ",user_sha)
    
    with open("rockyou.txt","r",encoding="utf-8", errors="ignore") as file :
        
        found = False 

        for line in file:
            passwd= line.strip()
            for algo in hash_type:
                covert_hash = covert(passwd,algo)
                
                if user_clean ==  covert_hash:
                    print(f"password Found Susseccfully: {passwd}")
                    
                    found = True
                    break
            if found:
                break


if __name__ == "__main__":
    main()