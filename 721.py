class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
                # Build graph where emails are connected within same account
        graph = defaultdict(list)
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            # Connect all emails to the first email (or to each other)
            first_email = account[1]
            email_to_name[first_email] = name
            
            for i in range(1, len(account)):
                email = account[i]
                email_to_name[email] = name
                if i > 1:
                    graph[first_email].append(email)
                    graph[email].append(first_email)
        
        visited = set()
        result = []
        
        def dfs(email, component):
            if email in visited:
                return
            visited.add(email)
            component.append(email)
            for neighbor in graph[email]:
                dfs(neighbor, component)
        
        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)
                name = email_to_name[email]
                result.append([name] + sorted(component))
        
        return result
