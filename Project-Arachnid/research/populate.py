from .models import ResearchPaper, ResearchProponent
from faker import Faker
from names import get_first_name, get_last_name
import random

file = '/home/wyvern/Documents/pdf/Cagayan.pdf'
fake = Faker()

'''
SCRIPT
from research.populate import start_generating
start_generating()
'''

def generate_fake_study():
	titles = [
		"Apoy as Heat Source",
		"Wood as Furniture",
		"The Utilization of Nuclear Bomb as Malunggay Leaves Extract",
		"The Utilization of Mangga Stems as an Alternative Pesticide"
	]
	study = ResearchPaper()
	study.category = random.choice(study.CATEGORY_CHOICES)[0]
	study.title = random.choice(titles)
	study.abstract = "This is an abstract"
	study.file = file
	study.save()
	return study

def generate_fake_proponent(paper):
	proponent = ResearchProponent()
	gender = random.choice(['male', 'female'])
	proponent.first_name = get_first_name(gender=gender)
	proponent.last_name = get_last_name()
	proponent.middle_name = get_last_name()
	proponent.research = paper
	proponent.save()
	return proponent

def start_generating(amount=10):
	for i in range(amount):
		print("Loop number {}".format(i + 1))
		study = generate_fake_study()
		print("Created fake study {}".format(study.title))
		for i in range(random.randint(1, 3)):
			proponent = generate_fake_proponent(study)
			print("Created fake proponent {} for study {}".format(proponent.first_name, study.title))
		print("\n")
