#基于list实现链表并实现倒序链表

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList(object):


    def __init__(self):
        #首节点
        self._head = None


    def isEmpty(self):
        if self._head is None:
            return True
        else:
            return False


    #在尾部添加数据
    def append(self,data):
        node = Node(data)
        #若链表不为空,
        if self.isEmpty():
            self._head = node
        else:
            cur = self._head
            while(cur.next is not None):
                cur = cur.next
            cur.next = node


    #在头部添加数据
    def add(self,data):
        node = Node(data)
        if (self._head is None):
            self._head = node
        else:
            node.next = self._head
            self._head = node


    #统计总数
    def length(self):
        if (self._head is None):
            return 0
        else:
            sums = 0
            cur = self._head
            #统计到当前无值
            while(cur is not None):
                sums+=1
                cur = cur.next
            return sums

    #idx 从0开始对应索引与数据一致
    def insert(self,idx,value):
        sums = self.length()

        if(idx <= 0):
            self.add(value)
        elif(idx >= sums):
            self.append(value)
        else:
            #起点都是从head开始
            node = Node(value)
            cur = self._head
            for i in range(idx - 1):
                cur = cur.next

            node.next = cur.next       # 0,1,2,3,4  (insert(2,v) ) => 0,1,v,2,3,4
            cur.next = node

    #删除指定index数据
    def remove_index(self,idx):
        if(idx > self.length() - 1):
            return -1
        else:
            if(idx<=0):
                self._head = self._head.next
            else:
                cur = self._head
                for i in range(idx - 1):
                    cur = cur.next
                cur.next = cur.next.next


    #删除首个value = item
    def remove_value(self, data):
        """删除节点"""
        cur = self._head
        pre = None
        while cur is not None:
            # 找到指定元素
            if cur.data == data:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return True
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    #打印全部数据
    def items(self):
        cur = self._head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    #倒序输出
    def reverse_print(self):
        temp = []
        cur = self._head
        while(cur is not None):
            temp.append(cur.data)
            cur = cur.next
        #print(temp)
        while(temp):
            print(temp.pop(-1))

    #反转链表
    def reverse_linklist(self):

        pre = None
        cur = self._head
        next = cur.next

        # 空链表
        if cur is None:             #由于cur已经是None才会结束故 head应该是 pre
            return cur

        while(cur is not None):
            cur.next = pre           # 当前cur node 的next node 为上一个 pre node
            pre = cur                # pre node 和 cur node均后移一格
            cur = next

            if (next is not None):
                next = next.next

        self._head = pre
        return 0



if __name__=="__main__":
    linklist = LinkList()
    for i in range(10):
        linklist.append(i)

    linklist.items()
    linklist.reverse_linklist()
    #linklist.insert(2,12)
    linklist.items()
    #linklist.reverse_print()




