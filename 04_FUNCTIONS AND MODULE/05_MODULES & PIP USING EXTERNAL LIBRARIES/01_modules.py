# Internal modules/ built in modules

import math
import mymodule
import requests

print(math.sqrt(25))
mymodule.hello()

r = requests.get("https://www.google.com")
print(r.text)