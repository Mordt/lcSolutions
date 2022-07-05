Red black trees

why red black trees?
    rb trees are self balancing BSTs due to their "colour" property.
    the rules around whether a node is red or black ensures that after an insertion
    or deletion, the tree remains balanced.

    this means that the tree is always in an optimal shape for searching.
    the time will remain around O(logn).

    these type of trees show identical memory footprint to classic trees.
    normal operations take h time (height of tree). search, insert and delete all become O(logn)
    with a red-black tree.

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

insertion
somewhat complex, involves a number of cases. we start by inserting the new node x in the tree just as we would
for any other bst, using the tree-insert function. the new node is labelled red and may destroy the red-black property.
the main loop moves up the tree, restoring the red-black property.

insertion code

rb_insert( Tree T, node x )
{
    /* Insert in the tree in the usual way */
    tree_insert(T, x);
    /* Now restore the red-black property */
    x->colour = red;
    while ((x != T->root) && (x->parent->colour == red))
    {
        if (x->parent == x->parent->parent->left)
        {
            /* If x's parent is a left, y is x's right 'uncle' */
            y = x->parent->parent->right;
            if (y->colour == red)
            {
                /* case 1 - change the colours */
                x->parent->colour = black;
                y->colour = black;
                x->parent->parent->colour = red;
                /* Move x up the tree */
                x = x->parent->parent;
            }
            else
            {
                /* y is a black node */
                if (x == x->parent->right)
                {
                    /* and x is to the right */
                    /* case 2 - move x up and rotate */
                    x = x->parent;
                    left_rotate(T, x);
                }
                /* case 3 */
                x->parent->colour = black;
                x->parent->parent->colour = red;
                right_rotate(T, x->parent->parent);
            }
        }
        else
        {
            /* repeat the "if" part with right and left
               exchanged */
        }
    }
    /* Colour the root black */
    T->root->colour = black;
}