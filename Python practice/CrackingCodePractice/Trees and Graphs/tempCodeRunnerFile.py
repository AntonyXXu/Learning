    def validate(self):
        ptr = self.root
        val = None
        return self._val(ptr, val)
        

    def _val(self, ptr, val):
        if not ptr:
            return True
        if not self._val(ptr.left, val):
            return False
        if val and val > ptr.val:
            return False
        val = ptr.val
        if not self._val(ptr.right, val):
            return False
        return True
