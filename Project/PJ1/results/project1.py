"""
Math 590
Project 1
Fall 2018

Partner 1: Yifan Li
Partner 2: Haohong Zhao
Date: 10/29/18
"""

# Import time, random, plotting, stats, and numpy.
import time
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy

"""
SelectionSort

This function will take in an array, and return the sorted array using 
selection sort algorithm.

INPUT
A: the original unsorted list

OUTPUT
returns the sorted list of A
"""
def SelectionSort(A):
    for i in range(len(A)): # Loop through the list
        currMin = A[i]
        minIndex = i
        for j in range(i+1, len(A)):
            # Search the unsorted component for the minimum unsorted element
            if A[j] < currMin:
                currMin = A[j]
                minIndex = j
        # Place the minimum unsorted element at the end of sorted list
        A[i], A[minIndex] = A[minIndex], A[i]
            
    return A

"""
InsertionSort

This function will take in an array, and return the sorted array using 
insertion sort algorithm.

INPUT
A: the original unsorted list

OUTPUT
returns the sorted list of A
"""
def InsertionSort(A):
    for i in range(len(A)): # Loop through the unsorted list
        for j in range(0, i): # Loop through the sorted component
            if A[i] < A[j]: # Insert the new element into sorted component
                A.insert(j, A[i])
                del A[i+1]
                break
            
    return A

"""
BubbleSort

This function will take in an array, and return the sorted array using 
bubble sort algorithm.

INPUT
A: the original unsorted list

OUTPUT
returns the sorted list of A
"""
def BubbleSort(A):
    for i in range(len(A)): # Loop through the unsorted list
        n = len(A) - i - 1 # Calculate the number of comparisons needed
        for j in range(n): # Swap adjacent elements if they are out of order
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
        
    return A
