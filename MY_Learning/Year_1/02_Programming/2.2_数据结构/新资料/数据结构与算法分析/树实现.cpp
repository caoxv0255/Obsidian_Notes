#include<iostream>

using namespace std;

template<typename DataType>
struct BiNode{
	DataType data;
	BiNode<DataType>*lchild,*rchild;
};

template<typename DataType>
class BiTree{
	public:
		BiTree(){root=Creat();}
		~BiTree(){Release(root);}
		void PreOrder(){PreOrder(root);}
		void InOrder(){InOrder(root);}
	private:
		BiNode<DataType>*Creat();
		void Release(BiNode<DataType>*bt);
		void PreOrder(BiNode<DataType>*bt);
		void InOrder(BiNode<DataType>*bt);
		BiNode<DataType>*root;
};

template<typename DataType>
BiNode<DataType>*BiTree<DataType>::Creat(BiNode<DataType>*bt){
	DataType ch;
	cin>>ch;
	if(ch=="#"){
		bt=NULL;
	}
	else{
		bt=new BiNode<DataType>;
		bt->data=ch;
		bt->lchild=Creat(bt->lchild);
		bt->rchild=Creat(bt->rchild);
	}
	return bt;
}

template<typename DataType>
void BiNode<DataType>::PreOrder(BiNode<DataType>*bt){
	if(!bt)return;
	else{
		cout<<bt->data;
		Preorder(bt->lchild);
		Preorder(bt->rchild);
	}
}

template<typename DataType>
void BiNode<DataType>::InOrder(BiNode<DataType>*bt){
	if(!bt)return;
	else{
		InOrder(bt->lchild);
		cout<<bt->data;
		InOrder(bt->rchild);
	}
}

int main(){
	
	
	
} 