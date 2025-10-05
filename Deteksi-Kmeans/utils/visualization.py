import matplotlib.pyplot as plt

def show_image_comparison(original, segmented):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax[0].imshow(original)
    ax[0].set_title("Citra Asli")
    ax[0].axis('off')
    ax[1].imshow(segmented)
    ax[1].set_title("Hasil Segmentasi")
    ax[1].axis('off')
    return fig
