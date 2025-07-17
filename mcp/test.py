import pyrhyme
g = pyrhyme.RhymeBrain()
results = g.rhyming_list("yellow", "en", maxResults = 50)
results = [x.word for x in results]
print(results)