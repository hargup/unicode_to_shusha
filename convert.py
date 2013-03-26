def is_ascii(c):
    try:
        c.encode().decode('ascii')
        return True
    except:
        return False

def post_process(str):
    #put i before the preceding letter
    output=''
    x=str.find('i')
    while x!=-1:
        if str[x-1]=='a':
           output=output+str[:x-2]+str[x]+str[x-2]+str[x-1]
        else:
            output=output+str[:x-1]+str[x]+str[x-1]
        str=str[x+1:]
        x=str.find('i')
    output=output+str
    return output

def main():
    uni_shu= {" ":" ",
   "आ":"a",
   "अ":"A",
   "आ":"Aa",
   "इ":"[",
   "इ":"[-",
   "उ":"]",
   "ऊ":"}",
   "ओ":"Aao",
   "औ":"AaO",
   "ए":"e",
   "ऐ":"eo",
   "क":"k",
   "ख":"K",
   "ग":"ga",
   "घ":"Ga",
   "ड़":"D,",
   "च":"ca",
   "छ":"C",
   "ज":"ja",
   "झ":"Ja",
   "ञ":"Ha",
   "ट":"T",
   "ठ":"z",
   "ड":"D",
   "ढ":"Z",
   "ण":"Na",
   "त":"t",
   "थ":"qa",
   "द":"d",
   "ध":"Q",
   "न":"na",
   "प":"p",
   "फ":"f",
   "ब":"ba",
   "भ":"Ba",
   "म":"ma",
   "थ":"q",
   "य":"ya",
   "र":"r",
   "ल":"la",
   "व":"va",
   "श":"Sa",
   "ह":"h",
   "ष":"Ya",
   "स":"sa",
   "प":"p",
   "ज़":"j,a",
   "ं":"M",
   "़":",",
   "ा":"a",
   "ि":"i",
   "ी":"I",
   "ु":"u",
   "ू":"U",
   "ृ":"R",
   "ॅ":"^",
   "े":"o",
   "ै":"O",
   "ो":"ao",
   "ौ":"aO",
   "्":"\\"
   }
    infile = open("hindi", "r")
    outfile = open('shusha_out', 'w')
    output = ''
    uni_in = infile.read()
    for uni_char in uni_in:
        if uni_char == '\n':
            output = output + '\n'
        if not is_ascii(uni_char) or uni_char == ' ':
            try:
                output = output + uni_shu[uni_char]
            except:
                print(uni_char)
    output = post_process(output)
    outfile.write(output)
    outfile.close()
    infile.close()

main()
