#include<iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
class Solution {
public:
    ListNode* reverse(ListNode* head, int k) {
        ListNode*p=head->next,*q,*s;
        int count=0;
        q=p;
        while(p){
            p=p->next;
            count++;
        }
        p=head;
        for(int b=0;b<count/2;b++){
        for(int a=0;a<k;a++){
            p=p->next;
        }
        for(long int i=k-1;k>0;i--){
            for(int j=0;j<i;j++){
                q=p;
                s=q->next;
                q->next=q->next->next;
                s->next=q;
            }
        }
        }
        return head;
    }
};

int main(){
	
ListNode *L = new ListNode();
ListNode *l1 = new ListNode(2);
ListNode *l2 = new ListNode(3);
ListNode *l3 = new ListNode(4);
L->next = l1;
l1->next = l2;
l2->next = l3;
Solution s;
ListNode*A=s.reverse(L,2);
A = A->next;
while(A != NULL){
	cout << A->val << endl;
	A = A->next;
}
}