## 学车不平台科目二/三预约训练脚本

现仅支持龙泉驾校的预约训练。

其它驾校的同学，如果也有相应需求，可以留言或通过邮件联系。

### python版本: 3.6

### 使用方法：
```bash
usage: xuechebu.py [-h] [-v] [-u USERNAME] [-p PASSWORD] [-i ID] [-d DAY]
                   [-t TIME]

学车不平台科目二/三预约训练脚本

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show version information

options:
  -u USERNAME    用户名
  -p PASSWORD    密码
  -i ID          教练ID
  -d DAY         预约日期, 例如 1990-1-1
  -t TIME        预约时段, 1代表8:00-12:00, 2代表13:00-17:00, 3代表17:00-20:00
```

### 教练ID的获取：
下图中的教练ID为16073。
![img1](https://github.com/tfrnghub/xuechebu/blob/master/ID.PNG)

### 注意：

参数-d 为可选项，其余为必选项。不选择参数-d 时，预约日期为默认值。

默认的预约日期：下一个将能预约的日期。下图中的默认预约日期为1月26日（2019-01-26）。

![img2](https://github.com/tfrnghub/xuechebu/blob/master/date.PNG)

如有疑问，可以留言讨论，也可以通过邮件联系。邮箱地址为tfrnghub@gmail.com。
