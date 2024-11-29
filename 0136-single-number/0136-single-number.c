int singleNumber(int* nums, uint16_t numsSize){
    int16_t res = nums[0];
    while(--numsSize) {res ^= nums[numsSize];}
    return res;
}