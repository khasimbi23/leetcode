class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        st=[0]
        visited={0}
        while st!=[]:
            r=st.pop()
            for nei in rooms[r]:
                if nei not in visited:
                    visited.add(nei)
                    st.append(nei)
        return len(visited)==len(rooms)
        