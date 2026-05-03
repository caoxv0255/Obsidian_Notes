#include<iostream>

using namespace std;

template<typename DataType>
struct Node{
	DataType data;
	Node<DataType>*next;//Node后面别忘了加<DataType>	
};

template<typename DataType>
class LinkList{
	public:
		LinkList();
		LinkList(DataType a[],int n);
		void PrintList();
		~LinkList();
	private:
		Node<DataType>*first;
};

template<typename DataType>
LinkList<DataType>::LinkList(){
	first=new Node<DataType>;
	first->next=nullptr;
}

template<typename DataType>
LinkList<DataType>::LinkList(DataType a[],int n){
	first=new Node<DataType>;
	Node<DataType> *p=first,*q;
	for(int i=0;i<n;i++){
		q=new Node<DataType>;
		q->data=a[i];
		p->next=q;
		p=p->next;
	}
	p->next=nullptr;
}

template<typename DataType>
void LinkList<DataType>::PrintList(){
	Node<DataType>*p=first->next;
	while(p){
		cout<<p->data;
		p=p->next;
	}
}

template<typename DataType>
LinkList<DataType>::~LinkList(){
	Node<DataType>*p=first;
	while(first){
		first=first->next;
		delete p;
		p=first;
	}
}

int main(){
	int arr[5]={1,2,3,4,5},i,x;
	LinkList<int> L(arr,5);
	L.PrintList();
}