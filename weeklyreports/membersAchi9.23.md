# 成员交付成果清单

请大家参考如下信息要素提交可见交付成果：（没有的可不列出）

构建包任务类：

- XXXX包：
  - issue：
  - obs：
  - PR：
  - 文档：

其它任务：

- issue标题：
  - issue链接：
  - PR：
  - 文档：

笔记类（这里特指自己学习、工作中总结的文档，不是以issue方式指定的任务）：

- 文档标题、链接

问题类（工作中发现和遇到的问题，必须以公开的方式可见才行，非可见不算可见交付）

- issue标题和链接



### 0.马驰

- 文档与指导：[#83](https://github.com/plctlab/openEuler-riscv/issues/83)

  

## 第一批

### 1.孙喆炘 [zhé xīn]

- [BaseOS_Base20: 19/20](https://build.openeuler.org/project/show/home:yx971:RISC-V:BaseOS:Base20)

- [stage 复现Base OS](https://build.openeuler.org/project/show/home:zxs-un:openEuler:riscv64:BaseOS:stage1)

- [ssh 配置](https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/ssh-agent-config.md)

  

### 2.刘佳伟

- **包构建任务**
  [mozjs52 的状态](https://github.com/plctlab/openEuler-riscv/issues/118)

  

- **学习记录**
  [如何给一个包打补丁-mozjs52](https://gitee.com/jiawei__liu/open-euler_riscv64/blob/master/doc/修52包的流程记录.md)
  [在openEuler项目中学到的一些linux操作](https://gitee.com/jiawei__liu/open-euler_riscv64/blob/master/doc/在openEuler项目中学到的一些linux操作.md)
  [记录我关于oe项目的一些疑惑](https://gitee.com/jiawei__liu/open-euler_riscv64/blob/master/doc/openEuler项目相关的一些基本概念的问答记录.md)



### 3.李诗洋

- ck包：
  - issue: https://gitee.com/openeuler/RISC-V/issues/I466NG?from=project-issue
  - obs: [合并后构建成功](https://build.openeuler.org/package/live_build_log/openEuler:Mainline:RISC-V/ck/standard_riscv64/riscv64) 
  - PR: https://gitee.com/openeuler-risc-v/ck/pulls/1

- kexec-tools:
  - issue: https://github.com/plctlab/openEuler-riscv/issues/142
  - obs: [obs构建失败日志](https://build.openeuler.org/package/live_build_log/openEuler:Mainline:RISC-V/kexec-tools/standard_riscv64/riscv64)
         [个人工程下修改构建成功日志](https://build.openeuler.org/package/live_build_log/home:LiShiYang:branches:openEuler:Mainline:RISC-V/kexec-tools/standard_riscv64/riscv64)

- httpd:
  - issue: https://github.com/plctlab/openEuler-riscv/issues/143


### 4.孙浩翔

**构建包任务类：**

- [OBS中valgrind相关依赖的处理](https://github.com/plctlab/openEuler-riscv/issues/129)

- jq：
  - issue：[链接](https://github.com/plctlab/openEuler-riscv/issues/136)
  - obs：[链接](https://build.openeuler.org/package/show/home:maxim.suen:branches:openEuler:Mainline:RISC-V/jq)
  - PR：[链接](https://gitee.com/openeuler-risc-v/jq/pulls/2)
- libdap:
  - issue：[链接](https://github.com/plctlab/openEuler-riscv/issues/140)
  - obs：[链接](https://build.openeuler.org/package/show/home:maxim.suen:branches:openEuler:Mainline:RISC-V/libdap)
  - PR（待合并）：[链接](https://gitee.com/openeuler-risc-v/libdap/pulls/1)

- fwupd、libsecret:
  - issue:[链接](https://github.com/plctlab/openEuler-riscv/issues/144)
- pytest:
  - issue:[链接](https://github.com/plctlab/openEuler-riscv/issues/107)

**笔记类**

- [smp32版镜像的使用](https://gitee.com/maximsuen/plct-internship-notes/blob/master/7.SMP32%E7%89%88OE%E5%92%8C%E7%9B%B8%E5%BA%94QEMU%E7%9A%84%E4%BD%BF%E7%94%A8.md)




## 第二批

### 5.许志凌

- http-parser包：
  [issue](https://github.com/plctlab/openEuler-riscv/issues/131)
  [obs](https://build.openeuler.org/package/show/home:xinminst:branches:openEuler:Mainline:RISC-V/http-parser)
  [PR](https://gitee.com/openeuler-risc-v/http-parser/pulls/1)
- isomd5sum包：
  [issue](https://github.com/plctlab/openEuler-riscv/issues/132)
  [obs](https://build.openeuler.org/package/show/home:xinminst:branches:openEuler:Mainline:RISC-V/isomd5sum)
  [PR](https://gitee.com/openeuler-risc-v/isomd5sum/pulls/1)
- pixman包：
  [issue](https://github.com/plctlab/openEuler-riscv/issues/139)
  [obs](https://build.openeuler.org/package/show/home:xinminst:branches:openEuler:Mainline:RISC-V/pixman)
  [PR](https://gitee.com/openeuler-risc-v/pixman/pulls/1)



### 6.邹通成

- #### ldns

  - obs构建：[link](https://build.openeuler.org/package/show/home:ChengZou:branches:openEuler:Mainline:RISC-V/ldns)
  - issue: [link](https://github.com/plctlab/openEuler-riscv/issues/141)

  #### iavf

  - obs构建：[link](https://build.openeuler.org/package/show/home:ChengZou:branches:openEuler:Mainline:RISC-V/iavf)

  #### i40e

  - obs构建: [link](https://build.openeuler.org/package/show/home:ChengZou:branches:openEuler:Mainline:RISC-V/i40e)



### 7.许嘉玲

构建包任务：

- sscg【failed包】
  [*issue：sscg](https://github.com/plctlab/openEuler-riscv/issues/147)
  [*obs：sscg](https://build.openeuler.org/package/show/home:nuomi:branches:openEuler:Mainline:RISC-V/sscg)

- apr-util【failed包】
  [*issue](https://github.com/plctlab/openEuler-riscv/issues/159)
- https://github.com/plctlab/openEuler-riscv/issues/151  15个包

笔记类：

- [spec学习](https://gitee.com/sticky-rice-wine/note/blob/master/spec自学.pdf)



### 8.颛孙宇翔 [zhuān sūn]

- 1.自行购买了云服务器，并建立了ssh连接，尝试安装openeuler失败
- [2.学习了Linux相关知识，](https://github.com/YuXiang-ZhuanSun/Blog)
- 3.完成《openEuler构建之OBS使用指导》的学习



## 第三批

### 9.高世豪

构建包任务类

- gettext
  [issue](https://github.com/plctlab/openEuler-riscv/issues/157)
  [obs](https://build.openeuler.org/package/show/home:gsh:branches:openEuler:Mainline:RISC-V/gettext)

- gspell
  [issue](https://github.com/plctlab/openEuler-riscv/issues/156)
  [obs](https://build.openeuler.org/package/show/home:gsh:branches:openEuler:Mainline:RISC-V/gspell)

- 正在学习如何在服务器上使用osc build 和 解决failed的包。



### 10.袁政

构建包任务类

- gunlib包：
  [issue：](https://github.com/plctlab/openEuler-riscv/issues/155)
  [obs：](https://build.openeuler.org/package/show/home:YuanZheng:branches:openEuler:Mainline:RISC-V/gnulib)

笔记类：
[spec文件学习.docx](https://github.com/plctlab/openEuler-riscv/files/7217241/spec.docx)

学习了rpm相关命令和功能，正在学着看懂构建log，并且studing连接老师提供的服务器进行构建



### 11.刘洋

- 在自己的主机上成功搭建好了所有环境，能够通过ssh连接服务器进行工作

  选择了2个相对简单的包进行构建学习，目前还在学习中....
  [gnu-ef](https://github.com/plctlab/openEuler-riscv/issues/152)
  [ant](https://github.com/plctlab/openEuler-riscv/issues/153)

  

### 12.温智翔

- [[excluded练习\]edac-utils](https://github.com/plctlab/openEuler-riscv/issues/122)
- [[broken练习\]efl](https://github.com/plctlab/openEuler-riscv/issues/120l)
- 学习了Linux操作系统的常用命令：
  https://blog.csdn.net/qq_23329167/article/details/83856430/
- 在b站上学习了《openEuler构建之OBS使用指导》
- 在CSDN等论坛学习并整理一些相关名词的解释及用法
- [学习笔记](https://gitee.com/wen-zhixiang/study-notes/blob/master/0909-0923学习笔记.md)
- 选择了[memleax](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/memleax)进行构建学习



### 13.杨心仪

- 1.我成功连接了ssh服务器，并且装上了openEuler和qemu
- 2.完成excluded包acpid与bpftrace的成功构建：
  [excluded包构建](https://github.com/plctlab/openEuler-riscv/issues/121)
- 3.完成broken包log4j，boost,efl的构建：
  [broken包构建](https://github.com/plctlab/openEuler-riscv/issues/119)
- 4.[完成Linux操作系统的常用命令的学习1](https://blog.csdn.net/qq_23329167/article/details/83856430/)
  [完成Linux操作系统的常用命令的学习2](https://www.bilibili.com/video/BV1H7411K7pZ)
- 5.完成《openEuler构建之OBS使用指导》的学习
- 6.[学习笔记](https://gitee.com/yxycrhistina/study-notes/blob/master/README.md)

