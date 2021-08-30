#include <iostream>
#include <vector>

using namespace std;

class ListNode {
public:
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Init
        ListNode *ans = new ListNode(0, NULL);
        ListNode *tmp = ans;
        
        while (l1 != NULL || l2 != NULL){
            if (l1 == NULL)
                tmp -> val += l2->val;
            else if ( l2 == NULL)
                tmp->val += l1->val;
            else
                tmp->val += (l1->val +l2->val);
            
            
            if (l1!= NULL)
                l1 = l1->next;
            
            if (l2!= NULL)
                l2 = l2->next;
            
            
            if (tmp -> val > 9){
                tmp -> val -= 10;
                tmp -> next = new ListNode(1, NULL);
            }else{
                if (l1 != NULL || l2 != NULL)
                    tmp -> next = new ListNode(0, NULL);
            }
            
            tmp = tmp -> next;
        
        }
        
        return ans;
    }
};


int main() {
    vector<int> l1_vector = {2,4,3};
    vector<int> l2_vector = {5,6,4,5};
    ListNode *tmp;

    ListNode *l1 = new ListNode(l1_vector[0], NULL);
    tmp = l1;

    for (int i = 1; i < l1_vector.size() ; i++){
        tmp->next = new ListNode(l1_vector[i], NULL);
        tmp = tmp ->next;
    }
    
    ListNode *l2 = new ListNode(l2_vector[0], NULL);
    tmp = l2;

    for (int i = 1; i < l2_vector.size() ; i++){
        tmp->next = new ListNode(l2_vector[i], NULL);
        tmp = tmp ->next;
    }

    ListNode *output;
    Solution solution;
    output = solution.addTwoNumbers(l1, l2);


    cout << "output: ";
    tmp = output;

    while (tmp != NULL){
        cout << tmp ->val << ", ";
        tmp = tmp -> next;
    }
    
    cout << endl;
    
    return 0;
}



