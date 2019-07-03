from notion.client import *
from notion.block import *
from datetime import datetime
from crawling_selenium import crawling


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
    my_token = 'b10d49a16fe9ad2db279f0fd4c3fbd8ef53d2748b2e9c63fca0e382d234b880262994cffba849a46702f71b9cc731cfe897fed9a0fedd942b24ea5aa89359adbbc235114357383b32be4fc460999'
    my_notion_page_url = 'https://www.notion.so/jaemin/0e0386aa405041b8bb7b1537ffed25f3?v=c7c08f40039e4db0b5ce1c90cefbdf6a'
    crawling_data = crawling()

    main(my_token, my_notion_page_url, crawling_data)
