'''
    In this program we are going to convert text to speech using google text to speech API.
    To use the above mentioned API, we need to import gTTS from gtts. Before that you have
    to install the gtts package using the command 'py -m pip install gtts'
'''
from gtts import gTTS
import os
from playsound import playsound # this is package is used to play audio

class FileOperation:
    '''This class is going to perform all the operations that needed for this program'''
    def __init__(self) -> None:
        self.__fname = input('Enter a name for text file:   ') + '.txt'
        self.__audioFile = input('Enter a name for audio file: ') + '.mp3'

    def writeFile(self) -> None:
        os.system('cls')
        if self.__fname.endswith('.txt'):
            with open(self.__fname,'w') as file:
                print('Enter the sentence you want to write into the file:')
                print('Enter ; for end of line',end='\n\t')
                sentence = input()
                sentence = sentence.replace(";","\n",-1)
                file.write(sentence)
        else:
            print('File name should be ended with .txt')   
        print(end='\n\n\n') 

    def readFile(self) -> None:
        os.system('cls')
        if self.__fname.endswith('.txt'):
            try:
                with open(self.__fname,'r') as file:
                    print('The file content is:')
                    print(file.read())
            except IOError:
                print(f'{self.__fname} file is not exists in the mentioned directory')
        else:
            print('File name should be ended with .txt')
        print(end='\n\n\n')

    def appendFile(self) -> None:
        os.system('cls')
        if os.path.isfile(self.__fname):
            with open(self.__fname,'a') as file:
                print('Enter the sentence you want to append into the file:')
                print('Enter ; for end of line',end='\n\t')
                sentence = input()
                sentence = sentence.replace(";","\n",-1)
                file.write(sentence) 
        else:
            print(f'{self.__fname} file does not exits')
        print(end='\n\n\n')

    def changeName(self) -> None:
        os.system('cls')
        print('Which file name do you want to change\n\t1.Text file\t(or)\n2.Audio file')
        choice = int(input())
        if choice == 1:
            newName = input('Enter new name for text file:\t')
            os.rename(self.__fname,newName)
            self.__fname = newName
        elif choice == 2:
            newName = input('Enter new name for audio file:\t')
            os.rename(self.__audioFile,newName)
            self.__audioFile = newName
        else:
            print('Invalid choice')
        print(end='\n\n\n')
    
    def textToSpeech(self) -> None:
        os.system('cls')
        try:
            with open(self.__fname,'r') as file:
                data = file.read()
                convertor = gTTS(text = data, lang='en', slow=False)
                convertor.save(self.__audioFile)
        except IOError:
            print(f'No file such as {self.__fname}')
        except Exception as e:
            print(e)
        else:
            print('Text file successfully converted to audio file')
        print('\n\n\n')

    def playAudio(self) -> None:
        try:
            playsound(self.__audioFile)
        except IOError:
            print(f'No such file as {self.__audioFile} to play')
        except Exception as e:
            print(e)
        else:
            print("Audio is successfully played")
        print('\n\n')

def main():
    action = FileOperation()
    switch = {
        1 : action.writeFile,
        2 : action.readFile,
        3 : action.appendFile,
        4 : action.changeName,
        5 : action.textToSpeech,
        6 : action.playAudio
    }
    while True:
        print("1.Write File\n2.Read File\n3.Append File\n4.Rename\n5.Convert Text to Speech\n6.Play the Audio\n0.Exit")
        choice = int(input('Enter your choice:  '))
        if choice != 0:
            requiredFunc = switch[choice]
            requiredFunc()
            print(type(requiredFunc))
        else:
            exit(0)
    
if __name__ == '__main__':
    os.system('cls')
    main()