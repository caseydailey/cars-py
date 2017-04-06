#Create an empty set named showroom.
cars = set()

#Add four of your favorite car model names to the set.
cars.add('volvo')
cars.add('subaru')
cars.add('ford')
cars.add('chevy')

#Print the length of your set.
print('length of cars: {}'.format(len(cars)))

#Pick one of the items in your show room and add it to the set again.
#not allowed as sets are enforced unique

#Using update(), add two more car models to your showroom with another set.
cars.update(['mercedes', 'jaguar'])
print('showroom: {}'.format(cars))

#You've sold one of your cars. Remove it from the set with the discard() method.
cars.discard('ford')
print('cars no ford: {}'.format(cars))

#create another set of cars in a variable junkyard
junkyard = set()

#add some different cars
junkyard.update(['saturn', 'nissan', 'mitsubishi'])
print('junkyard: {}'.format(junkyard))

#also add a few that are the same as in the showroom set
junkyard.update(['volvo', 'mercedes', 'jaguar'])

#Use the intersection method to see 
#which cars exist in both the showroom and that junkyard
def intersect(a, b):
	'''
	find intersection of two flat sets

	args
	a-- set a
	b-- set b
	
	returns--intersction of two flat sets
	'''
	return list(set(a) & set(b))

print('intersection of cars/junkyard: {}'.format(intersect(cars, junkyard)))

#Use the union method to combine the junkyard into your showroom.
combined_lots = cars | junkyard
print('combined lots: {}'.format(combined_lots))

#Use the discard() method to remove any cars that you acquired from the junkyard 
#that you want in your showroom.
combined_lots.discard('chevy')
print('curated lot (no chevy): {}'.format(combined_lots))







