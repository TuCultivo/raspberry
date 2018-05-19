import requests,json
import os
from PIL import Image

def send(lots, n_plants, id_farm):
    images_paths = os.listdir("images/")
    n_images = len(images_paths)
    if n_plants != n_images:
        print("el numero total de plantas no es igual al numero total de fotos")
        print("numero de plantas ingresadas: %d" % n_plants)
        print("el numero de fotos guardadas es %d" % n_images)
    else:
        url = 'http://pi2tucultivo.dis.eafit.edu.co/'
        cont = 0

        for i in lots.keys():
            for j in lots[i].keys():
                for k in range(lots[i][j]):
                    name = str(id_farm) + "_" + i + "_" + j + "_" +str(k+1) + ".jpg"
                    file = Image.open('images/' + images_paths[cont])
                    file.save('send/' + name)
                    cont += 1

        for image in os.listdir("send"):
            file = {'file':open('send/' + image, 'rb')}
            sended = False
            while not sended:
                r = requests.post(url, files=file)
                if r.status_code == 200:
                    sended = True
                else:
                    print("imagen no pudo ser enviada, reintentando")

            try:
               os.remove('send/' + image)
               #os.remove('images/' + image)
            except: pass


if __name__ == "__main__":
    id_farm = int(input("Ingrese id del cultivo >> "))
    n_images = 0
    n_lots = input("Va a ingresar imagenes de cuantos lotes? >> ")
    lots = {}
    for i in range(int(n_lots)):
        id_lot = input("Ingrese id del lote numero %d (en orden cronologio de tomada de fotos) >> " %(i+1))
        n_grooves = input("Va a ingresar imagenes de cuantos surcos del lote %d? >> " % (int(id_lot)))
        grooves = {}
        for j in range(int(n_grooves)):
            id_groove = input("Ingrese id del surco numero %d (en orden cronologio de tomada de fotos) >> " % (j+1))
            n_plants = int(input("Ingrese el numero de plantas del surco %d >> " % (int(id_groove))))
            grooves[id_groove] = n_plants
            n_images += n_plants
        lots[id_lot] = grooves
    send(lots, n_images, id_farm)
