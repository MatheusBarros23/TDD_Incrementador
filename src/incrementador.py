
class IncError(Exception):
    pass

class Incrementador:
    def inc(self,num):
        resp_l=[]
        if (type(num) is not list):
            num = [num]
        for i in range(len(num)):
            if (type(num[i]) is int and num[i] > 0):
                res = num[i] + 1
                resp_l.append(res)
            else:
                raise IncError()
        if (len(num) == 1):
            return resp_l[0]
        else:
            return resp_l