
#################################################################
#     															#
#	IAN RUSSELL													#
#	Short program to calculate grades      						#
#																#
#																#
#																#
#																#
#																#
#################################################################


import json
import sys
import getpass


# Create basic functionality than add user interaction
# Be able to append new assignment entries

# Import course data from JSON file

# FUNCTIONS


def average(numbers):

	"""
	Basic average calculator takes in parameter 
	'numbers' which is any list of numbers (e.g. homework scores).
	"""
	total = sum(numbers)
	
	# Protect against div by zero
	if total == 0:
		return 0
		
	else:
		total = float(total)
		total = total/len(numbers)
		return total
	


# def class average
	
	
		
def get_average(course):

	"""
	Take in list parameter (grades) 
	Use weights for...
	HOMEWORK
	QUIZZES
	TESTS
	LABS
	"""
	
	# Calls average function and takes in COURSE to and retrives info via key
	
	homework = average(course["Homework"])
	quizzes = average(course["Quizzes"])
	tests = average(course["Tests"])
	projects = average(course["Projects"])
	labs = average(course["Labs"])
	final = average(course["Final"])
	
	# Weighted average
	
	cAvg = 0
	cAvg = homework*course["hWeight"]
	cAvg += quizzes*course["qWeight"]
	cAvg += tests*course["tWeight"]
	cAvg += projects*course["pWeight"]
	cAvg += labs*course["lWeight"]
	cAvg += final*course["fWeight"]
	
	return cAvg
	
# def letter grade
	# Take in class average integer parameter (score) 


def get_letter(score):
	
	if score >= 97:
		return "A+"
	elif score >= 93 and score < 97:
		return "A"
	elif score >= 90 and score < 93:
		return "A-"
	elif score >= 87:
		return "B+"
	elif score >= 83 and score < 87:
		return "B"
	elif score >= 80 and score < 83:
		return "B-"
	elif score >= 77:
		return "C+"
	elif score >= 73 and score < 77:
		return "C"
	elif score >= 70 and score < 73:
		return "C-"
	elif score >= 67:
		return "D+"
	elif score >= 64 and score < 97:
		return "D"
	elif score >= 60 and score < 64:
		return "D-"
	else:
		return "F"
		
# Take in courses list from data to calculate GPA using letter grades

		
def GPA(allClasses):
	
	# intialize Grade Point Total
	GPTotal = 0.00
	
	# find total possible grade points
	
	TotalCredits = 0.0 
	
	for course in allClasses:
	
	    TotalCredits += course["gp"]
	
	
	
	for course in allClasses:
		
		classLetter = get_letter(get_average(course))
		
        #assign letter grade to grade point equivalent and multiply by total possible points
		if classLetter == "A+" or classLetter == "A":
			GPTotal += 4.00*course["gp"]
		elif classLetter == "A-":
			GPTotal += 3.67*course["gp"]
		elif classLetter == "B+":
			GPTotal += 3.33*course["gp"]
		elif classLetter == "B":
			GPTotal += 3.00*course["gp"]
		elif classLetter == "B-":
			GPTotal += 2.67*course["gp"]
		elif classLetter == "C+":
			GPTotal += 2.33*course["gp"]
		elif classLetter == "C" or classLetter == "C-" or classLetter == "D+":
			GPTotal += 2.00*course["gp"]
		elif classLetter == "D":
			GPTotal += 1.00*course["gp"]
		else:
			GPTotal += 0.00

    
	return GPTotal/TotalCredits
	
	
# Function to add grades	
	
def addGrade(course, section, grade):

    # Determine class
    
    appended = data["courses"][course][section]
    
    # Append list  
	
    appended.append(grade)
    print appended
    return appended
	
	


def removeGrade(course, section):
	"""
	Function removes grades from JSON file 
	"""

    # Determine class
    
    removed = data["courses"][course][section]
    
    # delete most recent entry 
	
    last = len(removed) - 1
    
    del removed[last] 
    print removed
    return removed

# Import all course data

with open('GradeBook.json') as f:
  data = json.load(f)




# Menu Interface



print
print
print "#######################################"
print "#                                     #"
print "#   Hi, Ian.                          #"
print "#                                     #"
print "#   Let's see how you're doing...     #"
print "#                                     #"
print "#######################################"
print 
print





#PASSWORD

pswd = "false"
while pswd != "mezzanine":
	pswd = getpass.getpass('PASSWORD : ')

# menu loop

while pswd == "mezzanine":

	
	print
	print
	selection = raw_input("What would you like to do? : ")
	type(selection)
	
	# Make case insensitve 
	selection = selection.lower()
	print 
	print


################################################################################
	
	if selection == "view letters":
		
		print "Here are your letter grades: "
		print "======================================================"
		print
		
		# loop through each class in class_list to retrieve letter grade by input of score
		
		for course in data['courses']:
			
			print "#  " + course["Course"] + " =========> " + get_letter(get_average(course))
		
		print
		print "======================================================="	
		print 
		
