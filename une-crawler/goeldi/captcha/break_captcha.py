import pickle
from keras.models import load_model
import numpy as np
import cv2

def Tratar_Imagem(path):
    img = cv2.imread(path, 0)
    _, img = cv2.threshold(
        img, 127, 255, cv2.THRESH_BINARY or cv2.THRESH_OTSU)
    img = img[0:50, 40:160]
    letra1 = img[0:50, 0:24]
    letra1 = np.expand_dims(letra1, axis=2)
    #cv2.imwrite(f'test/letra1.png', letra1) 
    letra2 = img[0:50, 24:48]
    letra2 = np.expand_dims(letra2, axis=2)
    #cv2.imwrite(f'test/letra2.png', letra2) 
    letra3 = img[0:50, 48:72]
    letra3 = np.expand_dims(letra3, axis=2)
    #cv2.imwrite(f'test/letra3.png', letra3) 
    letra4 = img[0:50, 72:96]
    letra4 = np.expand_dims(letra4, axis=2)
    #cv2.imwrite(f'test/letra4.png', letra4) 
    letra5 = img[0:50, 96:120]
    letra5 = np.expand_dims(letra5, axis=2)
    #cv2.imwrite(f'test/letra5.png', letra5)
    dados = [letra1, letra2, letra3, letra4, letra5]
    dados = np.array(dados, dtype='float') / 255

    return dados

def BreakCaptcha(path):

    with open(r'goeldi\captcha\label.dat', 'rb') as label:
        lb = pickle.load(label)
        label.close()

    model = load_model(r"goeldi\captcha\modelo_treinado.hdf5")

    dados = Tratar_Imagem(path)
    pred = model.predict(dados)
    r = lb.inverse_transform(pred)

    return "".join(list(r))


