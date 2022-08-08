inputs = [1,2,3,4,4,5]

class LinkedList:
    val = 0
    nx = None

inputs = LinkedList()
inputs.val = 1
inputs.nx = LinkedList()

inputs.nx.val = 1
inputs.nx.nx = LinkedList()

inputs.nx.nx.val = 1
inputs.nx.nx.nx = LinkedList()

inputs.nx.nx.nx.val = 4
inputs.nx.nx.nx.nx = LinkedList()

inputs.nx.nx.nx.nx.val = 4
inputs.nx.nx.nx.nx.nx = LinkedList()

inputs.nx.nx.nx.nx.nx.val = 5
inputs.nx.nx.nx.nx.nx.nx = None

print(inputs.val, inputs.nx.val, inputs.nx.nx.val, inputs.nx.nx.nx.val,
    inputs.nx.nx.nx.nx.val, inputs.nx.nx.nx.nx.nx.val)

def deldup(node: LinkedList):
    if node==None: return node

    if node.nx!=None:
        while node.nx!=None and node.val==node.nx.val:
            node = node.nx

        return deldup(node.nx)
    node.nx = deldup(node.nx)
    return node

deldup(inputs)
while inputs:
    print(inputs.val)
    inputs = inputs.nx

# struct ListNode *deleteDuplicates(struct ListNode *head)
# {
#     if (!head)
#         return NULL;

#     if (!head->next) {
#         /* Remove all duplicate numbers */
#         while (!head->next ? head->val == head->next->val : false)
#             head = head->next;
#         return deleteDuplicates(head->next);
#     }

#     head->next = deleteDuplicates(head->next);
#     return head;
# }