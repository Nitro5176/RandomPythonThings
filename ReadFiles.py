import pdfplumber
import pyttsx3
import time
import keyboard

pdf = pdfplumber.open('.pdf')
page = pdf.pages[0]
text = page.extract_text()

questions = []
answers = []
numbers = "1234567890"
numbers = ["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9." "10.", "11.", "12.", "13.", "15.", "16."]
letters = ["a.", "b.", "c.", "d.", "e.", "f.", "g", "h."]

listOfWords = text.replace("\t", " ").splitlines()
# engine = pyttsx3.init()
# engine.say(text)
# engine.runAndWait()
for i in listOfWords:

    for j in numbers:
        if j in i:
            questions.append(i)
            break
    for j in letters:
        if j in i:
            answers.append(i)
            break

    # print(questions)
    # print(answers)

countQ = 0
countA = 1


def speak(speakThis):
    engine = pyttsx3.init()
    engine.say(speakThis)
    engine.runAndWait()

countinganswers = 1
while True:
    flag = False
    speak(questions[countQ])
    userIn = input("enter to continue or r for repeat: ").lower()
    if userIn == "r":
        flag = True
    elif userIn == "":
        print("Answers")
    else:
        while True:
            print("are you stupid? im asking r or enter key")
            userInput = input("enter to continue or r for repeat: ").lower()
            if userInput == "":
                break
            elif userInput == "r":
                flag = True


    while flag:
        speak(questions[countQ])
        userIn = input("enter to continue or r for repeat: ")
        if userIn == "":
            flag = False
        elif userIn == "r":
            flag = True
        else:
            print("are you stupid? im asking r or enter key")


    countQ += 1
    repetitive = 0
    for i in answers[countA:]:
        if letters[0] in i:
            repetitive += 1
        if repetitive > 1:
            countA = countinganswers
            break
        speak(answers[countinganswers])
        userIn = input("enter to continue or r for repeat: ")
        if userIn == "r":
            flag = True
        elif userIn == "":
            print("next Answer")
        else:
            while True:
                print("are you stupid? im asking r or enter key")
                userInput = input\
                ("enter to continue or r for repeat: ").lower()
                if userInput == "":
                    break
                elif userInput == "r":
                    flag = True

        while flag:
            speak(answers[countinganswers])
            userIn = input("enter to continue or r for repeat: ")
            if userIn == "":
                flag = False
            elif userIn == "r":
                flag = True
            else:
                print("are you stupid? im asking r or enter key")
        countinganswers += 1
        # speak(answers)
    speak("end of question")
    input("Click enter to continue: ")





print(text)
pdf.close()
