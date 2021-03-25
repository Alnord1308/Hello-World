import os
from dotenv import load_dotenv

load_dotenv()

MyVariable = os.getenv('MyVariable')
print(MyVariable)
