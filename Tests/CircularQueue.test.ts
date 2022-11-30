import { MyCircularQueue } from "../System Design/CircularQueue";

describe('CircularQueue', () => {
    let k: number;
    let value: number;
    test('Stack', () => {
        let myCircularQueue = new MyCircularQueue(3);
        expect(myCircularQueue.enQueue(1)).toBe(true); // return True
        myCircularQueue.enQueue(2); // return True
        myCircularQueue.enQueue(3); // return True
        myCircularQueue.enQueue(4); // return False
        myCircularQueue.Rear();     // return 3
        myCircularQueue.isFull();   // return True
        myCircularQueue.deQueue();  // return True
        myCircularQueue.enQueue(4); // return True
        myCircularQueue.Rear();     // return 4
    });
    test('enQueue', () => {
        let myCircularQueue = new MyCircularQueue(3);
        expect(myCircularQueue.enQueue(2)).toBe(true);
        expect(myCircularQueue.Front()).toBe(2);
        expect(myCircularQueue.length).toBe(1);
        expect(myCircularQueue.enQueue(3)).toBe(true);
        expect(myCircularQueue.length).toBe(2);
        myCircularQueue.enQueue(4)
        expect(myCircularQueue.Link()).toStrictEqual([2,4]);
    });
    test('deQueue', () => {
        let myCircularQueue = new MyCircularQueue(3);
        myCircularQueue.enQueue(2)
        myCircularQueue.enQueue(3)
        myCircularQueue.enQueue(4)
        expect(myCircularQueue.isFull()).toBe(true);
        myCircularQueue.deQueue()
        expect(myCircularQueue.isFull()).toBe(false);
        expect(myCircularQueue.Rear()).toBe(3)
        
    });
    test('Front', () => {
        let myCircularQueue = new MyCircularQueue(3);
        expect(myCircularQueue.Front()).toBe(-1);
        expect(myCircularQueue.enQueue(3)).toBe(true);
        expect(myCircularQueue.Front()).toBe(3);
    });
    test('Rear', () => {
        let myCircularQueue = new MyCircularQueue(3);
        expect(myCircularQueue.Rear()).toBe(-1);
        expect(myCircularQueue.enQueue(3)).toBe(true);
        expect(myCircularQueue.Rear()).toBe(3);
        myCircularQueue.enQueue(4)
        expect(myCircularQueue.Rear()).toBe(3);
    });
    test('isEmpty', () => {
        let myCircularQueue = new MyCircularQueue(3);
        expect(myCircularQueue.isEmpty()).toBe(true);
        myCircularQueue.enQueue(4);
        expect(myCircularQueue.isEmpty()).toBe(false);
    });
    test('isFull', () => {
        let myCircularQueue = new MyCircularQueue(3);
        expect(myCircularQueue.isFull()).toBe(false);
        myCircularQueue.enQueue(4);
        myCircularQueue.enQueue(4);
        myCircularQueue.enQueue(4);
        expect(myCircularQueue.isFull()).toBe(true);
    });
});