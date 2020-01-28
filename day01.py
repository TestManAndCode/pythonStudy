users = {
    "Angelica": {
        "Blues Traveler": 3.5,
        "Broken	Bells": 2.0,
        "Norah	Jones": 4.5,
        "Phoenix": 5.0,
        "Slightly	Stoopid": 1.5,
        "The	Strokes": 2.5,
        "Vampire	Weekend": 2.0
    },
    "Bill": {
        "Blues	Traveler": 2.0,
        "Broken	Bells": 3.5,
        "Deadmau5": 4.0,
        "Phoenix": 2.0,
        "Slightly	Stoopid": 3.5,
        "Vampire	Weekend": 3.0
    },
    "Chan": {
        "Blues	Traveler": 5.0,
        "Broken	Bells": 1.0,
        "Deadmau5": 1.0,
        "Norah	Jones": 3.0,
        "Phoenix": 5,
        "Slightly	Stoopid": 1.0
    },
    "Dan": {
        "Blues	Traveler": 3.0,
        "Broken	Bells": 4.0,
        "Deadmau5": 4.5,
        "Phoenix": 3.0,
        "Slightly	Stoopid": 4.5,
        "The	Strokes": 4.0,
        "Vampire	Weekend": 2.0
    },
    "Hailey": {
        "Broken	Bells": 4.0,
        "Deadmau5": 1.0,
        "Norah	Jones": 4.0,
        "The	Str okes": 4.0,
        "Vampire	Weekend": 1.0
    },
    "Jordyn": {
        "Broken	Bells": 4.5,
        "Deadmau5": 4.0,
        "Norah	Jones": 5.0,
        "Phoeni x": 5.0,
        "Slightly	Stoopid": 4.5,
        "The	Strokes": 4.0,
        "Vampire	Weekend": 4.0
    },
    "Sam": {
        "Blues	Traveler": 5.0,
        "Broken	Bells": 2.0,
        "Norah	Jones": 3.0,
        "Phoe nix": 5.0,
        "Slightly	Stoopid": 4.0,
        "The	Strokes": 5.0
    },
    "Veronica": {
        "Blues	Traveler": 3.0,
        "Norah	Jones": 5.0,
        "Phoenix": 4.0,
        "Slig htly	Stoopid": 2.5,
        "The	Strokes": 3.0
    }
}
print(users["Veronica"])

def minkowski(rating1,rating2,r):
    """ 
        闵可夫斯基距离计算
    """
    distance = 0
    # 遍历用户评分数据
    for key in rating1:
        # 判断是否有一致的key
        if key in rating2:
            # 获取参数的和
            distance += pow(abs(rating1[key]-rating2[key]),r)
    #开根
    return pow(distance,1/r)

def manhattan(rating1, rating2):
    """计算曼哈顿距离
    参数格式为键值对
    """
    distance = 0
    # 遍历用户评分数据
    for key in rating1:
        # 判断是否有一致的key
        if key in rating2:
            # 计算曼哈顿距离
            distance += abs(rating1[key]-rating2[key])
    return distance


def computeNearesNeighbor(username, users):
    """ 计算所有用户至username用户的距离，倒序排列并返回结果列表 
        username 为对比用户名称 users为对比的用户数据组·
    """
    distances = []
    #遍历用户数据
    for user in users:
        #若不是相同的用户则计算曼哈顿距离
        if user != username:
            #计算用户的曼哈顿距离
            # distance = manhattan(users[user], users[username])
            #计算闵氏距离
            distance = minkowski(users[user], users[username],2)
            #将结果以元组的格式添加到列表中
            distances.append((distance, user))
            # 按距离排序————距离近的排在前面
    distances.sort()
    return distances

#获得结果计算
distanceRecord=computeNearesNeighbor('Hailey',users)

print(distanceRecord)

def recommend(username,users):
    """ username：需要推荐的用户名称
        users:需要挖掘的用户数据
        找到距离最短的用户推荐 没评分过的数据
    """
    distanceRecord=computeNearesNeighbor(username,users)
    #推荐数据
    recommendData=[]
    #获得推荐用户名称
    recommendUserName=distanceRecord[0][1]
    #获得推荐用户评分数据
    recommendUser=users[recommendUserName]
    #需推荐用户评分数据
    userInfo=users[username]
    for key in recommendUser:
        if not key in userInfo:
            recommendData.append((key,recommendUser[key]))
            #结果倒序排序 params(列表数据，对比的元素，排序规则)
    return sorted(recommendData,key=lambda score:score[1],reverse=True)
    
print("获取推荐数据")
print(recommend('Hailey',users))



