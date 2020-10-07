class Node:
    def __init__(self, data):
        self.item = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("List tidak memiliki element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, end=" ")
                n = n.next
            print("\n")

    def insert_at_start(self, data):
        new_node = Node(data) #kita bikin node baru
        new_node.next = self.start_node #kita isi nexterensi atau next nya dari node yang dibuat sama Head nya
        self.start_node = new_node #head nya kita ganti dengan node baru yang udah dibikin

    def insert_at_end(self, data):
        new_node = Node(data) #kita bikin node baru
        if self.start_node is None: #kalo head nya kosong
            self.start_node = new_node #headnya langsung ke isi sama node barunya
            return
        n = self.start_node #n ini buat nampung head nya jadi head nya ga akan ke ubah
        while n.next is not None: #nah karena n udah di ganti sama head, otomatis n itu isinya node pertama jadi punya atribut "item" sama "next"
            n = n.next #kan ini bakal di ulang terus sampe nexterensi dari nodenya tu kosong, nah biar ngulang terus. tiap looping n nya di ganti sama n.next biar dia ganti ke node selanjutnya
        n.next = new_node #begitu sampe node terakhir dimana next nya none nnt next nya di isi sama node baru yg kita masukin 

    def insert_after_item(self, data, after):
        if self.start_node is None:
            return "List tidak memiliki element"

        new_node = Node(data)
        current_node = self.start_node
        while current_node.item != after:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def insert_before_item(self, data, before):
        if self.start_node is None:
            return "List tidak memiliki element"
        
        if self.start_node.item == before:
            self.insert_at_start(data)
        else:
            new_node = Node(data)
            current_node = self.start_node
            while current_node.next.item != before:
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

    def delete_at_start(self):
        current_node = self.start_node #ini bikin variabel buat nampung headnya, jadi otomatis variabelnya keisi node pertama
        self.start_node = current_node.next #disini headnya kita isi sama nexterensi dari node pertama otomatis adalah node kedua
        current_node.next = None #nah node pertamanya nextnya kita apus, otomatis dia terputus sama linkedlistnya jadi node kedua otomatis jadi node pertama
        del current_node.item #ini kita ngepaus node pertamanya

    def delete_at_end(self):
        try:
            current_node = self.start_node
            while current_node.next.next is not None:
                current_node = current_node.next
            del current_node.next.item
            current_node.next = None
        except AttributeError:
            self.delete_at_start()

    def delete_after_item(self, after):
        current_node = self.start_node
        while current_node.item != after:
            current_node = current_node.next
        if current_node.next != None:
            after_current_node = current_node.next
            current_node.next = after_current_node.next
            after_current_node.next = None
            del after_current_node.item
        
    
    def delete_before_item(self, before):
        current_node = self.start_node
        if self.start_node.next.item == before:
            self.delete_at_start()
        elif before != self.start_node.item:
            while current_node.next.next.item != before:
                current_node = current_node.next
            after_current_node = current_node.next
            current_node.next = after_current_node.next
            after_current_node.next = None
            del after_current_node.item
    

new_linked_list = LinkedList()

print("=== Insert item di akhir linked list ===")
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.traverse_list()

print("=== Insert item di awal linked list ===")
new_linked_list.insert_at_start(1)
new_linked_list.insert_at_start(2)
new_linked_list.insert_at_start(3)
new_linked_list.traverse_list()

print("=== Insert item sebelum item lain dalam linked list ===")
new_linked_list.insert_before_item(17, 10)
new_linked_list.traverse_list()

print("=== Insert item Setelah item lain dalam linked list ==")
new_linked_list.insert_after_item(11, 5)
new_linked_list.traverse_list()

print("=== Delete item di akhir linked list ===")
new_linked_list.delete_at_end()
new_linked_list.traverse_list()

print("=== Delete item di awal linked List ==")
new_linked_list.delete_at_start()
new_linked_list.traverse_list()

print("=== Delete item setelah item lain dalam linked list ===")
new_linked_list.delete_after_item(17)
new_linked_list.traverse_list()

print("=== Delete item sebelum item lain dalam linked list ===")
new_linked_list.delete_before_item(5)
new_linked_list.traverse_list()





