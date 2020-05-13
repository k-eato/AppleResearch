import numpy as np
import pandas as pd
import tensorflow.keras
import tensorflow as tf
import scipy
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import  Dropout, Input
from tensorflow.keras.layers import Dense, Flatten, GaussianNoise, AveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import itertools
import matplotlib.pyplot as plt

def run():
        train_path = '/home/keato/Documents/ResearchProject/models/research/labelImg/data/classify_train'
        valid_path = '/home/keato/Documents/ResearchProject/models/research/labelImg/data/val'
        test_path = '/home/keato/Documents/ResearchProject/models/research/labelImg//data/classify_test'
        train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(224,224), classes=['Healthy_Apple', 'Rotten_Apple'], batch_size=25)
        valid_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size=(224,224), classes=['Healthy_Apple', 'Rotten_Apple'], batch_size=25)
        test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(224,224), classes=['Healthy_Apple', 'Rotten_Apple'], batch_size=25)


	# plots images with labels within jupyter notebook
        def plots(ims, figsize=(24,12), rows=4, interp=False,
	titles=None):
            if type(ims[0]) is np.ndarray:
                ims = np.array(ims).astype(np.uint8)
                if (ims.shape[-1] != 3):
                   ims = ims.transpose((0,2,3,1))
            f = plt.figure(figsize=figsize)
            cols = len(ims)//rows if len(ims) % 2 == 0 else len(ims)//rows + 1
            for i in range(len(ims)):
                sp = f.add_subplot(rows, cols, i+1)
                sp.axis('Off')
                if titles is not None:
                   sp.set_title(titles[i], fontsize=32)
                plt.imshow(ims[i], interpolation=None if interp else 'none')

        imgs, labels = next(train_batches)
        plots(imgs, titles=labels)
        vgg16_model = tensorflow.keras.applications.resnet50.ResNet50(weights='imagenet', include_top=False, input_tensor=Input(shape=(224,224,3)))

        for layer in vgg16_model.layers[:-13]:
             layer.trainable = False
        	 
        # Create the model
        model = Sequential()
 
	# Add the vgg convolutional base model
        model.add(vgg16_model)
 
	# Add new layers
        #model.add(AveragePooling2D(pool_size=2))
        model.add(Flatten())
        model.add(Dropout(0.5))
        model.add(Dense(800, activation='relu'))
        model.add(Dropout(0.5))
        model.add(GaussianNoise(.1))
        model.add(Dense(2, activation='softmax'))
        
	 
	# Show a summary of the model. Check the number of trainable parameters
        model.summary()

        model.compile(loss='categorical_crossentropy', optimizer=tensorflow.keras.optimizers.Adam(lr=1e-4), metrics=['acc'])
        history = model.fit_generator(
              train_batches,
              steps_per_epoch=train_batches.samples/train_batches.batch_size ,
              epochs=4,
              validation_data=valid_batches,
              validation_steps=valid_batches.samples/valid_batches.batch_size,
              verbose=1)

        def to_label(value):
            if value==0:
               return 'Healthy'
            else:
               return 'Rotten'
        test_imgs, test_labels = next(test_batches)
        predictions = model.predict(test_imgs)
        df = pd.DataFrame()
        df['actual'] = test_labels[:,1]
        df['predicted'] = np.round(predictions[:,1])
        df['predicted_labels']=df['predicted'].map(lambda x: to_label(x))
        plots(test_imgs, titles=df['predicted_labels'])
        while next(test_batches, '0') != '0':
            test_imgs, test_labels = next(test_batches)
            test_loss, test_acc = model.evaluate(test_imgs,  test_labels, verbose=2)
            print('\nTest accuracy:', test_acc)














