import sys
import os
from datetime import datetime,timedelta
import time
import pdb
import utils as ut
import numpy as np
import math
import bst 


def prepare_donor_list(out,donor_list):
	donor = out[2]
	if donor in donor_list.keys():
		donor_list[donor][2] += out[4] # add the contribution
		donor_list[donor][1] += 1 # add one count to number of contributions
		donor_list[donor][0] = out[0] #recipient
	else:
		donor_list[donor] = [out[0],1,out[4]]
		
	return donor_list	

def prepare_repeat_donor_list(out,repeat_donor_list):
	repeat_donor = out[3]#zip
	#pdb.set_trace()
	if repeat_donor in repeat_donor_list.keys():
		repeat_donor_list[repeat_donor][2] += out[4] # add the contribution
		repeat_donor_list[repeat_donor][1] += 1 # add one count to number of contributions
		repeat_donor_list[repeat_donor][0] = out[0] #recipient
	else:
		repeat_donor_list[repeat_donor] = [out[0],1,out[4]]
		
	return repeat_donor_list

def prepare_output(recipient,contribution, num_contribution,out):
	zip = int(out[3])#zip
	recipient = out[0]
	amt = out[4]
	contribution[recipient][zip] += amt
	num_contribution[recipient][zip] += 1
	
	total_amt = 0
	total_trans = 0
	
	for i in contribution:
		total_amt += np.sum(contribution[i])
		total_trans += np.sum(num_contribution[i])
		
	#repeat_donor = sorted(donor_contribution[donor_contribution.nonzero()])
	#rank = math.ceil( float(p)*len(repeat_donor)/100)
	#pdb.set_trace()
	#percentile = repeat_donor[rank-1]
	
	
		
	return total_amt,total_trans,	
	
#########################################################
'''
MAIN PROGRAM
'''
#########################################################

#fname = './input/itcont.txt'
fname = sys.argv[1]
#pname = './input/percentile.txt'
pname = sys.argv[2]
oname = sys.argv[3]
f0 = open(fname,'r')
#percentile
f1 = open(pname,'r')
#output file
fout = open(oname,'w')
p = f1.readline().strip().split()[0]
#pdb.set_trace()
p = int(p)

#pdb.set_trace()

donor_list = {}
past_donor_list =[]
past_yr = 0
while True:
	line = f0.readline().strip().split('|')
	if len(line) < 2:
		break
	
	inp = [line[0].strip(),line[7].strip(),line[10].strip(),line[13].strip(),line[14].strip(),line[15].strip()]
	#pdb.set_trace()
	
	# Check the input
	out = ut.check_input(inp)
	
	if out:
		#print(out)
		current_yr = out[-1]
		#print(current_yr,past_yr)
		if current_yr > past_yr:
			#pdb.set_trace()
			#push the existing donor name list to past donor list 
			past_donor_list += donor_list.keys()
			repeat_donor_list = {}
			recipient_list = []
			contribution = {}
			num_contribution = {}
			#Create a new Binary Tree
			T = bst.BST()
			past_yr = current_yr
			
		#else:
			#push donor name to past donor list
		#	continue
			
		#create a dictionary with donor name as the key 
		# and [recipient,total amt contributed, number of contribution]
		
		donor = out[2]
		#pdb.set_trace()
		donor_list = prepare_donor_list(out,donor_list)
		if donor in past_donor_list: # identify repeat donor
			recipient = out[0]
			
			if recipient not in recipient_list:
				recipient_list.append(recipient)
				contribution[recipient]  = np.zeros(99999)
				num_contribution[recipient] = np.zeros(99999)
			
			total = prepare_output(recipient,contribution, num_contribution,out)
			T.insert(out[4])
			#pdb.set_trace()
			z = T.inorder()
			#pdb.set_trace()
			rank = math.ceil( float(p)*T.getsize()/100)
			#pdb.set_trace()
			percentile = (list(z)[rank-1])
			#pdb.set_trace()
			#print(contribution_list)
			
			ans = [recipient,out[3],str(current_yr),str(percentile),str(int(total[0])),str(int(total[1]))]
			#print(current_yr)
			#print(zip,repeat_donor_list[zip])
			#print(*ans,sep = '|')
			#print(('|').join(ans))
			fout.write(('|').join(ans)+'\n')
			
			#for i in repeat_donor_list:
			#	print(i,repeat_donor_list[i])
		

			#print('')
		else:
			continue
			
	else:
		continue
		
#f0.close()
#f1.close()
#fout.close()
		
		
		
		
		
		
		
		
		
		
		