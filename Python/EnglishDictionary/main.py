import functions
import sys

def main():

    while True:
        word = input("Find a name in English dictionary: ")
        word = word.lower()
        if word == '/exit':
            break
        elif functions.translate(word):
            print (' \n'.join(functions.translate(word)))
        elif functions.similar_search(word):
            searched = functions.similar_search(word)
            print ('Did you mean?(Y/N):',searched)
            answer = str(input())
            answer = answer.lower()
            if answer == 'y':
                print (' \n'.join(functions.translate(searched)))
            else:
                print ("Unknown word... Try again or type '/exit' to quit.")
        else:
            print ("Unknown word... Try again or type '/exit' to quit.")


if __name__ == '__main__':
    main()