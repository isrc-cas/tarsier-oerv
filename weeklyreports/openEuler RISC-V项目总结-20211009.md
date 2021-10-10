本项目目的是构建riscv64下的openEuler 操作系统，该系统22.03的目标是能够支持可视化界面、bishengJDK等功能，且能够在D1上运行。

系统的构建依托于OBS：https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V 。



为了完成openEuler RISC-V系统的构建，构建一个具有可视化界面的操作系统。需要完成如下的任务：

1、当前基于OBS构建系统openEuler:Mainline:RISC-V 工程下的4127个软件包的构建，使得工程下所有软件包构建状态都succeeded 。

> 这4127个包大部分都是系统所需要的的基础软件包，是操作系统所需的，目前需要让所有包能够在构建系统中build succeeded ，由源码生成二进制包。当前大量的包都是failed和unresolvable状态，这些状态的包我们需要逐一修复，使得每个包都能succeeded 。
>
> 说明：4127个包并不是最终的定义，可能部分包根据使用场景不需要加入系统最终去掉。有些需要的包还未纳入都当前的构建系统，包的纳入和移除是根据需求和应用场景定义的。

| datetime | succeeded | failed | unresolvable | broken | disabled | excluded |
| -------- | --------- | ------ | ------------ | ------ | -------- | -------- |
| 20210908 | 1907      | 252    | 1889         | 16     | 1        | 62       |
| 20210922 | 1924      | 211    | 1913         | 16     | 1        | 62       |
| 20210926 | 2206      | 266    | 1576         | 16     | 1        | 62       |
| 20210930 | 2309      | 170    | 1570         | 16     | 1        | 61       |
| 20211009 | 2312      | 168    | 1569         | 16     | 1        | 61       |

（1）openEuler:Mainline:RISC-V  failed状态的包逐一进行修复，使之能够succeeded 

（2）openEuler:Mainline:RISC-V  unresolvable状态的包能够补助其构建所需的依赖包，使得构建完成，并最终状态为succeeded 

