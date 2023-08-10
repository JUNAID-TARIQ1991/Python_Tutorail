'''Constructor (__init__ method):
The constructor is called when you create an instance of 
the TagCloud class. It initializes the tags attribute as an empty dictionary, 
where the tags and their frequencies will be stored.'''

"""Method add:
The add method is used to add a new tag to the tag cloud or update the frequency of an existing tag. 
It takes the tag as input parameter.

Here's how the add method works:

If the tag is already present in the tags dictionary, it increments the value (frequency) 
of that tag by 1.
If the tag is not present in the tags dictionary, it adds the tag as a new key with a value of 1 
(since it appears for the first time)."""


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        iter(self.tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("Python")
cloud.add("c++")
print(cloud['PYTHON'])
print(cloud.__getitem__('python'))
print(cloud.__len__())
########
print()
