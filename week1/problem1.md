# Q1.
1. FuncA
```c
void FuncA(struct node **start, int value) {
    if (!*start) {
        struct node *new_node = malloc(sizeof(struct node));
        new_node->data = value;
        new_node->next = new_node->prev = new_node;
        *start = new_node;
        return;
    }
    struct node *last = (*start)->prev;
    struct node *new_node = malloc(sizeof(struct node));
    new_node->data = value;
    new_node->next = *start;
    (*start)->prev = new_node;
    new_node->prev = last;
    last->next = new_node;
}
```
 - start node 不存在時
    - 創建一個新 node (value)
    - prev = node = next => 前後指標皆指向自己
    - 回存 node 實例到 start
 - start node 存在時
    - last: 取得 start node 的前一個 node 指標 (推測可能為last node)
    - 建立新的 node (value)
    - node.next -> start
    - start.prev -> node
    - node.prev -> last
    - last.next -> node
    - view: 
        - last <-> node <-> start
        - [node] <-> start <-> ... <-> last <-> node <-> [start]

> FuncA: 用來建立新的node，並將此node新增至此circle linked list的最後一個節點


2. FuncB
```c
void FuncB(struct node **start, int value) {
    struct node *last = (*start)->prev;
    struct node *new_node = malloc(sizeof(struct node));
    new_node->data = value;
    new_node->next = *start;
    new_node->prev = last;
    last->next = (*start)->prev = new_node;
    *start = new_node;
}
```
 - last: 保存start.prev (推測為最後一個node)
 - node: 建立新node (value)
 - view: 
    last <-> node <-> start
             ^
             set this to start
> FuncB: 建立新的node，並將其新增至此circle linked list的第一個節點

3. FuncC
```c
void FuncC(struct node **start, int value1, int value2) {
    struct node *new_node = malloc(sizeof(struct node));
    new_node->data = value1;
    struct node *temp = *start;
    while (temp->data != value2)
        temp = temp->next;
    struct node *next = temp->next;
    temp->next = new_node;
    new_node->prev = temp;
    new_node->next = next;
    next->prev = new_node;
}
```
 - 建立新的node (value1) 
 - temp: 紀錄start
 - 遍歷list，直到找到value2
 - next: value2 -> next
 - view: value2 <-> node <-> next
> FuncC: 建立新的node，並將其插入至 value2 node 之後 

---
# Q2
```c
#include <stdio.h>
#include <stdlib.h>

/* Link list node */
struct node {
    int data;
    struct node *next;
};

int FuncX(struct node *head, int *data) {
    struct node *node;
    for (node = head->next; node && node != head; node = node->next)
        data++;
    return node - head;
}

struct node *node_new(int data) {
    struct node *temp = malloc(sizeof(struct node));
    temp->data = data; temp->next = NULL;
    return temp;
}

int main() {
    int count = 0;
    struct node *head = node_new(0);
    head->next = node_new(1);
    head->next->next = node_new(2);
    head->next->next->next = node_new(3);
    head->next->next->next->next = node_new(4);
    // head(0) -> node(1) -> node(2) -> node(3) -> node(4)
    printf("K1 >> %s\n", FuncX(head, &count) ? "Yes" : "No"); // 4 => Yes; count = 0
    head->next->next->next->next = head; 
    // head(0) -> node(1) -> node(2) -> node(3) -> [head(0)]
    printf("K2 >> %s\n", FuncX(head, &count) ? "Yes" : "No"); // 0 => No; count = 0
    head->next->next->next->next->next = head->next;  // same
    // head(0) -> node(1) -> node(2) -> node(3) -> [head(0)]
    printf("K3 >> %s\n", FuncX(head, &count) ? "Yes" : "No"); // 0 => No; count = 0
    head->next = head->next->next->next->next->next->next->next->next;
    // head(0) -> [head(0)]
    printf("K4 >> %s\n", FuncX(head, &count) ? "Yes" : "No"); // 0 => No; count = 0
    printf("K5 >> %d\n", head->next->data); // 0
    printf("count >> %d\n", count); // 0
    return 0;
}
```

1. FuncX用途
```c
int FuncX(struct node *head, int *data) {
    struct node *node;
    for (node = head->next; node && node != head; node = node->next)
        data++;
    return node - head;
}
```
 - node: 宣告node變數空間
 - node = head->next (start point)
 - node && node != head: (node 不為空) && (node 不為 head)  # 因此list為circle linked list
 - node = node->next: 步進方法，移動到下一個節點
 - data++: data記憶體位置移動1個int (32bit)，未回存，不影響caller的位置
 - 回傳linked list占用的記憶體寬度，若 node-head==0 表示此為circle linked list

2. K1 >> 後面接的輸出為何 Yes
3. K2 >> 後面接的輸出為何 No
4. K3 >> 後面接的輸出為何 No
5. K4 >> 後面接的輸出為何 No
6. K5 >> 後面接的輸出為何 0
7. count >> 後面接的輸出為何 0