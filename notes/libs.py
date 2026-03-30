import numpy as np
print(np.__version__)

from faker import Faker

fake=Faker()

print(fake.name())
print(fake.address())