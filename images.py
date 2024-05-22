import numpy as np
import matplotlib.pyplot as plt
import pickle
from keras.models import load_model as ld
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = ld("C:/Users/hp/Desktop/Siri Raj Benda/Theft-Detection/models/model_14.h5")

model_temp = ResNet50(weights="imagenet", input_shape=(224,224,3))

model_resnet = Model(model_temp.input,model_temp.layers[-2].output)

def preprocess_image(img):
    img = image.load_img(img, target_size=(224,224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

def encode_image(img_path):
    img = preprocess_image(img_path)
    feature_vector = model_resnet.predict(img)
    feature_vector = feature_vector.reshape((1,feature_vector.shape[1]))
    return feature_vector


with open("C:\/Users/hp/Desktop/Siri Raj Benda/Theft-Detection/pickle_files/word_to_idx.pkl","rb") as f:
    word_to_idx = pickle.load(f)
    
with open("C:/Users/hp/Desktop/Siri Raj Benda/Theft-Detection/pickle_files/idx_to_word.pkl","rb") as f:
    idx_to_word = pickle.load(f)

def predict_caption(photo):
    in_text = "startseq"
    max_len = 35
    for _ in range(max_len):
        sequence = [word_to_idx[w] for w in in_text.split() if w in word_to_idx]
        sequence = pad_sequences([sequence], maxlen=max_len, padding='post')

        ypred =  model.predict([photo,sequence])
        ypred = ypred.argmax()
        word = idx_to_word[ypred]
        in_text+= ' ' +word
        
        if word =='endseq':
            break
        
        
    final_caption =  in_text.split()[1:-1]
    final_caption = ' '.join(final_caption)
    
    return final_caption

def caption_this_image(image):
    encode = encode_image(image)
    caption = predict_caption(encode)
    return caption

