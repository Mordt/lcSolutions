int level = 0;
Queue<Node> queue = new LinkedList<>();
queue.add(root);
while(!queue.isEmpty()){
    int level_size = queue.size();
    while (level_size-- != 0) {
        Node temp = queue.poll();
        if (temp.right != null) queue.add(temp.right);
        if (temp.left != null) queue.add(temp.left);
    }    
    level++;
}