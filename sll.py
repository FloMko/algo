class SinglyLinkedList:    
     def __init__(self):    
         self.tail = None         
         self.head = None         
         self.size = 0            
     def append(self, data):      
         self.size +=1       
         node = Node(data)        
         if self.head:       
             self.head.next = node
             self.head = node
         else:               
             self.tail = node  
             self.head = node      
     def size(self):               
         return self.size          
     def iter(self):               
         current = self.tail   
         while current:            
             val = current.data    
             current = current.next    
             yield val                       
