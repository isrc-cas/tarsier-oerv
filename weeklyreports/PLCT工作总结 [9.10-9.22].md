# 工作总结 [9.10-9.22]

## 过去两周的进展

1. 构建流程调整

   - 完成了riscv源码仓的建立：https://gitee.com/openeuler-risc-v

     - [完成]未被src-openeuler/接受的pr提到openeuler-risc-v仓（[12个PR](https://gitee.com/organizations/openeuler-risc-v/pull_requests?assignee_id=&author_id=&label_ids=&label_text=&milestone_id=&priority=&project_id=&project_type=&scope=&search=&sort=closed_at+desc&status=all&target_project=&tester_id=)）
     - **维护两个版本元信息文件(mainline和baseOS)：包含openeuler-risc-v的仓和src-openeuler的仓**
     - **根据元信息文件得到两个工程的obs配置文件**

     

2. [WIP] openEuler:Mainline:RISC-V工程构建：

   | 状态         | 9月8日 | 9月22日 | 变化说明 |
   | ------------ | ------ | ------- | -------- |
   | succeeded    | 1907   | 1924    | 增17     |
   | failed       | 252    | 211     | 减41     |
   | unresolvable | 1889   | 1913    | 增24     |
   | broken       | 16     | 16      |          |
   | disabled     | 1      | 1       |          |
   | excluded     | 62     | 62      |          |

   问题：

   - main工程每次构建，哪些包构建成功了、包的状态变化没有很直观的展示。后续通过数据抓取和对比建立统计数据。

     

3. [WIP]  BaseOS：刚开始，梳理出用于构建riscv linux操作系统的基础包。@孙喆炘

   - 第一批构建目标（76个基础包）：https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/build-obs-baseos-repo.md

   - 构建地址：https://build.openeuler.org/project/show/home:yx971:RISC-V:BaseOS

     - 成功构建：39个包   [详细清单](https://github.com/xijing21/openEuler-riscv/blob/main/data/BaseOs.xlsx)

     - 构建失败正在推进的包有4个：**glibc**、automake、openssl、perl

       

4. obs工具

   - obs包和构建状态抓取工具：

     - 工具：https://github.com/plctlab/openEuler-riscv/tree/main/scripts/dependent_package
     - 数据：https://github.com/plctlab/openEuler-riscv/tree/main/data/obsBuildStatus   

     

5. 包分析（优先解决哪些包？哪些包容易被解决？共性问题处理等）：

   - 获取obs main中包状态为unresolvable 但其缺少依赖其实是succeeded的软件包列表：https://github.com/plctlab/openEuler-riscv/issues/117

   - 按照经验给出的构建优先级：https://gitee.com/openeuler/RISC-V/issues/I45G4I?from=project-issue#note_6605790_link 

   - unresolvable包的转换和处理（对unresolvable包缺少的依赖包数量和包进行统计分析，对依赖数最少进行处理）：https://github.com/plctlab/openEuler-riscv/issues/135

   - 对包的依赖关系进行分析统计，从重要性（被依赖多）、难度（依赖的包多）、当前构建状态等多角度：

     https://github.com/xijing21/openEuler-riscv/blob/main/data/compare/compare_20210922.xlsx

   - spec中遇到valgrind或者valgrind-devel的处理：https://github.com/plctlab/openEuler-riscv/issues/129

     

6. **[延迟到11月]** 9.23演示D1/BishengJDK 图形界面的游戏 

   > 受疫情影响，会议改为线上会议，原本的展示计划延迟到11月。

   

7. **[暂缓]** 桌面图像界面的支持(xfce)：存少数体验提升问题外，基本功能已完成。

   - 菜单栏等重影黑块问题

   - 卡，慢




## 未来两周计划

1. 建立obs构建状态和数据跟踪表格

   > 目前obs没有统一的构建日志，比如上述的包的状态的变更，没有比较直观的展示：计划通过工具去执行和完成

2. 继续完成riscv源码仓增设后的后续工作

   - **维护两个版本元信息文件(mainline和baseOS)：包含openeuler-risc-v的仓和src-openeuler的仓**
   - **根据元信息文件得到两个工程的obs配置文件**

3. 继续上述[5.包分析]思路，按照一类问题，一类解决办法的方式去分批、分类解决问题。可以根据实际情况考虑的其它操作有：

   - 对4127个包中，触发构建时处于阻塞状态的包如果对构建任务（带界面操作系统）无帮助，可以去掉相应的软件包
   - 对xfce所需的包进行自顶向下的包需求分析、包在obs中包含、构建状态分析：从而聚焦核心包开展相应工作

   

## 问题

- openEuler:Mainline:RISC-V obs工程中的4127个包，主要是“继承”自https://build.openeuler.org/project/show/openEuler:Mainline 工程（4187个包），之前的思路主要是解决构建状态为：failed、unresolvable状态的包，将其转换为succeeded。现在开始反思，4127个包是否都是riscv所需要的，我们的近期的核心目标是出一个有界面的openeuler操作系统。从功能上来说，需要能够支持界面。

- excluded状态包：之前认为是spec文件缺少了对riscv64架构的支持。但是后续查询后发现，这种状态下的很多包都不太适合riscv架构，有的甚至只支持x86等。这也使得我们在进行包构建的过程中，不仅要关注包的构建状态，依赖，还需要关注包的功能，用途。去掉一些与目标无关的包也未尝不可。

  



