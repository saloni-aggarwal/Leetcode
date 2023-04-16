/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        List<ListNode> val = new ArrayList<>();
        while(head != null) {
            if(val.contains(head)) {
                return true;
            } 
            val.add(head);
            head = head.next;
        }
        return false;
    }
}