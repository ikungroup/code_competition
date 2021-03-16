# 本代码是计算简单优化问题 为一维的优化
import random
class bird:
    def __init__(self,speed,position,fit,BestPosition,BestFit):
        self.speed = speed
        self.position = position
        self.fit = fit
        self.BestPosition = BestPosition
        self.BestFit = BestFit
#构建的粒子的参数，其中bird 表示粒子的意思
class PSO:
    def __init__(self,fitFunc,birdNum,w,c1,c2,solutionspace):
        self.fitFunc = fitFunc
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.birds, self.best = self.initbirds(birdNum,solutionspace)
#fitFunc 表示目标函数，本文需要求出目标函数的最小值（目标函数需要设置）
    def initbirds(self,size,solutionspace):
        birds = []
        for i in range(size):
            position = random.uniform(solutionspace[0],solutionspace[1])
            speed = 0
            fit = self.fitFunc(position)
            birds.append(birds(speed,position,fit,position,fit))
            best = birds[0]
        for bird in birds:
            if bird.fit > best.fit:
                    best = bird
        return birds,best

    def updataBirds(self):
        for bird in self.birds:
            bird.speed = self.w * bird.speed + self.c1 * random.random() * (bird.lBestPosition - bird.position) + self.c2 * random.random() * (self.best.position - bird.position)
            bird.position = bird.position+bird.speed
            bird.fit = self.fitFunc(bird.position)
            if bird.fit > bird.BestFit:
                bird.BestFit = bird.fit
                bird.BestPosition = bird.position

    def solve(self, maxIter):
        for i in range(maxIter):
            self.updataBirds()
            for bird in self.birds:
                if bird.fit > self.best.fit:
                    self.best = bird