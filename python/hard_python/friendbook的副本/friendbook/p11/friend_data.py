import random
xings_str = "李，王，张，刘，陈，杨，黄，赵，周，吴，徐，孙，朱，马，胡，郭，林，何，高，梁，郑，罗，宋，谢，唐，韩，曹，许，邓，萧，冯，曾，程，蔡，彭，潘，袁，于，董，余，苏，叶，吕，魏，蒋，田，杜，丁，沈，姜，范，江，傅，钟，卢，汪，戴，崔，任，陆，廖，姚，方，金，邱，夏，谭，韦，贾，邹，石，熊，孟，秦，阎，薛，侯，雷，白，龙，段，郝，孔，邵，史，毛，常，万，顾，赖，武，康，贺，严，尹，钱，施，牛，洪，龚"
mings_str = "大，二，三，四，五，六，七，八，九"
add_score_things = "点赞，赞美，投币，充电，打电话，帮助，送礼物"
reduce_score_things = "骂，打，欺骗，白嫖，要挟"

names = []
records = [((1, '张三'), '骂了', (2, '李四'), -1)]  # 张三 骂了 李四 减1分；王五 请吃饭 马六 加1分

def mock_names():
    xings = xings_str.split("，")
    mings = mings_str.split("，")
    for i in range(1000):
        xing = random.choice(xings)
        ming = random.choice(mings)
        names.append((i+1, xing+ming))

def mock_records():
    good_things = add_score_things.split("，")
    bad_things = reduce_score_things.split("，")
    things = good_things + bad_things
    for i in range(10000):
        n1 = random.choice(names)
        n2 = random.choice(names)
        thing = random.choice(things)
        if(things.index(thing) >= len(good_things)):
            score = -1
        else:
            score = 1
        records.append((n1, thing, n2, score))

def mock_data():
    print("mocking data")
    mock_names()
    mock_records()
    print("finished mock data")

mock_data()
