from datetime import datetime

from notion.client import *
from notion.block import *
from notion.smoke_test import get_collection_schema


def run_live_smoke_test(token_v2, parent_page_url_or_id):

    client = NotionClient(token_v2=token_v2)

    parent_page = client.get_block(parent_page_url_or_id)

    page = parent_page.children.add_new(PageBlock, title="{}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    cvb = page.children.add_new(CollectionViewBlock)
    collection = client.get_collection(client.create_record("collection", parent=cvb, schema=get_collection_schema()))
    view = client.get_collection_view(client.create_record("collection_view", parent=cvb, type="table"), collection=collection)
    view.set("collection_id", collection.id)
    cvb.set("collection_id", collection.id)
    cvb.set("view_ids", [view.id])

    row = collection.add_row()
    row.estimated_value = 42122
    row = collection.add_row()
    row.estimated_value = 4212



    # print(collection.get_rows())

    # for aa in a:
    #     a.remove(aa)
    #     a.clear()
    # #


token = 'b10d49a16fe9ad2db279f0fd4c3fbd8ef53d2748b2e9c63fca0e382d234b880262994cffba849a46702f71b9cc731cfe897fed9a0fedd942b24ea5aa89359adbbc235114357383b32be4fc460999'
b = 'https://www.notion.so/jaemin/ba93c9f0b57042ef969f64473c37151a'
run_live_smoke_test(token, b)

