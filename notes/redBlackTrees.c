Red black trees

BST with one extra attribute for each node: colour, red or black. also need to keep track of the parent of each node.
so the red black structue would be:

struct t_red_black_node {
    enum { red, black } colour;
    void *item;
    struct t_red_black_node *left,
                     *right,
                     *parent;
    }

rn null nodes which terminate the tree are leaves and coloured black.

Definition of a red black tree

A red black tree is a BST with the following red-black properties:
    1. every node is either red or black.
    2. every leaf (null) is black
    3. if a node is red, then both its children are black.
        (3 implies that on any path from root to leaf, red nodes must not be adjacent.)
        (however any number of black nodes may appear in a sequence.)
    4. every simple path from a node to a descendant leaf contains the same number of black nodes.

the number of black nodes on any path from, but not including, a node x to a leaf is called the black height of a node, denoted bh(x). we can prove the following lemma:
lemma:
    a red black tree with n internal nodes has height at most 2log(n+1).
    this demonstrates why red-black BSTs are good, they can always be searched in O(logn) time.

as with heaps, additions and deletions from red-black trees destroy the red black property, so it needs to be restored.
to achieve this, we observe the followeing operations on red-black trees.

Rotations:
    a rotation is a local operation in a search tree that preserves in order traversal key ordering.

        y     ->    x
      /   \       /   \
     x     c     a     y
   /   \             /   \
  a     b           b     c

    Note that in both trees, an inorder traversal yields a,x,b,y,c

left rotate code:
left_rotate( Tree T, node x ) {
    node y;
    y = x->right;
    /* Turn y's left sub-tree into x's right sub-tree */
    x->right = y->left;
    if ( y->left != NULL )
        y->left->parent = x;
    /* y's new parent was x's parent */
    y->parent = x->parent;
    /* Set the parent to point to y instead of x */
    /* First see whether we're at the root */
    if ( x->parent == NULL ) T->root = y;
    else
        if ( x == (x->parent)->left )
            /* x was on the left of its parent */
            x->parent->left = y;
        else
            /* x must have been on the right */
            x->parent->right = y;
    /* Finally, put x on y's left */
    y->left = x;
    x->parent = y;
    }
    