# PARTIALLY WRONG! NO FLAG USED TO INDICATE. USE A WHILE LOOP AS OUTER LOOP
"""
MergeSort

This function will take in an array, and return the sorted array using 
merge sort algorithm.

INPUT
A: the original unsorted list

OUTPUT
returns the sorted list of A
"""
def MergeSort(A):
    # Base cases
    if len(A) == 1:
        return A
    elif len(A) == 2:
        if A[0] > A[1]:
            return [A[1], A[0]]
        else:
            return A
    # Divide & Conquer (recursion)
    else:
        L = MergeSort(A[0:len(A)//2])
        R = MergeSort(A[len(A)//2:])
        mergedA = []
        i = 0
        j = 0
        # Merge sorted halves
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                mergedA.append(L[i])
                i += 1
            else:
                mergedA.append(R[j])
                j += 1
        if i >= len(L):
            for index in range(j, len(R)):
                mergedA.append(R[index])
        else:
            for index in range(i, len(L)):
                mergedA.append(L[index])
        
        # NOTE: Used to fix the issue introduced by the testing code
        for index in range(len(mergedA)):
            A[index] = mergedA[index]
        
        return A
                

"""
QuickSort

Sort a list A with the call QuickSort(A, 0, len(A)).

INPUT
A: the original unsorted list
i, j: required indices

OUTPUT
returns the sorted list of A
"""
def QuickSort(A, i, j):
    # Base case
    if i >= j-1:
        return A
    # Choose the last element in the array as the pivot
    pivot = A[j-1]
    pivotIndex = j-1
    
    left = i
    right = j-2 #rightmost index is j-2 since A[j-1] is used as pivot
    while left < right: # Loop through the list to find elements for swap
        # Try to find an element larger than pivot on the left side
        while A[left] < pivot and left < right:  
            left += 1 
        # Try to find an element smaller than pivot on the right side
        while A[right] >= pivot and left < right:
            right -= 1
        A[left], A[right] = A[right], A[left] # Swap these two elements
        
    if A[left] >= A[pivotIndex]: # Pivot chosen is the minimum value in array
        A[left], A[pivotIndex] = A[pivotIndex], A[left]
    else: # Pivot chosen is the maximum value in array
        left += 1
        
    # Recursion
    QuickSort(A, i, left)
    QuickSort(A, left+1, j)
    
    return A

"""
isSorted

This function will take in an original unsorted list and a sorted version of
that same list, and return whether the list has been properly sorted.

Note that this function does not change the unsorted list.

INPUTS
unA: the original unsorted list
sA:  the supposedly sorted list

OUTPUTS
returns true or false
"""
def isSorted(unA, sA):
    # Copy the unsorted list.
    temp = unA.copy()
    
    # Use python's sort.
    temp.sort()

    # Check equality.
    return temp == sA

"""
testingSuite

This function will run a number of tests using the input algorithm, check if
the sorting was successful, and print which tests failed (if any).

This is not an exhaustive list of tests by any means, but covers the edge
cases for your sorting algorithms.

INPUTS
alg: a string indicating which alg to test, the options are:
    'SelectionSort'
    'InsertionSort'
    'BubbleSort'
    'MergeSort'
    'QuickSort'

OUTPUTS
Printed statements indicating which tests passed/failed.
"""
def testingSuite(alg):
    # First, we seed the random number generator to ensure reproducibility.
    random.seed(1)

    # List of possible algs.
    algs = ['SelectionSort', 'InsertionSort', \
            'BubbleSort', 'MergeSort', 'QuickSort']

    # Make sure the input is a proper alg to consider.
    if not alg in algs:
        raise Exception('Not an allowed algorithm. Value was: {}'.format(alg))
    
    # Create a list to store all the tests.
    tests = []

    # Create a list to store the test names.
    message = []

    # Test 1: singleton array
    tests.append([1])
    message.append('singleton array')

    # Test 2: repeated elements
    tests.append([1,2,3,4,5,5,4,3,2,1])
    message.append('repeated elements')

    # Test 3: all repeated elements
    tests.append([2,2,2,2,2,2,2,2,2,2])
    message.append('all repeated elements')

    # Test 4: descending order
    tests.append([10,9,8,7,6,5,4,3,2,1])
    message.append('descending order')

    # Test 5: sorted input
    tests.append([1,2,3,4,5,6,7,8,9,10])
    message.append('sorted input')

    # Test 6: negative inputs
    tests.append([-1,-2,-3,-4,-5,-5,-4,-3,-2,-1])
    message.append('negative inputs')

    # Test 7: mixed positive/negative
    tests.append([1,2,3,4,5,-1,-2,-3,-4,-5,0])
    message.append('mixed positive/negative')

    # Test 8: array of size 2^k - 1
    temp = list(range(0,2**6-1))
    random.shuffle(temp)
    tests.append(temp)
    message.append('array of size 2^k - 1')

    # Test 9: random real numbers
    tests.append([random.random() for x in range(0,2**6-1)])
    message.append('random real numbers')

    # Store total number of passed tests.
    passed = 0

    # Loop over the tests.
    for tInd in range(0,len(tests)):
        # Copy the test for sorting.
        temp = tests[tInd].copy()

        # Try to sort, but allow for errors.
        try:
            # Do the sort.
            eval('%s(tests[tInd])' % alg) if alg != 'QuickSort' \
            else eval('%s(tests[tInd],0,len(tests[tInd]))' % alg)
            
            # Check if the test succeeded.
            if isSorted(temp, tests[tInd]):
                print('Test %d Success: %s' % (tInd+1, message[tInd]))
                passed += 1
            else:
                print('Test %d FAILED: %s' % (tInd+1, message[tInd]))

        # Catch any errors.
        except Exception as e:
            print('')
            print('DANGER!')
            print('Test %d threw an error: %s' % (tInd+1, message[tInd]))
            print('Error: ')
            print(e)
            print('')

    # Done testing, print and return.
    print('')
    print('%d/9 Tests Passed' % passed)
    return

"""
measureTime

This function will generate lists of varying lengths and sort them using your
implemented fuctions. It will time these sorting operations, and store the
average time across 30 trials of a particular size n. It will then create plots
of runtime vs n. It will also output the slope of the log-log plots generated
for several of the sorting algorithms.

INPUTS
sortedFlag: set to True to test with only pre-sorted inputs
    (default = False)
numTrials: the number of trials to average timing data across
    (default = 30)

OUTPUTS
A number of genereated runtime vs n plot, a log-log plot for several
algorithms, and printed statistics about the slope of the log-log plots.
"""
def measureTime(sortedFlag = False, numTrials = 30):
    # Print whether we are using sorted inputs.
    if sortedFlag:
        print('Timing algorithms using only sorted data.')
    else:
        print('Timing algorithms using random data.')
    print('')
    print('Averaging over %d Trials' % numTrials)
    print('')
    
    # First, we seed the random number generator to ensure consistency.
    random.seed(1)

    # We now define the range of n values to consider.
    if sortedFlag:
        # Need to look at larger n to get a good sense of runtime.
        # Look at n from 20 to 980.
        # Note that 1000 causes issues with recursion depth...
        N = list(range(1,50))
        N = [20*x for x in N]
    else:
        # Look at n from 10 to 500.
        N = list(range(1,51))
        N = [10*x for x in N]

    # Store the different algs to consider.
    algs = ['SelectionSort', 'InsertionSort', \
            'BubbleSort', 'MergeSort', \
            'QuickSort', 'list.sort']

    # Preallocate space to store the runtimes.
    tSelectionSort = N.copy()
    tInsertionSort = N.copy()
    tBubbleSort = N.copy()
    tMergeSort = N.copy()
    tQuickSort = N.copy()
    tPython = N.copy()

    # Create some flags for whether each sorting alg works.
    correctFlag = [True, True, True, True, True, True]

    # Loop over the different sizes.
    for nInd in range(0,len(N)):
        # Get the current value of n to consider.
        n = N[nInd]
        
        # Reset the running sum of the runtimes.
        timing = [0,0,0,0,0,0]
        
        # Loop over the 30 tests.
        for test in range(1,numTrials+1):
            # Create the random list of size n to sort.
            A = list(range(0,n))
            A = [random.random() for x in A]

            if sortedFlag:
                # Pre-sort the list.
                A.sort()

            # Loop over the algs.
            for aI in range(0,len(algs)):
                # Grab the name of the alg.
                alg = algs[aI]

                # Copy the original list for sorting.
                B = A.copy()
                
                # Time the sort.
                t = time.time()
                eval('%s(B)' % alg) if aI!=4 else eval('%s(B,0,len(B))' % alg)
                t = time.time() - t

                # Ensure that your function sorted the list.
                if not isSorted(A,B):
                    correctFlag[aI] = False

                # Add the time to our running sum.
                timing[aI] += t

        # Now that we have completed the numTrials tests, average the times.
        timing = [x/numTrials for x in timing]

        # Store the times for this value of n.
        tSelectionSort[nInd] = timing[0]
        tInsertionSort[nInd] = timing[1]
        tBubbleSort[nInd] = timing[2]
        tMergeSort[nInd] = timing[3]
        tQuickSort[nInd] = timing[4]
        tPython[nInd] = timing[5]

    # If there was an error in one of the plotting algs, report it.
    for aI in range(0,len(algs)-1):
        if not correctFlag[aI]:
            print('%s not implemented properly!!!' % algs[aI])
            print('')

    # Now plot the timing data.
    for aI in range(0,len(algs)):
        # Get the alg.
        alg = algs[aI] if aI != 5 else 'Python'

        # Plot.
        plt.figure()
        eval('plt.plot(N,t%s)' % alg)
        plt.title('%s runtime versus n' % alg)
        plt.xlabel('Input Size n')
        plt.ylabel('Runtime (s)')
        if sortedFlag:
            plt.savefig('%s_sorted.png' % alg, bbox_inches='tight')
        else:
            plt.savefig('%s.png' % alg, bbox_inches='tight')

    # Plot them all together.
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(N,tSelectionSort, label='Selection')
    ax.plot(N,tInsertionSort, label='Insertion')
    ax.plot(N,tBubbleSort, label='Bubble')
    ax.plot(N,tMergeSort, label='Merge')
    ax.plot(N,tQuickSort, label='Quick')
    ax.plot(N,tPython, label='Python')
    legend = ax.legend(loc='upper left')
    plt.title('All sorting runtimes versus n')
    plt.xlabel('Input Size n')
    plt.ylabel('Runtime (s)')
    if sortedFlag:
        plt.savefig('sorting_sorted.png', bbox_inches='tight')
    else:
        plt.savefig('sorting.png', bbox_inches='tight')

    # Now look at the log of the sort times.
    logN = [(numpy.log(x) if x>0 else -6) for x in N]
    logSS = [(numpy.log(x) if x>0 else -6) for x in tSelectionSort]
    logIS = [(numpy.log(x) if x>0 else -6) for x in tInsertionSort]
    logBS = [(numpy.log(x) if x>0 else -6) for x in tBubbleSort]
    logMS = [(numpy.log(x) if x>0 else -6) for x in tMergeSort]
    logQS = [(numpy.log(x) if x>0 else -6) for x in tQuickSort]

    # Linear regression.
    mSS, _, _, _, _ = stats.linregress(logN,logSS)
    mIS, _, _, _, _ = stats.linregress(logN,logIS)
    mBS, _, _, _, _ = stats.linregress(logN,logBS)

    # Plot log-log figure.
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(logN,logSS, label='Selection')
    ax.plot(logN,logIS, label='Insertion')
    ax.plot(logN,logBS, label='Bubble')
    legend = ax.legend(loc='upper left')
    plt.title('Log-Log plot of runtimes versus n')
    plt.xlabel('log(n)')
    plt.ylabel('log(runtime)')
    if sortedFlag:
        plt.savefig('log_sorted.png', bbox_inches='tight')
    else:
        plt.savefig('log.png', bbox_inches='tight')

    # Print the regression info.
    print('Selection Sort log-log Slope (all n): %f' % mSS)
    print('Insertion Sort log-log Slope (all n): %f' % mIS)
    print('Bubble Sort log-log Slope (all n): %f' % mBS)
    print('')

    # Now strip off all n<200...
    logN = logN[19:]
    logSS = logSS[19:]
    logIS = logIS[19:]
    logBS = logBS[19:]
    logMS = logMS[19:]
    logQS = logQS[19:]

    # Linear regression.
    mSS, _, _, _, _ = stats.linregress(logN,logSS)
    mIS, _, _, _, _ = stats.linregress(logN,logIS)
    mBS, _, _, _, _ = stats.linregress(logN,logBS)
    mMS, _, _, _, _ = stats.linregress(logN,logMS)
    mQS, _, _, _, _ = stats.linregress(logN,logQS)

    # Print the regression info.
    print('Selection Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mSS))
    print('Insertion Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mIS))
    print('Bubble Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mBS))
    print('Merge Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mMS))
    print('Quick Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mQS))

    # Close all figures.
    plt.close('all')
