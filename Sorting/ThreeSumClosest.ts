export function threeSumClosest(nums: number[], target: number): number {
    let twoSum = new Map<number, Set<number[]>>();
    let smDelta;
    for(let i = 0; i < nums.length; i++) {
        for(let j = 0; j < nums.length; j++) {
            if(i != j) {
                const sum = nums[i]+nums[j];
                if(twoSum.has(sum)) {
                    twoSum.get(sum)?.add([i, j])
                } else {
                    let set = new Set<number[]>();
                    set.add([i, j]);
                    twoSum.set(sum, set);
                }
            }
        }
    }

    let sorted = Array.from(twoSum.keys());
    sorted.sort();
    
    for(let k = 0; k < nums.length; k++) {
        for(let l = 0; l < sorted.length; l++) {
            if(k twoSum.get())
        }
    }

    // find twosum
    return nums[0]+target
};