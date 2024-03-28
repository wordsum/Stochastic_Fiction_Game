import numpy
import uuid
from datetime import datetime

# Story Elements
settingTime = ["Past", "Present", "Future"]

settingPlace =  ["Mountains", "Space", "Sky", "City", "Town", "Room", "Plains", "River", "Lake", "Park", "Ocean", "House", "Vehicle", "Plane", "Swamp", "School", "Office", "Basement", "Construction Site", "Lab", "Jail", "Train", "Boat", "Cave", "Jungle", "Desert", "Ranch", "Plane", "Bathroom", "Tunnel", "Amusement Park", "Museum", "Car"]

primary_characters = ["One", "Two", "Many", "Many"]

conflict = ["Person vs. Person", "Person vs. Self", "Person vs Nature", "Person vs Technology", "Person vs Society", "Person vs Supernatural", "Person vs. Destiny"]

pointOfView = ["First", "First", "Second", "Third", "Third", "Third"]

genre = ["Horror", "Western", "Romance", "Fantasy", "Adventure", "Science Fiction", "Sports", "Mystery", "Comedy", "Dystopian", "Utopian", "Crime", "Magical Realism", "Oulipo", "Thriller", "Fable", "Tall Tale"]

tense = ["Past Tense", "Present Tense"]

format = ["Flash Fiction", "Novel First Chapter", "Flash Fiction", "Flash Fiction", "Novel Last Chapter", "Flash Fiction", "Flash Fiction", "YOUR FORMAT"]

title = str(uuid.uuid4())

# Create
with open('story/stochastic-fiction-game-' + title + '.txt', 'w') as f:
	print('Stochastic Fiction Game ' + title, file=f)
	print('UTC Start Time: ' + str(datetime.utcnow()), file=f)
	print('Story Elements:', file=f)
	print('\tSetting - Time: ' + numpy.random.choice(settingTime), file=f)
	print('\tSetting - Main Location: ' + numpy.random.choice(settingPlace), file=f)
	print('\tConflict: ' + numpy.random.choice(conflict), file=f)
	print('\tQuantity of Primary Characters: ' + numpy.random.choice(primary_characters), file=f)
	print('\tPoint of View: ' + numpy.random.choice(pointOfView), file=f)
	print('\tTense: ' + numpy.random.choice(tense), file=f)
	print('\tGenre: ' + numpy.random.choice(genre), file=f)
	print('\tFormat: '  + numpy.random.choice(format), file=f)
	print('Game Rules:', file=f)
	print('\tA. Setup Game Environment.', file=f)
	print('\tB. Read stochastic outline.', file=f)
	print('\tC. Write a story with **Story Elements** in 120 minutes or fewer.', file=f)
	print('\tD. Score the story, the it, 1-4:', file=f)
	print('\t\t>1. It\'s poop.', file=f)
	print('\t\t>2. People that love you will enjoy the stink.', file=f)
	print('\t\t>3. Rewrite it to rid it of the stench.', file=f)
	print('\t\t>4. Editing it may help it smell like perfume.', file=f)
        
	print('########## Story ##########', file=f)
	print('', file=f)
	print('', file=f)
	print('', file=f)
	print('###########################', file=f)
	print('########## Contributing Thought ##########', file=f)
	print('', file=f)
	print('', file=f)
	print('', file=f)
	print('###########################', file=f)
