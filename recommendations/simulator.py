#coding=utf-8
import random,string

def getDataByTX(tx):
    '''
    返回具有特性tx的商品，有约13%的噪音

    热门商品模拟:
    前 1% 商品拥有 7% 的点击,
    前 5% 商品拥有 31% 的点击,
    前 10% 商品拥有 53% 的点击,
    前 20% 商品拥有 75% 的点击,
    前 50% 商品拥有 90% 的点击,

    id平均值为82**
    '''
    pos = random.randint(0,4)
    itemId = int((random.randint(1,int('9'*50)))**(0.1))-1 
    data = str(itemId).rjust(5,'0')
    tx = data[:pos]+str(tx)+data[pos+1:]
    return tx[0:4]

def getOneDayDatas():
    datas=[]
    ipCount = 10000 #每天10000个ip
    avgClickCount = 7 #每个ip平均7次点击
    for i in range(ipCount):
        datas.append([])
        tx = random.randint(0,9) # 每个ip从0到9十个特性中随机喜欢一个
        for j in range(random.randint(1,20)): # 每个ip最少点击1次，最多20次
            if random.randint(0,9) < avgClickCount: 
                data = getDataByTX(tx)
                if data not in datas[i]:
                    datas[i].append(data)

    return dict([(str(datas.index(data)),data) for data in datas if len(data) > 1])

if __name__ == '__main__':
    import recommendate
    r={}
    for i in range(10):
        d=getOneDayDatas()
        recommendate.calculateRecommendations(r,d)
        print 'day: ',i
    file = open('simtemp','w')
    for k,v in r.items():
        file.write(k)
        file.write('\n')
        v.reverse()
        for relation,id in v:
            file.write(str(id).ljust(10,' '))
            file.write(str(relation))
            file.write('\n')
        file.write('\n\n')
