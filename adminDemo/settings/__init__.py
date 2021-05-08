import platform

from .com_settings import *
if platform.node()=="server_pro":
    from .pro_settings import *
else:
    from .dev_settings import *