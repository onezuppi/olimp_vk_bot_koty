import pyttsx3
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice','en')
for v in voices:
    print(v.name)
    if v.name == "Microsoft Irina Desktop - Russian":
        tts.setProperty('voice',v.id)
tts.say("hello world")
tts.runAndWait()
