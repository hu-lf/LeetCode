# 1.栈

class Stack(object):  

    def __init__(self):
        self.list = []  # 数据栈
    
    def push(self, element):
        self.list.append(element)

    def pop(self):       
        return self.list.pop()
                
    def top(self):
        return self.list[-1]

    def isEmpty(self):
    	return self.list == []

class Solution:

	def __init__(self):
		self.stack = Stack()
        
	def isValid(self, string):  # 1.(){} 2.{[()]}  3.}()  4.({}
		                        # s.split() ×
		panduan = ('()','[]','{}')

		for s in string:
			if s in (')','}',']'):
				if self.stack.isEmpty():
					return False
				elif (self.stack.pop()+s) in panduan:   # 左右对称，不是等于
					continue
				else:
					return False
			self.stack.push(s)

		if self.stack.isEmpty():
			return True
		else:
			return False

# 测试项        
StringList = ['(){}[]','{[()}','{()}([])','}()','({}','){}']

for string in StringList:
	solution = Solution()
	print(solution.isValid(string))


# 2.消除括号
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s  or '[]' in s or '{}' in s:
            s = s.replace('()', "")
            s = s.replace('[]', "")
            s = s.replace('{}', "") 
        return s == ''	
