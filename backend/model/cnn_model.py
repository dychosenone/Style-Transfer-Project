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

class Model():

    def __init__(self, content_img, style_img) -> None:
        self.cnn = models.vgg19(pretrained=True)

        self.norm_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
        self.norm_std = torch.tensor([0.229, 0.224, 0.225]).to(device)

        self.image_size = 128
        self.loader = transforms.Compose([transforms.Resize(self.image_size),
                transforms.ToTensor()])

        self.unloader = transforms.ToPILImage()

    def __call__(self, content_img, style_img) -> None:

        styleImage = self.loadImage(style_img)
        contentImage = self.loadImage(content_img)

        plt.figure()
        self.imshow(styleImage)

        pass

    # View Image Function
        
    def imshow(self, tensor, title=None):
        image = tensor.cpu().clone()  # we clone the tensor to not do changes on it
        image = image.squeeze(0)      # remove the fake batch dimension
        image = self.unloader(image)
        plt.imshow(image)
        if title is not None:
            plt.title(title)
        plt.pause(0.001) # pause a bit so that plots are updated

    # Load Image Function
    def loadImage(self, path):
        image = Image.open(path)
        image = self.loader(image).unsqueeze(0)

        return image.to(device, torch.float)

    