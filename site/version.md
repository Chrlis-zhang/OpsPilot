# 2.5

* [Munchkin] Django Unfold 升级为0.33.0

# 2.4

* [Pilot] 优化主动消息触达动作
* [Pilot] 新增 `帮助` 关键词: /help
* [Pilot] 新增 联网检索能力：
  * /online_search - 切换为联网检索模式
  * /exit_online_search - 退出联网检索模式
* [Pilot] 优化 使用虚拟队列区分Pilot的消息总线
* [Pilot] 新增 `查看Jenkins任务列表` 关键词
  * /list_jenkins_jobs: 查看Jenkins任务列表
  * /jenkins_build_log: 查看Jenkins任务日志
  * /analyze_build_log: 分析Jenkins任务日志
  * /build_jenkins_pipeline: 构建Jenkins任务
* [Munchkin] 机器人新增自动化技能模块
* [Munchkin] 新增 知识集成 能力，支持自动化采集WeOps知识
* [OCR Server] 新增Azure OCR支持

# 2.3

* [Classicfy Aiops Server] 新增经典AIOPS算法服务，内置时序预测、异常检查、根因分析、日志聚类算法
* [Bionics] 新增图表生成服务，负责将时间序列指标生成图片
* [Chunk Server] 新增 支持PDF扫描件识别
* [Only Office] 新增 Only Office基础服务

# 2.2

* [基础服务] 新增SaltStack Server
* [基础服务] 新增OCR Server
* [Munchkin] 优化多处RAG解析细节
* [Munchkin] 支持上传Zip格式的文件知识
* [Munchkin] 优化  K8S调度支持使用Service Account
* [Pilot] Pilot新增 `/reset`关键词
* [ChatServer] 新增 `智谱AI公有云` 支持
* [ChatServer] 优化 日志输出，API调用错误的时候提示异常原因
* [ChunkServer] 优化 Word类型文档解析逻辑，标题和段落在初始拆分的时候合并一个Chunk
* [ChunkServer] 优化 MD文件转换为Word解析
* [ChunkServer] 修复 PPT解析过早return的bug
* [RagServer] 优化 提取索引的Batch大小到参数中
