from lib import wall_method
import datetime


def posts_period(date_start: datetime, date_finish: datetime, vk_auth) -> list:
    """
    Gets a list of posts on the group's wall for the specified period.
    The start date and end date are included in the period.

    :param date_start: The start date of the period. Must contain day, month, year.
    :param date_finish: End date of the period. Must contain day, month, year.
    :param vk_auth: The VK Authentication object contains data for authentication and access to the method.
    :return: List of dictionaries with posts.
    """
    offset = 0
    count = 100
    vk_wall = wall_method.WallMethod()
    post_catalog = list()
    day_post_flag = True

    while day_post_flag:
        post_wall_info = vk_wall.post_wall(vk_auth, offset, count)
        if post_wall_info:
            post_info: list = post_wall_info.get("response").get("items")
        else:
            break
        for post in post_info:
            date_post = datetime.datetime.fromtimestamp(post.get("date"))
            if date_start >= date_post <= date_finish:
                post_catalog.append(post)
            elif date_post < date_start:
                day_post_flag = False
                break
        offset += count
    return post_catalog


