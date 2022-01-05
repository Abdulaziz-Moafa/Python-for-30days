#dictionaries

convert_month = {
    "Jan":"january",
    "feb": "febraury",
    "mar": ["march ","is the third month",1,2,3],
    4:444,
    5:True

}
print(convert_month["mar"])

print(convert_month.get("azoz ", "the value does not exist")) #is better than print(convert_month["mar"]) bc it gaves notes if the value are exist or not
print(convert_month.get(4, "the value does not exist"))
print(convert_month.get(5, "the value does not exist"))

sampleSet = {"Jodi", "Eric", "Garry"}
sampleSet.add("Vicki")
print(sampleSet)