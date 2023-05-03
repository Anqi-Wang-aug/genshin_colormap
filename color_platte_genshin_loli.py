import numpy as np
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import pyplot as plt
import matplotlib as mpl

colors = {'qiqi':['#e7e9ea', '#9d7197', '#714076', '#292854', '#666794', '#aca497'],
          'klee':['#F8ECD4','#cda67f', '#A3250F', '#372221'],
          'sayu':['#e9dac0', '#c69b7a', '#969376', '#554542'],
          'diona':['#353340', '#e5d8d3', '#a57044', '#cda3a0', '#54749c'],
          'dori':['#402b59', '#b174c3', '#f5e2f0', '#a57d56'],
          'nahida':['#404c31', '#667840', '#8da06d', '#f1f1e8', '#ddd9bd', '#685639'],
          'yaoyao':['#5a3b29', '#d8c966', '#d9d59c', '#8f9551', '#64684c']}

try:
    for key in colors:
        plt.get_cmap(key)
        mpl.cm.unregister_cmap(key)
except ValueError: pass

x = np.random.rand(200)
y = np.random.rand(200)
color_bar = np.random.rand(200)

graph_num = 1
for key in colors: 
    color_map = LinearSegmentedColormap.from_list(key, colors[key])
    mpl.colormaps.register(cmap=color_map)

    plt.subplot(170+graph_num)
    
    plt.scatter(x,y,c=color_bar, cmap=key)
    plt.colorbar()
    
    graph_num+=1
plt.show()