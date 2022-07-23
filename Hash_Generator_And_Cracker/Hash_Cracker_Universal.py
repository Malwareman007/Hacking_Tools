import hashlib,binascii
hash_type=input("Enter the hash type\n1 md5\n2 sha1\n3 Sha224\n4 SHA256\n5 SHA512\n6 NTLM\n")
path_to_wordlist = input ("Enter path to word list\n")
input_hash=input("Enter the hash crack\n")
def md5_crack(hash_to_crack,path_to_wordlist):
    c = 1
    with open (path_to_wordlist, encoding='utf-8') as file1:
        for line in file1:
            current_pass = line.replace('\n', '').rstrip()
            hash_current = hashlib.md5 (current_pass.encode('utf-8')).hexdigest()
            c += 1
            if c%100000 == 0:
                print (f"Done {c} passwords current{current_pass}")
            if hash_current == hash_to_crack:
                print (f"Password found ---> {current_pass}")
                break
def sha1_crack(hash_to_crack,path_to_wordlist):
    c = 1
    with open (path_to_wordlist, encoding='utf-8') as file1:
        for line in file1:
            current_pass = line.replace('\n', '').rstrip()
            hash_current = hashlib.sha1(current_pass.encode('utf-8')).hexdigest()
            c += 1
            if c%100000 == 0:
                print (f"Done {c} passwords current{current_pass}")
            if hash_current == hash_to_crack:
                print (f"Password found ---> {current_pass}")
                break
def sha224_crack(hash_to_crack,path_to_wordlist):
    c = 1
    with open (path_to_wordlist, encoding='utf-8') as file1:
        for line in file1:
            current_pass = line.replace('\n', '').rstrip()
            hash_current = hashlib.sha224(current_pass.encode('utf-8')).hexdigest()
            c += 1
            if c%100000 == 0:
                print (f"Done {c} passwords current{current_pass}")
            if hash_current == hash_to_crack:
                print (f"Password found ---> {current_pass}")
                break
def sha256_crack(hash_to_crack,path_to_wordlist):
    c = 1
    with open (path_to_wordlist, encoding='utf-8') as file1:
        for line in file1:
            current_pass = line.replace('\n', '').rstrip()
            hash_current = hashlib.sha256(current_pass.encode('utf-8')).hexdigest()
            c += 1
            if c%100000 == 0:
                print (f"Done {c} passwords current{current_pass}")
            if hash_current == hash_to_crack:
                print (f"Password found ---> {current_pass}")
                break
def sha512_crack(hash_to_crack,path_to_wordlist):
    c = 1
    with open (path_to_wordlist, encoding='utf-8') as file1:
        for line in file1:
            current_pass = line.replace('\n', '').rstrip()
            hash_current = hashlib.sha512(current_pass.encode('utf-8')).hexdigest()
            c += 1
            if c%100000 == 0:
                print (f"Done {c} passwords current{current_pass}")
            if hash_current == hash_to_crack:
                print (f"Password found ---> {current_pass}")
                break
def NTLM_crack(hash_to_crack,path_to_wordlist):
    c = 1
    with open (path_to_wordlist, encoding='utf-8') as file1:
        for line in file1:
            current_pass = line.replace('\n', '').rstrip()
            hash_current = hashlib.NTLM(current_pass.encode('utf-8')).hexdigest()
            c += 1
            if c%100000 == 0:
                print (f"Done {c} passwords current{current_pass}")
            if hash_current == hash_to_crack:
                print (f"Password found ---> {current_pass}")
                break

if hash_type =="1":
     md5_crack (input_hash, path_to_wordlist)
if hash_type =="2":
     sha1_crack(input_hash, path_to_wordlist)
if hash_type == "3":
    sha224_crack(input_hash, path_to_wordlist)
if hash_type =="4":
     sha256_crack(input_hash, path_to_wordlist)
if hash_type =="5":
     sha512_crack(input_hash, path_to_wordlist)
if hash_type =="6":
     NTLM_crack(input_hash, path_to_wordlist)
