#Resolved
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}  # Treat emails as nodes in a graph and track the root for every email, belonging to a connected component
        email_name = {}  # Track the name every email is connected to

        def find(email):
            while email != parent[email]:
                parent[email] = parent[parent[email]]
                email = parent[email]
            return email

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                parent[root_b] = root_a

        for obj in accounts:
            name = obj[0]
            emails = obj[1:]

            for e in emails:
                if e not in parent:
                    parent[e] = e
                email_name[e] = name

            root = emails[0]
            for e in emails[1:]:
                union(root, e)

        # Group connected emails
        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)

        res = []
        for root, emails in groups.items():
            # Assemble each name with its respective emails
            entry = [email_name[root]] + sorted(emails)

            res.append(entry)
        return res