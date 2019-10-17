import json
import matplotlib.pyplot as plt


data = {"han": 78365, "hon": 25529, "hen": 2352, "den": 138894, "det": 54994, "denna": 2350, "denne": 601}

data = json.dumps(data)
data = json.loads(data)

for item in data:
    plt.bar(item, data[item]/1000,alpha=0.5, color='blue')

plt.ylabel('counts [x1000]')
plt.title('Article usage count')
plt.show()
