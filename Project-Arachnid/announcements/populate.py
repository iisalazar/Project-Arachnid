from .models import Announcement
from arachnid.settings import MEDIA_URL
import os
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Etiam non quam lacus suspendisse faucibus. Nec ultrices dui sapien eget mi proin sed libero. Non pulvinar neque laoreet suspendisse. Morbi blandit cursus risus at ultrices mi tempus. Aenean sed adipiscing diam donec adipiscing. Rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar. Ultrices vitae auctor eu augue ut lectus. Adipiscing at in tellus integer feugiat. Blandit aliquam etiam erat velit. Ut lectus arcu bibendum at varius vel. In est ante in nibh mauris cursus mattis. Varius quam quisque id diam. Risus feugiat in ante metus dictum at. Fermentum leo vel orci porta non pulvinar neque laoreet. Sagittis orci a scelerisque purus semper eget duis. Massa enim nec dui nunc mattis enim ut tellus."


file = os.path.join(MEDIA_URL, 'announcement_documents/RRLSniPepe.docx')

def generate(amount=10):
	for i in range(amount):
		announcement = Announcement()
		announcement.title = "Sample title"
		announcement.description = text
		announcement.file = file
		announcement.save()
		print("Created announcement {}".format(announcement))
