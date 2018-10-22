from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '14509587'
API_KEY = 'GxiA1EkLafm7MiZVY0qhWfec'
SECRET_KEY = 'YQ1Ssbpqgs9qj0zkcv6lCHsGBTck63HA'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('images/example.jpg')

""" 调用通用文字识别, 图片为远程url图片 """
# res=client.basicGeneralUrl(url);

""" 调用通用文字识别, 图片为本地图片 """
res = client.general(image)
print(res)
