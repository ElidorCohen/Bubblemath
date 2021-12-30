class ProfilePage():

    def __init__(self, name, institute, advisor, user_points, userrank_in_inst, listofUsers, inst_points, inst_rank):
        self.name = name
        self.institute = institute
        self.advisor = advisor
        self.user_points = user_points
        self.listofUsers = listofUsers
        self.inst_points = inst_points
        self.inst_rank = inst_rank
        self.userrank_in_inst = userrank_in_inst


    def get_data(self):
        print(self.name)
        print(self.institute)
        print(self.advisor)
        print(self.user_points)
        print(self.userrank_in_inst)
        print(self.inst_points)
        print(self.inst_rank)
        print(self.listofUsers)