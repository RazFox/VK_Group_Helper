from lib import wall_method
import datetime


def posts_one_month(date_month: datetime, vk_auth) -> list:
    """
    Gets a list of group wall posts for the specified month.

    :param date_month: Date of the first day of the month. Must contain at least the month and year.
    :param vk_auth: The VK Authentication object contains data for authentication and access to the method.
    :return: List of dictionaries with posts.
    """
    offset = 0
    count = 100
    vk_wall = wall_method.WallMethod()
    post_catalog = list()

    while True:
        post_wall_info = vk_wall.post_wall(vk_auth, offset, count)
        if post_wall_info:
            post_info: list = post_wall_info.get("response").get("items")
        else:
            break
        for post in post_info:
            date_post = datetime.datetime.fromtimestamp(post.get("date"))
            if (date_post.month == date_month.month) and (date_post.year == date_month.year):
                post_catalog.append(post)
            elif date_post < date_month:
                break
        offset += count
    return post_catalog
