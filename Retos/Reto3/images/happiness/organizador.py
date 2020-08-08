import os
import shutil
from csv import reader

# Rutas 
#ruta_csv = '/home/juferoga/repos/facial_expressions/data/legend.csv'
ruta_csv = '/home/juferoga/repos/facial_expressions/data/500_picts_satz.csv'
#ruta_img = '/home/juferoga/repos/facial_expressions/images/'

# directories of emotions
ruta_anger = './anger/'
ruta_contempt = './contempt/'
ruta_disgust = './disgust/'
ruta_fear = './fear/'
ruta_happiness = './happiness/'
ruta_neutral = './neutral/'
ruta_sadness = './sadness/'
ruta_surprise = './surprise/'

ruta_tmp = '/tmp/IMAGES/'

the_image = 'AAAAA_thefile.jpg'

i=0

with open(ruta_csv) as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        try:
            if row[2] == "anger":
                print("Anger")
                shutil.move(row[1],ruta_anger)
            elif row[2] == "contempt":
                print("Contempt")
                shutil.move(row[1],ruta_contempt)
            elif row[2] == "disgust":
                print("Disgust")
                shutil.move(row[1],ruta_disgust)
            elif row[2] == "fear":
                print("Fear")
                shutil.move(row[1],ruta_fear)
            elif row[2] == "happiness":
                print("Happiness")
                shutil.move(row[1],ruta_happiness)
            elif row[2] == "neutral":
                print("Neutral")
                shutil.move(row[1],ruta_neutral)
            elif row[2] == "sadness":
                print("Sadness")
                shutil.move(row[1],ruta_sadness)
            elif row[2] == "surprise":
                print("Surprise")
                shutil.move(row[1],ruta_surprise)
            else:
                shutil.move(row[1],ruta_tmp)
                #os.rename("./"+the_image,ruta_tmp)
        except:
            print("no encontrado",row[1],ruta_tmp)
    # print(row[1])
        # print(row[2])
        # if(row[2] == "anger"):
        #     print(row[1],row[2])
        # i=i+1