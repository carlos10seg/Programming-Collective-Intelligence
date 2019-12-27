#from recommendations import critics, sim_distance, sim_pearson
import recommendations as recs
import pydelicious

# c1 = critics['Lisa Rose']['Lady in the Water']
# print(c1)

# c2 = critics['Toby']
# print(c2)

# d1 = sim_distance(critics, 'Lisa Rose', 'Jack Matthews')
# print(d1)

#print(recs.sim_pearson(recs.critics, 'Lisa Rose', 'Gene Seymour'))

# matches = recs.topMatches(recs.critics, 'Toby', n=3)
# print(matches)
# matches2 = recs.topMatches(recs.critics, 'Toby', n=3, similarity=recs.sim_distance)
# print(matches2)


# recommendations1 = recs.getRecommendations(recs.critics, 'Toby')
# print(recommendations1)

# recommendations2 = recs.getRecommendations(recs.critics, 'Toby', recs.sim_distance)
# print(recommendations2)

# print(recs.transform_critics())


# movies = recs.transformPrefs(recs.critics)
# matches = recs.topMatches(movies, 'Superman Returns')
# print(matches)
# recommendations = recs.getRecommendations(movies, 'Just My Luck')
# print(recommendations)


# itemsim = recs.calculateSimilarItems(recs.critics)
# print(itemsim)
# recItems = recs.getRecommendedItems(recs.critics, itemsim, 'Toby')
# print(recItems)


prefs = recs.loadMovieLens()
#print(prefs['87'])
# user-based recommendations:
user_recs =  recs.getRecommendations(prefs, '87')[0:30]
print(user_recs)
# item-based recommendations:
item_sim = recs.calculateSimilarItems(prefs, n=50)
item_recs = recs.getRecommendedItems(prefs, item_sim, '87')[0:30]
print(item_recs)