################################################################################
		
	elif selection == "view scores":
	
		print "Here are your numerical averages:"
		print "======================================================="
		print
		
		# loop through each class in class_list and retrieve only numerical average
		
		for course in data['courses']:
			
			avg = get_average(course)
			avg = str(avg)
			print "#  " + course["Course"] + " ============> " + avg 
		
		print
		print "======================================================="	
		print 
		
		
################################################################################		
		
		# call gpa function
		
	elif selection == "view gpa":
		print "====================="
		print "#       " + str(GPA(data['courses'])) + "         #"
		print "====================="
		print
		print
	
	
		
################################################################################		
		
	elif selection == "view all":
		
		
		
		print "Here are your grades so far: "
		print "======================================================="
		print 
		print "Your GPA is currently: %f" % GPA(data['courses'])
		print

		# loop through each class in class_list and call all functions
		
		for course in data['courses']:
			
			
			
			print "#  " + course["Course"] + " =========> " \
			 + get_letter(get_average(course)) \
			  + " with a score of ~ %d" % get_average(course)
			  
		print
		print "======================================================="	
		print
	
################################################################################
		
	elif selection == "view homework":
	    
	    	
		for course in data['courses']:
		        
		        print course["Course"].upper()
		        print
		        print course["Homework"] 
		        print
		        print "========================================================"
		        print

################################################################################
		    
	elif selection == "view quizzes":
	    
	    	
	    for course in data['courses']:
		        
		        print course["Course"].upper()
		        print
		        print course["Quizzes"] 
		        print
		        print "========================================================"
		        print	

################################################################################
		
	elif selection == "view tests":
	    
	    	
	    for course in data['courses']:
		        
		        print course["Course"].upper()
		        print
		        print course["Tests"] 
		        print
		        print "========================================================"
		        print	

################################################################################
		        
	elif selection == "view labs":
	    
	    	
	    for course in data['courses']:
		        
		        print course["Course"].upper()
		        print
		        print course["Labs"] 
		        print
		        print "========================================================"
		        print			        

################################################################################
		        
	elif selection == "view projects":
	    
	    	
	    for course in data['courses']:
		        
		        print course["Course"].upper()
		        print
		        print course["Projects"] 
		        print
		        print "========================================================"
		        print	
		        
################################################################################

# Add grade 
# Call addGrade

        elif selection == "add grade":
        
        
        
            cls = "bunk"
            
            while (cls != 0 and cls !=1 and cls != 2 and cls != 3) : 
            
              cls = raw_input("Course: ")
              print
              type("cls")
              cls = cls.lower()
          
              if cls == "sci comp":
            
                  cls = 0
                  
                  print "Confirmed"
                  print
            
            
              elif cls == "linear":
          
                  cls = 1
                  
                  print "Confirmed"
                  print
            
          
              elif cls == "prob":
          
                  cls = 2
                  
                  print "Confirmed"
                  print
            
            
              elif cls == "java":
          
                  cls = 3
                
                  print "Confirmed"
                  print
            
              else:
                
                  cls = "invalid"
                  print cls   
                
              
              
            sec = raw_input("Section: ")
            type(sec)
        
       
            print 
            print "Grade: "
            print
            grade = input()
            type(grade)
        
            addGrade(cls, sec, grade)

            print
            
                                 
################################################################################

# Remove grade 
# Call removeGrade

        elif selection == "remove":
        
        
        
            cls = "bunk"
        
           
            
            while (cls != 0 and cls !=1 and cls != 2 and cls != 3) : 
            
              cls = raw_input("Course: ")
              print
              type("cls")
              cls = cls.lower()
          
              if cls == "sci comp":
            
                  cls = 0
                  
                  print "Confirmed"
                  print
            
            
              elif cls == "linear":
          
                  cls = 1
                  
                  print "Confirmed"
                  print
            
          
              elif cls == "prob":
          
                  cls = 2
                  
                  print "Confirmed"
                  print
            
            
              elif cls == "java":
          
                  cls = 3
                
                  print "Confirmed"
                  print
            
              else:
                
                  cls = "invalid"
                  print cls   
                
              
              
            sec = raw_input("Section: ")
            type(sec)
        
      
        
            removeGrade(cls, sec)

            print





################################################################################
        elif selection == "save":
    
          with open ('GradeBook.json', 'w') as outfile:
            json.dump(data, outfile, indent = 2)
            print "CONFIRMED SAVE AS: \"GradeBook.json\""
################################################################################
    		        		        
		        		
	elif selection == "quit":
		
		print
		print "Go study."
		print
		sys.exit()
	
	
		
		
			
		
			
	
			

		
		

		
	

	
	
	








			
			
			
	
	
	
	

	
	




