import streamlit as st
from keras.datasets import mnist
import matplotlib.pyplot as plt
from skimage import color
from skimage import io
from skimage.transform import resize
from sklearn.cluster import MiniBatchKMeans
import numpy as np
from sklearn import metrics
from sklearn.metrics import accuracy_score
import cv2
from sklearn.decomposition import PCA
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# On s'assurer que les valeurs sont flottantes afin que nous puissions obtenir des points décimaux après la division
x_train = x_train.astype('float')
x_test = x_test.astype('float')
# Normaliser les codes RVB en les divisant par la valeur RVB maximale.
x_train = x_train/255.0
x_test = x_test/255.0
# Redimmension des données d'entrée
X_train = x_train.reshape(len(x_train),-1)
X_test = x_test.reshape(len(x_test),-1)
#PCA
pca = PCA(.80)
pca.fit(X_train)
X_train = pca.transform(X_train)
X_test = pca.transform(X_test)

total_clusters = len(np.unique(y_test))
# Initialisation du modèle K-means
kmeans = MiniBatchKMeans(n_clusters = total_clusters)
kmeans.fit(X_train)


def retrieve_info(cluster_labels,y_train):
    reference_labels = {}
    for i in range(len(np.unique(kmeans.labels_))):
        index = np.where(cluster_labels == i,1,0)
        num = np.bincount(y_train[index==1]).argmax()
        reference_labels[i] = num
    return reference_labels

reference_labels = retrieve_info(kmeans.labels_,y_train)

y_pred = np.random.rand(len(kmeans.labels_))
for i in range(len(kmeans.labels_)):
    y_pred[i] = reference_labels[kmeans.labels_[i]]

# Testdu modèle sur le Test set
kmeans = MiniBatchKMeans(n_clusters = 256)
kmeans.fit(X_test)
#calculate_metrics(kmeans,y_test)
reference_labels = retrieve_info(kmeans.labels_,y_test)
y_pred = np.random.rand(len(kmeans.labels_))
for i in range(len(kmeans.labels_)):
    y_pred[i] = reference_labels[kmeans.labels_[i]]


# Text/Title
st.title("Application Streamlit de classification d'image")

# Header/Subheader
st.header("Hello Streamlit")
st.subheader("Choisissez une image!")
# Text
st.text("Télécharger votre image en cliquant sur browse files!")

# telecharger les images
import streamlit as st
from PIL import Image
import numpy as np

img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

image = Image.open(img_file_buffer)
img_array = np.array(image)

if image is not None:
    st.image(
        image,
        caption=f"You amazing image has shape {img_array.shape[0:2]}",
        use_column_width=True,
    )


gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
st.text(f"Votre image est de shape comme un :{gray.shape}.")
size = (28, 28)
image_resize = resize(gray,size,anti_aliasing=True)

image_resize = image_resize.reshape(1, 28*28)
image_resize = pca.transform(image_resize)
predicted_cluster = kmeans.predict(image_resize)

prediction = y_pred[[predicted_cluster]]


# Text
st.text(f"Votre image est prédite comme un :{prediction}.")