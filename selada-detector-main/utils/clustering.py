from sklearn.cluster import KMeans
import numpy as np

def apply_kmeans(img, k=3):
    pixel_values = img.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k, random_state=0).fit(pixel_values)
    clustered_img = kmeans.cluster_centers_[kmeans.labels_].reshape(img.shape)
    clustered_img = (clustered_img * 255).astype(np.uint8)
    return clustered_img, kmeans.labels_.reshape(img.shape[:2])
