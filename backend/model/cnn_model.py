import os
from numpy import iterable
from sympy import content

import torch.optim as optim

import torch
import torch.nn as nn
import torch.nn.functional as F

import torchvision.transforms as transforms
import torchvision.models as models

from PIL import Image

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
UPLOAD_FOLDER = './uploads/'


class ContentLoss(nn.Module):

    def __init__(self, target) -> None:
        super(ContentLoss, self).__init__()
        self.target = target.detach()

    def forward(self, input):
        self.loss = F.mse_loss(input, self.target)

class StyleLoss(nn.Module):
    def __init__(self, target_feature) -> None:
        super(StyleLoss, self).__init__()
        self.target = self.gramMatrix(target_feature).detach()

    def forward(self, input):
        g = self.gramMatrix(input)
        self.loss = F.mse_loss(g, self.target)
        return input

    def gramMatrix(self, input):
        b,c,h,w = input.size()
        F = input.view(b, c, h*w)
        G = torch.bmm(F, F.transpose(1,2)) 
        G.div_(h*w)
        return G

class Normalization(nn.Module):
    def __init__(self, mean, std) -> None:
        super(Normalization, self).__init__()

        self.mean = torch.tensor(mean).view(-1,1,1)
        self.std = torch.tensor(std).view(-1,1,1)

    def forward(self, image):
        output = (image - self.mean) / self.std
        return output

class Model():

    def __init__(self) -> None:
        self.cnn = models.vgg19(pretrained=True).features.to(device).eval()

        self.norm_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
        self.norm_std = torch.tensor([0.229, 0.224, 0.225]).to(device)

        self.image_size = 128
        self.loader = transforms.Compose([transforms.Resize(self.image_size),
                transforms.ToTensor()])

        self.content_layers_default = ['conv_4']
        self.style_layers_default = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']

        self.normalization = Normalization(self.norm_mean, self.norm_std)

        self.model = nn.Sequential(self.normalization)

        self.content_losses = []
        self.style_losses = []

        self.unloader = transforms.ToPILImage()

    def styleTransfer(self, inputImg, styleImage, contentImage, optimizer, style_weight, content_weight):
        
        inputImg.requires_grad_(True)
        self.model.requires_grad_(False)

        iter = [0]
        n_epoch = 300

        while iter[0] <= n_epoch:

            def closure():

                with torch.no_grad():
                    inputImg.clamp_(0,1)

                optimizer.zero_grad()
                self.model(inputImg)
                s_score = 0
                c_score = 0

                for s in self.style_losses:
                    s_score += s.loss
                for c in self.content_losses:
                    c_score += s.loss

                s_score *= style_weight
                c_score *= content_weight

                loss = s_score + c_score
                loss.backward()

                iter[0] += 1
                if iter[0] % 50 == 0:
                    print("run {}:".format(iter))

                return s_score + c_score
            optimizer.step(closure)
            
        with torch.no_grad():
            inputImg.clamp_(0,1)

        return inputImg
        

    def __call__(self, content_img, style_img) -> None:
        print(style_img)
        styleImage = self.loadImage(os.path.join(UPLOAD_FOLDER, style_img))
        contentImage = self.loadImage(os.path.join(UPLOAD_FOLDER, content_img))

        assert styleImage.size() == contentImage.size(), \
            "Same size required."

        inputImg = contentImage.clone()
        optimizer = optim.Adam([inputImg])

        i = 0
        for layer in self.cnn.children():
            print(layer)
            if isinstance(layer, nn.Conv2d):
                i += 1
                name = 'conv_{}'.format(i)

            elif isinstance(layer, nn.ReLU):
                name = 'relu_{}'.format(i)
                layer = nn.ReLU(inplace=False)

            elif isinstance(layer, nn.MaxPool2d):
                name = 'pool_{}'.format(i)

            elif isinstance(layer, nn.BatchNorm2d):
                name = 'bn_{}'.format(i)

            else:
                raise RuntimeError('Unrecognized layer: {}'.format(layer.__class__.__name__))

            self.model.add_module(name, layer)

            if name in self.content_layers_default:
                target = self.model(contentImage).detach()
                content_loss = ContentLoss(target)
                self.model.add_module("content_loss_{}".format(i), content_loss)
                self.content_losses.append(content_loss)
            
            if name in self.style_layers_default:
                target = self.model(styleImage).detach()
                style_loss = StyleLoss(target)
                self.model.add_module("style_loss_{}".format(i), style_loss)
                self.style_losses.append(style_loss)

            for i in range(len(self.model) - 1, -1, -1):
                if isinstance(self.model[i], ContentLoss) or isinstance(self.model[i], StyleLoss):
                    break

        output = self.styleTransfer(inputImg, styleImage, contentImage, optimizer, 1000000, 1)

        output = output.cpu.clone()
        output = output.squeeze(0)
        output = self.unloader(output)

        return output


    # Load Image Function
    def loadImage(self, path):
        image = Image.open(path)
        image = self.loader(image).unsqueeze(0)

        return image.to(device, torch.float)

    