/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *twoSum(int *nums, int numsSize, int target)
{

    int *returnedBoi = malloc(2 * sizeof(int));
    if (returnedBoi == NULL)
    {
        printf("Error allocating memory!\n"); // print an error message
        return 1;                             // return with failure
    }

    for (int i = 0; i < numsSize; i++)
    {
        for (int j = 0; j < numsSize; j++)
        {
            if (i == j)
            {
                continue;
            }
            else if ((nums[i] + nums[j]) == target)
            {
                returnedBoi[0] = i;
                returnedBoi[1] = j;
                // to exit loops:
                j = numsSize;
                i = numsSize;
            }
        }
    }
    return returnedBoi;
}