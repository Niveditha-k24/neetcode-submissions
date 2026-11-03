class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        l = 0
        r = len(people) - 1
        people.sort()

        while l <= r:
            boats += 1

            if people[l] + people[r] <= limit:
                l += 1
                r-=1
            else:
                r-=1

           

        return boats