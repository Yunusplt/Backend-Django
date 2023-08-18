from .base import * 
# from decouple import config      bu .base sayfasindan geliyor. 

env_name = config("ENV_NAME") 
 
if env_name == "prod": 
 
    from .prod import * 
 
elif env_name == "dev": 
 
    from .dev import *