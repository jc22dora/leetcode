"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const ThreeSumClosest_1 = require("../Sorting/ThreeSumClosest");
describe('testing index file', () => {
    let nums;
    let target;
    let expected;
    test('nums = [-1,2,1,-4], target = 1', () => {
        nums = [-1, 2, 1, -4];
        target = 1;
        expected = 2;
        expect((0, ThreeSumClosest_1.threeSumClosest)([1], 2)).toBe(3);
    });
});
