import torch
from signal_propagation_plot.pytorch import get_average_channel_variance_by_depth
# from signal_propagation_plot.pytorch import get_average_feature_map_variance_by_depth
from signal_propagation_plot.pytorch import plot
import torchvision
import matplotlib.pyplot as plt
model = torchvision.models.resnet152()
model2 = torchvision.models.swin_v2_t()
model3 = torchvision.models.resnet18()
x = torch.randn(64, 3, 224, 224)
values = get_average_channel_variance_by_depth(model, x)
values2 = get_average_channel_variance_by_depth(model2, x)
values3 = get_average_channel_variance_by_depth(model3, x)
fig = plt.figure(figsize=(20, 18))
# plot 30 first values
plot(values[50:100], label='scale-dot', linewidth=2)
plot(values3[:50], label='scale-cosine', linewidth=2)
plot(values2[50:100], label='scale-soft-cosine', linewidth=3)
plt.rc('xtick', labelsize=20)
plt.rc('ytick', labelsize=20)
plt.rc('axes', labelsize=20)
plt.rc('legend', fontsize=20)
# change the xticks to show the depth
plt.xticks(range(0, 50), range(0, 50))
plt.xlabel('Depth', fontsize=20)
plt.ylabel('Average channel variance', fontsize=20)
plt.legend()
# change text size of the xticks, yticks and labels

plt.show()

# save figure to eps format
fig.savefig('signal_propagation_plot.png', format='png')
