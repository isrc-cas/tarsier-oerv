# openEuler for RISC-V

本项目目的是构建riscv64下的openEuler 操作系统，系统的构建依托于OBS：https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V 。

项目repo：https://gitee.com/openeuler/RISC-V

项目PLCT内部管理repo：https://github.com/plctlab/openEuler-riscv


### 项目总体进展 by 席静

1. 人员招聘与团队建设：建立13实习生团队和基础技能的学习培训
2. [WIP] 继续解决构建失败的包，完成21.09发版计划：计划成功支持3000+包+UI+bishengJDK等特定软件包
   - 约10多个包的处理：可在在[issue中搜索[构建失败]查看相关任务](https://gitee.com/openeuler/RISC-V/issues?utf8=%E2%9C%93&issue_search=%5B%E6%9E%84%E5%BB%BA%E5%A4%B1%E8%B4%A5%5D)
   - 将excluded:396(其中的60多个包非noarch包添加ExclusiveArch:riscv64后启动构建)、broken:21在obs上进行_service添加启动构建任务：[统计结果](https://github.com/plctlab/openEuler-riscv/blob/main/doc/excluded%2Bbroken.xlsx)
   - 构建问题分析：
     - 很多基础的包如glibc、coreutils、webkit2gtk3等都[未构建成功过一次](https://github.com/plctlab/openEuler-riscv/blob/main/weeklyreports/包构建现状.md)。
     - [riscv迭代构建问题](https://github.com/plctlab/openEuler-riscv/blob/main/weeklyreports/riscv%E8%BF%AD%E4%BB%A3%E6%9E%84%E5%BB%BA%E9%97%AE%E9%A2%98.md)


3. [WIP]  BaseOS：刚开始，梳理出用于构建riscv linux操作系统的基础包。

   - 第一批构建目标（76个基础包）：https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/build-obs-baseos-repo.md
   - 构建地址：https://build.openeuler.org/project/show/home:yx971:RISC-V:BaseOS

4. [WIP] 9.23演示D1/BishengJDK 图形界面的游戏

   - D1+openEuler：D1 openEuler 第三版镜像(HDMI接口可用)下载地址：https://mirror.iscas.ac.cn/plct/openEuler-D1-wifi-hdmi-20210817.img.bz2

   - D1+openEuler：D1 openEuler 第四版镜像(docker)下载地址：https://mirror.iscas.ac.cn/plct/openEuler-D1-wifi-hdmi-docker-20210826.img.bz2

   - D1+openEuler：D1 openEuler 第五版镜像(xfce)下载地址：（暂时未公开到plct mirror，计划解决一些问题后再更新）

   - [bishengJDK](https://gitee.com/openeuler/RISC-V/issues/I28H7L?from=project-issue)：本地编译运行测试通过；**rpm打包后续在obs构建平台中补充；**

     

5. 桌面图像界面的支持(xfce)：已经基本完成，还有一些问题待解决。@王俊强

   - 菜单栏等重影黑块问题

   - 卡，慢

6. 运维保障（辅助加速）：构建平台/环境搭建改进

   - [完成] 用于加速构建的oE QEMU 镜像-RV64 SMP32版本：https://mirror.iscas.ac.cn/plct/openEuler_SMP32-20210821.tar.bz2  

     > 刚刚实测以gzip为例，在worker02.tarsier上用qemu oE进行osc构建一个包的的速度是build.oE.org的4倍多

   - 共享依赖仓的搭建：https://mirror.iscas.ac.cn/openeuler-sig-riscv/ 

     - 打破循环依赖的包：https://mirror.iscas.ac.cn/openeuler-sig-riscv/forplct/ 
     - 子项目可引入的rpm包：https://mirror.iscas.ac.cn/openeuler-sig-riscv/subprjdep/ 

   - [WIP] PLCT-OBS构建系统：obs worker已经搭建，server正在搭建中。

     - https://build.tarsier-ci.org/   worker01.tarsier-ci.org + worker02.tarsier-ci.org


6. 测试工作

   - D1上oE镜像(0817版)测试：[在D1上运行8/17日最新的openEuler镜像，配合11.0.10版本的JDK镜像可以成功运行java语言版本的hello world](https://zhuanlan.zhihu.com/p/401285641?utm_source=wechat_session&utm_medium=social&s_r=0)
   - 在Qemu RISCV64虚拟机中安装Docker并运行RISCV Linux:https://zhuanlan.zhihu.com/p/399366057 
   - D1 openEuler 第五版镜像(xfce)测试：[问题列表](https://github.com/plctlab/openEuler-riscv/issues?q=is%3Aissue+is%3Aopen+xfce)
   - [bishengJDK java demo下棋游戏在[D1 openEuler 第五版镜像(xfce)]上的运行测试](https://github.com/plctlab/openEuler-riscv/issues/90)



## 实习生贡献清单

- [8.26-9.8](https://github.com/plctlab/openEuler-riscv/blob/main/weeklyreports/membersAchi9.8.md)

- [截止到8.30](https://github.com/plctlab/openEuler-riscv/blob/main/weeklyreports/membersAchi8.30.md)

