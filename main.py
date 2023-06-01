# Driver program for chord quiz
import argparse 
import matplotlib.pyplot as plt
import numpy as np
import random

def main(args):
    chord_list = open('chords/chords.txt', 'r').readlines()
    chord_list = [x.strip() for x in chord_list]
    
    while True:
        chord = random.choice(chord_list)
        img = plt.imread(f'chords/img/{chord}.png')
        # mp3 = load_mp3()
        print(chord)
        plt.imshow(img)
        plt.show()
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--endless', action='store_true', help="Ednlessly loop through chords, instead of finish quiz")
    main(None)