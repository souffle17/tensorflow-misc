import numpy as np
import keras._tf_keras.keras as keras
from keras._tf_keras.keras.datasets import cifar10
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras._tf_keras.keras.optimizers import Adam

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

print("Additional convolution layers: ", end="")

num_conv_layers = int(input())
    
print("Additional fully connected layers: ", end="")

num_dense_layers = int(input())
    
print("Epochs: ", end="")

num_epochs = int(input())

print("Model name: ", end="")

model_name = input()

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
for x in range(num_conv_layers): 
    model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
for x in range(num_dense_layers): 
    model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy'])

model.fit(x_train, y_train, epochs=num_epochs, validation_data=(x_test, y_test))

model.save(f"{model_name}.keras")