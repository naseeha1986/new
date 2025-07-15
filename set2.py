y_v={101,102,103,104,105,106}
print("Yesterday's visitors\n",y_v) 
t_v={103,104,105,107,108,109}
print("Today's visitors\n",t_v) 
print("Unique visitors today:\n", y_v & t_v)
print("Users who visited both day\n", y_v |t_v)
print("Users who visited only today\n", t_v - y_v)
print("Users who visited only yesterday\n", y_v - t_v)

