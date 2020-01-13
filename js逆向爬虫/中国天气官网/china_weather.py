def get_pwd():
    with open('china_weather.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    # 编译js函数
    ctx = execjs.compile(js_code)
    # 执行js中的getPassword函数，参数为password
    result = ctx.call('getPwd', 'a123456')
    return result
print(get_pwd())    
