from django.db import models
from bs4 import BeautifulSoup as bs
# Create your models here.
class Student(models.Model):
	image_url = models.CharField(max_length=50,blank=True) ##without base_addr
	name = models.CharField(max_length=50,blank=True)
	father_name = models.CharField(max_length=50,blank=True)
	roll_no = models.CharField(max_length=10,blank=True)
	student_status = models.CharField(max_length=50,blank=True)
	course_code = models.IntegerField()  ## extra table for mapping course_code -> course_name
	institution_code = models.IntegerField() ## mapping needed

	noe031i = models.CharField(max_length=3)
	noe031e = models.CharField(max_length=3)
	nec309i = models.CharField(max_length=3)
	nec309e = models.CharField(max_length=3)
	ncs301i = models.CharField(max_length=3)
	ncs301e = models.CharField(max_length=3)
	ncs302i = models.CharField(max_length=3)
	ncs302e = models.CharField(max_length=3)
	ncs303i = models.CharField(max_length=3)
	ncs303e = models.CharField(max_length=3)
	nhu301i = models.CharField(max_length=3)
	nhu301e = models.CharField(max_length=3)
	

	nhu402i = models.CharField(max_length=3)
	nhu402e = models.CharField(max_length=3)
	nas401i = models.CharField(max_length=3)
	nas401e = models.CharField(max_length=3)
	ncs401i = models.CharField(max_length=3)
	ncs401e = models.CharField(max_length=3)
	ncs402i = models.CharField(max_length=3)
	ncs402e = models.CharField(max_length=3)
	ncs403i = models.CharField(max_length=3)
	ncs403e = models.CharField(max_length=3)
	nec409i = models.CharField(max_length=3)
	nec409e = models.CharField(max_length=3)


	nec359pi = models.CharField(max_length=3)
	nec359pe = models.CharField(max_length=3)
	ncs351pi = models.CharField(max_length=3)
	ncs351pe = models.CharField(max_length=3)
	ncs353pi = models.CharField(max_length=3)
	ncs353pe = models.CharField(max_length=3)
	ncs355pi = models.CharField(max_length=3)
	ncs355pe = models.CharField(max_length=3)

	nec459pi = models.CharField(max_length=3)
	nec459pe = models.CharField(max_length=3)
	ncs451pi = models.CharField(max_length=3)
	ncs451pe = models.CharField(max_length=3)
	ncs453pi = models.CharField(max_length=3)
	ncs453pe = models.CharField(max_length=3)
	ncs455pi = models.CharField(max_length=3)
	ncs455pe = models.CharField(max_length=3)


	gp301 = models.CharField(max_length=3)
	gp401 = models.CharField(max_length=3)

