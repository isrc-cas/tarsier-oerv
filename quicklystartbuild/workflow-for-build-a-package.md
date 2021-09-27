# oE项目中build包的流程

本文不是介绍如何将一个非成功状态下的包怎么build成功，而是从工作流程的角度介绍在openeuler riscv项目中通过OBS构建系统进行工作的常规流程。



## 构建资源简介

在介绍工作流程之前，先介绍下个人开发者会接触到的构建资源，主要包含以下这些：

![1-资源信息](images/1-%E8%B5%84%E6%BA%90%E4%BF%A1%E6%81%AF.png)



## 问题定位操作流程

从观察和分析包开始，我们的常见流程是这样的（这个流程主要是初期对包的问题进行大致定位）：

![2-作业流程](images/2-%E4%BD%9C%E4%B8%9A%E6%B5%81%E7%A8%8B.png)





## 修改源文件解决问题流程

当我们确定一个包的问题必须通过修改源码来解决的时候，我们就需要执行以下流程：

![3-正式流程](images/3-%E6%AD%A3%E5%BC%8F%E6%B5%81%E7%A8%8B.png)



## 包构建进度跟踪

一个包修复完成，我们的终点是mainline工程下构建成功。在以上流程的执行过程中，我们会对每个关键流程进行监控，主要的跟踪表格详见共享Excel表格：

https://docs.qq.com/sheet/DUHFlV0haT2duWHBG?tab=BB08J2


请大家执行以上的流程，并对自己跟踪的包的状态在上述表格中进行维护。





## 问题

### 什么时候openeuler-risc-v向src-openeuler提交PR？

当OBS的openEuler:Mainline:RISC-V 工程完成了我们的构建目标，目标包都能反复构建成功（或者通过内部初测），达到发版状况的时候才会提交PR到上游。因此日常的工作流程中，不涉及到openeuler-risc-v向src-openeuler提交PR的过程。

这个操作将由riscv社区的管理员或者maintainer负责。



src-openeuler合并openeuler-risc-v的PR后，会由openeuler上游社区统一进行系统构建，测试，发布一个增加了支持riscv64的新操作系统版本。

