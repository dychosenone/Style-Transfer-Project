from torchvision import transforms
import torch

class ImageProcessing:
     
    def __init__(self, img_size) -> None:
          self.img_size = img_size

    def preProcessing(self):
        return transforms.Compose([transforms.Scale(self.img_size),
                           transforms.ToTensor(),
                           transforms.Lambda(lambda x: x[torch.LongTensor([2,1,0])]), #turn to BGR
                           transforms.Normalize(mean=[0.40760392, 0.45795686, 0.48501961], #subtract imagenet mean
                                                std=[1,1,1]),
                           transforms.Lambda(lambda x: x.mul_(255)),
                ])
        pass

    def postProcessing(self):
        return transforms.Compose([transforms.Lambda(lambda x: x.mul_(1./255)),
                           transforms.Normalize(mean=[-0.40760392, -0.45795686, -0.48501961], #add imagenet mean
                                                std=[1,1,1]),
                           transforms.Lambda(lambda x: x[torch.LongTensor([2,1,0])]), #turn to RGB
                ])
        pass

    def postProcessingTwo(self):
        return transforms.Compose([transforms.ToPILImage()])
        pass