# IN HVP AND CS WE RECORD ONLY THE SUBJECT IS CLEARED OR NOT
	hvp = models.CharField(max_length=10)
	cs = models.CharField(max_length=10)

	result_status = models.CharField(max_length=200)
	cop = models.CharField(max_length=200,blank=True)

	total_internal_odd_sem = models.IntegerField(default=0)
	total_external_odd_sem = models.IntegerField(default=0)
	total_marks_odd_sem = models.IntegerField(default=0)

	total_internal_even_sem = models.IntegerField(default=0)
	total_external_even_sem = models.IntegerField(default=0)
	total_marks_even_sem = models.IntegerField(default=0)
	
	total_internal = models.IntegerField(default=0)
	total_external = models.IntegerField(default=0)
	total_marks = models.IntegerField(default=0)



	def __str__(self):
		return self.roll_no

	#FOR TESTING PURPOSE WILL BE REMOVED BEFORE DEPLOYING
	def testu(self,rno):

		soup = bs(open('saved_page/'+rno+'.html'),'html.parser')
		
		#BASIC DETAILS
		self.image_url = 'saved_page' + soup.find(id='ctl00_ContentPlaceHolder1_imgstud')['src'][1:]
		self.name = soup.find(id='ctl00_ContentPlaceHolder1_lblName').get_text()
		self.father_name = soup.find(id='ctl00_ContentPlaceHolder1_lblF_NAME').get_text()
		self.roll_no =soup.find(id='ctl00_ContentPlaceHolder1_lblROLLNO').get_text()
		self.student_status =soup.find(id='ctl00_ContentPlaceHolder1_lblStatus').get_text()
		self.course_code = 10
		self.institution_code = 187


		#THEORY SUBJECTS ODD SEM
		self.noe031i = soup.find(id='ctl00_ContentPlaceHolder1_lblA1TS').get_text()
		self.noe031e = soup.find(id='ctl00_ContentPlaceHolder1_lblA1TE').get_text()
		self.nec309i = soup.find(id='ctl00_ContentPlaceHolder1_lblB1TS').get_text()
		self.nec309e = soup.find(id='ctl00_ContentPlaceHolder1_lblB1TE').get_text()
		self.ncs301i = soup.find(id='ctl00_ContentPlaceHolder1_lblC1TS').get_text()
		self.ncs301e = soup.find(id='ctl00_ContentPlaceHolder1_lblC1TE').get_text()
		self.ncs302i = soup.find(id='ctl00_ContentPlaceHolder1_lblD1TS').get_text()
		self.ncs302e = soup.find(id='ctl00_ContentPlaceHolder1_lblD1TE').get_text()
		self.ncs303i = soup.find(id='ctl00_ContentPlaceHolder1_lblE1TS').get_text()
		self.ncs303e = soup.find(id='ctl00_ContentPlaceHolder1_lblE1TE').get_text()
		self.nhu301i = soup.find(id='ctl00_ContentPlaceHolder1_lblF1TS').get_text()
		self.nhu301e = soup.find(id='ctl00_ContentPlaceHolder1_lblF1TE').get_text()


		#THEORY SUBJECTS EVEN SEM	
		self.nhu402i = soup.find(id='ctl00_ContentPlaceHolder1_lblA2TS').get_text()
		self.nhu402e = soup.find(id='ctl00_ContentPlaceHolder1_lblA2TE').get_text()
		self.nas401i = soup.find(id='ctl00_ContentPlaceHolder1_lblB2TS').get_text()
		self.nas401e = soup.find(id='ctl00_ContentPlaceHolder1_lblB2TE').get_text()
		self.ncs401i = soup.find(id='ctl00_ContentPlaceHolder1_lblC2TS').get_text()
		self.ncs401e = soup.find(id='ctl00_ContentPlaceHolder1_lblC2TE').get_text()
		self.ncs402i = soup.find(id='ctl00_ContentPlaceHolder1_lblD2TS').get_text()
		self.ncs402e = soup.find(id='ctl00_ContentPlaceHolder1_lblD2TE').get_text()
		self.ncs403i = soup.find(id='ctl00_ContentPlaceHolder1_lblF2TS').get_text()
		self.ncs403e = soup.find(id='ctl00_ContentPlaceHolder1_lblF2TE').get_text()
		self.nec409i = soup.find(id='ctl00_ContentPlaceHolder1_lblE2TS').get_text()
		self.nec409e = soup.find(id='ctl00_ContentPlaceHolder1_lblE2TE').get_text()


		#PRACTICAL SUBJECTS ODD SEM
		self.nec359pi = soup.find(id='ctl00_ContentPlaceHolder1_lblA1PS').get_text()
		self.nec359pe = soup.find(id='ctl00_ContentPlaceHolder1_lblA1PE').get_text()
		self.ncs351pi = soup.find(id='ctl00_ContentPlaceHolder1_lblB1PS').get_text()
		self.ncs351pe = soup.find(id='ctl00_ContentPlaceHolder1_lblB1PE').get_text()
		self.ncs353pi = soup.find(id='ctl00_ContentPlaceHolder1_lblC1PS').get_text()
		self.ncs353pe = soup.find(id='ctl00_ContentPlaceHolder1_lblC1PE').get_text()
		self.ncs355pi = soup.find(id='ctl00_ContentPlaceHolder1_lblD1PS').get_text()
		self.ncs355pe = soup.find(id='ctl00_ContentPlaceHolder1_lblD1PE').get_text()


		#PRACTICAL SUBJECT EVEN SEM
		self.nec459pi = soup.find(id='ctl00_ContentPlaceHolder1_lblD2PS').get_text()
		self.nec459pe = soup.find(id='ctl00_ContentPlaceHolder1_lblD2PE').get_text()
		self.ncs451pi = soup.find(id='ctl00_ContentPlaceHolder1_lblA2PS').get_text()
		self.ncs451pe = soup.find(id='ctl00_ContentPlaceHolder1_lblA2PE').get_text()
		self.ncs453pi = soup.find(id='ctl00_ContentPlaceHolder1_lblB2PS').get_text()
		self.ncs453pe = soup.find(id='ctl00_ContentPlaceHolder1_lblB2PE').get_text()
		self.ncs455pi = soup.find(id='ctl00_ContentPlaceHolder1_lblC2PS').get_text()
		self.ncs455pe = soup.find(id='ctl00_ContentPlaceHolder1_lblC2PE').get_text()


		self.gp301 = soup.find(id='ctl00_ContentPlaceHolder1_lblGP1').get_text()
		self.gp401 = soup.find(id='ctl00_ContentPlaceHolder1_lblGP2').get_text()

		self.hvp =soup.find(id='ctl00_ContentPlaceHolder1_lblsubstatus').get_text()
		self.cs = soup.find(id='ctl00_ContentPlaceHolder1_lblstataus2').get_text()

		self.result_status = soup.find(id='ctl00_ContentPlaceHolder1_lblSTAT_8').get_text()
		self.cop = soup.find(id='ctl00_ContentPlaceHolder1_lblCarryOver').get_text()
		

		self.total_internal_odd_sem = intC(self.noe031i) + intC(self.nec309i) + intC(self.ncs301i) + intC(self.ncs302i) + intC(self.ncs303i) + intC(self.nhu301i) + intC(self.nec359pi) + intC(self.ncs351pi) + intC(self.ncs353pi) + intC(self.ncs355pi) + intC(self.gp301)
		self.total_external_odd_sem = intC(self.noe031e) + intC(self.nec309e) + intC(self.ncs301e) + intC(self.ncs302e) + intC(self.ncs303e) + intC(self.nhu301e) + intC(self.nec359pe) + intC(self.ncs351pe) + intC(self.ncs353pe) + intC(self.ncs355pe)
		self.total_marks_odd_sem = self.total_internal_odd_sem + self.total_external_odd_sem

		self.total_internal_even_sem = intC(self.nhu402i) + intC(self.nas401i) + intC(self.ncs401i) + intC(self.ncs402i) + intC(self.ncs403i) + intC(self.nec409i) + intC(self.nec459pi) + intC(self.ncs451pi) + intC(self.ncs453pi) + intC(self.ncs455pi) + intC(self.gp401)
		self.total_external_even_sem = intC(self.nhu402e) + intC(self.nas401e) + intC(self.ncs401e) + intC(self.ncs402e) + intC(self.ncs403e) + intC(self.nec409e) + intC(self.nec459pe) + intC(self.ncs451pe) + intC(self.ncs453pe) + intC(self.ncs455pe)
		self.total_marks_even_sem = self.total_external_even_sem + self.total_internal_even_sem

		self.total_internal = self.total_internal_odd_sem + self.total_internal_even_sem
		self.total_external = self.total_external_odd_sem + self.total_external_even_sem
		self.total_marks = self.total_internal + self.total_external
		self.save()
		
		print("Data saved for roll_no",rno)
		return




	def automate(self,rno):
		try:
			soup = bs(open('result/static/saved_page/'+rno+'.html'),'html.parser')
			
			#BASIC DETAILS
			self.image_url = 'saved_page' + soup.find(id='ctl00_ContentPlaceHolder1_imgstud')['src'][1:]
			self.name = soup.find(id='ctl00_ContentPlaceHolder1_lblName').get_text().strip()
			self.father_name = soup.find(id='ctl00_ContentPlaceHolder1_lblF_NAME').get_text()
			self.roll_no =soup.find(id='ctl00_ContentPlaceHolder1_lblROLLNO').get_text()
			self.student_status =soup.find(id='ctl00_ContentPlaceHolder1_lblStatus').get_text()
			self.course_code = 10
			self.institution_code = 187


			#THEORY SUBJECTS ODD SEM
			self.noe031i = soup.find(id='ctl00_ContentPlaceHolder1_lblA1TS').get_text()
			self.noe031e = soup.find(id='ctl00_ContentPlaceHolder1_lblA1TE').get_text()
			self.nec309i = soup.find(id='ctl00_ContentPlaceHolder1_lblB1TS').get_text()
			self.nec309e = soup.find(id='ctl00_ContentPlaceHolder1_lblB1TE').get_text()
			self.ncs301i = soup.find(id='ctl00_ContentPlaceHolder1_lblC1TS').get_text()
			self.ncs301e = soup.find(id='ctl00_ContentPlaceHolder1_lblC1TE').get_text()
			self.ncs302i = soup.find(id='ctl00_ContentPlaceHolder1_lblD1TS').get_text()
			self.ncs302e = soup.find(id='ctl00_ContentPlaceHolder1_lblD1TE').get_text()
			self.ncs303i = soup.find(id='ctl00_ContentPlaceHolder1_lblE1TS').get_text()
			self.ncs303e = soup.find(id='ctl00_ContentPlaceHolder1_lblE1TE').get_text()
			self.nhu301i = soup.find(id='ctl00_ContentPlaceHolder1_lblF1TS').get_text()
			self.nhu301e = soup.find(id='ctl00_ContentPlaceHolder1_lblF1TE').get_text()


			#THEORY SUBJECTS EVEN SEM	
			self.nhu402i = soup.find(id='ctl00_ContentPlaceHolder1_lblA2TS').get_text()
			self.nhu402e = soup.find(id='ctl00_ContentPlaceHolder1_lblA2TE').get_text()
			self.nas401i = soup.find(id='ctl00_ContentPlaceHolder1_lblB2TS').get_text()
			self.nas401e = soup.find(id='ctl00_ContentPlaceHolder1_lblB2TE').get_text()
			self.ncs401i = soup.find(id='ctl00_ContentPlaceHolder1_lblC2TS').get_text().strip()
			self.ncs401e = soup.find(id='ctl00_ContentPlaceHolder1_lblC2TE').get_text().strip()
			self.ncs402i = soup.find(id='ctl00_ContentPlaceHolder1_lblD2TS').get_text().strip()
			self.ncs402e = soup.find(id='ctl00_ContentPlaceHolder1_lblD2TE').get_text().strip()
			self.ncs403i = soup.find(id='ctl00_ContentPlaceHolder1_lblF2TS').get_text().strip()
			self.ncs403e = soup.find(id='ctl00_ContentPlaceHolder1_lblF2TE').get_text().strip()
			self.nec409i = soup.find(id='ctl00_ContentPlaceHolder1_lblE2TS').get_text().strip()
			self.nec409e = soup.find(id='ctl00_ContentPlaceHolder1_lblE2TE').get_text().strip()


			#PRACTICAL SUBJECTS ODD SEM
			self.nec359pi = soup.find(id='ctl00_ContentPlaceHolder1_lblA1PS').get_text().strip()
			self.nec359pe = soup.find(id='ctl00_ContentPlaceHolder1_lblA1PE').get_text().strip()
			self.ncs351pi = soup.find(id='ctl00_ContentPlaceHolder1_lblB1PS').get_text().strip()
			self.ncs351pe = soup.find(id='ctl00_ContentPlaceHolder1_lblB1PE').get_text().strip()
			self.ncs353pi = soup.find(id='ctl00_ContentPlaceHolder1_lblC1PS').get_text().strip()
			self.ncs353pe = soup.find(id='ctl00_ContentPlaceHolder1_lblC1PE').get_text().strip()
			self.ncs355pi = soup.find(id='ctl00_ContentPlaceHolder1_lblD1PS').get_text().strip()
			self.ncs355pe = soup.find(id='ctl00_ContentPlaceHolder1_lblD1PE').get_text().strip()


			#PRACTICAL SUBJECT EVEN SEM
			self.nec459pi = soup.find(id='ctl00_ContentPlaceHolder1_lblD2PS').get_text().strip()
			self.nec459pe = soup.find(id='ctl00_ContentPlaceHolder1_lblD2PE').get_text().strip()
			self.ncs451pi = soup.find(id='ctl00_ContentPlaceHolder1_lblA2PS').get_text().strip()
			self.ncs451pe = soup.find(id='ctl00_ContentPlaceHolder1_lblA2PE').get_text().strip()
			self.ncs453pi = soup.find(id='ctl00_ContentPlaceHolder1_lblB2PS').get_text().strip()
			self.ncs453pe = soup.find(id='ctl00_ContentPlaceHolder1_lblB2PE').get_text().strip()
			self.ncs455pi = soup.find(id='ctl00_ContentPlaceHolder1_lblC2PS').get_text().strip()
			self.ncs455pe = soup.find(id='ctl00_ContentPlaceHolder1_lblC2PE').get_text().strip()


			self.gp301 = soup.find(id='ctl00_ContentPlaceHolder1_lblGP1').get_text().strip()
			self.gp401 = soup.find(id='ctl00_ContentPlaceHolder1_lblGP2').get_text().strip()

			self.hvp =soup.find(id='ctl00_ContentPlaceHolder1_lblsubstatus').get_text().strip()
			self.cs = soup.find(id='ctl00_ContentPlaceHolder1_lblstataus2').get_text().strip()

			self.result_status = soup.find(id='ctl00_ContentPlaceHolder1_lblSTAT_8').get_text().strip()
			self.cop = soup.find(id='ctl00_ContentPlaceHolder1_lblCarryOver').get_text().strip()
			

			self.total_internal_odd_sem = intC(self.noe031i) + intC(self.nec309i) + intC(self.ncs301i) + intC(self.ncs302i) + intC(self.ncs303i) + intC(self.nhu301i) + intC(self.nec359pi) + intC(self.ncs351pi) + intC(self.ncs353pi) + intC(self.ncs355pi) + intC(self.gp301)
			self.total_external_odd_sem = intC(self.noe031e) + intC(self.nec309e) + intC(self.ncs301e) + intC(self.ncs302e) + intC(self.ncs303e) + intC(self.nhu301e) + intC(self.nec359pe) + intC(self.ncs351pe) + intC(self.ncs353pe) + intC(self.ncs355pe)
			self.total_marks_odd_sem = self.total_internal_odd_sem + self.total_external_odd_sem

			self.total_internal_even_sem = intC(self.nhu402i) + intC(self.nas401i) + intC(self.ncs401i) + intC(self.ncs402i) + intC(self.ncs403i) + intC(self.nec409i) + intC(self.nec459pi) + intC(self.ncs451pi) + intC(self.ncs453pi) + intC(self.ncs455pi) + intC(self.gp401)
			self.total_external_even_sem = intC(self.nhu402e) + intC(self.nas401e) + intC(self.ncs401e) + intC(self.ncs402e) + intC(self.ncs403e) + intC(self.nec409e) + intC(self.nec459pe) + intC(self.ncs451pe) + intC(self.ncs453pe) + intC(self.ncs455pe)
			self.total_marks_even_sem = self.total_external_even_sem + self.total_internal_even_sem

			self.total_internal = self.total_internal_odd_sem + self.total_internal_even_sem
			self.total_external = self.total_external_odd_sem + self.total_external_even_sem
			self.total_marks = self.total_internal + self.total_external
			self.save()
			
			print("Data saved for roll_no",rno)
		except:
			print ("error in fetching data for ",rno);
		
		return
			


#CUSTOM TYPE CONVERTOR TO HANDLE ERRORS IN STR -> INT CONVERSION
def intC(num):
	try:
		num = int(num)
	except:
		if 'AB' in num or num.strip() == '' or 'xx' in num:
			num = 0;
		else:
			num = int(num.replace('*','').strip())
	return num