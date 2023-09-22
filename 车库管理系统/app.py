from flask import Flask, render_template, request
from data import car_number_list
'''链表 的数据结构'''


'''car_number 车牌号'''

'''model   型号'''

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def hello_login():
    # 登录到服务器 获取用户名与密码,然后进行校验,再记录信息
    # print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    # 获取用户名与密码,然后进行校验,再记录信息
    # for sal in car_number_list:
    #     if sal['name'] == username:

    # 登录成功之后返回后台页面
    return render_template('admin.html',
                           car_number_list=car_number_list)


@app.route('/delete/<name>')
def hello_delete(name):  # put application's code here
    # 删除逻辑 先找到信息,然后再删除
    for car_number in car_number_list:
        if car_number['name'] == name:
            # 列表删除元素的几种方式
            car_number_list.remove(car_number)
    return render_template('admin.html',
                           car_number_list=car_number_list)


@app.route('/change/<name>')
def hello_change(name):  # put application's code here
    # 删除逻辑 先找到信息,然后再删除
    for car_number in car_number_list:
        if car_number['name'] == name:
            # 应该是在前端进行修改
            return render_template('change.html',
                                   user=car_number)

    return render_template('admin.html',
                           car_number_list=car_number_list)


@app.route('/changed/<name>', methods=["POST"])
def hello_changed(name):
    """修改 拿到提交的信息"""
    # 删除逻辑 先找到信息,然后再删除
    for car_number in car_number_list:
        if car_number['name'] == name:
            car_number['name'] = request.form.get('name')
            car_number['model'] = request.form.get('model')
            car_number['position'] = request.form.get('position')
            car_number['car_number'] = request.form.get('car_number')

    return render_template('admin.html',
                           car_number_list=car_number_list)


@app.route('/add')
def hello_add():
    return render_template('add.html')


@app.route('/add2', methods=['POST'])
def hello_add2():
    car_number = {}
    # 获取浏览器发送过来的数据
    car_number['name'] = request.form.get('name')
    car_number['department'] = request.form.get('department')
    car_number['position'] = request.form.get('position')
    car_number['car_number'] = request.form.get('car_number')
    # 将数据保存
    car_number_list.insert(0, car_number)
    # 返回保存之后的页面
    return render_template('admin.html',
                           car_number_list=car_number_list)


if __name__ == '__main__':
    app.run()
