import os

from mimetypes import init
from click import style

import torch
import torch.nn as nn
import torch.nn.functional as F

import torchvision.transforms as transforms
import torchvision.models as models

from PIL import Image
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
UPLOAD_FOLDER = './uploads/'


class ContentLoss(nn.Module):

    def __init__(self, target) -> None:
        super(self, ContentLoss).__init__()
        self.target = target.detach()

    def forward(self, input):
        self.loss = F.mse_loss(input, self.target)

class StyleLoss(nn.Module):
    def __init__(self, target_feature) -> None:
        super(self, StyleLoss).__init__()
        self.target = self.gramMatrix(target_feature).detach()

    def forward(self, input):
        g = self.gramMatrix(input)
        self.loss = F.mse_loss(G, self.target)
        return input

    def gramMatrix(self, input):
        b,c,h,w = input.size()
        F = input.view(b, c, h*w)
        G = torch.bmm(F, F.transpose(1,2)) 
        G.div_(h*w)
        return G

class Normalization(nn.Module):
    def __init__(self, mean, std) -> None:
        super(self, Normalization).__init__()

        self.mean = torch.tensor(mean).view(-1,1,1)
        self.std = torch.tensor(std).view(-1,1,1)

    def forward(self, image):
        output = (image - self.mean) / self.std
        return output

class Model():

    def __init__(self) -> None:
        self.cnn = models.vgg19(pretrained=True)

        self.norm_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
        self.norm_std = torch.tensor([0.229, 0.224, 0.225]).to(device)

        self.image_size = 128
        self.loader = transforms.Compose([transforms.Resize(self.image_size),
                transforms.ToTensor()])

        self.content_layers_default = ['conv_4']
        self.style_layers_default = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']

        self.normalization = Normalization(self.norm_mean, self.norm_std)

        self.model = nn.Sequential(self.normalization)

    def styleTransfer():
        pass
        

    def __call__(self, content_img, style_img) -> None:
        print(style_img)
        styleImage = self.loadImage(os.path.join(UPLOAD_FOLDER, style_img))
        contentImage = self.loadImage(os.path.join(UPLOAD_FOLDER, content_img))

        output = self.styleTransfer()

        return output

        pass

    # Load Image Function
    def loadImage(self, path):
        image = Image.open(path)
        image = self.loader(image).unsqueeze(0)

        return image.to(device, torch.float)

    