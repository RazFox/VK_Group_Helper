import requests


class WallMethod:

    @classmethod
    def post_wall(cls, vk_auth, offset: int, count: int) -> dict or None:
        """
        Method for getting data from the community wall.

        :param vk_auth: Object with data for VC authentication
        :param offset: Mixing posts
        :param count: Number of posts received from the wall
        :return: If the request returns an error, then None will be returned,
        otherwise a dictionary with data will be returned.
        """
        post_data = requests.get('https://api.vk.com/method/wall.get', params={
            'access_token': vk_auth.token,
            'owner_id': vk_auth.owner_id,
            'domain': vk_auth.domain,
            'offset': offset,
            'count': count,
            'filter': "all",
            'extended': 1,
            'v': vk_auth.v_api,
        }).json()
        if post_data.get("error"):
            print(post_data.get("error").get("error_code"))
            print(post_data.get("error").get("error_msg"))
            return None
        return post_data
