考慮一個單向 linked list:
```c
typedef struct __list {
    int data;
    struct __list *next;
} list;
```
在不存在環狀結構的狀況下，以下函式能夠對 linked list 元素從小到大排序:
```c
list *sort(list *start) {
    // start node 不存在或是 只有一個node 直接回傳
    if (!start || !start->next)
        return start;
    list *left = start;
    list *right = left->next;
    LL0;
(a) left->next = NULL 
// (b) right->next = NULL
// (c) left = left->next
// (d) left = right->next

    left = sort(left);
    right = sort(right);

    // ^^^ 解開linked list

    // left 或 right 存在時
    for (list *merge = NULL; left || right; ) {
        // right 不存在 或是 left 存在並且 left<right
        if (!right || (left && left->data < right->data)) {
            // merge為空
            if (!merge) {
                LL1;
// (a) start = left
// (b) start = right
// (c) merge = left
// (d) merge = right
(e) start = merge = left
// (f) start = merge = right
            } else {
                LL2;
(a) merge->next = left
// (b) merge->next = right
                merge = merge->next;
            }
            LL3;
(a) left = left->next
// (b) right = right->next
// (c) left = right->next
// (d) right = left->next
        } else {
            if (!merge) {
                LL4;
// (a) start = left
// (b) start = right
// (c) merge = left
// (d) merge = right
// (e) start = merge = left
(f) start = merge = right
            } else {
                LL5;
// (a) merge->next = left
(b) merge->next = right
                merge = merge->next;
            }
            LL6;
// (a) left = left->next
(b) right = right->next
// (c) left = right->next
// (d) right = left->next
        }
    }
    return start;
}
```
請補完程式碼。

作答區

LL0 = ? (a)

(a) left->next = NULL
(b) right->next = NULL
(c) left = left->next
(d) left = right->next
LL1 = ? (e)

(a) start = left
(b) start = right
(c) merge = left
(d) merge = right
(e) start = merge = left
(f) start = merge = right
LL2 = ? (a)

(a) merge->next = left
(b) merge->next = right
LL3 = ? (a)

(a) left = left->next
(b) right = right->next
(c) left = right->next
(d) right = left->next
LL4 = ? (f)

(a) start = left
(b) start = right
(c) merge = left
(d) merge = right
(e) start = merge = left
(f) start = merge = right
LL5 = ? (b)

(a) merge->next = left
(b) merge->next = right
LL6 = ? (b)

(a) left = left->next
(b) right = right->next
(c) left = right->next
(d) right = left->next