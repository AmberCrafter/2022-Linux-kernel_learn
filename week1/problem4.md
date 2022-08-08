測驗 1
考慮一個單向 linked list，其結構定義為:
```c
typedef struct __node {                   
    int value;
    struct __node *next;
} node_t;
```
已知不存在 circular (環狀結構)，下方程式碼嘗試對該單向 linked list 進行 Quick sort，預期依據遞增順序。
```c
static inline void list_add_node_t(node_t **list, node_t *node_t) {
    node_t->next = *list;
    *list = node_t;
}

static inline void list_concat(node_t **left, node_t *right) {
    while (*left)
        LLL;
// (a) left = left->next
// (b) left = (*left)->next
(c) left = &((*left)->next)
// (d) *left = (*left)->next

    *left = right;
}

void quicksort(node_t **list)
{
    if (!*list)
        return;

    node_t *pivot = *list;
    int value = pivot->value;
    node_t *p = pivot->next;
    pivot->next = NULL;

    node_t *left = NULL, *right = NULL;
    while (p) {
        node_t *n = p;
        p = p->next;
        list_add_node_t(n->value > value ? AAA : BBB, n);
    }
// (a) &pivot
// (b) pivot
// (c) &left
// (d) left
(e) &right
// (f) right

// (a) &pivot
// (b) pivot
(c) &left
// (d) left
// (e) &right
// (f) right


    quicksort(&left);
    quicksort(&right);

    node_t *result = NULL;
    list_concat(&result, left);
    CCC;
// (a) llist_concat(&result, right)
(b) list_concat(&result, pivot); list_concat(&result, right)
// (c) list_concat(&result, right); list_concat(&result, pivot)
    *list = result;
}
```
對應的測試程式如下:
```c
static bool list_is_ordered(node_t *list) {
    bool first = true;
    int value;
    while (list) {
        if (first) {
            value = list->value;
            first = false;
        } else {
            if (list->value < value)
                return false;
            value = list->value;
        }
        list = list->next;
    }
    return true;
}

static void list_display(node_t *list) {
    printf("%s IN ORDER : ", list_is_ordered(list) ? "   " : "NOT");
    while (list) {
        printf("%d ", list->value);
        list = list->next;
    }
    printf("\n");
}

int main(int argc, char **argv) {
    size_t count = 20;

    node_t *list = NULL;
    while (count--)
        list = list_make_node_t(list, random() % 1024);

    list_display(list);
    quicksort(&list);
    list_display(list);

    if (!list_is_ordered(list))
        return EXIT_FAILURE;

    list_free(&list);
    return EXIT_SUCCESS;
}  
```      
參考執行輸出:

NOT IN ORDER : 1016 84 706 124 326 483 763 498 939 186 205 809 236 74 255 81 115 105 966 359 
    IN ORDER : 74 81 84 105 115 124 186 205 236 255 326 359 483 498 706 763 809 939 966 1016 
請補完程式碼，使得執行符合預期。

作答區

LLL = ?

(a) left = left->next
(b) left = (*left)->next
(c) left = &((*left)->next)
(d) *left = (*left)->next
AAA = ?

(a) &pivot
(b) pivot
(c) &left
(d) left
(e) &right
(f) right
BBB = ?

(a) &pivot
(b) pivot
(c) &left
(d) left
(e) &right
(f) right
CCC = ?

(a) llist_concat(&result, right)
(b) list_concat(&result, pivot); list_concat(&result, right)
(c) list_concat(&result, right); list_concat(&result, pivot)