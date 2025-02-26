# DictWrapper
This simplifies reading python dictionary data, gracefully records errors and missing data


# # Example usage:
# data = {'existing_key': 'value'}
# g = DictWrapper(data) (you can use another label)

# this is now the fin

#to get a value from your data ie name  
g.name
# yes SIMPLE       no data.get('name','')  OR  no data.['name']

# AND THE BEST PART

glog() 

# at the end VERBOSE
#or 

glog(0) 

# is silent

# USE AT YOUR PERIL - it saves a lot of typing 
# I WISH I HAD THIS WHEN I STARTED A BIG PROJECT
# would be a good teachers tool

# example

for record in data:
  g = DictWrapper(record)
  name = g.name
  country = g.country
  boat = g.boat

# better than!

for record in data:
  name = record['name']
# etc

  
