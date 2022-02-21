/*
 * CS7280 Special Topics in Database Management
 * Project 1: B-tree implementation.
 *
 * You need to code for the following functions in this program
 *   1. Lookup(int value) -> nodeLookup(int value, int node)
 *   2. Insert(int value) -> nodeInsert(int value, int node)
 *   3. Display(int node)
 *
 */

import java.util.Arrays;

final class Btree {

    /* Size of Node. */
    private static final int NODESIZE = 5;

    /* Node array, initialized with length = 1. i.e. root node */
    private Node[] nodes = new Node[1];

    /* Number of currently used nodes. */
    private int cntNodes;

    /* Pointer to the root node. */
    private int root;

    /* Number of currently used values. */
    private int cntValues;

    /*
     * B+ tree Constructor.
     */
    public Btree() {
        root = initNode();
        nodes[root].children[0] = createLeaf();
    }

    /*********** B tree functions for Public ******************/

    /*
     * Lookup(int value)
     *   - True if the value was found.
     */
    public boolean Lookup(int value) {
        return nodeLookup(value, root);
    }

    /*
     * Insert(int value)
     *    - If -1 is returned, the value is inserted and increase cntValues.
     *    - If -2 is returned, the value already exists.
     */
    public void Insert(int value) {
        if(nodeInsert(value, root) == -1) cntValues++;
    }


    /*
     * CntValues()
     *    - Returns the number of used values.
     */
    public int cntValues() {
        return cntValues;
    }

    /*********** B-tree functions for Internal  ******************/

    /*
     * nodeLookup(int value, int pointer)
     *    - True if the value was found in the specified node.
     *
     */
    private boolean nodeLookup(int value, int pointer) {
        //
        //
        // To be coded .................
        //
        //
        if (isLeaf(nodes[pointer])) {
            for (int i : nodes[pointer].values) {
                if (i == value) return true;
            }
        } else {
            for (int i = 0; i < 5; i++) {
                if (nodes[pointer].values[i] >= value) {
                    return nodeLookup(value, nodes[pointer].children[i]);
                }
            }
            return nodeLookup(value, nodes[pointer].children[5]);
        }

        return false;
    }

    /*
     * nodeInsert(int value, int pointer)
     *    - -2 if the value already exists in the specified node
     *    - -1 if the value is inserted into the node or
     *            something else if the parent node has to be restructured
     */
    private int nodeInsert(int value, int pointer) {
        //
        //
        // To be coded .................
        //
        //
        if (isLeaf(nodes[pointer])) {
            for (int i : nodes[pointer].values) {
                if (i == value) return -2;
            }

            for (int i = 0; i < nodes[pointer].values.length; i++) {
                if (nodes[pointer].values[i] == 0) {
                    nodes[pointer].values[i] = value;
                    Arrays.sort(nodes[pointer].values);
                    return -1;
                }
            }


        } else {
            for (int i = 0; i < 5; i++) {
                if (nodes[pointer].values[i] > value) {
                    int child = nodeInsert(value, nodes[pointer].children[i]);

                    if (child == -2 || child == -1) return value;
                    //else if ()
                }
            }
        }
        return value;
    }


    /*********** Functions for accessing node  ******************/

    /*
     * isLeaf(Node node)
     *    - True if the specified node is a leaf node.
     *         (Leaf node -> a missing children)
     */
    boolean isLeaf(Node node) {
        return node.children == null;
    }

    /*
     * initNode(): Initialize a new node and returns the pointer.
     *    - return node pointer
     */
    int initNode() {
        Node node = new Node();
        node.values = new int[NODESIZE];
        node.children =  new int[NODESIZE + 1];

        checkSize();
        nodes[cntNodes] = node;
        return cntNodes++;
    }

    /*
     * createLeaf(): Creates a new leaf node and returns the pointer.
     *    - return node pointer
     */
    int createLeaf() {
        Node node = new Node();
        node.values = new int[NODESIZE];

        checkSize();
        nodes[cntNodes] = node;
        return cntNodes++;
    }

    /*
     * checkSize(): Resizes the node array if necessary.
     */
    private void checkSize() {
        if(cntNodes == nodes.length) {
            Node[] tmp = new Node[cntNodes << 1];
            System.arraycopy(nodes, 0, tmp, 0, cntNodes);
            nodes = tmp;
        }
    }
}

/*
 * Node data structure.
 *   - This is the simplest structure for nodes used in B-tree
 *   - This will be used for both internal and leaf nodes.
 */
final class Node {
    /* Node Values (Leaf Values / Key Values for the children nodes).  */
    int[] values;

    /* Node Array, pointing to the children nodes.
     * This array is not initialized for leaf nodes.
     */
    int[] children;

    /* Number of entries
     * (Rule in B Trees:  d <= size <= 2 * d).
     */
    int size;
}
