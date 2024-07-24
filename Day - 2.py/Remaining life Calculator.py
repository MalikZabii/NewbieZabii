age= input ("What is your Current age?")
age_as_int= int(age)
years_remaining= 90-age_as_int
weeks_remaining= years_remaining*52
days_remaining=years_remaining*365
print ("You have "+ str(years_remaining) +" years remaining")
print ("You have "+ str(weeks_remaining) +" weeks remaining")
print ("You have "+ str(days_remaining) +" days remaining")

#This Program will consider that you will live until 90.