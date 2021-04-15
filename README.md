# ExecutorCommon

## Executor

任务执行者，对具体的框架进行抽象，实现以下功能：

* 统一的接口，使得开发者可以直接配置网络端口、读写数据，保证代码符合规定，而不出现自己写读取文件代码（`pd.read_csv("...")`）以及初始化端口等出现权限错误。
* 对具体框架的运行流程进行切分

变量

- comm：通讯模块
- stage_manager：
- ops：字典，表明可以调用的操作

### StageManager

实现以下功能：

* 远程的executor之间互相同步
* 通过GRPC接口供本地查询当前Executor状态

GRPC接口：

* GetStatus：获取当前状态（未开始=0，运行中=1，完成=2，错误=3，准备退出=4）
* GetStage：获取当前任务阶段，用于Executor之间同步
* CallExit：当任务完成后，Executor等待该指令；接收到该指令之后再退出。

## 配置文件config.json

```python
{
  "self_id": "abc",
  # 字符串，表示当前Executor的id

  "addr_dict": {
    "abc": "127.0.0.1:8001/8002",
    "def": "127.0.0.1:8003/8004",
    "ghi": "127.0.0.1:8005/8006"
  },
  # 参与计算环节的其他Executor的ID-地址映射，其中第1个端口是Executor自身通讯使用，第2个端口则是具体调用的程序所需的接口（比如Crypten自身接口）
    

  "input_data": [],
  "output_data": [],
  # 输入，输出文件的路径

  "executor": "base",
  # 调用哪个Executor的实例（如 Crypten，PS3I）

  "before_exec": ["hello"],
  "after_exec": ["hello"],
  # 运行脚本代码之前和之后需要执行的操作
  
  "extra_paras": {
    "learning_rate": 0.01
  }
  # 其他可能需要的参数
}
```

