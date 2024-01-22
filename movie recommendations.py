import spacy
nlp = spacy.load('en_core_web_md') # Importing spacy and loading the nlp model into variable nlp

# Movie to compare to
watched_movie = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
watched_movie = nlp(watched_movie)
# Potential next movies separated in a list
new_movies = ["Movie A :When Hiccup discovers Toothless isn't the only Night Fury, he must seek 'The Hidden World', a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.",
"Movie B :After the death of Superman, several new people present themselves as possible successors.",
"Movie C :A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.",
"Movie D :A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.",
"Movie E :A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.",
"Movie F :In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.",
"Movie G :The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.",
"Movie H :A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.",
"Movie I :Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow.",
"Movie J :Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."]

# Empty variables to assign the highest scoring movie to later
highest_score = 0
highest_score_movie = ""

# For loop that will compare the descriptions of the movies to each other through the nlp model. If the current score is higher than any previous score it will
# assign it to the highest_score variables which can be printed later
for movie in new_movies:
    similiarity_score = nlp(movie).similarity(watched_movie)
    if similiarity_score > highest_score:
        highest_score = similiarity_score
        highest_score_movie = movie[0:7]

print (f"Based on your watch history, we advice that you watch {highest_score_movie}.")