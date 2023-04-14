/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if(node == null)
            return node;
        Node newNode = new Node(node.val);
        Map<Node, Node> vis = new HashMap<>();
        LinkedList<Node> queue = new LinkedList<>();
        queue.add(node);
        vis.put(node, newNode);
        while(!queue.isEmpty()) {
            Node temp = queue.remove();
            for(Node neighbor: temp.neighbors) {
                if(!vis.containsKey(neighbor)) {
                    vis.put(neighbor, new Node(neighbor.val));
                    queue.add(neighbor);
                }
                vis.get(temp).neighbors.add(vis.get(neighbor));
            }
            
            
        }
        return newNode;
    }
}