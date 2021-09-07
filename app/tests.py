from django.test import TestCase
class URLTest(TestCase):
  def example_test(self):
    print("Invoekd in tests")
    response=self.client.get('/')
    
# Create your tests here.
