import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
from torch import optim

import torchvision 
from torchvision import transforms
from Vgg import VGG

def load_image(image_file):
	img = Image.open(image_file)
	return img

class StyleTransfer:

    def __init__(self) -> None:
        self.vgg = VGG()
        pass

    def runStyleTransfer() -> outputImage:
        outputImage = None
        
        max_iter = 500
        show_iter = 50
        optimizer = optim.LBFGS([self.opt_img])
        n_iter=[0]

        while n_iter[0] <= max_iter:
            
            def closure():
                optimizer.zero_grad()
                out = self.vgg(opt_img, loss_layers)
                layer_losses = [weights[a] * loss_fns[a](A, targets[a]) for a,A in enumerate(out)]
                loss = sum(layer_losses)
                loss.backward()
                n_iter[0]+=1

                return loss
            optimizer.step(closure)
        
        out_img = postp(opt_img.data[0].cpu().squeeze())




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
