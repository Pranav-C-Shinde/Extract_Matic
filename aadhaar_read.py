import re
def adhaar_read_data(text):
    res = text.split()
    name = None
    dob = None
    adh = None
    sex = None
    text0 = []
    lines = text.split('\n')
    for lin in lines:
        s = lin.strip()
        text0.append(s)

    sex = "FEMALE" if 'female' in text.lower() else "MALE"
    
    text0 = list(filter(None, text0))
    
    try:
        # Extract and clean name
        name = text0[0].strip().replace("8", "B").replace("0", "D").replace("6", "G").replace("1", "I")
        name = re.sub('[^a-zA-Z ]+', '', name)

        # Extract and clean DOB
        dob = text0[1][-10:].strip().replace('l', '/').replace('L', '/').replace('I', '/').replace('i', '/')
        dob = re.sub('[^0-9/]', '', dob)

        # Extract and clean Aadhaar number
        aadhar_number = ''.join(word + ' ' for word in res if len(word) == 4 and word.isdigit())
        adh = aadhar_number if len(aadhar_number.replace(' ', '')) >= 12 else "Aadhar number not read"
        
    except IndexError:
        pass

    data = {
        'Name': name,
        'Date of Birth': dob,
        'Adhaar Number': adh,
        'Sex': sex,
        'ID Type': "Adhaar"
    }
    return data


def findword(textlist, wordstring):
    lineno = -1
    for wordline in textlist:
        xx = wordline.split( )
        if ([w for w in xx if re.search(wordstring, w)]):
            lineno = textlist.index(wordline)
            textlist = textlist[lineno+1:]
            return textlist
    return textlist