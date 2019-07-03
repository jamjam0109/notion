from notion.client import *

token = 'b10d49a16fe9ad2db279f0fd4c3fbd8ef53d2748b2e9c63fca0e382d234b880262994cffba849a46702f71b9cc731cfe897fed9a0fedd942b24ea5aa89359adbbc235114357383b32be4fc460999'

notion_page_url = 'https://www.notion.so/jaemin/0e0386aa405041b8bb7b1537ffed25f3?v=c7c08f40039e4db0b5ce1c90cefbdf6a'

client = NotionClient(token_v2=token)

cv = client.get_collection_view(notion_page_url)

rows = cv.collection.get_rows()

