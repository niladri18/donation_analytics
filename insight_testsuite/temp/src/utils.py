import sys
import pdb


	
def check_input(inp):

	#Check name
	if len(inp[1])<1:
		return False
	else:
		name = inp[1]
	#pdb.set_trace()	

	#Check zip
	#pdb.set_trace()
	if(len(inp[2])) < 5:
		return False
	else:
		zip = inp[2][:5]
		
	#pdb.set_trace()	
	#check other id 
	if len(inp[-1])>1:
		return False
		
	#check date
	if len(inp[-3]) < 8:
		return False
	else:
		year = int(inp[-3][-4:])
		
	#check recipient id
	if len(inp[0])!=9:
		return False
	else:
		recipient = inp[0]
	
	#check transaction amt
	if float(inp[4]):
		amt = int(inp[4])
	else:
		return False
		
	donor = name+zip
	out = [recipient, name, donor, zip,amt, year]
	#all_donors[donor]= [recipient, zip,amt, year]
	return out