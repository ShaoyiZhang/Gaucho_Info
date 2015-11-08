import re

def ValidLink(ifile):
	with open(ifile,'rt') as in_file:
		homePage = in_file.read()
	getCOELink = re.compile(r'CollegesDepartments/coe/(.*?).aspx', re.MULTILINE | re.DOTALL)
	getLASLink = re.compile(r'ls-intro/(.*?).aspx', re.MULTILINE | re.DOTALL)

	COE = ''
	LAS = ''
	COE = ' '.join(re.findall(getCOELink, homePage))
	LAS = ' '.join(re.findall(getLASLink, homePage))
	COE = ' '.join(unique_list(COE.split()))
	LAS = ' '.join(unique_list(LAS.split()))
	with open('COE.txt','w') as out_file:		
		out_file.write(COE)
	with open('LAS.txt','w') as out_file:
		out_file.write(LAS)
	frontCOE = 'https://my.sa.ucsb.edu/catalog/Current/CollegesDepartments/coe/'
	end = '.aspx?DeptTab=Courses'
	frontLAS = 'https://my.sa.ucsb.edu/catalog/Current/CollegesDepartments/ls-intro/'
	webList = ''
	for department in COE.split():
		webList += (frontCOE+department+end+'\n')
	for department in LAS.split():
		webList += (frontLAS+department+end+'\n')
	with open('webList.txt','w') as out_file:
		out_file.write(webList)
	print webList.split()



def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
	#a='calvin klein design dress calvin klein'
	#a=' '.join(unique_list(a.split()))

ValidLink('UndergraduateEducation.html')