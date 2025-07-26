
class BasicTrackingDict(dict):
    # TODO: Think about how we could track things during iteration,
    # dictionary views seems to complecate this. (returned from .keys, .values, .items)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.accessed_keys = set()
        self.modified_keys = set()

    def __getitem__(self, key):
        self.accessed_keys.add(key)
        return super().__getitem__(key)

    def get(self, key, default=None, /):
        self.accessed_keys.add(key)
        return super().get(key, default)

    def __setitem__(self, key, value):
        self.modified_keys.add(key)
        return super().__setitem__(key, value)

    def update(self, *args, **kwargs):
        kwargs = dict(kwargs)
        if args:
            other = args[0]
            if hasattr(other, "keys"):
                self.modified_keys.update(other.keys())
            else:
                self.modified_keys.update(k for k,_ in other)
            return super().update(other)
        else:
            self.modified_keys.update(kwargs.keys())
            return super().update(**kwargs)
            
    def __ior__(self, other):
        if hasattr(other, "keys"):
            self.modified_keys.update(other.keys())
        else:
            self.modified_keys.update(k for k,_ in other)
        return super().__ior__(other)


