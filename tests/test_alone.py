import requests

urls = 'http://112.13.89.101:9011/v1/pc/user/rddb/list/'
# headers = {
#     'authonrition': '''eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMzgwODUzNjYtMDhmYS0xMWU5LTg1YjEtZTBkNTVlOGYyZDlhIiwidXNlcm5hbWUiOiJhZG1pbiIsImlzc3VlciI6ImRldl9qdHdfaXNzdWVyIiwiZXhwIjoxNTQ3NTE4Njg3LCJzb3VyY2UiOjEsImVtYWlsIjpudWxsfQ.38x9GdbVPHJRnyLAK_psSravb_XF4YF7Be-eDo4VzuE'''}

# r = requests.get(urls, headers=headers)
r = requests.get(urls)
print(r)
