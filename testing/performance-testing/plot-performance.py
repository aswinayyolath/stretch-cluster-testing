# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np
import json

submariner_1 = open('stretch-submariner/1-topic-16-partitions-1kb-Kafka-iter-1.json')
cilium_1 = open('stretch-cilium/1-topic-16-partitions-1kb-Kafka-iter-1.json')
normal_1 = open('non-stretch/1-topic-16-partitions-1kb-Kafka-iter-1.json')

submariner_2 = open('stretch-submariner/1-topic-16-partitions-1kb-Kafka-iter-2.json')
cilium_2 = open('stretch-cilium/1-topic-16-partitions-1kb-Kafka-iter-2.json')
normal_2 = open('non-stretch/1-topic-16-partitions-1kb-Kafka-iter-2.json')

submariner_3 = open('stretch-submariner/1-topic-16-partitions-1kb-Kafka-iter-3.json')
cilium_3 = open('stretch-cilium/1-topic-16-partitions-1kb-Kafka-iter-3.json')
normal_3 = open('non-stretch/1-topic-16-partitions-1kb-Kafka-iter-3.json')


data_sub_1 = json.load(submariner_1)
data_cil_1 = json.load(cilium_1) 
data_normal_1 = json.load(normal_1) 

data_sub_2 = json.load(submariner_2)
data_cil_2 = json.load(cilium_2) 
data_normal_2 = json.load(normal_2) 

data_sub_3 = json.load(submariner_3)
data_cil_3 = json.load(cilium_3) 
data_normal_3 = json.load(normal_3) 

fig, axs = plt.subplots(2,2)

def plotQuantiles(json_key,plot_x, plot_y,title,x_label,y_label):
    x1 = [float(val) for val in data_sub_1[json_key].keys()]
    y1 = data_sub_1[json_key].values()

    x2 = [float(val) for val in data_cil_1[json_key].keys()]
    y2 = data_cil_1[json_key].values()

    x3 = [float(val) for val in data_normal_1[json_key].keys()]
    y3 = data_normal_1[json_key].values()

    x4 = [float(val) for val in data_sub_2[json_key].keys()]
    y4 = data_sub_2[json_key].values()

    x5 = [float(val) for val in data_cil_2[json_key].keys()]
    y5 = data_cil_2[json_key].values()

    x6 = [float(val) for val in data_normal_2[json_key].keys()]
    y6 = data_normal_2[json_key].values()

    x7 = [float(val) for val in data_sub_3[json_key].keys()]
    y7 = data_sub_3[json_key].values()

    x8 = [float(val) for val in data_cil_3[json_key].keys()]
    y8 = data_cil_3[json_key].values()

    x9 = [float(val) for val in data_normal_3[json_key].keys()]
    y9 = data_normal_3[json_key].values()

    axs[plot_x,plot_y].plot(x1, y1,label='Submariner', color='red')  
    axs[plot_x,plot_y].plot(x2, y2, label='Cilium', color='blue')  
    axs[plot_x,plot_y].plot(x3, y3, label='Non Strech', color='green')  

    axs[plot_x,plot_y].plot(x4, y4, color='red')  
    axs[plot_x,plot_y].plot(x5, y5, color='blue')  
    axs[plot_x,plot_y].plot(x6, y6, color='green')  

    axs[plot_x,plot_y].plot(x7, y7,color='red')  
    axs[plot_x,plot_y].plot(x8, y8, color='blue')  
    axs[plot_x,plot_y].plot(x9, y9, color='green')  
    axs[plot_x,plot_y].legend() 

    axs[plot_x,plot_y].set_title(title)
    axs[plot_x,plot_y].set_xlabel(x_label)
    axs[plot_x,plot_y].set_ylabel(y_label)

def plotBar(json_key,plot_x, plot_y,title,x_label,y_label):
    y1=np.mean(data_sub_1[json_key])
    y2=np.mean(data_sub_2[json_key])
    y3=np.mean(data_sub_3[json_key])

    axs[plot_x,plot_y].bar(['Sub1','Sub2','Sub3'],[y1,y2,y3], color='red')

    y4=np.mean(data_cil_1[json_key])
    y5=np.mean(data_cil_2[json_key])
    y6=np.mean(data_cil_3[json_key])
    axs[plot_x,plot_y].bar(['Cil1','Cil2','Cil3'],[y4,y5,y6], color='blue')


    y7=np.mean(data_normal_1[json_key])
    y8=np.mean(data_normal_2[json_key])
    y9=np.mean(data_normal_3[json_key])
    axs[plot_x,plot_y].bar(['Norm1','Norm2','Norm3'],[y7,y8,y9], color='green')


    axs[plot_x,plot_y].set_title(title)
    axs[plot_x,plot_y].set_xlabel(x_label)
    axs[plot_x,plot_y].set_ylabel(y_label)

plotQuantiles('aggregatedEndToEndLatencyQuantiles',0,0,'aggregatedEndToEndLatencyQuantiles','Benchmark Progress Precentile','Aggregated End To End Latency (ms)')
plotQuantiles('aggregatedPublishLatencyQuantiles',0,1,'aggregatedPublishLatencyQuantiles','Benchmark Progress Precentile','Aggregated Percentile Latency (ms)')

# plotQuantiles('aggregatedEndToEndDelayLatencyQuantiles',0,1,'Benchmark testing results for stretched kafka cluster','Benchmark Progress Precentile','Aggregated End To End Delay Latency (ms)')
# plotQuantiles('aggregatedPublishDelayLatencyQuantiles',1,0,'Benchmark testing results for stretched kafka cluster','Benchmark Progress Precentile','Aggregated Percentile Delay Latency (ms)')


plotBar('publishRate',1,0,'Average Publish Rate','Network Technology','Number of Messages')
plotBar('consumeRate',1,1,'Average Consume Rate','Network Technology','Number of Messages')

plt.show()  # display
