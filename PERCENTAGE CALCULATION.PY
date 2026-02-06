print("Enter Marks Obtained in four subjects: ")
Math = int(input("Maths :"))
English = int(input("English :"))
Science = int(input("Science :"))
SocialStudies = int(input("Social Studies: "))
sum = Math+English+Science+SocialStudies
print("sum of Math,English,Science and Social Studies")

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)