from django.core.management.base import BaseCommand
from faker import Faker
import random
from django.contrib.auth import get_user_model
from fake.models import Product

class Command(BaseCommand):
    help = 'inserting dummy data'


    def __init__(self, *args , **kwargs):
        super(Command , self).__init__(args, kwargs)
        self.fake = Faker()
        
    
    def handle(self, *args, **kwargs):
        User = get_user_model()
        user = User.objects.create(username = 'ali' , email = self.fake.email , password = self.fake.password)
        choices = ['HP' , 'apple' , 'microsoft']
        rand_name = random.choice(choices)
        product = Product.objects.create(name = rand_name , category = 'PC')