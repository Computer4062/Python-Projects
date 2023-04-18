import cv2
import torch
import torch.nn as nn
from skimage import io
import torchvision

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.pool = nn.MaxPool2d(2, 2)

        self.l1 = nn.Linear(16 * 5 * 5, 120)
        self.l2 = nn.Linear(120, 84)
        self.l3 = nn.Linear(84, 2)

    def forward(self, x):
        x = nn.functional.relu(self.conv1(x))
        x = self.pool(x)
        x = nn.functional.relu(self.conv2(x))
        x = self.pool(x)

        x = x.reshape(-1, 16 * 5 * 5)

        x = nn.functional.relu(self.l1(x))
        x = nn.functional.relu(self.l2(x))
        x = torch.log_softmax(self.l3(x), 1)

        return x

def main():
    camera = cv2.VideoCapture(0)
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

    labels = ['Mihan', 'Other']
    path = "D:/Mihan/Python-project-programmes/pythonProjects/Algorithm/ImageComparison/images/image.jpg"

    net = Net().to(torch.device('cpu'))
    net.load_state_dict(torch.load('cnn.pth'))
    net.eval()

    transform = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Resize((32, 32))
    ])

    while True:
        ret, frame = camera.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = classifier.detectMultiScale(img, scaleFactor = 1.5, minNeighbors = 5)

        for (x, y, w, h) in faces:
            roi = img[y: y+h, x: x+w]
            cv2.rectangle(frame, (x , y), (x + w , y + h), (255, 0, 0), 2)
            cv2.imwrite(path, roi)

            image = io.imread(path)
            image = transform(image)

            prediction = net(image)
            predicted = torch.argmax(prediction)
            cv2.putText(frame, labels[predicted.item()], (x, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('camera', frame)

        if cv2.waitKey(1) == ord('e'): break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

