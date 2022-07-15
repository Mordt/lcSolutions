notes on the Trie data structure

Intro
  tries are an efficient data retrieval data structure.
  search complexities can be brought down to optimal time (key length) with tries.
  
  a well balanced BST will allow you to search for values in O(M*logn) time, where M is the length of the key.
  in contrast, a trie can search for the key in O(M) time. The tradeoff comes in terms of space.

structure
  every trie node consists of a set of multiple branches alongside a boolean end of word key.
  the key isendofword is used to distinguish the last node in a trie node.
  an english alphabet node appears as follows

  """
  struct TrieNode 
  { 
      struct TrieNode *children[ALPHABET_SIZE];
       // isEndOfWord is true if the node 
       // represents end of a word 
       bool isEndOfWord; 
  }; 
  """

inserting a key
  every character of the input key is treated as an individual trie node. children is an array of pointers
  to next level trie nodes.
  the key character acts as an index to the array children. If the input key is new or an extension of an existing key
  we need to construct the non-existing nodes of the existing key, and mark the end of the word for the last node.  
