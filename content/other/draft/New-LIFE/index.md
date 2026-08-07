---
title: "New LIFE"
date: 2026-01-18T15:10:37+08:00
summary: "给 Sophie 的信 | 📬"
series: ["草稿"]
series_order: 1
type: "posts"
---

<!-- require APlayer -->
<link rel="stylesheet" href="/renderjs/aplayer/dist/APlayer.min.css">
<script src="/renderjs/aplayer/dist/APlayer.min.js"></script>
<!-- require MetingJS -->
<script src="/renderjs/meting/dist/Meting.min.js"></script>


<p class="fonts-delphiaVillagefont"> All Or Nothing </p>

<meting-js
    name="Lava (From _Lava_) "
    artist="Kuana Torres Kahele_Napua Greig_James Ford Murphy"
    url="/voice/kugou/sophieSong/Lava (From _Lava_) - Kuana Torres Kahele_Napua Greig_James Ford Murphy/Lava (From 'Lava').mp3 "
    cover="/voice/kugou/sophieSong/Lava (From _Lava_) - Kuana Torres Kahele_Napua Greig_James Ford Murphy/Lava (From 'Lava')_封面.jpg"
    lrc="/voice/kugou/sophieSong/Lava (From _Lava_) - Kuana Torres Kahele_Napua Greig_James Ford Murphy/Lava (From 'Lava')_合并歌词.lrc" 
    autoplay="false"
    loop="false"
    mutex="true">
</meting-js>

# Sophiw 😄

我在未来等你。
嗯，现在去，跑着去。

## 二级标题

为什么段落之间没有空行呢？
为什么段落之间没有空行呢？


为什么段落之间没有空行呢？

```c
#include <stdio.h>
int main() {
    printf("Hello\n");  // 这是注释

    return 0;
}

```

```python
import torch 
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms


# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Hyper-parameters
sequence_length = 28
input_size = 28
hidden_size = 128
num_layers = 2
num_classes = 10
batch_size = 100
num_epochs = 2
learning_rate = 0.003

# MNIST dataset
train_dataset = torchvision.datasets.MNIST(root='../../data/',
                                           train=True, 
                                           transform=transforms.ToTensor(),
                                           download=True)

test_dataset = torchvision.datasets.MNIST(root='../../data/',
                                          train=False, 
                                          transform=transforms.ToTensor())

# Data loader
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size, 
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size, 
                                          shuffle=False)

# Bidirectional recurrent neural network (many-to-one)
class BiRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(BiRNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_size*2, num_classes)  # 2 for bidirection
    
    def forward(self, x):
        # Set initial states
        h0 = torch.zeros(self.num_layers*2, x.size(0), self.hidden_size).to(device) # 2 for bidirection 
        c0 = torch.zeros(self.num_layers*2, x.size(0), self.hidden_size).to(device)
        
        # Forward propagate LSTM
        out, _ = self.lstm(x, (h0, c0))  # out: tensor of shape (batch_size, seq_length, hidden_size*2)
        
        # Decode the hidden state of the last time step
        out = self.fc(out[:, -1, :])
        return out

model = BiRNN(input_size, hidden_size, num_layers, num_classes).to(device)


# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    
# Train the model
total_step = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        images = images.reshape(-1, sequence_length, input_size).to(device)
        labels = labels.to(device)
        
        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (i+1) % 100 == 0:
            print ('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}' 
                   .format(epoch+1, num_epochs, i+1, total_step, loss.item()))

# Test the model
with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in test_loader:
        images = images.reshape(-1, sequence_length, input_size).to(device)
        labels = labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    print('Test Accuracy of the model on the 10000 test images: {} %'.format(100 * correct / total)) 

# Save the model checkpoint
torch.save(model.state_dict(), 'model.ckpt')

```


{{< notebook-bg >}}
[
  {"src":"/pic/svg/sticker-balloon.svg","size":130,"left":"50%","top":"50%","rotate":-30,"opacity":1},
  {"src":"/pic/svg/sticker-alpaca.svg","size":80,"left":"50%","top":"50%","rotate":5,"opacity":1},
  {"src":"/pic/svg/sticker-alpaca.svg","size":180,"left":20,"top":"20%","rotate":5,"opacity":0.35},
  {"src":"/pic/svg/sticker-balloon.svg","size":90,"right":30,"bottom":30,"rotate":-6}
]
{{< /notebook-bg >}}
