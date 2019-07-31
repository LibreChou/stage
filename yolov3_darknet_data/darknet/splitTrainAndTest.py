import random
import os
import subprocess
import sys

def split_data_set(image_dir):

    f_test = open("data_test.txt", 'w')
    f_val = open("data_val.txt", 'w')
    f_train = open("data_train.txt", 'w')
    
    path, dirs, files = next(os.walk(image_dir))
    data_size = len(files)
    data_train_size = int(0.8 * data_size)

    ind = 0
    number_test = 0
    data_test_size = int(0.1 * data_size)
    test_array = random.sample(range(data_size), k=data_test_size)
    
    for f in os.listdir(image_dir):
        if(f.split(".")[1] == "JPG"):
            ind += 1
            if ind in test_array:
                f_test.write(image_dir+'/'+f+'\n')
                number_test += 1
            else:
                f_train.write(image_dir+'/'+f+'\n')

    indice = -10
    nb = 0
    number_val = 0
    number_train = 0
    data_val_size = int(0.1 * data_size)
    val_array = random.sample(range(data_train_size), k=data_val_size)

    f_train = open("data_train.txt", 'r')
    lines = f_train.readlines()
    f_train.close()
    f_train = open("data_train.txt", 'w')
    for line in lines:
            indice += 1
            if indice in val_array:
                f_val.write(line)
            else:
                number_train += 1
                f_train.write(line)
    f_train.close()
    f_val.close()
    f_test.close()
    print("Nombre d'images au total :",len(os.listdir(image_dir)))
    print("Nombre d'images en apprentissage :",number_train)
    print("Nombre d'images en validation :",len(val_array))
    print("Nombre d'images en test :",len(test_array))
split_data_set(sys.argv[1])
