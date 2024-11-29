#include <stdlib.h>
#include <string.h>

// Function to find k most frequent elements
int* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {
    int maxVal = 10000;  // Maximum absolute value for nums[i]
    
    // Step 1: Count frequencies using a fixed array for range [-10000, 10000]
    int* count = (int*)calloc(2 * maxVal + 1, sizeof(int));

    // Count the frequency of each element in nums
    for (int i = 0; i < numsSize; i++) {
        count[nums[i] + maxVal]++;  // Shift nums[i] by maxVal to handle negatives
    }

    // Step 2: Create buckets where index represents frequency
    // Allocate array of lists of elements based on frequency
    int** buckets = (int**)calloc(numsSize + 1, sizeof(int*));
    int* bucketSizes = (int*)calloc(numsSize + 1, sizeof(int));

    // Step 3: Track the number of unique elements and group them by frequency
    for (int i = 0; i < 2 * maxVal + 1; i++) {
        if (count[i] > 0) {
            int freq = count[i];
            bucketSizes[freq]++;
        }
    }

    // Allocate memory for each bucket based on the frequency counts
    for (int i = 1; i <= numsSize; i++) {
        if (bucketSizes[i] > 0) {
            buckets[i] = (int*)malloc(bucketSizes[i] * sizeof(int));
        }
    }

    // Fill the buckets with elements based on their frequencies
    int* currentIndex = (int*)calloc(numsSize + 1, sizeof(int));  // Track current index for each bucket
    for (int i = 0; i < 2 * maxVal + 1; i++) {
        if (count[i] > 0) {
            int freq = count[i];
            buckets[freq][currentIndex[freq]++] = i - maxVal;  // Store the element in the appropriate bucket
        }
    }

    // Step 4: Collect the top k elements by iterating from the highest frequency bucket
    int* result = (int*)malloc(k * sizeof(int));
    int idx = 0;

    for (int i = numsSize; i > 0 && idx < k; i--) {
        if (bucketSizes[i] > 0) {
            for (int j = 0; j < bucketSizes[i] && idx < k; j++) {
                result[idx++] = buckets[i][j];  // Add the most frequent elements
            }
        }
    }

    // Set the return size
    *returnSize = k;

    // Free allocated memory
    free(count);
    for (int i = 1; i <= numsSize; i++) {
        if (bucketSizes[i] > 0) {
            free(buckets[i]);
        }
    }
    free(buckets);
    free(bucketSizes);
    free(currentIndex);

    return result;
}
