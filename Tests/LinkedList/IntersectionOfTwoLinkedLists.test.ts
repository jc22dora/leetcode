import { intersection } from "../../LinkedList";

describe('Intersection Of Two Linked Lists', () => {
    test('test', () => {
        let intersectVal = 8
        let listA = [4,1,8,4,5]
        let listB = [5,6,1,8,4,5]
        let skipA = 2
        let skipB = 3
        let max = Math.max(listA.length, listB.length)
        let intersect: intersection = {
            intersectVal: undefined,
            listA: listA,
            listB: listB,
            skipA: 0,
            skipB: 0,
            max: 0
        }
    });
})