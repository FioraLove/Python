### 代理池设计原理：
 
 1. 代理池存放在json数据集中，格式为：
 ```json
 {
  "https": ["https://113.226.18.243:80",
        "https://175.11.214.29:808",
        "https://118.190.145.138:9001",
        "https://182.112.89.23:8118"],
  "http": []
}
 ```
 
2. 读取json数据，利用random函数，随机从IP数组里选择一个值，利用访问http://icanhazip.com/ 返回的IP进行测试，推荐使用
 
说明：利用的http://icanhazip.com/ 返回的IP进行校验，如返回的是代理池的IP，说明代理有效，否则实际代理无效

3. 如果两个IP对比相同，就直接读取的json数组再次保存在json文件中；如果对比不相同，则利用数组的remove(value)函数，移除掉无效IP代理，一直迭代对比下去

4. 最后将经过迭代后的IP数组保存在json文件中

