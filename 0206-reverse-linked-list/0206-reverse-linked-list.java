/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null){
            return head;
        }
        ListNode curr = head, nxt = head.next;
        head.next = null;
        while(nxt != null) {
            ListNode temp = nxt;
            nxt = nxt.next;
            temp.next = curr;
            curr = temp;
        }
        return curr;
        
    }
}