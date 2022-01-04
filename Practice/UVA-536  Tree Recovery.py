# Give Preorder and Inorder string
# Find the Postorder string
# Example :
# input : DBACEGF ABCDEFG 、 output : ACBFGED


# Method 1
def postorder(preorder: str, inorder: str, pre: int, in_low: int, in_high: int):
    if in_low >= in_high:
        print(pre)
        return pre

    # inorder : MLR, preorder : LMR, inorder[i] == preorder[preI] --> find the mid variable
    for i in range(in_low, in_high):
        # i = mid variable position
        if inorder[i] == preorder[pre]:
            pre = postorder(preorder, inorder, pre + 1, in_low, i)   # left subtree
            pre = postorder(preorder, inorder, pre, i + 1, in_high)  # right subtree
            print(str(inorder[i]))
            break

    print(pre)
    return pre


def main():
    preorder, inorder = input().split()
    postorder(preorder, inorder, 0, 0, len(inorder))
    print()


if __name__ == "__main__":
    main()


# Method 2
def postorder(preorder: str, inorder: str, pre_front: int, pre_rear: int, in_front: int, in_rear: int):
    i = inorder.find(preorder[pre_front])   # find the root in inorder, return index value
    if i > in_front:   # left tree
        postorder(preorder, inorder, pre_front + 1, pre_front + i - in_front, in_front, i - 1)
    if i < in_rear:   # right tree
        postorder(preorder, inorder, pre_rear - in_rear + i + 1, pre_rear, i + 1, in_rear)
    print(preorder[pre_front], end='')


def main():
    preorder, inorder = input().split()
    postorder(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)
    print()


if __name__ == "__main__":
    main()
