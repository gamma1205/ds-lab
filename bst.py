#include<iostream>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int x) {
        data = x;
        left = right = NULL;
    }
};
void insertNode(Node* &root, int x) {
    if (root == NULL) {
        root = new Node(x);
        return;
    }
    if (x < root->data)
        insertNode(root->left, x);
    else if (x > root->data)
        insertNode(root->right, x);
}
void display(Node* root) {
    if (root != NULL) {
        display(root->left);
        cout << root->data << " ";
        display(root->right);
    }
}
int main() {
    Node* root = NULL;
    int choice, value;

    while (true) {
        cout << "\n--- Binary Search Tree ---\n";
        cout << "1. Insert\n";
        cout << "2. Display (Inorder)\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter value to insert: ";
                cin >> value;
                insertNode(root, value);
                break;

            case 2:
                cout << "BST Inorder Traversal: ";
                display(root);
                cout << endl;
                break;

            case 3:
                cout << "Exiting... Bye cutie \n";
                return 0;

            default:
                cout << "Invalid choice! Try again.\n";
        }
    }
}
