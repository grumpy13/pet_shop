from django.test import TestCase
from .forms import PetForm
from .models import Pet
from django.urls import reverse


# Create your tests here.
class PetFormTest(TestCase):

	def test_form(self):
		form = PetForm(
			data={
			"name":"dog",
			"age": 5,
			"sex": "Female",
			"price": 5.5,
			}
		)
		self.assertTrue(form.is_valid())


class PetListViewTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		Pet.objects.create(
			name="croc",
			age=7,
			sex="Male",
			price=66.66
			)
		Pet.objects.create(
			name="bunny",
			age=7,
			sex="Male",
			price=60.66
			)


	def test_url(self):
		response = self.client.get(reverse('pets-list'))
		self.assertEqual(response.status_code, 200, msg="make sure the url for the pet list is named correctly and that the view gives no erros")


	def test_context(self):
		response = self.client.get(reverse('pets-list'))
		pets = Pet.objects.all()
		self.assertEqual(response.context["pets"].count(), pets.count(), msg="check the query sent through the context in the pets list view")
		self.assertEqual(response.context["pets"][0].name, pets[0].name, msg="check the context of the pets list")
		self.assertEqual(response.context["pets"][1].name, pets[1].name, msg="check the context of the pets list")


	def test_template(self):
		response = self.client.get(reverse('pets-list'))
		pets = Pet.objects.all()
		self.assertContains(response, pets[0].name,  msg_prefix="are you displaying the pets in the pets list template")
		self.assertContains(response, pets[1].name,  msg_prefix="are you displaying the pets in the pets list template")


class PetDetailsViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Pet.objects.create(
			name="croc",
			age=7,
			sex="Male",
			price=66.66
			)
		Pet.objects.create(
			name="bunny",
			age=7,
			sex="Male",
			price=60.66
			)


	def test_url(self):
		response = self.client.get(reverse('pet-details', args=[1]))
		self.assertEqual(response.status_code, 200, msg="make sure the url for the pet details is named correctly and that the view gives no erros")
		response = self.client.get(reverse('pet-details', args=[2]))
		self.assertEqual(response.status_code, 200, msg="make sure the url for the pet details is named correctly and that the view gives no erros")


	def test_context(self):
		response = self.client.get(reverse('pet-details', args=[1]))
		pet = Pet.objects.get(id=1)
		
		self.assertEqual(response.context["pet"].name, pet.name, msg="check the context in pet details view")
		self.assertEqual(response.context["pet"].age, pet.age, msg="check the context in pet details view")
		self.assertEqual(response.context["pet"].price, pet.price, msg="check the context in pet details view")

		response = self.client.get(reverse('pet-details', args=[2]))
		pet = Pet.objects.get(id=2)

		self.assertEqual(response.context["pet"].name, pet.name, msg="check the context in pet details view")
		self.assertEqual(response.context["pet"].age, pet.age, msg="check the context in pet details view")
		self.assertEqual(response.context["pet"].price, pet.price, msg="check the context in pet details view")


	def test_template(self):
		response = self.client.get(reverse('pet-details', args=[1]))
		pet = Pet.objects.get(id=1)

		self.assertContains(response, pet.name,  msg_prefix="are you displaying the correct pet details in the pet details template")
		self.assertContains(response, pet.age,  msg_prefix="are you displaying the correct pet details in the pet details template")
		self.assertContains(response, pet.sex,  msg_prefix="are you displaying the correct pet details in the pet details template")
		self.assertContains(response, pet.price,  msg_prefix="are you displaying the correct pet details in the pet details template")

		response = self.client.get(reverse('pet-details', args=[2]))
		pet = Pet.objects.get(id=2)

		self.assertContains(response, pet.name,  msg_prefix="are you displaying the correct pet details in the pet details template")
		self.assertContains(response, pet.age,  msg_prefix="are you displaying the correct pet details in the pet details template")
		self.assertContains(response, pet.sex,  msg_prefix="are you displaying the correct pet details in the pet details template")
		self.assertContains(response, pet.price,  msg_prefix="are you displaying the correct pet details in the pet details template")
		

class PetCreateViewTest(TestCase):

	def test_url(self):
		response = self.client.get(reverse('create-pet'))
		self.assertEqual(response.status_code, 200, msg="make sure the url for the pet create is named correctly and that the view gives no erros")


	def test_creation(self):
		data = {
			"name":"dog",
			"age": 5,
			"sex": "Female",
			"price": 5.5,
		}
		response = self.client.post(reverse('create-pet'), data)
		self.assertRedirects(response, reverse('pet-details', args=[1]), msg_prefix="is the view redirecting to the correct page after creating a pet")

		pet = Pet.objects.get(id=1)
		self.assertEqual(pet.name,  data["name"], msg="pet was not created correctly")
		self.assertEqual(pet.age,  data["age"], msg="pet was not created correctly")
		self.assertEqual(pet.price,  data["price"], msg="pet was not created correctly")
		self.assertEqual(pet.sex,  data["sex"], msg="pet was not created correctly")

		data = {
			"name":"croc",
			"age": 5,
			"sex": "Female",
			"price": 5.5,
		}
		response = self.client.post(reverse('create-pet'), data)
		self.assertRedirects(response, reverse('pet-details', args=[2]), msg_prefix="is the view redirecting to the correct page after creating a pet")

		pet = Pet.objects.get(id=2)
		self.assertEqual(pet.name,  data["name"], msg="pet was not created correctly")
		self.assertEqual(pet.age,  data["age"], msg="pet was not created correctly")
		self.assertEqual(pet.price,  data["price"], msg="pet was not created correctly")
		self.assertEqual(pet.sex,  data["sex"], msg="pet was not created correctly")


class PetUpdateViewTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		Pet.objects.create(
			name="croc",
			age=7,
			sex="Male",
			price=66.66
			)
		Pet.objects.create(
			name="bunny",
			age=7,
			sex="Male",
			price=60.66
			)


	def test_url(self):
		response = self.client.get(reverse('update-pet', args=[1]))
		self.assertEqual(response.status_code, 200, msg="make sure the url for the pet update is named correctly and that the view gives no erros")


	def test_get(self):
		pet = Pet.objects.get(id=1)
		response = self.client.get(reverse("update-pet", args=[1]))
		self.assertContains(response, pet.name, msg_prefix="check update form or view")

	def test_update(self):
		pet = Pet.objects.get(id=1)
		data = {
			"name":"cat",
			"age": pet.age,
			"sex": pet.sex,
			"price": pet.price,
		}
		response = self.client.post(reverse("update-pet", args=[1]), data)
		pet = Pet.objects.get(id=1)
		self.assertRedirects(response, reverse('pet-details', args=[1]), msg_prefix="make sure correct redirection occurs after update")
		self.assertEqual(data["name"], pet.name, msg="update was not done correctly")
		self.assertEqual(data["age"], pet.age, msg="update was not done correctly")
		self.assertEqual(pet.id, 1, msg="update was not done correctly")



class PetDeleteViewTest(TestCase):

	def setUp(self):
		Pet.objects.create(
			name="croc",
			age=7,
			sex="Male",
			price=66.66
			)
		Pet.objects.create(
			name="bunny",
			age=7,
			sex="Male",
			price=60.66
			)


	def test_delete(self):
		response = self.client.get(reverse('delete-pet', args=[1]))
		self.assertRedirects(response, reverse("pets-list"), msg_prefix="make sure correct redirection occurs after deletion")
		self.assertEqual(Pet.objects.filter(id=1).count(), 0)

	









		





