#email extraction
pattern = r"[\w.]+@[\w.]+\.\w+" # r represent any raw pattern [] set of charcter\w(any word that contain a-z charcter 0-9 digit and underscore)

#.(any charcter except new line) +(one or more occurance ) \.(represent special dot) \w+(one or moreoccurance containg a=z,0-9)

print(re.findall(pattern,txt))

pattern1 = r"\b\d{10}\b"


phn = re.findall(pattern1,txt)
print(phn)

for i in phn:
    if re.match( r"[0-9]{10}", i):
        print("Valid phone number")
        
    else:
        print("invalid number")


print(re.findall(pattern1,txt))


pattern1 = r"\b\d{10}\b"


phn = re.findall(pattern1,txt)
print(phn)

for i in phn:
    if re.match( r"[0-9]{10}", i):
        print("Valid phone number")
        
    else:
        print("invalid number")


print(re.findall(pattern1,txt))


pattern3 = r"https?://[^\s]+"

urls = re.findall(pattern3, txt)

print(urls)

#finding hashtag

pattern4 = r"#\w+"

hastag = re.findall(pattern4,txt)
print(hastag)

#extracting number from text
pattern5 = r"\d+"

numtxt = re.findall(pattern5,txt)
print(numtxt)

email_pattern = r"[\w.]+@[\w.]+\.\w+"
phone_pattern = r"[0-9]{10}"
url_pattern = r"https?://[^\s]+"

emails = re.findall(email_pattern, data)
phones = re.findall(phone_pattern, data)
urls = re.findall(url_pattern, data)

print("Emails:", emails)
print("Phones:", phones)
print("URLs:", urls)