from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        start = None
        litter = {}

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        k = len(litter)
        target = (1 << k) - 1

        if target == 0:
            return 0

        q = deque([(start[0], start[1], 0, energy)])
        
        # Track max energy seen for each (r, c, mask)
        visited = {(start[0], start[1], 0): energy}

        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            moves += 1
            for _ in range(len(q)):
                r, c, mask, curr_energy = q.popleft()

                if curr_energy == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n) or classroom[nr][nc] == 'X':
                        continue

                    new_energy = curr_energy - 1
                    new_mask = mask

                    if classroom[nr][nc] == 'L':
                        idx = litter[(nr, nc)]
                        new_mask |= (1 << idx)

                    if new_mask == target:
                        return moves

                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    if new_energy == 0:
                        continue

                    key = (nr, nc, new_mask)
                    # Only add/prune if we found a strictly better (higher) energy level
                    if key not in visited or new_energy > visited[key]:
                        visited[key] = new_energy
                        q.append((nr, nc, new_mask, new_energy))

        return -1