# 过去两周的进展

## 1、人员招聘与团队建设

- 全勤投入正式员工：2人
- 非全勤投入正式员工：≥1个
- 招聘实习生：9人   3人全勤+进度OK，2人加入略晚继续观察   
- 志愿者：若干   暂时还没开始做什么



## 2、基础知识的学习

### 集训：

通过当前项目文档初步了解项目目标、现状、主要任务+沟通答疑
源码仓、依赖仓、obs project等基本概念与关系
如何在obs中查看oE riscv project构建状态
如何查看构建错误的包、看日志、分析问题原因

> 对200个左右的构建失败的包进行日志查看和问题初步分析：感受构建失败的主要问题，尝试对问题进行分类

如何在obs中新增一个package
如何在obs中修改已有软件包
如何搭建本地openEuler RISC-V 环境（4-5人基础环境已经搭建成功）




### 分工：（刚启动）

构建失败问题的收集与整理
构建失败原因分析
spec相关
obs在线构建与本地osc构建应用场景
文档


## 3、本地环境搭建

4~5人已经成功完成了基础环境的搭建

## 4、文档

在学习的过程中，输出文档，详见：[https://gitee.com/openeuler/RISC-V/issues/I42QDD?from=project-issue](https://gitee.com/openeuler/RISC-V/issues/I42QDD?from=project-issue)
问题：文档的管理目前还未正规化，大部分暂时收录在gitee个人仓库，后续调整提交到主仓库；


# 现状

过去两周属于集训期，主要基调是集体学习、基础环境搭建、文档素材积累和初步输出；
成果：
1、对200多个构建失败的包进行日志查看和问题整理——》并不是都能根据日志找到错误的根本原因
2、4~5人完成了本地openEuler RISC-V 环境搭建
3、部分稳定输出：[https://gitee.com/openeuler/RISC-V/issues/I42QDD?from=project-issue](https://gitee.com/openeuler/RISC-V/issues/I42QDD?from=project-issue)
4、D1上安装openEuler riscv：未同步

下一步方向：
1、尝试动手去解决包构建失败的问题
2、文档工作

# 问题

1、当前在线obs构建会锁定在kernel包的构建，卡在这里，后续工作不好开展。之前讨论过两种方式：
第一种：本地构建——》到底怎么构建，是否有参考或详细的指导文档？
第二种：讨论和确定利用OBS的staging 的workflow 构建最新代码的openEuler RISC-V工程 的可行性。详见：[https://gitee.com/openeuler/RISC-V/issues/I42JP7](https://gitee.com/openeuler/RISC-V/issues/I42JP7)

2、对于没有经验的人，如何去解决包构建失败的问题。

3、本地构建的目的：
（1）有些包需要在本地调试去寻找问题，本地构建更方便；
（2）本地构建验证是否需要验证软件包的最终产物是否可用？——》目前是只要求包构建成功，还是包在oE riscv操作系统能够正常使用（比如功能操作层面核心功能可用）


3、本地的qemu+oE riscv操作系统环境的搭建，想放到服务器上去做，可否基于虚拟机或者docker容器去搭建？——》是否有过成功的尝试？

# 需要协作的事宜

1、上述问题1
2、文档管理方式：[https://gitee.com/openeuler/RISC-V/issues/I3ZBFW](https://gitee.com/openeuler/RISC-V/issues/I3ZBFW)
有经验的人多写文档、录视频；
文档方式：

   - issue+标签方式
   - md+PR



# 未来两周计划

1、尝试动手去解决包构建失败的问题  @Maxim @[PandaGix](https://gitee.com/pandagix) @liujiawe @xijing @sunhaoxiang
 **第一步：** 寻找一个构建成功的包，每人都尝试按照流程进行构建；
目的：学习进阶——体验和熟悉工作流程


 **第二步：**  找一个问题容易解决的包，每人都尝试去解决这个包的问题，相互构沟通，完成和解决包的问题；
目的：学习进阶——从简单的问题入手，学习如何去解决构建问题；

 **第三步：** 人分别去认领一个构建失败的包（从简单的开始），分别去分析和解决所负责的包的问题；
目的：执行项目任务——解决包构建失败的问题；
2、文档工作    @xijing  @Maxim @[PandaGix](https://gitee.com/pandagix) @liujiawe @sunhaoxiang
文档管理规范化
文档内容增加，暂时计划推进【如何加入社区成为贡献者】相关内容
3、D1上安装openEuler riscv：@wangxiang

4、通过添加tag等方式提升obs的构建效率？ @wuwei

