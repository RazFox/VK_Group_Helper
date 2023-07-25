import os.path
from dotenv import load_dotenv


class VKAuthentication:

    def __init__(self):
        self.token = None
        self.v_api = None
        self.group_id = None
        self.owner_id = None
        self.domain = None

    def settings_read(self, path_env):
        if os.path.isfile(path_env):
            load_dotenv(path_env)
            self.token = os.getenv("VK_TOKEN")
            self.v_api = os.getenv("VK_API")
            self.group_id = os.getenv("VK_GROUP_ID")
            self.owner_id = os.getenv("VK_OWNER_ID")
            self.domain = os.getenv("VK_DOMAIN")
        else:
            raise OSError
