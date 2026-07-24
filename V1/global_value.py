class g_val(object):
    global_dict={}
    def set_dict(self,key,value):
        self.global_dict[key] = value
    def get_dict(self,key):
        return self.global_dict[key]

    @classmethod
    def show_dict(cls):
        return cls.global_dict
