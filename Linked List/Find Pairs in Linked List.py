def findPairs(head: Node, k: int) -> [[int]]:
    start = head
    end = head
    ans = []

    # Traverse the linked list to the end.
    while end.next != None:

        end = end.next

    while start.data < end.data:

        sum = start.data + end.data

        if sum == k:

            ans.append([start.data, end.data])

        if sum < k:

            start = start.next

        else:

            end = end.prev
