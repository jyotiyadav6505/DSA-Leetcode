def subsequences(arr, K):
    result = []

    def solve(index, current, total):

        # Base case
        if index == len(arr):
            if total == K:
                result.append(current[:])
            return

        # Take the element
        current.append(arr[index])
        solve(index + 1, current, total + arr[index])

        # Undo
        current.pop()

        # Don't take the element
        solve(index + 1, current, total)

    solve(0, [], 0)

    return result