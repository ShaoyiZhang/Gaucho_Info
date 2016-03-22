import re

def ValidLink(ifile):
	# generate  
	LAS = ''
	COE = ' '.join(re.findall(getCOELink, homePage))
	LAS = ' '.join(re.findall(getLASLink, homePage))
	COE = ' '.join(UniqueList(COE.split()))
	LAS = ' '.join(UniqueList(LAS.split()))
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

def CourseInfoByDepartment(ifile):
	with open(ifile,'rt') as in_file:
		htmlPage = in_file                   #title        unit                                   prerequisite   description                       title       units
	getLower = re.compile(r'CourseDisplay.<b>"(.*?)"<b>.<b>(.*?)<b>.<i>.<br>.Prerequisite:</strong>"(.*?)"</i>."(.*?)"</div>'|r'CourseDisplay.<b>"(.*?)"<b>.<b>(.*?)<b>.<i>$".".2px;">$"(.*?)"')
	jsonOneDepartment = htmlPage.findall(getLower)
	print jsonOneDepartment 

def UniqueList(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist     