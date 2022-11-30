import { threeSumClosest } from '../Sorting/ThreeSumClosest';

describe('testing index file', () => {
    let nums: number[];
    let target: number;
    let expected: number;
  test('nums = [-1,2,1,-4], target = 1', () => {
    nums = [-1,2,1,-4];
    target = 1;
    expected = 2;
    expect(threeSumClosest([1], 2)).toBe(3);
  });
});