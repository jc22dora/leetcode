import { ListNode } from ".";

export function hasCycle(head: ListNode | null): boolean {
    let walker: ListNode | null = head;
    let runner: ListNode | null = head;
    while(runner) {
        if(!runner.next) {
            return false;
        } else {
            walker = walker?.next?? null;
            runner = runner?.next?.next ?? null;
        }
        if(walker === runner) {
            return true;
        }
    }
    return false;
};