（3）将excluded:396(其中的60多个包非noarch包添加ExclusiveArch:riscv64后启动构建)、broken:21在obs上进行_service添加启动构建任务：[统计结果](https://github.com/plctlab/openEuler-riscv/blob/main/doc/excluded%2Bbroken.xlsx)

（4）对包的构建通过数据分析、问题分类的方式进行分析和任务分配（优先解决哪些包？哪些包容易被解决？共性问题处理等）：

- [完成]获取obs main中包状态为unresolvable 但其缺少依赖其实是succeeded的软件包列表：https://github.com/plctlab/openEuler-riscv/issues/117

- [完成]按照经验给出的构建优先级：https://gitee.com/openeuler/RISC-V/issues/I45G4I?from=project-issue#note_6605790_link

- [进行中]unresolvable包的转换和处理（对unresolvable包缺少的依赖包数量和包进行统计分析，对依赖数最少进行处理）：https://github.com/plctlab/openEuler-riscv/issues/135

- [完成]对包的依赖关系进行分析统计，从重要性（被依赖多）、难度（依赖的包多）、当前构建状态等多角度：

  https://github.com/xijing21/openEuler-riscv/blob/main/data/compare/compare_20210922.xlsx

- [完成]spec中遇到valgrind或者valgrind-devel的处理：https://github.com/plctlab/openEuler-riscv/issues/129

  

2、系统可视化桌面功能支持

> 一个好用的系统需要提供可视化操作界面，因此需要加入一系列的桌面功能相关的软件包。目前linux桌面套件种类很多，基于调研，我们初步定义轻量桌面套件xfce

（1）桌面套件调研：
- [完成]不同桌面套件的对比选型：xfce较为轻量，适合riscv架构
- [完成]xfce所需的软件包调研
  - https://gitee.com/xijing666/rv-oe_work/issues/I46ULA

（2）桌面套件构建
- [完成90%以上，还有部分bug待修复]本地构建
  - SUSE Chromium rpm 在openEuler进行测试 (baidu ok, B站加载不了)https://build.opensuse.org/package/show/openSUSE:Factory:RISCV/chromiu
  - 修复xfce部分bug和添加输入法
  
- [进行中]集成到构建系统中

  

3、[进行中]BaseOS for openEuler RISC-V

> 这是一个从0开始构建openEuler RISC-V 能够自举的最小集合操作系统的分支任务。目前基于openEuler:Mainline:RISC-V 4127个软件包的构建都是基于种子二进制依赖仓库，这种在未实现操作系统自举的时候就加入了太多的软件包，依赖仓也加入了很多二进制包，这样做会出现依赖仓的软件包变化时，某一些软件包的构建结果不稳定总是能够成功，因此启动了一个从0开始，分批次逐步加入软件包，在上一批次软件包能够自举后再加入新的软件包的构建方式去完成操作系统构建。

- stage1:23个包全部构建成功：https://build.openeuler.org/project/monitor/home:zxs-un:openEuler:riscv64:BaseOS:stage1
- Stage2: 82个包 65个成功：https://build.openeuler.org/project/monitor/home:zxs-un:openEuler:riscv64:BaseOS:stage2



4、bishengJDK软件包在oe riscv系统中的支持

- [bishengJDK](https://gitee.com/openeuler/RISC-V/issues/I28H7L?from=project-issue)：本地编译运行测试通过；**rpm打包后续在obs构建平台中补充；**

  

5、openEuler RISC-V在全志哪吒D1开发板上的支持与测试

（1）D1+openEuler镜像制作

- [完成] D1+openEuler：D1 openEuler 第一版镜像下载地址：https://mirror.iscas.ac.cn/plct/openEuler-D1-20210731.img.bz2

- [完成] D1+openEuler：D1 openEuler 第二版镜像(wifi可用)下载地址：https://mirror.iscas.ac.cn/plct/openEuler-D1-wifi-enabled-20210810.img.bz2

- [完成] D1+openEuler：D1 openEuler 第三版镜像(HDMI接口可用)下载地址：https://mirror.iscas.ac.cn/plct/openEuler-D1-wifi-hdmi-20210817.img.bz2

- [完成] D1+openEuler：D1 openEuler 第四版镜像(增加docker)下载地址：https://mirror.iscas.ac.cn/plct/openEuler-D1-wifi-hdmi-docker-20210826.img.bz2

- [完成] D1+openEuler：D1 openEuler 第五版镜像(增加xfce+bishengJDK)下载地址：（暂时未公开到plct mirror，计划解决一些问题后再更新）

（2）测试工作

- D1上oE镜像(0817版)测试：[在D1上运行8/17日最新的openEuler镜像，配合11.0.10版本的JDK镜像可以成功运行java语言版本的hello world](https://zhuanlan.zhihu.com/p/401285641?utm_source=wechat_session&utm_medium=social&s_r=0)

- 在Qemu RISCV64虚拟机中安装Docker并运行RISCV Linux:https://zhuanlan.zhihu.com/p/399366057 

- D1 openEuler 第五版镜像(xfce)测试：[问题列表](https://github.com/plctlab/openEuler-riscv/issues?q=is%3Aissue+is%3Aopen+xfce)

- [bishengJDK java demo下棋游戏在[D1 openEuler 第五版镜像(xfce)]上的运行测试](https://github.com/plctlab/openEuler-riscv/issues/90)

  

6、工作流程改进+效率提升

（1）[完成]构建流程调整

- [完成]完成了riscv源码仓的建立：https://gitee.com/openeuler-risc-v
  - [完成]未被src-openeuler/接受的pr提到openeuler-risc-v仓（[12个PR](https://gitee.com/organizations/openeuler-risc-v/pull_requests?assignee_id=&author_id=&label_ids=&label_text=&milestone_id=&priority=&project_id=&project_type=&scope=&search=&sort=closed_at+desc&status=all&target_project=&tester_id=)）
- [完成]重新梳理工作流程：https://github.com/plctlab/openEuler-riscv/blob/main/quicklystartbuild/workflow-for-build-a-package.md
- [周期性工作持续进行]对修复的包在关键结点建立跟踪表格：https://docs.qq.com/sheet/DUHFlV0haT2duWHBG?tab=BB08J2



（2）[完成] 用于加速构建的oE QEMU 镜像-RV64 SMP32版本：https://mirror.iscas.ac.cn/plct/openEuler_SMP32-20210821.tar.bz2  

> 刚刚实测以gzip为例，在worker02.tarsier上用qemu oE进行osc构建一个包的的速度是build.oE.org的4倍多



（3）[完成] 为了让PLCT同事更加便捷的添加构建所需的依赖包，建立了共享依赖仓和包同步机制：https://mirror.iscas.ac.cn/openeuler-sig-riscv/ 

- 打破循环依赖的包：https://mirror.iscas.ac.cn/openeuler-sig-riscv/forplct/ 
- 子项目可引入的rpm包：https://mirror.iscas.ac.cn/openeuler-sig-riscv/subprjdep/ 



（4）[完成]完成obs包抓取工具，并定期(每次构建完成后)抓取构建数据，对构建状态建立跟踪机制

- [完成]obs包和构建状态抓取工具：https://github.com/plctlab/openEuler-riscv/tree/main/scripts/dependent_package
- [周期性工作持续进行]obs构建数据：
  - 构建状态对比：https://github.com/plctlab/openEuler-riscv/blob/main/data/obsBuildStatus/obsBuild.xlsx
  - 每次构建详细数据：https://github.com/plctlab/openEuler-riscv/tree/main/data/obsBuildStatus
  - 构建信息对比：https://github.com/plctlab/openEuler-riscv/tree/main/data/compare



7、附件---任务与问题管理

项目gitee repo：https://gitee.com/openeuler/RISC-V

项目github repo：https://github.com/plctlab/openEuler-riscv

