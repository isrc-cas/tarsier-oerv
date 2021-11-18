## 一、了解项目

### 1. 项目背景

参考文档：[项目介绍](https://github.com/plctlab/openEuler-riscv/blob/main/quicklystartbuild/introduction.md)



### 2. 工作目标与工作任务

目标计划是在2021年9月出一个openEuler发行版，支持的packages数量达到3000+以上，但是目前存在构建过程中失败的packages，所以当前任务是：
（1）了解构建失败原因
（2）在本地复现构建失败现象
（3）根据失败的原因，解决问题
关于具体工作内容和方法请务必查看“oE-SIG”中群文件中的讲解视频、任务清单、工作说明和 [SIG-RISC-V双周例会会议纪要](https://etherpad.openeuler.org/p/sig-RISC-V-meetings)  以及  [gitee上仓库中置顶issue](https://gitee.com/openeuler/RISC-V/issues/I1U0YD?from=project-issue)



### 3. 工作仓库

- [openEuler RISC-V OBS构建工程](https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V)   ：https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V 

  > openEuler RISC-V OBS构建工程

- [openEuler所有构建工程的源码仓](https://gitee.com/src-openeuler)  :  https://gitee.com/organizations/src-openeuler/projects 

  >  OBS构建工程中所有软件包的源码来之源码仓

- openEuler riscv源码仓：https://gitee.com/openeuler-risc-v

  > openEuler riscv源码仓是为了加速riscv pull request审核流程而设置的一个中间仓库，用于维护在openeuler riscv构建环境下需要维护的源码包。（需要修改的才放这里，不需要修改的依然使用src-openeuler源码仓的源码）

- [gitee上openEuler RISC-V SIG 管理的仓库](https://gitee.com/openeuler/RISC-V) : https://gitee.com/openeuler/RISC-V 

  > 是openEuler RISCV的正式工作平台，对于PLCT小组成员来说，对外的交流、沟通、bug反馈等，需要在gitee issue中进行反馈。

- [github上openEuler RISC-V 仓库](https://github.com/plctlab/openEuler-riscv) : https://github.com/plctlab/openEuler-riscv

  > 为了方便PLCT内部对实习生和员工的管理（PLCT内部项目全部都是github，这里也是为了统一），所有实习生和员工的日常工作安排和工作成果的提交都在github中。
  >
  > 新人不清楚怎么处理github和gitee的关系时：就先满足所有的工作都先提交到github即可。



### 4. 项目资源

1.  [openEuler官网](https://openeuler.org/zh/) 

2.  [openEuler的B站视频](https://space.bilibili.com/527064077/channel/detail?cid=159892&ctype=0)

   > 一定要看【玩转openEuler系列直播之基础知识】的【[【玩转openEuler系列直播 5】openEuler构建之OBS使用指导](https://www.bilibili.com/video/BV1YK411H7E2)】。
   >
   > 其它openEuler B站的视频，有时间也可以多学习。

3.  小组内资料共享：“oE-SIG”QQ群二维码如下。

   >  在QQ群文件中，存放了一些关于项目问题的答疑视频，都是我们曾经的疑问，可以更好的帮助了解项目。群文件中的视频，请按照日期查看。
   > ![输入图片说明](images/151056_8b673580_9256217.png "屏幕截图.png")



4. 关于openEuler OBS构建

   [OBS官方用户指导：obs-user-guide](https://openbuildservice.org/help/manuals/obs-user-guide/)

   > 在B站、QQ群文件已经有不少视频，但是这里还是要推荐这个网站，更加全面。在B站、QQ群文件中已经有了OBS构建的视频。但是这里还是推荐。
   
5. [技术报告分享汇总](https://github.com/plctlab/openEuler-riscv/wiki/%E5%88%86%E4%BA%AB%E6%8A%A5%E5%91%8A)

   

## 二、项目现状

- [项目最新现状（保持定期更新）](https://github.com/plctlab/openEuler-riscv/blob/main/weeklyreports/projectReport.md)
- 项目双周进展
  - [PLCT工作总结 [7.16-7.28]](https://github.com/plctlab/openEuler-riscv/blob/main/weeklyreports/PLCT%E5%B7%A5%E4%BD%9C%E6%80%BB%E7%BB%93%20%5B7.16-7.28%5D.md)
  - [PLCT工作总结 [7.29-8.11]](https://github.com/plctlab/openEuler-riscv/blob/main/weeklyreports/PLCT%E5%B7%A5%E4%BD%9C%E6%80%BB%E7%BB%93%20%5B7.29-8.11%5D.md)
  - [PLCT工作总结 [8.12-8.25]](https://github.com/plctlab/openEuler-riscv/blob/main/weeklyreports/PLCT%E5%B7%A5%E4%BD%9C%E6%80%BB%E7%BB%93%20%5B8.12-8.25%5D.md)
- [项目组成员（PLCT）](https://github.com/plctlab/openEuler-riscv/blob/main/members.md)



## 三、其它

### openEuler社区

由于我们的工作管理和成果提交是在openEuler社区上，因此需要了解openEuler社区的一些基本管理规范与要求。参考资料如下：
[参与openEuler社区](https://gitee.com/openeuler/community/blob/master/zh/contributors/README.md)
[openEuler packaging guidelines](https://gitee.com/openeuler/community/blob/master/zh/contributors/packaging.md)



### 关于开源

[gitee上有关开源以及issue和PR的介绍](https://gitee.com/gitee-community/opensource-guide)

