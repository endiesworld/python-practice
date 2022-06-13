from dotenv import load_dotenv
import os
load_dotenv()
os_version = os.getenv('COMPUTER_VISISON')
print(os_version)
