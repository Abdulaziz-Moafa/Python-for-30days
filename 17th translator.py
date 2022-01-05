

def translate (str): #functon take fron the user
    translation = ""
    for letter in str: #for loop ,, for checking every latter
        if letter in "aeiou": #اذا في حرف من الكلمة متطابق مع الاحرف هذي
            translation = translation+"z" #حوله الحرف الى z
        else:
            translation = translation + letter
    return translation

print(translate(input("enter a phrase : ")))
##########################

def translate(str):
    for letter in str:
        if letter in "aieouAIEOU":
            if letter.islower ():
                str = str.replace (letter , "z")
            else:
                str = str.replace (letter , "Z")
    return str

print (translate(input("Enter a phrase : ")))
