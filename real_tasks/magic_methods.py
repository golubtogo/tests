class Version:
    def __init__(self, major=0, minor=0, patch=0):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    def __gt__(self, other):
        if self.major > other.major:
            return True
        elif self.major < other.major:
            return False
        else:
            if self.minor > other.minor:
                return True
            elif self.minor < other.minor:
                return False
            else:
                if self.patch > other.patch:
                    return True
                else:
                    return False

    def __lt__(self, other):
        if self.major < other.major:
            return True
        elif self.major > other.major:
            return False
        else:
            if self.minor < other.minor:
                return True
            elif self.minor > other.minor:
                return False
            else:
                if self.patch < other.patch:
                    return True
                else:
                    return False

    def __eq__(self, other):
        return self.major == other.major and self.minor == other.minor and self.patch == other.patch



v101 = Version(1, 0, 1)
v1011 = Version(1, 0, 1)
v121 = Version(1, 2, 1)


print(v101 > v121)
