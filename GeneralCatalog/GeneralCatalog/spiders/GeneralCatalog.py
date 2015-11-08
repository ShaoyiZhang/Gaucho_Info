import scrapy

class GeneralCatalog(scrapy.Spider):
    name = "GeneralCatalog"
    allowed_domains = ['']
    with open('webList.txt','rt') as in_file:
    	url = in_file.read()
    start_urls = url.split()
    #start_urls = [
    #    "https://my.sa.ucsb.edu/catalog/Current/CollegesDepartments/ls-intro/math.aspx?DeptTab=Courses",
    #    "https://my.sa.ucsb.edu/catalog/Current/CollegesDepartments/ls-intro/stats.aspx?DeptTab=Courses"
    #]

    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)