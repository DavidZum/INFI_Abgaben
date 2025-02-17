from tensorflow import keras
from keras import layers

num_classes = 3
input_shape = (180, 180, 3)

d = keras.preprocessing.image_dataset_from_directory('Aufgabe_06/img_resized/', image_size=(180, 180), label_mode='categorical', batch_size= 1000)

images = None
labels = None

print("Class names: %s" % d.class_names) # Welche Kategorien gibt es generell


for d, l in d.take(1):
    images = d
    labels = l
    
print(images.shape)

model = keras.Sequential([
keras.Input(shape=input_shape),
    layers.Rescaling(1.0 / 255),
    layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
    layers.BatchNormalization(),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
    layers.BatchNormalization(),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(128, kernel_size=(3, 3), activation="relu"),
    layers.BatchNormalization(),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(256, kernel_size=(3, 3), activation="relu"),
    layers.BatchNormalization(),
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.5),
    layers.Dense(128, activation="relu"),
    layers.Dense(num_classes, activation="softmax"),
    ])

model.summary()

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

history = model.fit(images, labels, batch_size=128, epochs=20, validation_split=0.1)


model.save('Aufgabe_06/model.h5')
model.save_weights('Aufgabe_06/model.weights.h5')