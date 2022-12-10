
import csv
import pandas as pd
import matplotlib.pyplot as plt

# silly script for getting hands dirty with some of the physical aspects of this data
with open('heart.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        line_count += 1
    print(f'Processed {line_count} lines.')


# first let's try and average age and gender across this dataset
# pretty simple

df = pd.read_csv("heart.csv")

sexcol = df["sex"]
agecol = df["age"]
cholcol = df["chol"]
colorcol = df["thal"]

mendata = []
womendata = []

mencholdata = []
womencholdata = []

menbpdata = []
womenbpdata = []

menpaindata = []
womenpaindata = []

mencolordata = []
womencolordata = []


num_male = 0
num_female = 0
total_age = 0
age_f = 0
age_m = 0

cholcol = df["chol"]
paincol = df["cp"]
bpcol = df["trestbps"]

for line in sexcol:
    if (line == 1):
        num_male = num_male + 1
    elif (line == 0):
        num_female = num_female + 1

print("Total Male: " + str(num_male))
print("Total Female: " + str(num_female))

# get the sample average

print("Avg male: " + str(float(num_male) / float(num_male + num_female)))
print("Avg female: " + str(float(num_female) / float(num_male + num_female)))

for line in agecol:
    total_age = total_age + line
    
print("Avg age: "  + str(float(total_age)/float(1025)))


for i in range(1,1025):
    if (sexcol[i] == 1):
        age_m = age_m + agecol[i]
        mendata.append(agecol[i])
        mencholdata.append(cholcol[i])
        menbpdata.append(bpcol[i])
        menpaindata.append(paincol[i])
        mencolordata.append(colorcol[i])
    elif (sexcol[i] == 0):
        age_f = age_f + agecol[i]
        womendata.append(agecol[i])
        womencholdata.append(cholcol[i])
        womenbpdata.append(bpcol[i])
        womenpaindata.append(paincol[i])
        womencolordata.append(colorcol[i])



print("Avg age female: "  + str(float(age_f)/float(1025)))
print("Avg age male: "  + str(float(age_m)/float(1025)))


print("Avg bp female: " + str(sum(womenbpdata)/len(womenbpdata)))
print("Avg bp male: " + str(sum(menbpdata)/len(menbpdata)))


print("Avg pain female: " + str(sum(womenpaindata)/len(womenpaindata)))
print("Avg pain male: " + str(sum(menpaindata)/len(menpaindata)))


print("Avg color female: " + str(sum(womencolordata)/len(womencolordata)))
print("Avg color male: " + str(sum(mencolordata)/len(mencolordata)))

print("Avg cholesterol female: " + str(sum(womencholdata)/len(womencholdata)))
print("Avg cholesterol male: " + str(sum(mencholdata)/len(mencholdata)))
      
# plot the distribution of sex and some of the hd data...
# such as age and serum cholesterol levels. 

df.plot(kind='scatter',x = "chol", y = "age")
plt.title("Cholesterol Level versus Age (Mixed Gender)")
plt.xlabel("Serum cholesterol level (mg/l)")
plt.ylabel("Age (years)")
plt.show()

plt.scatter(mencholdata, mendata)
plt.title("Cholesterol Level versus Age (Male)")
plt.xlabel("Serum cholesterol level (mg/l)")
plt.ylabel("Age (years)")
plt.show()


plt.scatter(womencholdata, womendata)
plt.title("Cholesterol Level versus Age (Women)")
plt.xlabel("Serum cholesterol level (mg/l)")
plt.ylabel("Age (years)")
plt.show()


df.plot(kind ='scatter', x='chol', y= 'cp')
plt.title("Cholesterol Level versus Chest Pain Severity (Mixed Gender)")
plt.xlabel("Serum cholesterol level (mg/l)")
plt.ylabel("Pain Level (0-3)")
plt.show()

df.plot(kind='bar', x='thal', y='chol')
plt.title("Cholesterol Level versus Number of Visible Arteries")
plt.xlabel("Serum cholesterol level (mg/l)")
plt.ylabel("Number of main arteries visible in fluoroscopy")
plt.show()


plt.title("Number of Arteries Visible after Fluoroscopy")
plt.xlabel("Number of main arteries visible in fluoroscopy")
plt.ylabel("Number of respondents (Mixed Gender)")
plt.hist(colorcol, 14)
plt.show()


plt.title("Number of Arteries Visible after Fluoroscopy (Male)")
plt.xlabel("Number of main arteries visible in fluoroscopy")
plt.ylabel("Number of respondents")
plt.hist(mencolordata, 14)
plt.show()


plt.title("Number of Arteries Visible after Fluoroscopy (Female)")
plt.xlabel("Number of main arteries visible in fluoroscopy")
plt.ylabel("Number of respondents")
plt.hist(womencolordata, 14)
plt.show()

df.plot(kind='scatter', x='chol', y='trestbps')
plt.title("Cholesterol Level versus Blood Pressure (Mixed Gender)")
plt.ylabel("Resting Blood Pressure (mm/Hg)")
plt.xlabel("Serum cholesterol level (mg/l)")
plt.show()


plt.scatter(womenpaindata, womencholdata)
plt.title("Cholesterol Level versus Chest Pain Severity (Female)")
plt.xlabel("Serum cholesterol level (mg/l)")
plt.ylabel("Pain Level (0-3)")
plt.show()

plt.scatter(womencholdata, womenbpdata)

plt.title("Cholesterol Level versus Blood Pressure (Female)")
plt.ylabel("Resting Blood Pressure (mm/Hg)")
plt.xlabel("Serum cholesterol level (mg/l)")
plt.show()


plt.scatter(mencholdata, menpaindata)
plt.title("Cholesterol Level versus Chest Pain Severity (Male)")
plt.xlabel("Serum cholesterol level (mg/l)")
plt.ylabel("Pain Level (0-3)")
plt.show()

plt.scatter(mencholdata, menbpdata)
plt.title("Cholesterol Level versus Blood Pressure (Male)")
plt.ylabel("Resting Blood Pressure (mm/Hg)")
plt.xlabel("Serum cholesterol level (mg/l)")
plt.show()
