# 了解项目
## 项目简介
openEuler RISCV 是开源操作系统openEuler下的一个子工程，目的是让openEuler操作系统能够在RISC-V精简指令集硬件架构上运行。
openEuler riscv64与x86_64、aarch64是openEuler总工程下的不同的子工程（Project）；

本文档中描述的项目主体默认情况下全部都是openEuler riscv64；



## 项目目标
### 背景简述


在介绍目标之前，先想个问题，你认为一个操作系统应该包含什么？我们一般人都能够想到如下这些：

- 操作系统内核
- 各种各样的软件包
- 操作系统安装镜像下载
- 文档
- 为了让操作系统能够支持很多的硬件，需要对不同硬件进行适配

可能还有很多，但是主要的应该就是如上的一些我们在使用别的操作系统中熟悉的内容了。


那这些在别的操作系统上你能看到、获取到的东西，都是一个操作系统需要做的事情。在本项目中，openEuler RISCV 做的是一个linux的开源的操作系统，但是要做的事情，要完成的内容与别的操作系统是相似的。

这个事情细分下来很多，所以openEuler RISCV SIG（简单理解为项目组吧）要做的事情也很多。尤其是我们的软件包，按照不同的重要程度，依赖关系，我们还可以继续划分（为了大家理解项目目的，不严谨的初略的划分）：

- 基础的软件包（可以理解为操作系统必备）

kernel gcc glibc libc zlib
systemd Xorg gtk qt NetworkManager Qemu opengl
python perl ruby java nodejs
gnome kde firefox

- 其它增强功能的软件包

isula / atune / stratovirt / bishengjdk(risc-v)

- GUI相关的软件包

gnome xfce  

- 根据不同应用场景选择安装的软件包

repo server   
IDE工具

分类方式不一而论，分类还可以继续细化。不管怎么分，我们能发现，**操作系统能够支持的软件包（packages）是越多越好的。**




### 项目目标

**总结来说，项目目标是从至少3个方面：**
**1、软件方面：也就是操作系统+软件包。支持尽可能多的软件包（暂定3000+）、稳定、好用；**
**2、硬件方面：让更多的riscv指令集架构的硬件能够顺利的安装使用openEuler riscv操作系统；**
**3、文档：**

- **让更多的人能够加入到社区，为openEuler riscv项目做贡献，加速操作系统生态的成熟；**
- **让操作系统的用户，方便、容易的上手使用；**




## 项目现状
### 发展历史
这是openEuler RISCV SIG成立以来的一个发展图：
![](https://cdn.nlark.com/yuque/0/2021/png/12590933/1627467424680-3ec757e6-7545-4024-b8b8-b2b10de3c8e8.png#align=left&display=inline&height=683&margin=%5Bobject%20Object%5D&originHeight=683&originWidth=1247&status=done&style=none&width=1247)



### 版本发布计划

下图是openEuler riscv的一个版本发布历史和规划：

- 半年发布一个创新版本：维护周期半年
- 2年发布一个商用版本（LTS）：维护周期4年；下游的OSV厂商基于LTS版本去做发行版提供给客户；



![](https://cdn.nlark.com/yuque/0/2021/png/12590933/1627467401623-a108435c-ee74-4ab9-a4be-3298500a2576.png#align=left&display=inline&height=672&margin=%5Bobject%20Object%5D&originHeight=672&originWidth=1237&status=done&style=none&width=1237)

### 项目现状与主要任务
#### 项目现状：

- 当前已经发布的最新的创新版本为openEuler 21.03；
- 下一个发布版本是2021年9月发布的openEuler 21.09版本。



**openEuler 21.09版本要支持的内容（我们要实现的阶段性目标）：**

1. 【已完成】Kernel 同步到5.10
1. 【进行中，重中之重】支持3000+ Packages
1. 【进行中，重点，与2同步】将openEuler riscv的版本更新到最新的openEuler版本（这里的openEuler版本指的是x86、aarch64的最新版本。因为openEuler在riscv64、x86、aarch64等不同架构上，按照上游总工程的设计理念是**代码归一、同架构二进制归一**）
1. 【进行中，中等重要】支持更多的硬件
1. 【优先级低】UI、docker image等其它



**以上这些目标是有顺序的，其中1是最基础的前提，2和3是当前最重要，最主要的工作内容。4需要硬件厂商的支持，也需要看硬件厂商的开发板的发布进度，优先级略低；5则优先级相对最低，当1-3完成时，才有基础、有必要去做5；**




#### 主要任务：
为了发布21.09版本，当前未完成且正在做的**最重要的任务**是：
**1、让操作系统支持的软件包的扩充到3000+（含版本升级）**
**2、文档**
> 需要做的事情多，需要更多的人加入，更多的人加入需要了解项目、学习如何在社区贡献，都需要文档指导。



**那么要让操作系统的软件包支持到3000+需要做哪些事情？**
按照做事的流程来说，至少分两个阶段：
**第一个阶段：让软件包（package）能够在openEuler riscv64环境下被成功的构建；**
**第二个阶段：**软件包能够在openEuler riscv64系统上成功的安装和正常的启动和使用（能安装、软件装好之后能启动不会闪退等、启动之后核心功能甚至全部功能能正常使用）

**我们目前正在做的是第一个阶段：构建**

