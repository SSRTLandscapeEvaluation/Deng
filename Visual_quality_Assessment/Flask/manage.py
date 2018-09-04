#time:class15,2:03
from flask_script import Manager ,Server
from laeval_cadesign import app,db
from flask_migrate import Migrate,MigrateCommand
from models import Imageseval,imagesinfodf #导入数据模型

manager = Manager(app)#将app传给Manager对象，初始化Flask Script
migrate = Migrate(app,db)#通过app对象和SQLAlchemy的实例化Migrate对象

manager.add_command("server",Server())

manager.add_command('db',MigrateCommand)#添加数据库迁移命令MigrateCommand，可以直接在Terminal中的python manage.py执行

@manager.shell
def make_shell_context():
    return dict(app=app,db=db, Imageseval=Imageseval,imagesinfodf=imagesinfodf)

if __name__ == "__main__":
    manager.run()
    
