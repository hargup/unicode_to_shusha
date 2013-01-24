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
def convert(file_name):
	file=open(file_name,'r')
	outfile=open('shusha_out','w')
	output=''
	#print(file.read())
	ulist=make_list()
	print(ulist)
	for line in file:
		#only for files without space
		line=line.replace(' ','   ')		
		for i in range(len(line)/3):
			print(type(i))
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
				print(type(ulist))
				print(type(ulist[index-126]))
				output=output+ulist[index-128]
				print(ulist[index-128])
	outfile.write(output)
	return output

convert('hindi')
