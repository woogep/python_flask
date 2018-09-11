#-*- coding:utf-8



import time

def fbis(num):
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

def main():
    result = fbis(10)
    print result

if __name__=='__main__':        #if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
                                #当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行
    main()


