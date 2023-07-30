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
            if date_start <= date_post <= date_finish:
                post.update({"url": "https://vk.com/{}?w=wall{}_{}".format(
                    vk_auth.domain,
                    vk_auth.owner_id,
                    post.get("id"))})
                post_catalog.append(post)
            elif date_post < date_start:
                day_post_flag = False
                break
        offset += count
    return post_catalog


def posting_data_cleaner(post_data: list[dict]) -> list[dict]:
    """
    Iterate over the list with data on posts.
    Using the keys, we get data from the post and collect a new list of dictionaries.

    Contains data (keys):
        Post ID (messages) - post_id
        Number of comments - comments_count
        Number of views - views_count
        Number of likes - likes_count
        Total number of reposts - reposts_count
        Number of reposts per wall - reposts_wall
        Number of reposts per message - reposts_mail
        Post text (messages) - text_message
        Post date - date

    :param post_data: List with dictionaries. Post data
    :return:  List of dictionaries. Cleared and only selected post data
    """
    post_list = list()
    for post in post_data:
        post_list.append(
            {
                "post_id": post.get("id"),
                "comments_count": post.get("comments").get("count"),
                "views_count": post.get("views").get("count"),
                "likes_count": post.get("likes").get("count"),
                "reposts_count": post.get("reposts").get("count"),
                "reposts_wall": post.get("reposts").get("wall_count"),
                "reposts_mail": post.get("reposts").get("mail_count"),
                "text_message": post.get("text"),
                "date": post.get("date"),
                "url": post.get("url")
            }
        )
    return post_list
