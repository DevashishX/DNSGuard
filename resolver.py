import dns.resolver

import logging

class Resolver():

    def __init__(self, nameservers = ["1.1.1.1", "8.8.8.8", "8.8.4.4"]):
        self.internalResolver = dns.resolver.Resolver()
        self.internalResolver.nameservers = nameservers
        pass
    
    def resolve(self, toresolve):
        ips = []
        for addr in toresolve:
            ans = self.internalResolver.query(addr, "A")
            for a in ans:
                ips.append([addr, str(a)])
        return ips
        pass

    def resolveZone(self, toresolve):
        zones = []
        for addr in toresolve:
            ans = self.internalResolver.query(addr, "A")
            ans = ans.rrset.to_text()
            zones.append(ans)
        return zones
        # ans = self.internalResolver.query(toresolve, "A")
        # return ans.rrset.to_text()
    pass

if __name__ == "__main__":
    # main()
    pass
