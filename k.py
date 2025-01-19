import speech_recognition as sr
import threading
import pyttsx3
import queue
import subprocess

def listen_for_audio(recognizer, microphone, audio_queue):
    with microphone as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Start speaking...")

        while True:
            try:
                
                audio = recognizer.listen(source)
                audio_queue.put(audio)  

            except sr.UnknownValueError:
                print("Sorry, I didn't understand that.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except KeyboardInterrupt:
                print("Stopping audio capture.")
                break


def recognize_speech(recognizer, audio_queue, language="en-US"):
    c=0
    newfile = ["hey", "jarvis", "open", "new", "file"]
    file = ["hey", "jarvis", "open", "existing", "file"]
    closefile=["hey", "jarvis", "close", "file"]
    youtube = ["hey", "jarvis", "open", "youtube"]
    closeyoutube=["hey", "jarvis", "close", "youtube"]
    chrome = ["hey", "jarvis", "open", "chrome"]
    closechrome=["hey","jarvis","close","chrome"]
    calculator = ["hey", "jarvis", "open", "calculator"]
    closecalculator=["hey", "jarvis", "close", "calculator"]
    replace=["hey","jarvis","replace"]
    nf=" "

    while True:
        if not audio_queue.empty():  
            audio = audio_queue.get()  

            try:
                print(f"Recognizing in {language}...")
                
                text = recognizer.recognize_google(audio, language=language)
                print(f"You said: {text}")
                
               
                if all(word in text.lower() for word in newfile):
                    c=1
                    a=input("Enter name of file:")
                    nf=open(f"{a}.txt",'w+')
                    print("file opened succesfully,")
                    print("Do not forget to close the file by saying hey jarvis close file")

                elif all(word in text.lower() for word in file):
                    c=2
                    b=input("Enter name of file you want to open:")
                    try:
                        nf=open(f"{b}.txt",'a+')
                        print("Existing file opened succesfully")
                        print("Do not forget to close the file by saying hey jarvis close file")
                    except Exception:
                        print("File not found or file does not exist")

                elif all(word in text.lower()for word in closefile):
                    if c!=0:
                        nf.close()
                        c=0
                        print("file closed")
                    else:
                        print("No file to close")
                  
                if all(word in text.lower() for word in youtube):
                    subprocess.Popen(['chrome', 'https://www.youtube.com'])
                    print("Opening YouTube...")

                if all(word in text.lower() for word in closeyoutube):
                    subprocess.run(['taskkill', '/F', '/IM','chrome.exe' ])
                    print("youtube closed")

                if all(word in text.lower() for word in chrome):
                    subprocess.run('chrome')
                    print("Opening Chrome...")

                if all(word in text.lower() for word in closechrome):
                    subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe'])
                    print("chrome closed")

                if all(word in text.lower() for word in calculator):
                    subprocess.run('calc')
                    print("Opening Calculator...")

                if all(word in text.lower() for word in closecalculator):
                  subprocess.run(['taskkill', '/F', '/IM', 'CalculatorApp.exe'])
                  print("Calculator closed")

                if all(word in text.lower() for word in replace):
                    if c!=0:
                        z=input("Enter word to replace:")
                        x=input("Enter new word to replace old word with")
                        nf.seek(0)
                        content=nf.read()
                        if z in content:
                            ucontent=content.replace(z,x)
                            nf.seek(0)
                            nf.truncate()
                            nf.write(ucontent)
                        else:
                            print("No such word found in file")

                    else:
                        print("No file open to perform replace operation")

                if c==1:
                    nf.write(text+" ")
                
                elif c==2:
                    nf.write(" "+text)
            except sr.UnknownValueError:
                print("Sorry, I didn't understand that.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")


audio_queue = queue.Queue()


    


language_input = input("Select language (1 for English, 2 for Gujarati): ")
if language_input == "2":
    language="gu-IN"
else:
   language="en-US"

recognizer = sr.Recognizer()
microphone = sr.Microphone()

    
listen_thread = threading.Thread(target=listen_for_audio, args=(recognizer, microphone, audio_queue))
listen_thread.daemon = True
listen_thread.start()

   
recognize_thread = threading.Thread(target=recognize_speech, args=(recognizer, audio_queue, language))
recognize_thread.daemon = True
recognize_thread.start()

    
listen_thread.join()
recognize_thread.join()
