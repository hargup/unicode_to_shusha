def is_ascii(c):
    try:
        c.encode().decode("ascii")
        return True
    except:
        return False

def halant_correction(s):
	output = ""
	x = s.find("\\")
	while x > 0:
		print("X is :%d",x)
		if s[x-1] == "a":
			output = output + s[:x-1]
		s = s[x+1:]
		x = s.find("\\")
	return output

def post_process(s):
    #put i before the preceding letter
    output = ""
    x = s.find("i")
    while x != -1:
        if s[x-1] == "a":
           output = output+s[:x-2]+s[x]+s[x-2]+s[x-1]
        else:
            output = output+s[:x-1]+s[x]+s[x-1]
        s = s[x+1:]
        x = s.find("i")
    output = output+s
    output = halant_correction(output)
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
   "ज़":"j,a",
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
    outfile = open("shusha_out", "w")
    output = ""
    uni_in = infile.read()
    for uni_char in uni_in:
        if uni_char == "\n":
            output = output + "\n"
        if not is_ascii(uni_char) or uni_char == " ":
            try:
                output = output + uni_shu[uni_char]
            except:
                print(uni_char)
    output = post_process(output)
    outfile.write(output)
    outfile.close()
    infile.close()

main()
