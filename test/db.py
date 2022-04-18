import json 
class MysqlDatabases:
    def __init__(self):
        with open('users.json',mode='r',encoding='utf-8') as f:
            text=f.read()
        self.users=json.loads(text)

             
       
    def check_login(self,username,password):
        for user in self.users:
            if username==user['username']:
                if password==user["password"]:
                    return True,'登陆成功'
                else:
                    return False ,'登陆失败，密码不存在'
        
        return False ,'登陆失败，用户不存在'
db=MysqlDatabases()
if __name__ == "__main__":
    print(db.check_login('admin','123456'))