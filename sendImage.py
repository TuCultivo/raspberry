import requests,json
import os

def send(lots, n_plants):
    images_paths = os.listdir(".")
    n_images = len(images_paths)
    if n_plants != n_images:
        print("el numero total de plantas no es igual al numero total de fotos")
        print("numero de plantas ingresadas: %d" % n_plants)
        print("el numero de fotos guardadas es %d" % n_images)
    else:
        url = 'http://pi2tucultivo.dis.eafit.edu.co/'
        cont = 0
        #print(lots)
        #print(lots["1"])
        #print(len(lots["1"]["1"]))
        for i in lots.keys():
            for j in lots[i].keys():
                for k in range(lots[i][j]):
                    name = i + "_" + j + "_" + "1" + "_" +str(k+1) + ".jpg"
                    print(name)
                    # file = open(images_paths[cont], 'rw')
                    # file.write('send/' + name)
                    # file.close()

        send_images_paths = os.listdir("send/")
        for image in send_images_paths:
            file = {'file':open('send/' + image, 'rb')}
            sended = False
            while not sended:
                
            # file = {'file':open('images/' + image, 'rb')}
            # sended = False
            # while not sended:
            #     r = request.post(url, files=file)
            #     if r.status_code == 200:
            #         sended = True
            #         print("sended image %s, original: %s" %(image, renamed))

#
# files ={'file':open('1_1_1_2.jpg', 'rb')}
# enviado=False
# while enviado==False:
#     r=requests.post(url, files=files)
#     if r.status_code == 200:
#         enviado=True
#         print(r.status_code)

if __name__ == "__main__":
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
    #print(lots)
    #print(list(lots.keys())[0])
    send(lots, n_images)
