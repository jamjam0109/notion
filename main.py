from notion.client import *
from notion.block import *
from datetime import datetime
from crawling import crawling


def main(token, notion_page_url, crawling_output):
    client = NotionClient(token_v2=token)
    cv = client.get_collection_view(notion_page_url)

    rows = cv.collection.get_rows()

    for row in rows:
        client.submit_transaction(
            build_operation(
                id=row.id,
                path=[],
                args={"alive": False},
                command="update",
            )
        )

    cv.collection.description = f'**Update Date: {datetime.now().strftime("%Y-%m-%d %H:%M")}**'

    for blog_name in crawling_output:
        row = cv.collection.add_row()
        row.blog = blog_name
        row.title = crawling_output[blog_name][0]
        row.date = crawling_output[blog_name][1]
        row.url = crawling_output[blog_name][2]


if __name__ == '__main__':
    my_token = 'f79be92f01c600cc67f628b5958f11a93263a737c35cc7707a27fa5f02e4c9f85474a6594569e6d5f786af18447506ef08b6dc31411e12c3ddd28f252a2b642c7f43368d98ddcf01f27f5ac35bbb'
    my_notion_page_url = 'https://www.notion.so/jaemin/0e0386aa405041b8bb7b1537ffed25f3?v=c7c08f40039e4db0b5ce1c90cefbdf6a'
    crawling_data = crawling()

    main(my_token, my_notion_page_url, crawling_data)
