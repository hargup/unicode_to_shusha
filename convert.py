def make_list():
    unicode=open("unicode","r")
	list=[]
	char_shusha=""
	for line in unicode:
		line=line[:-1]
		if line!="#line end":
			if line =="none":
				list=list+['']
			else:
				list=list+[line]
	print(list)
	return list
#return list
def post_process(str):
    #replace o- with O
    str=str.replace("o-","O")
    #put i before the preceding letter
    x=str.find('i')
    if str[x-1]=='a':
        str=str[:x-2]+str[x]+str[x-2]+str[x-1]+str[x:]
    else:
        str=str[:x-1]+str[x]+str[x-1]+str[x:]
    return str
	
def convert(file_name):
	file=open(file_name,'r')
	outfile=open('shusha_out','w')
	output=''
	#print(file.read())
	ulist=make_list()
	for line in file:
		#only for files without space
		line=line.replace(' ','   ')		
		for i in range(len(line)/3):
			char=line[i*3:(i+1)*3]
			if char=='   ':
				output=output+' '
			else:
				print(char)
				hex_val=char.encode('hex')
				print(hex_val)
				hex_val=hex_val[-2:]
				print(hex_val)
				index=int(hex_val,16)
				print(index)
				output=output+ulist[index-128]
				print(ulist[index-128])
	outfile.write(output)
	return output

convert('hindi')
		
			
