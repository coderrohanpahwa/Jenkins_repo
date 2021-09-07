from django.test import TestCase
class URLTest(TestCase):
  def example_test(self):
    print("Invoekd in tests")
    response=self.client.get('/')
    self.assertEquals(response.status_code,200)
# Create your tests here.
