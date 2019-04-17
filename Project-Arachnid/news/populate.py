from .models import News
from arachnid.settings import BASE_DIR
import random, os
from PIL import Image

'''
SCRIPT
from news import populate
populate.generate_random_stuff()
'''

image = os.path.join(BASE_DIR, 'static/img/stock/macaw-poly.jpg')

names = [
"Tessa Hubbard",
"Steve Kaur",
"Garin Dotson",
"Arandeep Ibarra",
"Samanta Mcmahon",
"Evie-Mae Peel",
"Alisa Harding",
'Breanna Henry',
"Aras Dennis",
"Safiya Hodson",
]

random_text = '''
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Etiam non quam lacus suspendisse faucibus. Nec ultrices dui sapien eget mi proin sed libero. Non pulvinar neque laoreet suspendisse. Morbi blandit cursus risus at ultrices mi tempus. Aenean sed adipiscing diam donec adipiscing. Rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar. Ultrices vitae auctor eu augue ut lectus. Adipiscing at in tellus integer feugiat. Blandit aliquam etiam erat velit. Ut lectus arcu bibendum at varius vel. In est ante in nibh mauris cursus mattis. Varius quam quisque id diam. Risus feugiat in ante metus dictum at. Fermentum leo vel orci porta non pulvinar neque laoreet. Sagittis orci a scelerisque purus semper eget duis. Massa enim nec dui nunc mattis enim ut tellus.

Nunc pulvinar sapien et ligula ullamcorper malesuada proin. Blandit volutpat maecenas volutpat blandit aliquam etiam. Aliquam sem et tortor consequat id porta nibh venenatis cras. In eu mi bibendum neque egestas congue. Pulvinar elementum integer enim neque volutpat ac tincidunt. Praesent elementum facilisis leo vel fringilla est. Enim facilisis gravida neque convallis a. Nisi scelerisque eu ultrices vitae auctor. Massa tincidunt dui ut ornare lectus sit amet est. Pharetra et ultrices neque ornare aenean.

Ligula ullamcorper malesuada proin libero nunc consequat interdum varius sit. Hac habitasse platea dictumst vestibulum rhoncus. Ac turpis egestas maecenas pharetra convallis posuere morbi leo. Blandit libero volutpat sed cras ornare arcu. Eget dolor morbi non arcu risus quis varius quam quisque. Dignissim cras tincidunt lobortis feugiat vivamus at augue eget arcu. Diam volutpat commodo sed egestas egestas fringilla phasellus faucibus. At in tellus integer feugiat scelerisque varius. Sem fringilla ut morbi tincidunt. Habitasse platea dictumst quisque sagittis purus sit.

Massa tincidunt dui ut ornare lectus sit. Dui sapien eget mi proin sed. Id consectetur purus ut faucibus pulvinar elementum integer. Cursus vitae congue mauris rhoncus aenean vel elit. Viverra ipsum nunc aliquet bibendum. Quam vulputate dignissim suspendisse in. Libero justo laoreet sit amet. Elementum tempus egestas sed sed risus pretium quam vulputate. Dignissim convallis aenean et tortor at risus viverra adipiscing at. Ultrices vitae auctor eu augue ut lectus. Tellus cras adipiscing enim eu turpis egestas pretium aenean pharetra.

Accumsan lacus vel facilisis volutpat est velit egestas dui id. Libero volutpat sed cras ornare. Morbi blandit cursus risus at ultrices mi tempus. Quis eleifend quam adipiscing vitae proin sagittis nisl rhoncus. Enim sit amet venenatis urna. Pharetra magna ac placerat vestibulum lectus mauris ultrices. Imperdiet dui accumsan sit amet. Adipiscing bibendum est ultricies integer. Non diam phasellus vestibulum lorem sed. Velit ut tortor pretium viverra suspendisse potenti nullam ac. Rutrum quisque non tellus orci ac auctor augue mauris augue. Cursus metus aliquam eleifend mi. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla. Felis imperdiet proin fermentum leo vel orci porta non pulvinar.

Commodo quis imperdiet massa tincidunt nunc. Senectus et netus et malesuada fames ac turpis egestas maecenas. Hendrerit gravida rutrum quisque non tellus. Eget gravida cum sociis natoque penatibus et magnis dis. Amet volutpat consequat mauris nunc congue nisi vitae. Nunc vel risus commodo viverra maecenas accumsan lacus vel. Amet luctus venenatis lectus magna fringilla urna. Quis vel eros donec ac odio tempor orci dapibus. Sapien nec sagittis aliquam malesuada bibendum arcu vitae elementum. Mauris pharetra et ultrices neque ornare aenean euismod elementum.
'''

random_headline = "This is a headline"

def generate_random_stuff(amount=10):
	for i in range(amount):
		# Required fields:
		# Lead text, Headline, Headline Image, body
		# Additional fields to put..
		# Author, Cover Photo, Opening
	
		news = News(
			author = random.choice(names),
			lead_text = random_text,
			headline = random_text,
			headline_image = image,
			body_text = random_text,
			cover_photo = image,
			opening = "Opening...."
			)
		print("Saving news created by {}".format(news.author))
		news.save()
		news.publish()

