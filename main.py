'''

Code taken from: https://github.com/leongatys/PytorchNeuralStyleTransfer
Paper by Leo Gatys: https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf

'''

from PIL import Image



def load_image(image_file):
	img = Image.open(image_file)
	return img



def main():

    st.title("Photorealistic Style Transfer")
    st.write("Developed by Lorenz Alog, Jacob Dy, Jose Noblefranca and Patrick Ong")

    st.subheader("Upload Images for Style Transfer")

    content_image = st.file_uploader("Upload Content Image", type=["png","jpg","jpeg"])
    style_image = st.file_uploader("Upload Style Image", type=["png","jpg","jpeg"])

    #Final Output

    if style_image is not None:
        st.subheader("Final Output")
        st.image(load_image(style_image), width=250)


if __name__ == "__main__":
    main()
