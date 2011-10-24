#coding=utf-8
import __config__ as config
import random

def calculateRecommendations(relativity,clickStatistic):
    '''
    relativity = {'a':[(2,'b'),(8,'c')],'b':[(3,'a'),(3,'c')]}
    clickStatistic = {'ip1':['a','b'],'ip2':['b','c'],'ip3':['a','b']}
    '''
    #计算每个商品的点击次数
    clickCount = {}         #{a:2,b:2,}
    for ip,itemIds in clickStatistic.items():
        for itemId in itemIds:
            clickCount.setdefault(itemId,0)
            clickCount[itemId] += 1

    #计算相关点击次数
    relateClickCount = {}   #{a:{b:2,c:3},b:{a:2,c:1},}
    for ip,itemIds in clickStatistic.items():
        for i in itemIds:
            relateClickCount.setdefault(i,{})
            for j in itemIds:
                if i != j:
                    relateClickCount[i].setdefault(j,0)
                    relateClickCount[i][j] += 1

    #渐忘
    for itemId,relations in relativity.items():
        if relateClickCount.has_key(itemId):
            relativity[itemId] = [(relation*config.forget,reItemId) for relation,reItemId in relations]
            relativity[itemId].sort()

    #遗忘
    for itemId,relations in relativity.items():
        if relateClickCount.has_key(itemId) and len(relativity[itemId])>(config.relateLimit-config.lose[1]):
            loseCount = min(config.lose[0],len(relativity[itemId]))
            relativity[itemId]  = [(relation,reItemId) for relation,reItemId in relations[:loseCount] if random.random() < (float(config.lose[1]) / config.lose[0]) ] + relations[loseCount:]
            relativity[itemId].sort()

    #计算新的relation值
    newRelativity = {}
    for itemId, relations in relateClickCount.items():
        newRelativity.setdefault(itemId,{})
        for reItemId, reClickCount in relations.items():
            newRelativity[itemId][reItemId] = float(reClickCount)/(float(clickCount[reItemId])**config.cold)
        if relativity.has_key(itemId):
            newTotal = config.totalRelativity - sum([v for v,id in relativity[itemId]])
        else:
            newTotal = config.totalRelativity
        normalizeSum = sum(newRelativity[itemId].values())
        for k,v in newRelativity[itemId].items():
            newRelativity[itemId][k] = (float(v) / float(normalizeSum)) * float(newTotal)
        '''
        if not relativity.has_key(itemId):
            if sum([v for k,v in newRelativity[itemId].items()])<490:
                print newRelativity[itemId]
                print a
        '''

    #叠加relation值
    for itemId,relations in newRelativity.items():
        if relativity.has_key(itemId):
            reIds = [reItemId for relation,reItemId in relativity[itemId] if newRelativity[itemId].has_key(reItemId)]
            '''
            temp = [ (relation,reItemId) for reItemId,relation in newRelativity[itemId].items() if reItemId not in reIds] + [ (relation + newRelativity[itemId][reItemId],reItemId) for relation,reItemId in relativity[itemId] if newRelativity[itemId].has_key(reItemId)] + [ (relation,reItemId) for relation,reItemId in relativity[itemId] if not newRelativity[itemId].has_key(reItemId)]
            if sum([r for r,i in temp])<450:
                print relativity[itemId]
                print newRelativity[itemId]
                print a
            '''
            relativity[itemId] = [ (relation,reItemId) for reItemId,relation in newRelativity[itemId].items() if reItemId not in reIds] + [ (relation + newRelativity[itemId][reItemId],reItemId) for relation,reItemId in relativity[itemId] if newRelativity[itemId].has_key(reItemId)] + [ (relation,reItemId) for relation,reItemId in relativity[itemId] if not newRelativity[itemId].has_key(reItemId)]
        else:
            relativity[itemId] = [(relation,reItemId) for reItemId,relation in newRelativity[itemId].items()]
        relativity[itemId].sort()
        del relativity[itemId][:-config.relateLimit]
