
export class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

export function arrayToLinkedList(list: any[]): ListNode | null {
    let head: ListNode | null = null;
    for(let i=0; i<list.length;i++) {
        head = new ListNode(list[i], head)
    }
    return head;
}

export function arrayToCycle(list: any[], pos: number): ListNode | null {
    let temp: ListNode = new ListNode();
    let head: ListNode | null = new ListNode(list[0]);
    let end: ListNode | null = head;
    for(let i=1; i<list.length;i++) {
        head = new ListNode(list[i], head)
        if(i === pos) {
            temp = head;
        }
    }
    end.next = temp;
    return head;
}
export interface intersection {
    intersectVal : any,
    listA : any[],
    listB : any[],
    skipA : number,
    skipB : number,
    max : number,
}
export function arraysToIntersectedList(intersect: intersection) {
    let headA: ListNode = new ListNode();
    let headB: ListNode = new ListNode();
    let head: ListNode = new ListNode();
    
    let intersectedArr = intersect.listA.slice(intersect.skipA)
    let listA: any[] = intersect.listA.slice(0, intersect.skipA)
    let listB: any[] = intersect.listB.slice(0, intersect.skipB)
    let i: number = intersectedArr.length;
    while(i) {
        head = new ListNode(intersectedArr[i], head);
        i--;
    }
    let a = listA.length;
    let b = listB.length;
    while(true) {
        if(a < )
    }
}