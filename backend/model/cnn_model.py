import torch
import torch.nn as nn
import torch.nn.functional as F

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