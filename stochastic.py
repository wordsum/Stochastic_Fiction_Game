### Game Rules:

# A. Output stochastic outline.
# B. Read stochastic outline.
# C. Write a story with **Story Elements** in 120 minutes or fewer.
# D. Score the story 1-4:
# >1. Delete and start over.                                                        
# >2. Rewrite the story.                  
# >3. Write the story.
# >4. Editing may help it be a story.

### Story Elements:
# - Theme: God
# - Setting Time: Future
# - Setting Place: Mountains
# - Characters: One  
# - Point of View: First
# - Tense: Present Tense
# - Genre: Romance 


import numpy
import uuid
from datetime import datetime

#
# Story Elements
#
theme = ["Religion", "Politics", "Sexuality"]

settingTime = ["Past", "Present", "Future"]

settingPlace =  ["Mountains", "Space", "Sky", "City", "Town", "Room", "Plains", "River", "Lake", "Park", "Ocean", "House", "Vehicle", "Plane", "Swamp", "School", "Office", "Construction Site", "Lab", "Jail", "Train", "Boat", "Cave", "Jungle", "Desert", "Ranch"]

characters = ["One", "Two", "Three"]

pointOfView = ["First", "Second", "Third"]

genre = ["Horror", "Western", "Romance", "Fantasy", "Adventure", "Science Fiction", "Mystery", "Comedy", "Dystopian", "Utopian", "Surreal", "Magical Realism"]

tense = ["Past Tense", "Present Tense"]

title = str(uuid.uuid4())

#
# Create
#
with open('story/stochastic-fiction-game-outline' + title + '.txt', 'w') as f:
	print('Stochastic Fiction Game ' + title, file=f)
	print('UTC Start Time: ' + str(datetime.utcnow()), file=f)
	print('Game Rules:', file=f)
	print('\tA. Output stochastic outline.', file=f)
	print('\tB. Read stochastic outline.', file=f)
	print('\tC. Write a story with **Story Elements** in 120 minutes or fewer.', file=f)
	print('\tD. Score the story 1-4:', file=f)
	print('\t\t>1. Forget the story.', file=f)                                                     
	print('\t\t>2. Rewrite the story.', file=f)                  
	print('\t\t>3. Write the story.', file=f)
	print('\t\t>4. Editing may help it be a story.', file=f)
	print('Story Elements:', file=f)
#       Remove to try to understand what I mean by theme.
#	print('\tTheme: ' + numpy.random.choice(theme), file=f)
	print('\tSetting Time: ' + numpy.random.choice(settingTime), file=f)
	print('\tSetting Place: ' + numpy.random.choice(settingPlace), file=f)
	print('\tCharacters: ' + numpy.random.choice(characters), file=f)
	print('\tPoint of View: ' + numpy.random.choice(pointOfView), file=f)
	print('\tTense: ' + numpy.random.choice(tense), file=f)
	print('\tGenre: ' + numpy.random.choice(genre), file=f)
	print('########## Story ##########', file=f)
	print('', file=f)
	print('', file=f)
	print('', file=f)
	print('###########################', file=f)
