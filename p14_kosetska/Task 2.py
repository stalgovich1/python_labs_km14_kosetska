import json

with open('image_info_test-dev2017.json', 'w') as json_file:
    image=['image_info_test-dev2017.json']
category=['image_info_test-dev2017.json']
print(f'Images in sum: {(len(image))}')
print(f'Categories:{len(category)}')

for i in image:  
  if image=='000000000001.jpg':
        print("Link on image:",i['coco_url'])
        print("Height:",i['height'])
        print("Width:",i['width'])
        print("Id:",i['id'])

        image_id=max(image['id'])
        if image==image_id:
           print(image) 