import { ListNode } from ".";

 
export function deleteDuplicates(head: ListNode | null): ListNode | null {
    if(head) {
        if(head.val === head.next?.val) {
            head.next = head.next.next;
            deleteDuplicates(head)
        } else{
            deleteDuplicates(head.next)
        }
    }
    return head;
};

export function isEqual(l1: ListNode | null, l2: ListNode | null): boolean{
    if(l1 && l2) {
        if(l1.val != l2.val) {
            return false;
        }
        return isEqual(l1.next, l2.next)
    }
    if(l1 === null && l2 === null) return true
    return false;
}